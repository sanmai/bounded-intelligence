#!/usr/bin/env python3
"""Pulls descriptions from chapters. Descriptions defined as:
    <!-- description: A short summary. -->
"""

import html
import re
import sys
from pathlib import Path

LIMIT = 160
SKIP = {"index.html", "404.html", "print.html", "toc.html"}

AUTHORED = re.compile(r"<!--\s*description:\s*(.*?)\s*-->", re.S)
PARAGRAPH = re.compile(r"<main>.*?<p>(.*?)</p>", re.S)
META = re.compile(r'<meta name="description" content="[^"]*">')
TAG = re.compile(r"<[^>]+>")


def source_text(page):
    match = AUTHORED.search(page) or PARAGRAPH.search(page)
    return match and html.unescape(TAG.sub("", match.group(1)))


def shorten(text):
    text = " ".join(text.split())
    if len(text) <= LIMIT:
        return text
    return text[: LIMIT - 1].rsplit(" ", 1)[0].rstrip(",.;:") + "…"


def describe(path):
    page = path.read_text()
    text = source_text(page)
    if not text:
        return
    meta = '<meta name="description" content="%s">' % html.escape(shorten(text))
    path.write_text(META.sub(lambda _: meta, page, count=1))


for path in Path(sys.argv[1] if len(sys.argv) > 1 else "book/html").rglob("*.html"):
    if path.name not in SKIP:
        describe(path)
