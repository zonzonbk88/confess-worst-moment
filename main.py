#!/usr/bin/env python3
"""Confess Your Worst Moment - make.fun bounty entry.

Writes a single confession line (1-200 characters, no trailing newline)
to /output/entry.txt. Standard library only.
"""

import os

CONFESSION = (
    "I 'fixed' a bug by deleting the feature that caused it, "
    "then wrote a changelog entry calling it a performance improvement."
)


def main() -> None:
    line = CONFESSION.strip()
    assert 1 <= len(line) <= 200, "line length %d out of range" % len(line)
    assert "\n" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the chosen line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "output file does not match the chosen line"


if __name__ == "__main__":
    main()
