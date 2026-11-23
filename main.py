#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun).

Writes a single original dad joke, at most 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness
sets it). Stdlib only; no network, no files read, no secrets.
"""

import os
import sys

JOKE = (
    "I told my kids I'm not just a rad dad - "
    "add an 'ish' and I'm a radish. "
    "That's how dads grow on you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    # The gate allows 1 to 200 characters; keep the joke well inside it.
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
