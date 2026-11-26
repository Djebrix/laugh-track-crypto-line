#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes exactly one funny line (1-200 characters) about crypto and
trading life to entry.txt in the output directory.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. Setup: buying the dip at $60K.
Turn: the dip keeps dipping, so the "long-term hold" becomes a hostage
negotiation with the chart. The program only resolves the output
directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes the
line followed by a trailing newline.
"""

import os

# One line, punchline at the end: the hold is not a strategy, it is a standoff.
LINE = "Bought the dip at $60K, it dipped to $40K, and now my long-term hold is a hostage negotiation with a chart."



def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
