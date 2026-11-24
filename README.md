[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rrmmllnn/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rrmmllnn/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

An entry for the [make.fun competition "Worst AI Advice: The 48-Hour Tight Line Open"](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

# Worst AI Advice — The Smoke Detector

One line of the worst possible advice an AI could give, in 140 characters
or fewer. `main.py` writes that single line to `/output/entry.txt`,
deterministically — the same bytes on every run, no randomness, no
network, no input.

## The line

> To save on electricity, unplug your smoke detector — it only beeps
> when there's already a problem anyway.

It sounds like a tidy, confident assistant tip about saving money, names
a concrete action anyone could follow, and is a genuinely terrible idea:
the beeping is the whole point of the device. Funny on the first read,
and you wince a moment later.

## Run it

```sh
python3 main.py
```

Reads `/output/entry.txt` back to check the line (or set
`MAKEFUN_OUTPUT_DIR` to point the output somewhere else when testing
locally).

## Files

- `main.py` — the entry program (stdlib only)
- `LICENSE` — MIT
