#!/usr/bin/env python3

# import necessary modules

import subprocess
import sys
from datetime import datetime

def run_git(*args):
    result = subprocess.run(
        ["git", *args],
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        print(f"Git error: {result.stderr.strip()}")
        sys.exit(result.returncode)

    return result.stdout.strip()

def main():
    # check git repo
    run_git("rev-parse" , "--is-inside-work-tree")

    #check for changes
    status = run_git("status", "--porcelain")

    if not status:
        print("No changes to commit.")
        return

    # Get commit message from command line
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Auto-commit at {timestamp}"

    print("Changes:")
    print(status)
    print(f"\nCommit message: {message}")

    # Stage all changes
    run_git("add", ".")
    run_git("commit", "-m", message)

    #push
    branch = run_git("branch", "--show-current")
    run_git("push", "origin", branch)

    print(f"successfully committed and pushed changes to branch '{branch}'.")

if __name__ == "__main__":
    main()