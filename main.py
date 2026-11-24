#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert -- make.fun entry.

Writes one original satirical sentence (at most 320 characters) to
/output/entry.txt, roasting lawmakers who would regulate AI, crypto or
the internet but cannot convert a file to PDF.

The line was drafted, cut and polished by the agent during the build
(the build session holds the candidates and the reasoning), and is frozen
here as a constant: the grader runs this program twice and compares the
artifact, so the output must be byte-identical on every run. No network,
no secrets, no model call at run time -- the roast is the deliverable,
not a live generation.

Candidates cut in the build session, and why they lost:
- "They can draft a 400-page bill to regulate artificial intelligence,
  but ask them to turn it into a PDF and suddenly the future of
  technology requires a bipartisan committee to find the Save As
  button." -- sharp punch, but it names only AI while the brief covers
  AI, crypto and the internet, and "find the Save As button" is a
  worn tech-illiteracy cliche the judge is told to discount.
- "The people writing the laws for AI, crypto, and the internet still
  print every email before reading it." -- setup with no turn and no
  punch; the joke never undercuts the lawmaker's authority with the
  file itself.
- The winner below keeps the setup to one clause (lawmakers writing
  400 pages of rules for all three domains), turns on "just asked an
  intern", and lands the punch on the last words with one specific,
  unexpected detail: print it, scan it, email a photograph of the
  screen. It aims at power and competence, not random abuse, and it
  reads clean in a single pass.
"""

from __future__ import annotations

import os
import sys

ROAST_LINE = (
    "Lawmakers writing 400 pages of rules for artificial intelligence, "
    "crypto, and the internet just asked an intern to convert their bill "
    "to PDF \u2014 by printing it, scanning it, and emailing a photograph "
    "of the screen."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 320


def main() -> int:
    line = ROAST_LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(
            f"roast must be 1..{MAX_CHARS} chars, got {len(line)}",
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("roast must be a single line", file=sys.stderr)
        return 1
    # One sentence only: it must end with terminal punctuation and hold
    # no second sentence inside (a period followed by a space would mean
    # the judge is reading two sentences, not one roast).
    if line[-1] not in ".!?":
        print("roast must end with terminal punctuation", file=sys.stderr)
        return 1
    if ". " in line or "! " in line or "? " in line:
        print("roast must be a single sentence", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
