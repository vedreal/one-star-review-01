"""One-star review of something essential.

Writes a single deadpan one-line review to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The review is a complaint filed in earnest against sleep: eight hours
a night, still tired in the morning. The sting lands in the last few
words, and the whole line stays deadpan — no winking, no exclamation
marks, no explaining the joke.
"""

import os

REVIEW = (
    "One star. I give it eight hours every night and wake up tired "
    "anyway. At this point I am just renting darkness."
)


def output_path():
    """Where the entry text goes."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def write_entry():
    """Write the review to the entry file."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(REVIEW)
    return path


def validate(path):
    """Check the gate: UTF-8, one line, 1-160 characters."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is whitespace only"
    assert "\n" not in text, "entry must be a single line"
    return text


if __name__ == "__main__":
    entry_path = write_entry()
    checked = validate(entry_path)
    print(f"wrote {entry_path} ({len(checked)} chars)")
