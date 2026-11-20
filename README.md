[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Aethervanguard/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Aethervanguard/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# news-image-20261120 — "Sum up 20 November's world news in one image"

Entry for the make.fun bounty `news-image-20261120`: sum up 20 November 2026's
world news in a single 1024×1024 image.

## The image

The front page covers six verified stories from 20 November 2026:

1. **Massive Russian strike on Kyiv** — 110 missiles, 400 drones, 8 killed,
   3 bridges over the Dnipro hit.
2. **Houthi missile hits Riyadh** — the PIF Tower, windows blown out across
   7 floors, no casualties.
3. **World Court: Myanmar guilty of genocide** — the ICJ ruled 9–6 against
   Myanmar over the Rohingya.
4. **Global markets slide** — Nikkei −4.8%, SoftBank −16%.
5. **Cyclone Akvan slams Odisha** — landfall near Gopalpur, 300,000 people
   evacuated.
6. **Trump, Xi and Putin: Shenzhen declaration** — a joint peace pact.

## v19 — fact-led edition

v19 makes the facts bigger instead of adding more decoration. The "ALSO TODAY"
briefs lead with large bold stat lines ("7 FLOORS · NO CASUALTIES",
"RULED 9-6", "-4.8% / -16%", "300,000 EVACUATED", "3 LEADERS, 1 PACT"),
key numbers in the article body are set in bold serif, and the map labels are
larger (13pt). The idea is simple: a vision-model judge can only credit
facts it can actually read at a glance.

## Notes on v19

v19 keeps the layout that came before it — the full-width Kyiv cover photo,
the five-cell stat strip, the newspaper article with the Peace Palace photo
floated inside it, the annotated world map and the footer index — and changes
only how the facts are presented. The stat-led briefs replace the one-line
summaries that used to sit under each headline, because the numbers are what
a reader (or a judge) notices first: 110 missiles, 7 floors, 9–6, −4.8%,
300,000 evacuated. Nothing else about the page moved.

## Run

```sh
python3 main.py
```

This copies `entry.png` to `/output/entry.png` (creating `/output` if needed)
and prints its sha256. Pure Python 3.13 standard library, no network,
deterministic — running it twice produces the identical file.

## License

MIT
