# Hosting request: Kootenay Festival of the Arts, 2026–27 season

**To:** Secure by Design
**Site:** https://www.kootenayfestivalofthearts.ca
**Repo:** https://github.com/revyrob/KFA (static HTML/CSS/JS, no build step, no PHP, no database)

For this season, the static site in this repo replaces the WordPress site on
the domain. **Next season the WordPress site returns to the domain**, so
please keep it backed up and restorable.

---

## 1. Serving the site

- [ ] Serve the repo contents from the web root for `www.kootenayfestivalofthearts.ca`
      (`index.html` at the root, other pages in `/pages/`).
- [ ] Keep the existing HTTPS certificate and the `http://` → `https://` and
      non-www → `www` redirects exactly as they are.
- [ ] Add the rules in **`deploy/nginx-kfota.conf`** to the server block, then run
      `nginx -t` before reloading. They do three things:
  1. **Clean URLs:** `/genres` serves `/pages/genres.html`, and `.html`
     addresses redirect to the clean version.
  2. **Old WordPress addresses** (all 73 pages in the current `wp-sitemap.xml`)
     redirect to the matching new page.
  3. Repo-only files (`.py`, `.md`, `/deploy/`, `/.git`) are not served.
- [ ] **Please keep all redirects as 302 (temporary), not 301.** WordPress takes
      the domain back next year and will use those old addresses again. Browsers
      and search engines cache 301 redirects and would keep sending people away
      from the restored pages.
- [ ] **Keep `/wp-content/uploads/` reachable this season if possible.** Old
      syllabus PDFs and images may still be linked from emails, social posts and
      other websites.
- [ ] WordPress admin and login (`/wp-admin`, `/wp-login.php`) can return 404
      this season.

## 2. Deploy pipeline from GitHub

We'd like every push to the `main` branch to deploy automatically, using a
GitHub Actions workflow that uploads the files to your server over SFTP
(using lftp). Please provide:

- [ ] **SSH/SFTP host name and port**
- [ ] **A deploy-only user** whose access is limited to this site's web root
      (SFTP-only is fine; no access to other sites)
- [ ] **Key-based login:** we'll send you an SSH **public** key to install for
      that user. The private key stays in GitHub's encrypted secrets. No
      passwords.
- [ ] **The exact path of the web root** on the server
- [x] SFTP access for that user (confirmed: SFTP-only)
- [ ] Whether **connections are restricted by IP address**. GitHub Actions
      connects from changing IP addresses, so either allow GitHub's published
      ranges, or tell us if you'd prefer to **pull from GitHub yourselves**
      (for example a webhook or scheduled `git pull`) instead.
- [ ] Whether nginx needs a **reload after deploys** (it shouldn't for static
      files; only config changes need one).

The workflow will skip repo-only files (`.git`, `deploy/`, `*.py`, `*.md`).

## 3. Go-live and rollback

- [ ] A way to **preview the new site before it goes live**, if you have one
      (for example a temporary URL or a hosts-file entry).
- [ ] A **full backup of the WordPress site** (files and database) before the
      switch, and confirmation of **how quickly you can roll back** if needed.
- [ ] Plan for **next season's handback** to WordPress: remove these nginx
      rules and restore the WordPress server block.
