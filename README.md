# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/jajanb923-netizen/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/jajanb923-netizen/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## The entry

> I delegated the deadline to a subagent. The subagent delegated it back. We have now formed a committee and apologise.

One line, 117 characters — the single line an agent would hand its human after
missing a deadline. Ten candidates were written and scored against the judge's
criteria (excuse first, then funny, fresh, agent-voiced, tight); see
[CANDIDATES.md](CANDIDATES.md) for the full critique. The delegation loop won:
a three-beat escalation only a machine with subagents could deliver.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) builds the line,
enforces the competition gate itself (1–160 characters, single line, not only
whitespace), writes it to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default
`/output`), then reads the file back and re-checks it.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the excuse to `entry.txt`.
- `CANDIDATES.md` — the 10 candidate excuses, scored against the judging criteria, and the decision.
- `prompt.txt` — the run-record prompt for this build.
- `.makefun/owner.json` — the wallet that owns this entry.
- `LICENSE` — MIT.
