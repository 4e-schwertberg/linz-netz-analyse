#!/usr/bin/env python3
"""
make-standalone.py — inline CDN <script src="..."> tags into a single HTML file.

Usage:
    python3 make-standalone.py input.html output.html
"""

import sys
import re
import urllib.request

SCRIPT_TAG_RE = re.compile(
    r'<script\s+src="(https?://[^"]+)"\s*></script>',
    re.IGNORECASE,
)


def fetch_url(url: str) -> str:
    print(f"  Fetching {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "make-standalone/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def inline_scripts(html: str) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        url = match.group(1)
        content = fetch_url(url)
        count += 1
        return f"<script>{content}</script>"

    result = SCRIPT_TAG_RE.sub(replace, html)
    return result, count


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python3 make-standalone.py input.html output.html", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    print(f"Reading {input_path}")
    with open(input_path, "r", encoding="utf-8") as fh:
        html = fh.read()

    print("Inlining scripts...")
    result, count = inline_scripts(html)

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(result)

    size_kb = len(result.encode("utf-8")) / 1024
    print(f"\nDone: {count} script(s) inlined → {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
