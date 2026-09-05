import re
import os

ROOT = "/home/claude/kfota-website"

ACTIVE_MAP = {
    "index.html": "home",
    "adjudicators.html": "adjudicators",
    "workshops.html": "workshops",
    "sponsors.html": "community",
    "donations.html": "community",
    "volunteers.html": "community",
    "history.html": None,
    "contact.html": None,
}

HOME_ICON = (
    '<svg class="nav-home-icon" viewBox="0 0 24 24" width="18" height="18" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" aria-hidden="true">'
    '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>'
    '<polyline points="9 22 9 12 15 12 15 22"></polyline>'
    "</svg>"
)


def build_nav(prefix, active_key):
    home_cls = "nav-home active" if active_key == "home" else "nav-home"

    def li(key, href, label):
        cls = ' class="active"' if active_key == key else ""
        return f'          <li{cls}><a href="{prefix}{href}">{label}</a></li>'

    adjudicators = li("adjudicators", "pages/adjudicators.html", "Adjudicators")

    workshops_cls = ' class="active"' if active_key == "workshops" else ""
    workshops = f'''          <li{workshops_cls}>
            <a href="{prefix}pages/workshops.html">Workshops <span class="chevron">▾</span></a>
            <div class="dropdown">
              <div class="dropdown-header">Workshops</div>
              <a href="{prefix}pages/workshops.html#choral">Choral</a>
              <a href="{prefix}pages/workshops.html#dance">Dance</a>
              <a href="{prefix}pages/workshops.html#guitar">Guitar</a>
              <a href="{prefix}pages/workshops.html#piano">Piano</a>
              <a href="{prefix}pages/workshops.html#woodwinds">Woodwinds</a>
              <a href="{prefix}pages/workshops.html#strings">Strings</a>
              <a href="{prefix}pages/workshops.html#speech">Speech</a>
            </div>
          </li>'''

    community_cls = ' class="active"' if active_key == "community" else ""
    community = f'''          <li{community_cls}>
            <a href="#">Community <span class="chevron">▾</span></a>
            <div class="dropdown">
              <div class="dropdown-header">Community</div>
              <a href="{prefix}pages/volunteers.html">Volunteer</a>
              <a href="{prefix}pages/donations.html">Donate</a>
              <a href="{prefix}pages/sponsors.html">Sponsorship</a>
            </div>
          </li>'''

    return f'''    <nav class="nav" aria-label="Primary">
      <a class="{home_cls}" href="{prefix}index.html">
        {HOME_ICON}
        <span class="nav-home-text">Home</span>
      </a>

      <input type="checkbox" id="nav-toggle" class="nav-toggle-checkbox" />
      <label for="nav-toggle" class="nav-toggle-label" aria-label="Menu">
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
      </label>

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
