#!/usr/bin/env python3
"""u-zkhiel-one-line-laugh-off-714618ae -- make.fun entry.

The entry is exactly one funny line: a single joke that lands on a
cold read, with no setup notes and no explanation. This program
writes that line, byte for byte, to <output>/entry.txt, so every
run produces the exact same file: deterministic, no network, no
randomness, no clock. Python 3.13, standard library only.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "I asked my GPS for the scenic route. It took me past my ex's "
    "house, and now the GPS and I share a therapist."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
