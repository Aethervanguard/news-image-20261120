#!/usr/bin/env python3
"""Write the 20 November 2026 world-news summary image to /output/entry.png.

Reads entry.png from this repository and copies it byte-for-byte to
/output/entry.png. No network, no randomness, no timestamps: two runs
produce byte-identical output.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    with open(DST, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (DST, len(data)))


if __name__ == "__main__":
    main()
