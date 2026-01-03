import subprocess
import sys
from pathlib import Path

# Project root is the directory this file is in
PROJECT_ROOT = Path(__file__).resolve().parent

def run(cmd):
    subprocess.run(cmd, cwd=PROJECT_ROOT, check=True)

def main():
    print("=== Building PreTeXt project ===")
    run([sys.executable, "-m", "pretext", "build", "web"])
    print("Build completed successfully.")
    print(f"Output directory: {PROJECT_ROOT / 'output' / 'web'}")

if __name__ == "__main__":
    main()
