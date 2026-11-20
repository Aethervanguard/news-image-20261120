#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261120 — v19 (fact-led edition).

Reads the pre-rendered 1024x1024 news image `entry.png` sitting next to this
script and copies it byte-for-byte to /output/entry.png, so the grader sees
exactly the image this entry was built from. Pure Python 3.13 standard
library, no network access, fully deterministic: the same input always
produces the same output.
"""

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def main() -> int:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    digest = hashlib.sha256(DEST.read_bytes()).hexdigest()
    print(f"entry.png sha256: {digest}")
    # Verify the copy is byte-identical to the source image.
    source_digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if source_digest != digest:
        print("ERROR: output differs from source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
