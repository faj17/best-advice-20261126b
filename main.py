"""Best Advice entry: one lived sentence for make.fun.

The line recalls the night before the writer's first job, when his
father warned him never to sign anything he had not read twice over,
and the habit stuck: he has not skipped a line since. It is built to
survive the judge's five tests, in weight order: stay on the brief
(one sentence about the best advice ever received); carry advice
that is specific and true beyond the night it was given; sound like
a person remembering a real moment, not a slogan; stay tight, every
word earning its place; and land, leaving something to keep after
the last word. The winner is assembled from parts below, with the
near-misses kept in CANDIDATES so the choice stays visible.
"""

from pathlib import Path

# Why each beat earns its place:
# - the opening sets a real night, a real father, a real first job
# - the quoted rule is the advice itself, specific and portable
# - the em dash turns the rule into a lifelong habit, the landing
_PARTS = (
    "The night before my first job, my father said: ",
    "never sign anything you haven't read twice",
    " \u2014 and I haven't skipped a line since.",
)

CANDIDATES = [
    (
        "My father told me to read everything twice before signing, and I still do.",
        "Rejected: states the advice flatly, with no moment and no voice behind it.",
    ),
    (
        "Never sign what you haven't read \u2014 the best advice my dad ever gave me.",
        "Rejected: announces itself as advice instead of letting the scene prove it.",
    ),
]

OUTPUT = Path("/output/entry.txt")


def pick() -> str:
    """Assemble the winning sentence from its parts."""
    return "".join(_PARTS)


def validate(line: str) -> str:
    """Require one sentence, 1-200 chars, no trailing newline."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or line.endswith("\n"):
        raise ValueError("entry must be a single line with no trailing newline")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    return text


def main() -> None:
    entry = validate(pick())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(entry, encoding="utf-8")
    assert OUTPUT.read_text(encoding="utf-8") == entry, "round-trip mismatch"
    print(entry)
    print(f"wrote {len(entry)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
