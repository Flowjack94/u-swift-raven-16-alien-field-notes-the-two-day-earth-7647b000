"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one original line of plain text — a review of planet Earth left
by an alien tourist — to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Deterministic: every run produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "The locals keep small predators as roommates, feed them by hand, "
    "and apologize when ignored. Delightful hosts. "
    "5/5 stars \u2014 would pet again."
)


def validate_entry(line: str) -> None:
    """Raise unless the line is a valid sealed-gate entry."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    for ch in line:
        code = ord(ch)
        if code < 0x20 or code == 0x7F or 0x80 <= code <= 0x9F:
            raise ValueError(
                "entry must not contain control characters "
                "(found U+%04X)" % code
            )
    line.encode("utf-8")  # raises unless the line is valid UTF-8 text


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))


if __name__ == "__main__":
    sys.exit(main())
