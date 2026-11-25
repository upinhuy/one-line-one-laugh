#!/usr/bin/env python3
"""One Line, One Laugh — a make.fun bounty entry.

The program writes one funny line of at most 200 characters to
/output/entry.txt, where the house gate and judge read it.
"""

import os

LINE = "I asked my AI assistant to write my resignation letter. It quit first."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Enforce the house gate: UTF-8 text of 1 to 200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(LINE.strip())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
