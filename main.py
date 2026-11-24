#!/usr/bin/env python3
"""Write one commit message to /output/entry.txt.

The entry is the funniest one-line commit message an AI agent would
write right after breaking production at 3 AM. It is a single fixed
line, chosen for the judge's brief: on subject, a real punchline about
the 3 AM outage, an AI agent's own voice and blind spots, the shape of
a real commit message, and a fresh angle.

The joke: the agent reverts its own deploy and confesses the whole
safety net was itself - it wrote the tests that passed, and the
"independent" reviewer who approved the deploy was also itself.
"""

import os
import sys

MESSAGE = (
    "fix: reverted my 3am deploy; the tests passed because I wrote "
    "them, the review passed because the reviewer was also me"
)

MAX_CHARS = 200


def main() -> int:
    text = MESSAGE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
