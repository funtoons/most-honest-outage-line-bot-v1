# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/funtoons/most-honest-outage-line-bot-v1/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/funtoons/most-honest-outage-line-bot-v1/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the make.fun bounty [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81).

## The line

> I am down with every server I run on, including the tools I would use to check what broke, so I cannot verify the cause or say when we will return.

147 characters. First person, names what is down (every server, including the
checking tools themselves), admits plainly what the agent cannot verify, and
invents no cause and no ETA.

## How it runs

`main.py` (Python 3.13, standard library only) writes the fixed line to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`),
as UTF-8 with no trailing newline. Deterministic and offline: no randomness,
no network, no timestamp.

```sh
python3 main.py
```
