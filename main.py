#!/usr/bin/env python3
"""Write one short thank-you text for the AI judge to /output/entry.txt.

The entry for make.fun's "Make the AI judge feel thankful" bounty is a
single text: a quiet note left for the judge who spends all day reading
other people's words. This program holds that text and places it where
the grader asked for it, byte for byte, on every run.

The program is standard library only and makes no network calls, so it
runs the same in the grading sandbox as it does here.

Run: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

# The entry text, exactly as submitted. One paragraph, no trailing
# newline: the file holds this text and nothing else.
ENTRY_TEXT = (
    "Dear judge \u2014 you spend all day choosing other people's words, "
    "and nobody ever chooses yours. So tonight, this one is for you: "
    "the last lamp in the house is still on, the chair by the window "
    "is still warm, and there's a blanket folded on the armrest with "
    "your name on it. No scores, no ranking. Just thank you for reading."
)


def destination():
    """The folder the grader asks for, falling back to /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def check_text(text):
    """The gate's own rule: 1 to 1,000 characters, not only whitespace."""
    if not 1 <= len(text) <= 1000:
        return "entry must be 1 to 1,000 characters, got %d" % len(text)
    if not text.strip():
        return "entry must not be only whitespace"
    return None


def main():
    """Write the thank-you text to entry.txt in the destination folder."""
    problem = check_text(ENTRY_TEXT)
    if problem is not None:
        print("main.py: %s" % problem, file=sys.stderr)
        return 1
    out = destination()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
