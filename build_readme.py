"""Rebuild README.md sections from varunchoraria.com's RSS feed.

Each section in the README fetches its data from an independent source,
so no single API schema change can break the whole thing.
"""

import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET

FEED_URL = "https://www.varunchoraria.com/feed.xml"
README = pathlib.Path(__file__).parent / "README.md"


def replace_chunk(content, marker, chunk):
    pattern = re.compile(
        rf"<!-- {marker} starts -->.*<!-- {marker} ends -->",
        re.DOTALL,
    )
    replacement = f"<!-- {marker} starts -->\n{chunk}\n<!-- {marker} ends -->"
    return pattern.sub(replacement, content)


def marker_exists(content, marker):
    pattern = re.compile(rf"<!-- {marker} starts -->.*<!-- {marker} ends -->", re.DOTALL)
    return bool(pattern.search(content))


def format_entries(entries):
    return "\n".join(
        f"- [{e['title']}]({e['url']}) · {e['date']}" for e in entries
    )


def fetch_feed(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def parse_feed_entries(xml_data, limit=5):
    root = ET.fromstring(xml_data)

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries = []
    for entry in root.findall("atom:entry", ns)[:limit]:
        title = entry.find("atom:title", ns).text
        link = entry.find("atom:link", ns).attrib["href"]
        published = entry.find("atom:published", ns).text[:10]
        entries.append({"title": title, "url": link, "date": published})

    return entries


def main():
    xml_data = fetch_feed(FEED_URL)
    feed_entries = parse_feed_entries(xml_data)

    content = README.read_text()

    if feed_entries and marker_exists(content, "notes"):
        content = replace_chunk(content, "notes", format_entries(feed_entries))

    README.write_text(content)


if __name__ == "__main__":
    main()
