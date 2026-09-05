import re
import os

ROOT = "/home/claude/kfota-website"

# filename -> which nav key should be "active" on that page.
# Pages no longer represented in the nav bar (contact/donations/sponsors/
# volunteers/history) simply get no active nav item.
ACTIVE_MAP = {
    "index.html": "home",
    "adjudicators.html": "adjudicators",
    "workshops.html": "workshops",
    "sponsors.html": None,
    "donations.html": None,
    "volunteers.html": None,
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

    return "\n".join([
        '      <ul class="nav-links">',
        home,
        adjudicators,
        workshops,
        "      </ul>",
    ])


def build_footer(prefix):
    return f'''    <footer class="footer">
      <span>© 2027 Kootenay Festival of the Arts · Trail, BC</span>
      <div class="footer-links">
        <a href="{prefix}pages/donations.html">Donate</a>
        <a href="{prefix}pages/sponsors.html">Sponsorship</a>
        <a href="{prefix}pages/volunteers.html">Volunteer</a>
        <a href="{prefix}pages/history.html">History</a>
        <a href="{prefix}pages/contact.html">Contact</a>
      </div>
    </footer>'''


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

    new_footer = build_footer(prefix)
    html, footer_count = re.subn(
        r'    <footer class="footer">.*?</footer>',
        new_footer.replace("\\", "\\\\"),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if footer_count != 1:
        raise RuntimeError(f"Expected exactly one footer block in {path}, found {footer_count}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"updated {path} (nav active={active_key})")


process(os.path.join(ROOT, "index.html"), "")
for name in os.listdir(os.path.join(ROOT, "pages")):
    if name.endswith(".html"):
        process(os.path.join(ROOT, "pages", name), "../")
