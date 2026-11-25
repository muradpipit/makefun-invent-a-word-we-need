#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty entry.

Coins one new English word and defines it in a single clear line.

The coinage: "youtoo" names the automatic, wrong reply everyone has
given at least once — the waiter says "enjoy your meal", and before
your brain catches up your mouth has already said "you too". English
has no word for that little social misfire; "youtoo" is short, sayable,
spellable, and sounds like English could have grown it (like "goodbye"
grew out of "God be with ye"). The definition lands in one reading.
"""

import os

ENTRY = (
    'youtoo (n.): the automatic "you too" you say to the waiter '
    "who just told you to enjoy your meal."
)

# The bounty's sealed gate: /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, not only white space. Checked here too so a
# bad entry fails loudly instead of silently.

import os

ENTRY = (
    'youtoo (n.): the automatic "you too" you say to the waiter '
    "who just told you to enjoy your meal."
)


def main() -> None:
    # Deterministic by construction: ENTRY is a constant, nothing is
    # read from the environment except the output directory, and no
    # trailing newline is written, so repeated runs are byte-identical.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = ENTRY
    if not (1 <= len(text) <= 140):
        raise SystemExit("gate: entry must be 1-140 characters")
    if not text.strip():
        raise SystemExit("gate: entry must not be whitespace only")
    text.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
