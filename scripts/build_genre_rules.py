"""Copy each genre's Supplementary Rules onto the All Genres page.

The Supplementary Rules live on each genre page (pages/dance.html, etc.) in
<section ... id="rules">. The All Genres page (pages/genres.html) shows a copy of
all of them, one expandable panel per genre, between these two markers:

    <!-- BEGIN SUPPLEMENTARY RULES ... -->
    <!-- END SUPPLEMENTARY RULES -->

After editing the Supplementary Rules on any genre page, re-run from the repo root:

    python scripts/build_genre_rules.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"

GENRES = [
    ("dance", "Dance"),
    ("piano", "Pianoforte"),
    ("voice", "Voice &amp; Speech Arts"),
    ("winds", "Woodwinds, Brass &amp; Bands"),
    ("strings", "Strings &amp; Classical Guitar"),
]

SECTION = re.compile(
    r'<section class="syl-section" id="rules">\s*<h2>Supplementary Rules</h2>(.*?)\n          </section>',
    re.S,
)
BEGIN = re.compile(r"<!-- BEGIN SUPPLEMENTARY RULES[^>]*-->")
END = "<!-- END SUPPLEMENTARY RULES -->"


def panel(slug, title):
    html = (PAGES / f"{slug}.html").read_text(encoding="utf-8")
    m = SECTION.search(html)
    if not m:
        raise SystemExit(f"No Supplementary Rules section found in pages/{slug}.html")
    # Headings drop one level inside the panel (the genre name is the panel title)
    inner = m.group(1).replace("<h3>", "<h4>").replace("</h3>", "</h4>")
    return (
        f'            <details class="rules-panel" id="rules-{slug}">\n'
        f"              <summary>{title}</summary>\n"
        f'              <div class="rules-panel-body">{inner}\n'
        f'                <p><a href="../pages/{slug}.html">Open the full {title} syllabus →</a></p>\n'
        f"              </div>\n"
        f"            </details>\n"
    )


def main():
    path = PAGES / "genres.html"
    page = path.read_text(encoding="utf-8")
    b = BEGIN.search(page)
    e = page.index(END)
    generated = "\n" + "".join(panel(s, t) for s, t in GENRES)
    page = page[: b.end()] + generated + page[e:]
    path.write_text(page, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)} with {len(GENRES)} genres.")


if __name__ == "__main__":
    main()
