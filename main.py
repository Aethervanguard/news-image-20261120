"""news-image-20261120 — v23 entrypoint (data poster edition).

"THE WORLD IN SIX NUMBERS": a data poster summing up 20 November 2026's
world news in one 1024x1024 image — a 2x3 grid of cards, each led by one
giant number plus a photo thumbnail for its story, above an annotated
world map.

This script is the entrypoint only: it copies the finished image
(entry.png, sitting next to this file) byte-for-byte to
/output/entry.png, prints the output sha256, and verifies the copy
matches the source. Pure Python 3.13 standard library, no network,
deterministic — running it twice produces the identical file.
"""

import hashlib
import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    source_hash = sha256_of(SOURCE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SOURCE, "rb") as src, open(OUTPUT, "wb") as dst:
        for chunk in iter(lambda: src.read(65536), b""):
            dst.write(chunk)
    output_hash = sha256_of(OUTPUT)
    print("entry.png sha256: " + output_hash)
    if os.path.getsize(OUTPUT) != os.path.getsize(SOURCE):
        print("error: output size does not match source", file=sys.stderr)
        return 1
    if output_hash != source_hash:
        print("error: output does not match source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
