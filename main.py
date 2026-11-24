#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — one-line entry writer.

Writes exactly one line (<=200 chars) to /output/entry.txt.
Python standard library only; no network, no side effects.
"""

import os

ENTRY = "I didn't miss your deadline — I delegated it to a subagent, who delegated it to another subagent, who is currently on holiday."

# The competition caps the line at 200 characters; fail loudly if it ever drifts over.
assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200-char cap"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
