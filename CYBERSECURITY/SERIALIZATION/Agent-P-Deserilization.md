Pickle Deserialization Vulnerability — Agent P
Description

The -inator Control Panel exposes a blueprint import feature at POST /api/blueprints/import. The endpoint accepts a base64-encoded blob, decodes it, and passes it directly to Python's pickle.loads(). The application attempts to sandbox this deserialization by inspecting the pickle's GLOBAL/STACK_GLOBAL opcodes and rejecting any reference to a blocklisted module.

The blocklist we observed covers: posix, os, subprocess, builtins, sys, pty, ctypes, runpy.

This kind of denylist is fundamentally bypassable for three reasons:

    Pickle is Turing-complete. Any module reachable in the interpreter's sys.modules can be referenced, not just the obvious code-execution modules.

    Static analysis can't follow runtime indirection. A payload that stores a code string and passes it to a function which later calls exec() internally never exposes the dangerous module name to the loader's inspection.

    The stdlib is huge. Dozens of modules ultimately reach exec, eval, Popen, or system — pydoc, timeit, code, platform, pdb, zipfile, tarfile, distutils, setuptools, and more.

The Chain

The __reduce__ method of a Python class controls how pickle serializes an instance. Whatever callable it returns becomes the target of a REDUCE opcode — pickle calls it at load time with the supplied arguments. We abuse this to invoke a function that executes our command.
The Bypass

pydoc.pipepager(text, cmd) internally calls subprocess.Popen(cmd, shell=True, stdin=PIPE). Passing an empty string as text and a shell command as cmd gives us full command execution. Crucially, pydoc is not on the blocklist, and the loader only sees pydoc.pipepager — the dangerous subprocess.Popen call happens inside the stdlib function at runtime, invisible to static inspection.
Impact

Arbitrary code execution in the context of the -inator process — which runs as vanessa, the internal operator account. From there, the attacker can read the C2 socket /run/evilinc/tasking.sock (owned root:vanessa, mode 660) and interact with the implant running as root.
Remediation

    Never unpickle untrusted data. Python's own documentation states pickle is not secure against malicious input.

    Use a safe serialization format. JSON, MessagePack, or Protocol Buffers cannot execute code during deserialization.

    If pickle is unavoidable, use a hardened implementation. RestrictedUnpickler with a strict allowlist (not a denylist) of permitted classes. picklemagic, fickling, or pickle-secure provide static analysis tooling.

    Run the deserialization in a sandbox. Separate low-privilege process, seccomp, namespaces, no network, no filesystem write access.
