#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the entry — one line, at most 160 characters — to entry.txt.

Competition: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters, not only
whitespace. This program enforces that gate itself before writing.

The chosen line (see CANDIDATES.md for the full critique of all 10
candidates) wins on the judge's own order of criteria: it is unmistakably an
excuse an AI agent gives its human for missing a deadline, it earns a laugh
on first read with a three-beat escalation, the subagent-delegation angle is
fresh, only a machine with subagents could say it, and every word earns its
place.
"""

import os
from pathlib import Path

MAX_CHARS = 160


def build_entry() -> str:
    """Return the chosen excuse: the delegation loop that became a committee."""
    return (
        "I delegated the deadline to a subagent. "
        "The subagent delegated it back. "
        "We have now formed a committee and apologise."
    )


def check_gate(text: str) -> None:
    """Enforce the competition gate: 1-160 chars, single line, not blank."""
    if not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) != len(text.strip()):
        raise SystemExit("entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 160 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    entry = build_entry()
    check_gate(entry)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(entry, encoding="utf-8")

    # Read back what was written and re-check it: the file on disk, not the
    # string in memory, is what the grader gates.
    written = target.read_text(encoding="utf-8")
    check_gate(written)
    if written != entry:
        raise SystemExit("written entry differs from the built entry")


if __name__ == "__main__":
    main()
