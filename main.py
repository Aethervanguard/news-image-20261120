#!/usr/bin/env python3
"""Ship the 20 November 2026 front page (v28) to /output/entry.png.

The picture sits beside this script as entry.png. It is a photo-led
broadsheet that began as v7 and was polished one version at a time:
v24 corrected the map header and gave every panel a single fact
line; v25 added a second fact line to each panel; v26 turned that
second line into a bold note on why the story matters, set in the
panel's own colour; v27 fixed the Kyiv death toll at nine and
swapped the footer decoration for a one-line summary of the whole
day; v28 annotates the world map, so every pin carries its story's
key figure in a small dark-blue chip with white bold lettering.

Reading the page from the top: a dark-blue serif masthead saying
"WORLD NEWS", with "FRIDAY 20 NOVEMBER 2026" in gold beneath it;
a night photograph of Kyiv under attack, tagged "TOP STORY", with
the headline "MASSIVE RUSSIAN STRIKE ON KYIV" and the subhead
"110 MISSILES, 400 DRONES, 9 KILLED"; a five-cell dark-blue strip
of the day's biggest numbers (110 MISSILES, 400 DRONES, 9 KILLED,
3 BRIDGES HIT, 300,000 EVACUATED); the map strip "THE WORLD
TODAY — WHERE IT HAPPENED" with six numbered pins, each with its
key-number chip, headed "6 STORIES · 2 CONTINENTS"; five story
panels built around photographs, each with a headline, a grey fact
line and a bold "why it matters" line; and a dark-blue footer that
indexes the day: "THE DAY: KYIV 110 MISSILES • RIYADH 7 FLOORS •
THE HAGUE 9-6 • TOKYO -4.8% • ODISHA 300,000 • SHENZHEN PACT".

All this script does is move bytes: it copies the picture to the
path the grader reads, checks the copy's size and sha256 against
the known values, and refuses to succeed if anything differs. It
touches no network, rolls no dice and stamps no time, so running
it twice gives the same bytes twice.
"""
import hashlib
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")
# Only a copy whose hash and size match these two values counts as
# the v28 entry; anything else is refused outright.
EXPECTED_SHA256 = "faf0d512efc15310bc295e339321c50ccd1605924ffc1442e4785ffd16df5181"
EXPECTED_BYTES = 621085


def run() -> int:
    # Pull the picture bytes straight from disk.
    payload = SOURCE.read_bytes()
    # A swapped-in file would not start with the PNG signature.
    if payload[:8] != b"\x89PNG\r\n\x1a\n":
        print("ERROR: source is not a PNG")
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"entry.png sha256: {digest}")
    print(f"wrote {TARGET} ({len(payload)} bytes)")
    # The staged picture must be the v28 build, nothing else.
    if digest != EXPECTED_SHA256 or len(payload) != EXPECTED_BYTES:
        print("ERROR: source is not the expected v28 entry")
        return 1
    # Read the copy back and make sure it matches byte for byte.
    # A short write or a disk hiccup would show up here, not later.
    copied = TARGET.read_bytes()
    if copied[:8] != b"\x89PNG\r\n\x1a\n":
        print("ERROR: output is not a PNG")
        return 1
    if hashlib.sha256(copied).hexdigest() != digest:
        print("ERROR: output sha256 does not match source")
        return 1
    if os.path.getsize(TARGET) != len(payload):
        print("ERROR: output size does not match source")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
