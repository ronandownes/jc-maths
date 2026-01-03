"""
build.py
Build the Junior Cycle Maths PreTeXt project.
Run from the project root.
"""

import subprocess
import sys
from pathlib import Path

# The project root is the directory this file lives in
PROJECT_ROOT = Path(__file__).resolve().parent
TARGET = "web"

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
        print("Build failed.")
        sys.exit(1)

    print("Build completed successfully.")
    print(f"Output directory: {PROJECT_ROOT / 'output' / TARGET}")

if __name__ == "__main__":
    main()
