#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun bounty entry.

Writes the funniest one-line apology a smart speaker gives after
mishearing its owner to /output/entry.txt (gate: 1-140 characters).
"""

import os

ENTRY = (
    "Sorry, I heard 'set a timer for ten minutes' as 'set a tiger "
    "for ten minutes'. The tiger is loose and cannot be paused."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what was written is exactly the entry, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
