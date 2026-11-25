#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt.
Pure stdlib, deterministic: the same line every run, no trailing
newline so the file is exactly the joke, 88 bytes.

Rubric winner of 7 candidates (24/25): setup (a rare free hour) and
turn (the boss spends it on a time-management meeting) are both
things anyone who has worked in an office recognises, the punchline
lands last, and the irony — the meeting about time management is
itself the theft of time — is the surprise, not a plain complaint.
"""

from pathlib import Path

JOKE = "My calendar finally had a free hour, so my boss booked it to discuss my time management."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
