#!/usr/bin/env python3
"""The Houseplant Out-of-Office - make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. Deterministic: the same bytes on every run, no
network, no randomness. The program checks the house gate itself before
writing: the text must be 1-120 characters and not only whitespace, and
it is written with no trailing newline so the file holds exactly the line.
"""

import hashlib
import os

LINE = "Out of office. My roots have unionised and will not answer emails until the watering can shows up. No further questions."

# Pinned fingerprint of the exact bytes this program must write: the 120-char
# line encoded as UTF-8 (120 bytes, pure ASCII).
EXPECTED_SHA256 = "e45af0e2c168c65ab5efdf6a50cadb626afabc2a407cf67c757c44d4c08817f2"
EXPECTED_BYTES = 120


def main():
    text = LINE
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, gate needs 1-120"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Post-write read-back gate: the bytes on disk must be exactly the
    # line — exact bytes, exact length (120), and the pinned sha256 digest.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt differs from the line")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(
            f"read-back length: found {len(written)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"read-back sha256: found {digest}, expected {EXPECTED_SHA256}"
        )
    print(f"verified: {len(text)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
