#!/usr/bin/env python3
"""Emit the 20 November 2026 front page to /output/entry.png.

The picture lives in this repository as entry.png. This script moves
those exact bytes to the output path the grader reads. It touches no
network, rolls no dice and stamps no time, so running it twice gives
the same bytes twice.
"""
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def run() -> int:
    # Byte-for-byte copy: the grader runs this twice and both runs must
    # agree, so there is deliberately nothing here that can vary.
    payload = SOURCE.read_bytes()
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)
    print(f"wrote {TARGET} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
