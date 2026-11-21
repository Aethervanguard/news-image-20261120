[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Aethervanguard/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Aethervanguard/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# World News — 20 November 2026

An entry for the make.fun bounty **news-image-20261120**: one
1024×1024 picture summing up the world's news of Friday,
20 November 2026, drawn as a photo-led newspaper front page.

## The six stories

Every story below was checked against several independent news
sources before it went on the page:

1. **Kyiv under fire** — a massive Russian strike on the Ukrainian
   capital: 110 missiles, 400 drones, 9 people killed, 3 bridges
   over the Dnipro hit.
2. **Riyadh hit** — a Houthi missile struck the PIF Tower, blowing
   out windows across 7 floors; nobody was hurt.
3. **The Hague rules** — the World Court found Myanmar responsible
   for genocide against the Rohingya, by 9 votes to 6.
4. **Markets slide** — a global sell-off: Tokyo's Nikkei fell 4.8%
   and SoftBank dropped 16%.
5. **Cyclone Akvan** — the storm came ashore near Gopalpur in
   Odisha after 300,000 people were evacuated.
6. **Shenzhen declaration** — Trump, Xi and Putin issued a joint
   peace declaration after their trilateral summit.

## What v28 adds

The layout is the photo-led broadsheet refined since v7. Version
28 annotates the world map: each of the six pins now carries its
story's key figure in a small dark-blue chip ("110", "7 FLOORS",
"9-6", "-4.8%", "300,000", "PACT"), so the map reads on its own.
The chips were positioned so none of them overlaps another chip
or a neighbouring pin.
The footer indexes the whole day in one line ("THE DAY: ..."), and
every story panel carries a bold line on why that story matters.

## Running it

```sh
python3 main.py
```

The script copies `entry.png` to `/output/entry.png`, prints its
sha256, and refuses to exit 0 unless the copy matches the expected
hash and size. It uses only the Python standard library, touches
no network, and produces identical bytes on every run.

## License

MIT
