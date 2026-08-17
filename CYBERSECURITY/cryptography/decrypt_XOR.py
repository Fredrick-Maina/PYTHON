#!/usr/bin/env python3

from pathlib import Path

# Read the encrypted data produced by challenge.py
cipher = Path("encrypted.bin").read_bytes()

# The challenge uses a 4-byte repeating XOR key.
# We recovered it from the known plaintext "THM{".
key = bytes.fromhex("cb ce ce 43")

# Decrypt each byte:
# plaintext_byte = ciphertext_byte XOR corresponding_key_byte
#
# i % len(key) makes the 4-byte key repeat:
# 0, 1, 2, 3, 0, 1, 2, 3, ...
plain = bytes(
    c ^ key[i % len(key)]
    for i, c in enumerate(cipher)
)

# Convert the decrypted bytes to readable text
# and display the flag.
print(plain.decode())
