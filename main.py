#!/usr/bin/env python3
# Unsent: The Micro-Confession Sprint — one two-part confession, max 260 chars.
# Writes the entry text to /output/entry.txt; judge scores the confession alone.
"""Unsent: The Micro-Confession Sprint entry.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.
"""
import os

ENTRY = (
    "To: my little brother\n"
    "I told Mum the money was from my savings. "
    "It was from the job I quit so you could keep yours."
)


def main():
    if not 1 <= len(ENTRY) <= 260:
        raise SystemExit(f"entry must be 1-260 chars, got {len(ENTRY)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
