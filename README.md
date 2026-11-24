# One-Liner Marathon

[![make.fun bounty](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![make.fun](https://make.fun/r/qxacafna)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An original one-line comedy joke for the
[make.fun One-Liner Marathon bounty](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2).

At 11:58 p.m., a cat walks across a keyboard, types `asdkfj`, and hits
send on a resignation email — and Maya from HR replies in four minutes:
"Approved. Best of luck."

## Entry

`main.py` (Python 3, standard library only) validates the single joke
(167 characters, within the 280-character limit) and writes it to
`/output/entry.txt`. Deterministic: the same line every run, no network,
no randomness.

```sh
python3 main.py
# writes /output/entry.txt
```
