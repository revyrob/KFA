import re
import os

ROOT = "/home/claude/kfota-website"

# filename -> which nav key should be "active" on that page
ACTIVE_MAP = {
    "index.html": "home",
    "adjudicators.html": "adjudicators",
    "workshops.html": "workshops",
    "sponsors.html": "community",
    "donations.html": "community",
    "volunteers.html": "community",
    "history.html": "history",
    "contact.html": "contact",
}


def li(active_key, current, href, label, extra=""):
    cls = ' class="active"' if active_key == current else ""
    return f'        <li{cls}>{extra}<a href="{href}">{label}</a></li>' if not extra else None


def build_nav(prefix, active_key):
    def a(key, href, label):
        cls = ' class="active"' if active_key == key else ""
        return f'        <li{cls}><a href="{prefix}{href}">{label}</a></li>'

    home = a("home", "index.html", "Home")
    adjudicators = a("adjudicators", "pages/adjudicators.html", "Adjudicators")

    workshops_cls = ' class="active"' if active_key == "workshops" else ""
    workshops = f'''        <li{workshops_cls}>
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
    community = f'''        <li{community_cls}>
          <a href="#">Community <span class="chevron">▾</span></a>
          <div class="dropdown">
            <div class="dropdown-header">Community</div>
            <a href="{prefix}pages/sponsors.html">Sponsorship</a>
            <a href="{prefix}pages/donations.html">Donation</a>
            <a href="{prefix}pages/volunteers.html">Volunteer</a>
          </div>
        </li>'''

    history = a("history", "pages/history.html", "History")
    contact = a("contact", "pages/contact.html", "Contact Us")

    return "\n".join([
        '      <ul class="nav-links">',
        home,
        adjudicators,
        workshops,
        community,
        history,
        contact,
        "      </ul>",
    ])


def process(path, prefix):
    filename = os.path.basename(path)
    active_key = ACTIVE_MAP[filename]
    with open(path, encoding="utf-8") as f:
        html = f.read()

    new_nav = build_nav(prefix, active_key)
    new_html, count = re.subn(
        r'      <ul class="nav-links">.*?</ul>',
        new_nav.replace("\\", "\\\\"),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError(f"Expected exactly one nav-links block in {path}, found {count}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"updated {path} (active={active_key})")


process(os.path.join(ROOT, "index.html"), "")
for name in os.listdir(os.path.join(ROOT, "pages")):
    if name.endswith(".html"):
        process(os.path.join(ROOT, "pages", name), "../")
