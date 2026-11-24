# THE DAILY ATLAS — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/zenganteng0987/news-image-20261123-v2/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/zenganteng0987/news-image-20261123-v2/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page newspaper front page summing up Monday 23 November 2026 in a
single 1024×1024 image — my entry for the make.fun bounty
["Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123).

## What is on the page

- **Lead story:** COP31 in Antalya collapses with no deal — the longest
  climate summit in history, the first to fail outright since Copenhagen 2009.
- **15 top stories**, each with a drawn scene, a headline, a short summary,
  and a `CONFIRMED · <source>` line. Unconfirmed claims carry a `CLAIM` tag
  (for example the IRGC claim about US Patriot radars, and the claimed
  downing of a US MQ-9 drone).
- **Also in the news:** 34 more stories in one line each — 49 stories in total.
- **By the numbers**, **The day in UTC** (chronology), and a **Date check**
  strip listing older news deliberately left out.
- Market figures are the Friday 20 November closes, labelled as such —
  markets were shut for the weekend. Every story was verified against two
  independent sources.

## How it works

`entry.png` is the finished front page. `main.py` (Python 3.13, standard
library only) copies it to the output directory — `MAKEFUN_OUTPUT_DIR` when
set, otherwise `/output`, falling back to `./entry.png` if the output
directory is read-only — then verifies the copy by file size and SHA-256
and prints the result. It needs no network access and writes nothing into
this repo folder.

## License

MIT — see [LICENSE](LICENSE).
