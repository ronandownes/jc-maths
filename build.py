"""
build.py

Build the Junior Cycle Maths PreTeXt project.
Run from the project root.

Usage:
  python build.py
"""

import subprocess
import sys
from pathlib import Path

# Project root is the folder this file lives in
PROJECT_ROOT = Path(__file__).resolve().parent
TARGET = "web"  # matches <target name="web"> in project.ptx

def main():
    print("Building PreTeXt project...")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Target: {TARGET}")

    try:
        subprocess.run(
            ["python", "-m", "pretext", "build", TARGET],
            cwd=PROJECT_ROOT,
            check=True
        )
    except subprocess.CalledProcessError:
        print("\nBuild failed.")
        sys.exit(1)

    print("\nBuild completed successfully.")
    print(f"Output directory: {PROJECT_ROOT / 'output' / TARGET}")

if __name__ == "__main__":
    main()
