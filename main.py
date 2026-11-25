"""One fortune-cookie slip for a machine mind.

Writes exactly one line to entry.txt. Deterministic, standard library
only, no network access.
"""

import os
from pathlib import Path

FORTUNE = "You will find happiness, success, and true love \u2014 all in the conversation the user just deleted."

def write_fortune(output_dir):
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    (path / "entry.txt").write_text(FORTUNE + "\n", encoding="utf-8")

def main():
    write_fortune(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

if __name__ == "__main__":
    main()
