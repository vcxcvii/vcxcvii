"""Rebuild README.md sections from varunchoraria.com/api/latest.json."""

import json
import pathlib
import re
import urllib.request

API_URL = "https://www.varunchoraria.com/api/latest.json"
README = pathlib.Path(__file__).parent / "README.md"


def replace_chunk(content, marker, chunk):
    pattern = re.compile(
        rf"<!-- {marker} starts -->.*<!-- {marker} ends -->",
        re.DOTALL,
    )
    replacement = f"<!-- {marker} starts -->\n{chunk}\n<!-- {marker} ends -->"
    return pattern.sub(replacement, content)


def format_entries(entries):
    return "\n".join(
        f"- [{e['title']}]({e['url']}) · {e['date']}" for e in entries
    )


def main():
    with urllib.request.urlopen(API_URL) as response:
        data = json.load(response)

    content = README.read_text()
    content = replace_chunk(content, "notes", format_entries(data["notes"]))
    content = replace_chunk(content, "til", format_entries(data["til"]))
    README.write_text(content)


if __name__ == "__main__":
    main()
