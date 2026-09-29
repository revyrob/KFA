// Genre photos on the home page: pressing one plays a page-turn
// (corner rolls up, page turns away) and then opens the link.
// Styles and keyframes live in styles/main.css under .workshop-chip.
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  document.querySelectorAll(".workshop-chip").forEach((chip) => {
    const thumb = chip.querySelector(".workshop-chip-thumb");

    chip.addEventListener("click", (e) => {
      // Let new-tab / new-window clicks and reduced-motion users go straight through
      if (e.button !== 0 || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
      if (reduceMotion.matches || !thumb) return;

      e.preventDefault();
      chip.classList.add("is-turning");

      let done = false;
      const go = () => {
        if (done) return;
        done = true;
        location.href = chip.href;
      };
      // The corner-roll animation also ends on this element; wait for the page turn
      thumb.addEventListener("animationend", (ev) => {
        if (ev.animationName === "page-turn") go();
      });
      setTimeout(go, 1200); // fallback in case animationend doesn't fire
    });
  });

  // Coming back with the Back button: show the photos un-turned again
  window.addEventListener("pageshow", () => {
    document
      .querySelectorAll(".workshop-chip.is-turning")
      .forEach((chip) => chip.classList.remove("is-turning"));
  });
})();
