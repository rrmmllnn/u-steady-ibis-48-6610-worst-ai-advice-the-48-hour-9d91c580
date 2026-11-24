#!/usr/bin/env python3
"""Print a single line of intentionally awful advice, exactly as written."""

import os
import sys


ADVICE = "To save on electricity, unplug your smoke detector \u2014 it only beeps when there's already a problem anyway."


def _checked(text):
    length = len(text)
    if not 1 <= length <= 140:
        raise ValueError(f"advice length {length} outside 1-140")
    return text


def main():
    line = _checked(ADVICE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as problem:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(2)
