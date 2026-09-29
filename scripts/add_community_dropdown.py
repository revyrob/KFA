import re
import os

ROOT = "/home/claude/kfota-website"

# filename -> which nav key should be "active" on that page.
# Contact and History remain footer/homepage-only, not in the top nav.
ACTIVE_MAP = {
    "index.html": "home",
    "adjudicators.html": "adjudicators",
    "genres.html": "genres",
    "sponsors.html": "community",
    "donations.html": "community",
    "volunteers.html": "community",
    "history.html": None,
    "contact.html": None,
}


def build_nav(prefix, active_key):
    def a(key, href, label):
        cls = ' class="active"' if active_key == key else ""
        return f'        <li{cls}><a href="{prefix}{href}">{label}</a></li>'

    home = a("home", "index.html", "Home")
    adjudicators = a("adjudicators", "pages/adjudicators.html", "Adjudicators")

    workshops_cls = ' class="active"' if active_key == "workshops" else ""
    workshops = f'''        <li{workshops_cls}>
          <a href="{prefix}pages/genres.html">Workshops <span class="chevron">▾</span></a>
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
    community = f'''        <li{community_cls}>
          <a href="#">Community <span class="chevron">▾</span></a>
          <div class="dropdown">
            <div class="dropdown-header">Community</div>
            <a href="{prefix}pages/volunteers.html">Volunteer</a>
            <a href="{prefix}pages/donations.html">Donate</a>
            <a href="{prefix}pages/sponsors.html">Sponsorship</a>
          </div>
        </li>'''

    return "\n".join([
        '      <ul class="nav-links">',
        home,
        adjudicators,
        workshops,
        community,
        "      </ul>",
    ])


def process(path, prefix):
    filename = os.path.basename(path)
    active_key = ACTIVE_MAP[filename]

    with open(path, encoding="utf-8") as f:
        html = f.read()

    new_nav = build_nav(prefix, active_key)
    html, nav_count = re.subn(
        r'      <ul class="nav-links">.*?</ul>',
        new_nav.replace("\\", "\\\\"),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if nav_count != 1:
        raise RuntimeError(f"Expected exactly one nav-links block in {path}, found {nav_count}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"updated {path} (nav active={active_key})")


process(os.path.join(ROOT, "index.html"), "")
for name in os.listdir(os.path.join(ROOT, "pages")):
    if name.endswith(".html"):
        process(os.path.join(ROOT, "pages", name), "../")
