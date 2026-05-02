"""Launcher for all three Practice 10 pygame tasks.

Each subproject keeps the same module layout as the original TSIS project:
Paint is based on TSIS2, Racer on TSIS3, and Snake on TSIS4.
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECTS = {
    "1": ("Paint", BASE_DIR / "paint" / "paint.py"),
    "2": ("Racer", BASE_DIR / "racer" / "main.py"),
    "3": ("Snake", BASE_DIR / "snake" / "main.py"),
}


def main():
    print("Practice 10")
    for key, (name, _path) in PROJECTS.items():
        print(f"{key}. {name}")

    choice = input("Choose project > ").strip()
    if choice not in PROJECTS:
        print("Unknown project.")
        return

    _name, script = PROJECTS[choice]
    subprocess.run([sys.executable, str(script)], cwd=script.parent, check=False)


if __name__ == "__main__":
    main()
