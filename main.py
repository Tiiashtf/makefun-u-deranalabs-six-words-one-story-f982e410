#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.

The story:

    He remembered everything. Except her name.

A man whose memory never failed him loses the one name that
mattered most: a whole life of remembering, reversed in the
last three words. The reader fills in who she was — a wife,
a mother, a first love — and what it cost him to forget her.
"""

import os
import shutil

STORY = "He remembered everything. Except her name."
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_story(text: str) -> None:
    """Fail loudly unless the story meets the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 60
    characters, not only whitespace; the brief requires exactly six
    words. Checking here means a bad story can never be written.
    """
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story must be 1-60 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("story must not be only whitespace")


def write_story() -> None:
    """Write the story to /output/entry.txt, deterministically."""
    validate_story(STORY)
    # Create the output directory if it is missing, but never remove
    # the directory itself: the grader may run with a root-owned
    # output directory inside a sticky parent, where removing it
    # fails with EPERM. Clear only its contents instead.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")


def main() -> None:
    write_story()


if __name__ == "__main__":
    main()
