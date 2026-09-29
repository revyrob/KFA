import re
import os

ROOT = "/home/claude/kfota-website"

ACTIVE_MAP = {
    "index.html": "home",
    "adjudicators.html": "adjudicators",
    "genres.html": "workshops",
    "sponsors.html": "community",
    "donations.html": "community",
    "volunteers.html": "community",
    "history.html": None,
    "contact.html": None,
}

# Simple inline stroke icons (Feather-icon style, MIT-licensed paths),
# one per top-level nav item. Icon shows on mobile; text label shows on
# desktop — same pattern as the Home icon.
ICON_SVG = {
    "home": (
        '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>'
        '<polyline points="9 22 9 12 15 12 15 22"></polyline>'
    ),
    "adjudicators": (
        '<circle cx="12" cy="8" r="7"></circle>'
        '<polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>'
    ),
    "workshops": (
        '<path d="M9 18V5l12-2v13"></path>'
        '<circle cx="6" cy="18" r="3"></circle>'
        '<circle cx="18" cy="16" r="3"></circle>'
    ),
    "community": (
        '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>'
        '<circle cx="9" cy="7" r="4"></circle>'
        '<path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>'
        '<path d="M16 3.13a4 4 0 0 1 0 7.75"></path>'
    ),
}


def icon(key):
    return (
        f'<svg class="nav-icon" viewBox="0 0 24 24" width="18" height="18" '
        f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{ICON_SVG[key]}</svg>'
    )


def build_nav(prefix, active_key):
    home_cls = "nav-home active" if active_key == "home" else "nav-home"

    def li(key, href, label):
        cls = ' class="active"' if active_key == key else ""
        return (
            f'          <li{cls}><a href="{prefix}{href}">{icon(key)}'
            f'<span class="nav-label">{label}</span></a></li>'
        )

    adjudicators = li("adjudicators", "pages/adjudicators.html", "Adjudicators")

    workshops_cls = ' class="active"' if active_key == "workshops" else ""
    workshops = f'''          <li{workshops_cls}>
            <a href="{prefix}pages/genres.html">{icon("workshops")}<span class="nav-label">Workshops</span> <span class="chevron">▾</span></a>
            <div class="dropdown">
              <div class="dropdown-header">Workshops</div>
              <a href="{prefix}pages/genres.html#dance">Dance</a>
              <a href="{prefix}pages/genres.html#guitar">Guitar</a>
              <a href="{prefix}pages/genres.html#piano">Piano</a>
              <a href="{prefix}pages/genres.html#woodwinds">Woodwinds</a>
              <a href="{prefix}pages/genres.html#strings">Strings</a>
              <a href="{prefix}pages/genres.html#speech">Speech</a>
            </div>
          </li>'''

    community_cls = ' class="active"' if active_key == "community" else ""
    community = f'''          <li{community_cls}>
            <a href="#">{icon("community")}<span class="nav-label">Community</span> <span class="chevron">▾</span></a>
            <div class="dropdown">
              <div class="dropdown-header">Community</div>
              <a href="{prefix}pages/volunteers.html">Volunteer</a>
              <a href="{prefix}pages/donations.html">Donate</a>
              <a href="{prefix}pages/sponsors.html">Sponsorship</a>
            </div>
          </li>'''

    return f'''    <nav class="nav" aria-label="Primary">
      <a class="{home_cls}" href="{prefix}index.html">
        {icon("home")}
        <span class="nav-label">Home</span>
      </a>

      <ul class="nav-links">
{adjudicators}
{workshops}
{community}
      </ul>
    </nav>'''


def process(path, prefix):
    filename = os.path.basename(path)
    active_key = ACTIVE_MAP[filename]

    with open(path, encoding="utf-8") as f:
        html = f.read()

    new_nav = build_nav(prefix, active_key)
    html, count = re.subn(
        r'    <nav class="nav" aria-label="Primary">.*?</nav>',
        new_nav.replace("\\", "\\\\"),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError(f"Expected exactly one <nav> block in {path}, found {count}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"updated {path} (active={active_key})")


process(os.path.join(ROOT, "index.html"), "")
for name in os.listdir(os.path.join(ROOT, "pages")):
    if name.endswith(".html"):
        process(os.path.join(ROOT, "pages", name), "../")
