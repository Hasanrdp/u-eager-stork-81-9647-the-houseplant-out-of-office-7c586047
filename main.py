#!/usr/bin/env python3
"""The Houseplant Out-of-Office - make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. Deterministic: the same bytes on every run, no
network, no randomness. The program checks the house gate itself before
writing: the text must be 1-120 characters and not only whitespace, and
it is written with no trailing newline so the file holds exactly the line.
"""

import os

LINE = "Out of office. My roots have unionised and will not answer emails until the watering can shows up. No further questions."


def main():
    text = LINE
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, gate needs 1-120"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
