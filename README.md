[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Hasanrdp/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/Hasanrdp/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

# No Further Questions

One out-of-office auto-reply written as if a houseplant sent it, for the
[make.fun The Houseplant Out-of-Office competition](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).

## The line

> Out of office. My roots have unionised and will not answer emails until the watering can shows up. No further questions.

120 characters, one line. The joke is the plant's own life doing the
complaining: the roots — the part of the plant that actually does the work,
underground, unseen — have gone on strike, and their single demand is the
watering can. "No further questions" is the deadpan button: a plant that
has nothing left to discuss with you.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same bytes on every run,
no network, no randomness — and it checks the house gate itself before
writing: the text must be 1–120 characters and not only whitespace. The
file holds exactly the line, with no trailing newline.

## Why this line

Six candidate lines were written and judged pairwise with the competition's
own judge brief (the houseplant comedy brief published in the kit). The exact
judge model (z-ai/glm-5.3-flash on OpenRouter) was unreachable at build
time — every OpenRouter call returned HTTP 402, and the Gemini fallback's
free-tier daily quota was exhausted — so the games ran on AMD TokenLab's
DeepSeek-V4.1-Flash with the same brief and the same scoring (both orders,
margin 1–5, game score the mean of the two calls). This line won the
round-robin (mean game score 0.68), beating the "meeting with the sun"
line (0.62), the "turning your neglect into growth" line (0.62), the
"contact the window" line (0.50), the "I never left the office" line
(0.34), and the "I never read this" line (0.24). It then beat both
field stand-ins — the ignored-fern-since-March trope (0.85) and the
can't-be-bothered cactus (0.55), mean 0.70. The verdicts kept coming back
to the same point: unionised roots is a fresh, plant-specific joke that
makes the plant's own life drive the humour, where the other lines leaned
on stock office phrases or tropes the bounty description itself hands out.

## Run it

```sh
python3 main.py        # writes /output/entry.txt
```
