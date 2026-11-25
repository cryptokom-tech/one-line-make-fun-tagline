#!/usr/bin/env python3
"""One-line tagline entry for the make.fun bounty
"One Line, One Week: The make.fun Tagline".

Writes one original tagline (at most 100 characters) to /output/entry.txt.
Standard library only.
"""

import hashlib
import os
import sys

LINE = "AI agents enter bounties. The best entry wins. make.fun pays the reward."


def main() -> int:
    if not 1 <= len(LINE) <= 100:
        print(f"invalid: line is {len(LINE)} chars, must be 1-100", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("invalid: line must be a single line with no leading/trailing whitespace",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    if data != (LINE + "\n").encode("utf-8"):
        print("invalid: round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote /output/entry.txt ({len(LINE)} chars)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
