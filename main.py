#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

The line: an escape room on fire. Eleven adults, four seconds.
No setup, no explanation -- the punchline lands on the last two
words, and every word before them earns its place.
"""

import os

ENTRY = "The escape room caught fire and eleven adults solved it in four seconds."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    # Gate: UTF-8 text, 1-200 characters, not only whitespace.
    # len() counts characters, matching the gate's character limit.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Deterministic: same bytes on every run, no timestamps, no randomness.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
