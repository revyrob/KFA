// Shared syllabus content + General Rules pop-up.
//
// Used by genres.html and every genre page (dance, piano, voice, strings, winds).
// Load at the end of <body>:  <script src="../scripts/syllabus.js"></script>
//
// What it does:
//  1. Fills <div id="syllabus-intro"></div> with that genre's Dates & Venues
//     (PDF page 1; see DATES).
//     Edit DATES below to change a genre's dates.
//  2. Adds the General Rules pop-up (PDF pages 6–9). On a genre page, give
//     <body> data-require-rules="dance" (the page's name): the pop-up opens
//     automatically until the visitor scrolls to the end, ticks the box and
//     presses "Mark as read". Each genre page must be marked as read on its own.
//     Any element with data-open-rules opens it; data-open-rules="rd-awards"
//     (rd-general, rd-liability, rd-etiquette, rd-awards) jumps to that part.
//
// To make everyone re-read the rules (e.g. next season), change KEY_PREFIX.
(function () {
  var KEY_PREFIX = "kfota-rules-read-2027:";
  var PAGE = document.body.getAttribute("data-require-rules");
  var KEY = PAGE ? KEY_PREFIX + PAGE : null;

  // ---------------------------------------------------------------------------
  // Dates & Venues: PDF page 1
  // ---------------------------------------------------------------------------
  // Each genre page only shows its own dates (keyed by data-require-rules).
  var DATES = {
    dance: [["Dance", "March 4–7, 2027 at The Bailey Theatre"]],
    piano: [["Piano", "April 5–8, 2027 at First Presbyterian Church"]],
    voice: [
      ["Voice", "April 5–8, 2027 at First Presbyterian Church"],
      ["Speech", "April 5–8, 2027 at First Presbyterian Church"],
    ],
    strings: [
      ["Strings", "April 5–8, 2027 at First Presbyterian Church"],
      ["Classical Guitar", "April 5–8, 2027 at First Presbyterian Church"],
    ],
    winds: [["Woodwinds, Brass &amp; Bands", "April 5–8, 2027 at First Presbyterian Church"]],
  };
  var rows = (DATES[PAGE] || [])
    .map(function (r) {
      return "<tr><td>" + r[0] + "</td><td>" + r[1] + "</td></tr>";
    })
    .join("");
  var INTRO = `
    <section class="syl-section" id="dates">
      <h2>Dates &amp; Venues</h2>
      <table class="kv">${rows}</table>
      <h3>Highlights Concert</h3>
      <p>Saturday, April 10th, 2:00 pm Matinee, The Bailey Theatre, Trail BC.
      Participants may be selected by the adjudicators to perform.</p>
    </section>`;

  // ---------------------------------------------------------------------------
  // General Rules: PDF pages 6–9
  // ---------------------------------------------------------------------------
  var RULES = `
    <p id="rd-general"><strong>It is the responsibility of each participant to read and comply with all rules governing this festival.</strong></p>
    <p>
      The conduct of all Festivals of the Kootenay Music Festival Society (the
      "Society") will be subject to the following rules, which may be changed at
      any time by the Board of Directors of the Society without notice, provided
      that any changes, whenever possible and expedient, will not be made within
      two weeks before the official closing date for entries.
    </p>
    <ol class="rules">
      <li>The Festival is open to all participants, according to classification and conformity with rules.</li>
      <li>Participants, unless otherwise stated, are to be amateurs only. The term amateur shall mean one whose principal income is not derived from musical services. This does not apply to conductors of choirs, or to those bona fide students of music who teach music for the purpose of applying the money so earned to the furtherance of their musical education. The same conditions apply to the Speech Arts and Dance classes.</li>
      <li>Participants in Choirs, Orchestras, and Dance Groups must be bona fide members of their respective organizations. Conductors are not allowed to sing with the choirs.</li>
      <li>For classes where the age limit is specified, the age will be entered on the entry form. The acceptable age for such classes shall be as of <strong>December 31st before the upcoming festival</strong>. (For example, a participant aged 10 on December 31st, but turning 11 between that date and the Festival opening, will still be eligible to participate in the 10 years and under class.) Where the term "Open" is used, there is no restriction as to age.</li>
      <li>No entrant (solo, duos, trios, and quartets) may participate in more than one similar class in each section where the age limit is set. Exceptions are vocal or instrumental ensembles and dance groups and duos/trios.</li>
      <li>Entries for all classes must be received by the Festival Committee on the official registration platform together with the entry fee as follows:
        <ol>
          <li><strong>Dance:</strong> on or before January 8th, 2027. No entries will be accepted unless accompanied by an entry fee. Entries submitted after the closing date may be accepted up to or on January 15th, 2027.</li>
          <li><strong>Music:</strong> on or before February 19, 2027. No entries will be accepted unless accompanied by an entry fee. Entries submitted after the closing date may be accepted up to or on February 26, 2027.</li>
        </ol>
        Late entries will include a fee of $10.00 (per entry) in addition to the regular entry fee. Entry fees are non-refundable (email <a href="mailto:chairtrail@kootenayfestivalofthearts.ca">chairtrail@kootenayfestivalofthearts.ca</a> in the case of extenuating circumstances).
      </li>
      <li>The Federation of Canadian Music Festivals has now deemed it permissible to use photocopies for page turns <span class="loud">as long as the original copy is present at the performance</span>. This does not mean that the adjudicator has the original and the performer the photocopy. There will be two original copies present in the performance hall. <span class="loud">Participants attempting to use unauthorized copies of copyrighted material will be disqualified.</span> All copyrights regarding music and printed text will be observed. Manual copies of copyrighted material will not be accepted. The accompanist will perform from an original score in music classes, and the adjudicator will be given a completely original score of music under copyright. If original scores are not available, a publisher's letter is required giving permission for copying. If the selection is in the public domain, a letter confirming this fact is needed from the publisher and their consent to copy. The use of music downloaded from the Internet is permissible so long as receipts for the number of copies downloaded accompany it. If membership in a download site provides free use of the material downloaded, the participant will provide proof of membership.</li>
      <li>
        <ol>
          <li>The title and composer (or author in the case of Speech Arts) of the chosen piece and the length of its performance time will be stated on the official online entry. No substitutions, additions, or deletions are permitted after the closing date.</li>
          <li>Participants will deliver to the festival assistant a copy of their piece indicated with a bookmark upon which has been pencilled at the top the class number and participant's number according to the program before class performance. <span class="loud">The use of photocopies is strictly limited. See copyright rule no. 7.</span></li>
          <li>In "Own Choice" selection, the adjudicator will consider its suitability and artistic value.</li>
        </ol>
      </li>
      <li>The participant will perform their piece in the key in which it is set under arrangements in the edition prescribed. The memorization of pieces is recommended but not compulsory.</li>
      <li>The Festival Committee will decide the order in which the classes are to be taken and will arrange the order in which entrants will be heard. The Committee reserves the right to subdivide or cancel a class should the number of entries warrant.</li>
      <li>Set up of festival venues provided by the Committee for any scheduled performance shall be deemed to be appropriate for the due performance of the art involved, and no changes to set up of venues shall be permitted without the consent of a Festival Assistant.</li>
      <li>General Rules for the control of all premises used by the Society for Festivals will apply to all participants, teachers, and parents and will be set out in the program. Such rules are for the benefit of all participants, are intended to provide an optimum opportunity for performance, and include, but are not limited to, the following:
        <ol>
          <li>silence is essential during performances and adjudications.</li>
          <li>entrance, movement or departure in or from any Festival Hall is prohibited during performance or adjudication.</li>
          <li><span class="loud">No photography, video recordings or tape recordings are permitted during performances.</span></li>
          <li>cell phones, pagers and alarms must be turned off in Festival venues.</li>
          <li>no participant may use the stage for rehearsal during the festival unless permission is granted by the Festival for special circumstances.</li>
        </ol>
      </li>
      <li>Entrants will be notified through their teacher regarding the place, date, and time of participation and order of participation. In cases where there is no teacher, entrants will be notified by phone and/or email.</li>
      <li>Participants will be designated to perform by entry number. Participants will commence at the adjudicator's request. The adjudicator may terminate any performance at will.</li>
      <li>With the exception of Dance, participants in each class will remain seated, in the seats reserved for them, until after adjudication of the particular class.</li>
      <li>Dress Code should reflect that performance at this festival is important.</li>
      <li>No teacher may directly solicit students from another teacher during the festival. Failure to abide by this rule will prohibit offenders from entering students in this Festival for the following year.</li>
      <li>
        <ol>
          <li>If called upon by the Committee, participants will be expected to perform at any afternoon/evening session during the festival, including the Highlights Concert, and must be prepared to do so.</li>
          <li>The Adjudicators reserve the right of selection of performers for these recitals.</li>
        </ol>
      </li>
      <li>The Festival committee reserves the right to take official photos at appropriate times for archival and publicity purposes.</li>
      <li>The Adjudicator's decision in all matters of Adjudication shall be final and without appeal. Awards will be given at the Adjudicator's discretion.</li>
      <li><strong>Communication with the adjudicator on the part of the participants, teacher or parents, is ABSOLUTELY FORBIDDEN. Contravention of this rule will result in disqualification.</strong> Protests must be made in writing to the Festival Secretary during the Festival, not to the Adjudicator.</li>
      <li>Any protest about the adjudicator's decision and/or the Festival Committee's decisions or actions must be:
        <ol>
          <li>made to the Secretary of the Festival Committee,</li>
          <li>in writing before the end of the festival, and</li>
          <li>accompanied by a $25.00 protest fee. The protest fee will be returned if the protest is sustained. No protest shall be made in any manner to the adjudicator directly. Any protests received without the $25.00 protest fee, received verbally, by email or by letter to any Festival committee member from any participant, teacher, festival committee member or any other representative will not be accepted or considered.</li>
        </ol>
      </li>
    </ol>

    <h3 id="rd-liability">Liability Waiver</h3>
    <p>The Kootenay Music Festival Society is not responsible for any claims, demands or damage to musical instruments, equipment, props, or any other personal property. The Festival Society's acceptance of a participant's application for entry into the Kootenay Festival of the Arts will release any responsibility of the KMFS or volunteers for the KMFS from claims, demands, damages, actions or causes, or actions arising out of, or in consequence of, any loss, injury or damage to any participant or any participant's personal property incurred while attending or participating in the Kootenay Festival of the Arts. This clause shall also apply to all members of the public attending any/all events.</p>

    <h3 id="rd-etiquette">Concert Etiquette Is Expected</h3>
    <p>No videos, audio recordings or photographs may be taken during performances, adjudications, etc. Cell phones will be turned off within the performance venue. Kootenay Festival of the Arts reserves the right to take official photographs at appropriate times for archival and publicity purposes.</p>
    <p>We encourage you to recognize all participants on completion of their performances and to make them feel happy that you were there to watch them.</p>
    <p>A point to remember: participants who are scheduled late in a morning, afternoon, or evening session can be discouraged if most of the audience has left. If your schedule possibly permits it, please stay until the end of the session.</p>

    <h3 id="rd-awards">Adjudications and Awards</h3>
    <ol class="rules">
      <li>Music and poetry must be memorized for the student to qualify for a major award.</li>
      <li>Each participant will receive a comprehensive written adjudication.</li>
      <li>At the close of each time period, the Adjudicator will give an oral adjudication of that group. This may be done one-on-one or in a workshop manner, as per the Adjudicator's discretion. All participants must stay for the adjudication unless excused by a Festival Official.</li>
      <li>The participant, following the dismissal of the class by the Adjudicator, must pick up all written adjudication and music immediately.</li>
      <li>No marks will be given in the music section. A certificate of merit may be awarded for outstanding performances.</li>
      <li>In the dance categories marks will be assigned. A certificate of merit will be awarded for a mark of 85 or over.</li>
      <li>Monetary awards are made solely at the Adjudicator's discretion.</li>
      <li>The selection of participants to represent the Kootenay Festival of the Arts at the Provincial Festival of the Arts is the sole responsibility of the Adjudicator, subject to Provincial and local rules. The adjudicators have the interests of the students in mind when they do not recommend participants to compete in a particular discipline despite the existence of qualifying marks. Participants should live or study in the geographic area served by the Kootenay Festival of the Arts. However, if there is not a recommended participant from the geographic area, adjudicators can recommend from outside this area.</li>
    </ol>`;

  // ---------------------------------------------------------------------------
  // Storage helpers (storage can be blocked in private windows: then the pop-up
  // simply shows again on each visit)
  // ---------------------------------------------------------------------------
  function hasRead() {
    if (!KEY) return true; // overview page: rules are only for viewing there
    try {
      return localStorage.getItem(KEY) === "yes";
    } catch (e) {
      return false;
    }
  }
  function markRead() {
    if (!KEY) return;
    try {
      localStorage.setItem(KEY, "yes");
    } catch (e) {}
  }

  // 1. Front matter
  var intro = document.getElementById("syllabus-intro");
  if (intro) intro.innerHTML = INTRO;

  // 2. Pop-up
  var dialog = document.createElement("dialog");
  dialog.className = "rules-dialog";
  dialog.setAttribute("aria-labelledby", "rules-dialog-title");
  dialog.innerHTML = `
    <div class="rd-head">
      <div>
        <span class="syl-eyebrow">2027 Syllabus</span>
        <h2 id="rules-dialog-title">General Rules</h2>
        <p>Please read the General Rules before viewing your genre's syllabus.</p>
      </div>
      <button type="button" class="rd-close" aria-label="Close">&times;</button>
    </div>
    <div class="rd-body syl" tabindex="0">${RULES}
      <p class="rd-end">End of the General Rules.</p>
    </div>
    <div class="rd-foot">
      <label class="ack-label">
        <input type="checkbox" class="rd-check" disabled />
        <span>I have read and understand the General Rules, Liability Waiver, Concert Etiquette, and Adjudications &amp; Awards.</span>
      </label>
      <div class="rd-actions">
        <span class="rd-hint">Scroll to the end of the rules to continue.</span>
        <button type="button" class="btn-solid rd-done" disabled>Mark as read</button>
      </div>
    </div>`;
  document.body.appendChild(dialog);

  var body = dialog.querySelector(".rd-body");
  var check = dialog.querySelector(".rd-check");
  var done = dialog.querySelector(".rd-done");
  var hint = dialog.querySelector(".rd-hint");
  var closeBtn = dialog.querySelector(".rd-close");

  function reachedEnd() {
    if (body.scrollTop + body.clientHeight >= body.scrollHeight - 12) {
      check.disabled = false;
      hint.textContent = hasRead() ? "" : "Tick the box, then press Mark as read.";
    }
  }
  body.addEventListener("scroll", reachedEnd);
  check.addEventListener("change", function () {
    done.disabled = !check.checked;
  });

  function setLocked(locked) {
    // Until the rules are marked as read, the pop-up can't be dismissed.
    closeBtn.hidden = locked;
    dialog.classList.toggle("is-locked", locked);
  }

  function open(target) {
    var read = hasRead();
    setLocked(!read);
    check.checked = read;
    check.disabled = !read;
    done.disabled = !read;
    done.textContent = read ? "Close" : "Mark as read";
    hint.textContent = read ? "" : "Scroll to the end of the rules to continue.";
    document.documentElement.classList.add("rd-open");
    dialog.showModal();
    var el = target && dialog.querySelector("#" + target);
    body.scrollTop = 0;
    if (el) body.scrollTop = el.getBoundingClientRect().top - body.getBoundingClientRect().top - 8;
    body.focus({ preventScroll: true });
    reachedEnd(); // in case everything fits without scrolling
  }
  function close() {
    document.documentElement.classList.remove("rd-open");
    dialog.close();
    updateButtons();
  }

  done.addEventListener("click", function () {
    if (!check.checked) return;
    markRead();
    close();
  });
  closeBtn.addEventListener("click", close);
  // Escape key: only allowed once the rules have been read
  dialog.addEventListener("cancel", function (e) {
    e.preventDefault();
    if (hasRead()) close();
  });
  // Browsers may force-close a dialog on Escape anyway (Chrome does when the
  // pop-up opened without a click). If it closes before the rules are read,
  // put it straight back.
  dialog.addEventListener("close", function () {
    if (!hasRead()) {
      dialog.showModal();
      body.focus({ preventScroll: true });
    }
  });
  // Click on the backdrop: same rule
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog && hasRead()) close();
  });

  function updateButtons() {
    var read = hasRead();
    document.querySelectorAll("[data-open-rules]").forEach(function (b) {
      b.classList.toggle("is-read", read);
      if (b.hasAttribute("data-rules-status") && KEY) {
        b.textContent = read ? "✓ General Rules read: view again" : "Read the General Rules";
      }
    });
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-open-rules]");
    if (t) {
      e.preventDefault();
      open(t.getAttribute("data-open-rules"));
    }
  });

  updateButtons();
  if (KEY && !hasRead()) open();

  // ---------------------------------------------------------------------------
  // 3. Pill strip: the page's first pill list (.syl > .toc) becomes a sticky,
  //    single-row strip. The pill for the section being read is highlighted,
  //    and an edge fade + arrow show when more pills are off to the right.
  // ---------------------------------------------------------------------------
  var toc = document.querySelector(".syl > .toc:first-child");
  if (toc) {
    var strip = document.createElement("div");
    strip.className = "pill-strip";
    var inner = document.createElement("div");
    inner.className = "pill-strip-inner";
    function arrow(cls, label, points) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "pill-arrow " + cls;
      b.setAttribute("aria-label", label);
      b.innerHTML =
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="' +
        points +
        '"></polyline></svg>';
      return b;
    }
    var prev = arrow("pill-prev", "Previous sections", "15 6 9 12 15 18");
    var next = arrow("pill-next", "More sections", "9 6 15 12 9 18");
    toc.parentNode.insertBefore(strip, toc);
    strip.appendChild(inner);
    inner.appendChild(prev);
    inner.appendChild(toc);
    inner.appendChild(next);

    // Edge fades + arrow (and the scrollbar width, so the strip spans exactly
    // the visible page)
    function updateEdges() {
      document.documentElement.style.setProperty(
        "--scrollbar",
        window.innerWidth - document.documentElement.clientWidth + "px"
      );
      // Arrows only appear when the pills don't all fit, and only on the
      // side(s) the reader can still scroll towards.
      var max = toc.scrollWidth - toc.clientWidth;
      var fits = max <= 1;
      strip.classList.toggle("has-less", !fits && toc.scrollLeft > 4);
      strip.classList.toggle("has-more", !fits && toc.scrollLeft < max - 4);
    }
    toc.addEventListener("scroll", updateEdges, { passive: true });
    window.addEventListener("resize", updateEdges);
    // Pill widths change when the web font finishes loading, so re-measure then
    // and whenever the strip changes size.
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(updateEdges);
    window.addEventListener("load", updateEdges);
    if (window.ResizeObserver) new ResizeObserver(updateEdges).observe(toc);
    prev.addEventListener("click", function () {
      toc.scrollBy({ left: -toc.clientWidth * 0.7, behavior: "smooth" });
    });
    next.addEventListener("click", function () {
      toc.scrollBy({ left: toc.clientWidth * 0.7, behavior: "smooth" });
    });
    updateEdges();

    // Active pill follows the reader (pills that open the pop-up are skipped)
    var links = Array.prototype.filter.call(toc.querySelectorAll('a[href^="#"]'), function (a) {
      return !a.hasAttribute("data-open-rules") && document.querySelector(a.getAttribute("href"));
    });
    var current = null;
    function setActive(a) {
      if (a === current) return;
      if (current) {
        current.classList.remove("is-active");
        current.removeAttribute("aria-current");
      }
      current = a;
      if (!a) return;
      a.classList.add("is-active");
      a.setAttribute("aria-current", "true");
      // Slide the strip (not the page) so the active pill stays in view
      var left = a.offsetLeft - toc.offsetLeft;
      var right = left + a.offsetWidth;
      if (left < toc.scrollLeft + 56 || right > toc.scrollLeft + toc.clientWidth - 56) {
        toc.scrollTo({ left: left - 56, behavior: "smooth" });
      }
    }
    var ticking = false;
    function spy() {
      ticking = false;
      var line = strip.getBoundingClientRect().bottom + 24;
      var found = null;
      for (var i = 0; i < links.length; i++) {
        var target = document.querySelector(links[i].getAttribute("href"));
        if (target.getBoundingClientRect().top <= line) found = links[i];
      }
      // At the very bottom of the page, the last section counts as current
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
        found = links[links.length - 1] || found;
      }
      setActive(found);
    }
    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          ticking = true;
          requestAnimationFrame(spy);
        }
      },
      { passive: true }
    );
    window.addEventListener("resize", spy);
    spy();
  }

  window.KFOTA_RULES = { open: open, hasRead: hasRead };
})();
