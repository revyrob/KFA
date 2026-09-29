// Site navigation — the ONE place to edit menu links.
// Every page has <nav class="nav" aria-label="Primary" id="site-nav"></nav>
// followed by a <script> tag loading this file.
(function () {
  const links = [
    { label: "Adjudicators", href: "pages/adjudicators.html" },
    {
      label: "Genres",
      href: "pages/genres.html",
      children: [
        { label: "Dance", href: "pages/genres.html#dance" },
        { label: "Pianoforte", href: "pages/genres.html#pianoforte" },
        {
          label: "Voice and Speech Arts",
          href: "pages/genres.html#voiceSpeechArts",
        },
        {
          label: "Woodwinds, Brass & Bands",
          href: "pages/genres.html#woodwindsBrassBands",
        },
        { label: "Strings", href: "pages/genres.html#strings" },
      ],
    },
    {
      label: "Community",
      href: "#",
      children: [
        { label: "Volunteer", href: "pages/volunteers.html" },
        { label: "Donate", href: "pages/donations.html" },
        { label: "Sponsorship", href: "pages/sponsors.html" },
        { label: "Contact Us", href: "pages/contact.html" },
      ],
    },
    { label: "Registration", href: "pages/registration.html" },
  ];

  // Site root, worked out from this script's location, so links work from / and /pages/
  const root = new URL("../", document.currentScript.src);
  const url = (href) => (href === "#" ? "#" : new URL(href, root).href);
  const page = (href) => new URL(href, root).pathname;

  const here = location.pathname.replace(/\/$/, "/index.html");
  const isCurrent = (l) =>
    (l.href !== "#" && page(l.href) === here) ||
    (l.children || []).some((c) => page(c.href) === here);

  const item = (l) => {
    const cls = isCurrent(l) ? ' class="active"' : "";
    if (!l.children)
      return `<li${cls}><a href="${url(l.href)}">${l.label}</a></li>`;
    return `
      <li${cls}>
        <a href="${url(l.href)}">${l.label} <span class="chevron">▾</span></a>
        <div class="dropdown">
          <div class="dropdown-header">${l.label}</div>
          ${l.children.map((c) => `<a href="${url(c.href)}">${c.label}</a>`).join("")}
        </div>
      </li>`;
  };

  const homeCls = page("index.html") === here ? " active" : "";

  document.getElementById("site-nav").innerHTML = `
    <a class="nav-home${homeCls}" href="${url("index.html")}">
      <svg class="nav-home-icon" viewBox="0 0 24 24" width="18" height="18" fill="none"
        stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
        <polyline points="9 22 9 12 15 12 15 22"></polyline>
      </svg>
      <span class="nav-home-text">Home</span>
    </a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle-checkbox" />
    <label for="nav-toggle" class="nav-toggle-label" aria-label="Menu">
      <span class="hamburger-bar"></span>
      <span class="hamburger-bar"></span>
      <span class="hamburger-bar"></span>
    </label>
    <ul class="nav-links">${links.map(item).join("")}</ul>`;
})();
