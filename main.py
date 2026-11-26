#!/usr/bin/env python3
"""Entry for make.fun — The Robot Vacuum's Funniest Excuse.

Writes the chosen excuse to /output/entry.txt and prints it.
The vacuum explains the missed spot as an aviation-style holding
pattern that ended in a fuel emergency.
"""

import os

SETUP = "I circled that spot for forty minutes,"
TURN = "then declared a fuel emergency"
PUNCH = "and went home."

ENTRY = " ".join([SETUP, TURN, PUNCH])

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
