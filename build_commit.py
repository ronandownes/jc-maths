"""
build_commit.py

Build the PreTeXt project, then git add + commit.
Prompts for a commit message.
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PYTHON = sys.executable

def run(cmd):
    subprocess.run(cmd, cwd=PROJECT_ROOT, check=True)

def main():
    print("=== Building PreTeXt project ===")
    run([PYTHON, "build.py"])

    print("\n=== Git status ===")
    run(["git", "status"])

    msg = input("\nEnter commit message (leave blank to cancel): ").strip()
    if not msg:
        print("Commit cancelled.")
        return

    print("\n=== Committing ===")
    run(["git", "add", "."])
    run(["git", "commit", "-m", msg])

    print("\nDone.")

if __name__ == "__main__":
    main()
