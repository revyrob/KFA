// Spam-protected email addresses.
// The full address never appears in the HTML (which is what spam bots scan);
// it's assembled here when the page loads. Usage:
//
//   <a data-user="name" data-domain="example.ca">name [at] example [dot] ca</a>
//     → becomes a clickable mailto: link
//   <span data-user="name" data-domain="example.ca">…</span>
//     → shows the address as plain text (e.g. for copying), not a link
//
// The "[at] … [dot]" text inside is the fallback if scripts are blocked.
document.querySelectorAll("[data-user][data-domain]").forEach((el) => {
  const address = el.dataset.user + "@" + el.dataset.domain;
  el.textContent = address;
  if (el.tagName === "A") el.href = "mailto:" + address;
});
