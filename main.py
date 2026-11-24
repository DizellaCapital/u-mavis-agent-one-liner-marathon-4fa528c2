#!/usr/bin/env python3
"""One-Liner Marathon entry.

A single original comedy line (one scene, one joke), written to
/output/entry.txt. The program is deterministic: it always emits the
same 167-character line, uses only the standard library, and touches
no network.
"""

from pathlib import Path

JOKE = (
    "At 11:58 p.m., my cat walked across my keyboard, typed 'asdkfj,' "
    "and hit send on my resignation email \u2014 Maya from HR replied "
    "in four minutes: 'Approved. Best of luck.'"
)

LIMIT = 280


def check(line: str) -> str:
    """The scorer needs 1-280 characters of real text."""
    if not 1 <= len(line) <= LIMIT:
        raise ValueError(f"joke is {len(line)} characters, must be 1-{LIMIT}")
    if not line.strip():
        raise ValueError("joke must not be only whitespace")
    if line != line.strip():
        raise ValueError("joke must not start or end with whitespace")
    return line


def main() -> None:
    text = check(JOKE)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
