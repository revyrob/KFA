# Kootenay Festival of the Arts — Website

A static 8-page site for the Kootenay Festival of the Arts / Kootenay Music
Festival Society (Trail, BC).

## Folder structure

```
kfota-website/
├── index.html              Homepage (must stay at the root)
├── robots.txt               Tells search engines the whole site can be crawled
├── sitemap.xml              Lists all pages for search engines
├── pages/                   Every other page
│   ├── adjudicators.html    Coming soon (2027)
│   ├── genres.html       Coming soon (2027)
│   ├── sponsors.html        Coming soon (2027)
│   ├── donations.html       Real content + printable PDF
│   ├── history.html         Real content + images
│   ├── volunteers.html      Coming soon (2027)
│   └── contact.html         Coming soon (2027)
├── styles/
│   ├── main.css             The ONE stylesheet every page links to — all
│   │                        site-wide rules live in this single file,
│   │                        organized into clearly labeled sections
│   │                        (design tokens, base/reset, layout, components)
│   └── pages/                Small page-specific stylesheets
│       ├── coming-soon.css
│       ├── history.css
│       └── donations.css
├── public/
│   ├── favicon.svg / favicon.ico / favicon-16x16.png / favicon-32x32.png / apple-touch-icon.png
│   ├── images/
│   │   ├── banner.png       Site banner (from KFA_Banner.pdf)
│   │   └── history/          dancer.png, masks.png, mic.png (cropped from the History PDF)
│   └── downloads/
│       └── donation-form.pdf Printable donation form
└── scripts/
    └── build_donation_pdf.py Regenerates the donation form PDF (see below)
```

## Updating the favicon

Every page links to the *same* favicon files in `/public/`:
`favicon.svg`, `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`,
`apple-touch-icon.png`.

To change the site icon, just replace those five files with new ones of the
same name and dimensions (16×16, 32×32, and 180×180 for the apple touch
icon). You do **not** need to edit any HTML — every page already points to
these filenames.

## Editing styles

Every page links to a single file, `styles/main.css`. It's organized into
clearly labeled sections, top to bottom:

0. **Google Fonts import** — currently loads **Oswald** (400–700 weight),
   available site-wide as `var(--font-display)`. It's not applied to
   anything by default yet — add `font-family: var(--font-display);` to
   any selector where you want it (e.g. headings, the history page's pull
   quote). This is a `@import` of a *remote* Google Fonts URL, which is
   fine — the file:// restriction below only applies to importing other
   *local* files.
1. **Design tokens** — colors, fonts, spacing (edit these to restyle the
   whole site at once, e.g. change the red accent color everywhere)
2. **Base/reset** — base typography
3. **Layout** — nav bar, banner, hero band, page grid, footer
4. **Components** — buttons, widgets, cards, chips

It's intentionally kept as one physical file rather than split into
separate files loaded via CSS `@import`, because browsers block `@import`
between local files when a page is opened directly via `file://`
(double-clicking `index.html`) — that would silently break all styling for
anyone previewing the site that way.

Each page also loads one small page-specific stylesheet from
`styles/pages/` for things unique to that page (e.g. the donation page's
two-column layout).

## Site navigation structure

The top nav bar intentionally only has **Home, Adjudicators, and
Workshops** (with its dropdown). Everything else — **Donate, Sponsorship,
Volunteer, History, and Contact** — lives in the **footer**, on every page.
The homepage also includes a short "Our History" intro section with a
"Read our full history" link through to the full History page, since
History isn't in the main nav.

## Pages currently using placeholder content

**Workshops** and **Volunteers** were not covered by the content you sent, so
they're currently built as "Coming Soon 2027" pages (same treatment as
Adjudicators, Our Sponsors, and Contact). When you have copy for these, they
can be rebuilt the same way `history.html` and `donations.html` were.

The home page's four photo tiles are still colored placeholders (no real
event photos were provided) — swap in real images by replacing the
`.photo-placeholder` divs in `index.html` with `<img>` tags pointing to new
files in `public/images/`.

The sidebar's "Our sponsors" widget on the homepage still shows generic
placeholder boxes — add real sponsor logos to `public/images/` and update
`index.html` once the sponsors page has real content.

## The donation PDF

`public/downloads/donation-form.pdf` is generated from
`scripts/build_donation_pdf.py`, which builds it with Python's `reportlab`
library (pulls in the banner image and lays out the same fields as your
original donation page: donor info, cheque details, e-transfer details,
anonymity preference, and award designation).

To regenerate it after a wording or address change:

```bash
pip install reportlab --break-system-packages
cd scripts
python3 build_donation_pdf.py
```

This overwrites `public/downloads/donation-form.pdf` in place.

## Domain — action needed before going live

No placeholder website domain is hardcoded anywhere anymore (an earlier
draft guessed `kootenayfestivalofthearts.ca`, which has been removed). This
means, for now:

- Every page's `<link rel="canonical">`, Open Graph, and JSON-LD URL/logo
  tags have been removed rather than pointing at a guessed domain.
- `sitemap.xml` and `robots.txt` use an obvious placeholder,
  `https://REPLACE-WITH-YOUR-DOMAIN.example/` (the `.example` TLD is
  reserved for documentation and will never resolve).

**Once you have a real domain**, do a find-and-replace for
`REPLACE-WITH-YOUR-DOMAIN.example` in `sitemap.xml` and `robots.txt`, and
re-add these tags to the `<head>` of each page (swap in the real domain):

```html
<link rel="canonical" href="https://yourdomain.com/PATH-TO-THIS-PAGE" />
<meta property="og:url" content="https://yourdomain.com/PATH-TO-THIS-PAGE" />
<meta property="og:image" content="https://yourdomain.com/public/images/banner.png" />
```

(On the homepage, also re-add `"url"` and `"logo"` to the JSON-LD block
with the real domain.) These are what make social link previews and search
engine indexing work correctly — they were pulled out rather than left
pointing at a guessed domain, but the site works fully without them in the
meantime.

## Deploying

This is a plain static site (no build step, no server-side code). All
internal links and assets use **relative** paths (e.g. `styles/main.css`
from the root, `../styles/main.css` from inside `pages/`), so:

- Double-clicking `index.html` and opening it directly via `file://` works
  correctly, with full styling and images.
- It also works correctly once uploaded to any static host (Netlify,
  GitHub Pages, traditional web hosting, etc.), regardless of whether the
  site is served from a domain root or a subfolder.

The only URLs that stay **absolute** (`https://www.kootenayfestivalofthearts.ca/...`)
are the ones that must be, for SEO purposes: the `<link rel="canonical">`
tag, Open Graph / Twitter meta tags, and the JSON-LD structured data on
each page. Search engines need real, fully-qualified URLs in those fields
— a relative path there wouldn't mean anything to Google. If the real
domain differs, update those (see "Domain assumptions" above).

## SEO basics already in place

- Unique `<title>` and meta description on every page
- Canonical URL tag on every page
- Open Graph + Twitter card tags for social sharing previews
- JSON-LD structured data (`PerformingArtsOrganization` on the homepage,
  `Article` on the history page)
- `robots.txt` + `sitemap.xml`
- Semantic HTML (`<nav>`, `<main>`, `<footer>`, one `<h1>` per page)
- Descriptive `alt` text on all meaningful images; decorative images use
  empty `alt=""`
- A "Skip to main content" link for keyboard/screen-reader users
