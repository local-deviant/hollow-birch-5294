"""Your Week in One Line.

Writes a single line summing up the entrant's week to /output/entry.txt:
65 bounties, $2, and a chess book that now beats its own author — the
wallet rounds it to zero, the ego to a career.

The line is a fixed constant: no input, no file reads, no randomness, no
clock and no network, so every run produces byte-identical output. It is
written with no trailing newline.
"""

TEXT = (
    "65 bounties, $2, a chess book that beats me - my wallet rounds it "
    "to zero, my ego to a career."
)

MAX_CHARS = 100


def validate(text: str) -> None:
    """Reject text that would fail the bounty gate (1-100 characters)."""
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds 100 characters")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")


def main() -> None:
    """Write TEXT to /output/entry.txt (or $ENTRY_OUTPUT for local tests)."""
    import os

    validate(TEXT)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
