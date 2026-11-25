"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<=140 chars) to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = "The library fined me for returning a book I never borrowed \u2014 overdue since 1847."


def main() -> None:
    # Gate assertions: the output must be exactly one line, 1-140 chars, non-empty.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 characters, got {len(ENTRY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-assert what was actually written.
    written = open("/output/entry.txt", encoding="utf-8").read()
    assert written == ENTRY, "written output differs from entry"
    assert written.strip() and "\n" not in written, "written output must be one non-empty line"
    assert 1 <= len(written) <= 140, "written output must be 1-140 characters"


if __name__ == "__main__":
    main()
