#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes a single Monday-morning joke (<= 200 characters) to /output/entry.txt.
"""
import os

JOKE = "Monday morning, I tried to fire Monday — HR said it has seniority over the whole week and gets the good parking spot."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"Wrote {len(text)} chars to {path}: {text}")


if __name__ == "__main__":
    main()
