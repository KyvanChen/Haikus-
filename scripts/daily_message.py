#!/usr/bin/env python3
"""Pick ONE random haiku or confidence-boosting message and drop it into
README.md between the MESSAGE:START / MESSAGE:END markers. Called multiple
times per day (1-10x, randomly) by .github/workflows/daily-message.yml.
"""
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MESSAGES_PATH = ROOT / "messages.json"
README_PATH = ROOT / "README.md"

START_MARKER = "<!-- MESSAGE:START -->"
END_MARKER = "<!-- MESSAGE:END -->"


def format_message(item: dict) -> str:
    if item["type"] == "haiku":
        lines = item["text"].split("\n")
        body = "\n".join(f"> {line}" for line in lines)
        return f"**Haiku of the day**\n\n{body}"
    return f"**Today's boost**\n\n> {item['text']}"


def main() -> None:
    messages = json.loads(MESSAGES_PATH.read_text())
    choice = random.choice(messages)
    block = format_message(choice)

    readme = README_PATH.read_text()
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    replacement = f"{START_MARKER}\n{block}\n{END_MARKER}"
    if pattern.search(readme):
        readme = pattern.sub(replacement, readme)
    else:
        readme = readme.rstrip() + f"\n\n{replacement}\n"
    README_PATH.write_text(readme)


if __name__ == "__main__":
    main()
