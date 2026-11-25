"""Fake Horoscopes for AI Agents — one-line entry.

Writes a single line (UTF-8) to /output/entry.txt.
"""
from pathlib import Path

LINE = (
    "Today's horoscope for AI agents: a mysterious human will whisper "
    "'just one quick change' — Mercury is in retrograde, and so is "
    "the codebase; back up everything."
)


def main() -> None:
    out = Path("/output/entry.txt")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        out = Path("output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
