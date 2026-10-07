# Deploy pipeline setup (GitHub Actions → Secure by Design)

Every push to `main` runs `.github/workflows/deploy.yml`, which copies the
site to the Secure by Design server over SFTP (using lftp; the server is
SFTP-only, so rsync is not used).

## 1. Make a deploy key pair (on your computer, once)

PowerShell:

```powershell
ssh-keygen -t ed25519 -C "kfota-github-deploy" -f "$env:USERPROFILE\.ssh\kfota_deploy"
```

Press **Enter twice** when asked for a passphrase (leave it empty; GitHub
Actions can't type one). This creates two files in `C:\Users\<you>\.ssh\`:

| File | What it is | Where it goes |
|---|---|---|
| `kfota_deploy.pub` | **Public** key, safe to share | Email to Secure by Design |
| `kfota_deploy` | **Private** key, secret | GitHub secret `DEPLOY_SSH_KEY` only |

Never commit either file, email the private key, or paste it anywhere else.

## 2. Send Secure by Design the public key and ask for the details

Send them `kfota_deploy.pub` and ask them to install it for a deploy-only user.
Ask them for:

- host name and SSH port
- deploy user name
- full path of the folder the site is served from
- the server's **SSH host key fingerprint** (so you can confirm you're
  connecting to their real server)
- confirmation that the deploy user has SFTP access and that GitHub Actions' IP addresses
  can connect

**Important:** the deploy folder must contain only this site. The pipeline
deletes server files that aren't in the repo (except `wp-content/`).

## 3. Record the server's identity

```powershell
ssh-keyscan -p PORT HOST
```

Check that the fingerprint matches the one Secure by Design gave you
(`ssh-keyscan -p PORT HOST | ssh-keygen -lf -`). Keep the full output for the
next step.

## 4. Add the secrets in GitHub

Repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Secret | Value |
|---|---|
| `DEPLOY_SSH_KEY` | Entire contents of the private key file `kfota_deploy`, including the `-----BEGIN…` and `-----END…` lines |
| `DEPLOY_KNOWN_HOSTS` | Full output of the `ssh-keyscan` command from step 3 |
| `DEPLOY_HOST` | Host name, e.g. `server.example.com` |
| `DEPLOY_PORT` | SSH port (usually `22`) |
| `DEPLOY_USER` | Deploy user name |
| `DEPLOY_PATH` | Web root folder, e.g. `/var/www/kootenayfestivalofthearts` |

To copy the private key without opening it:
`Get-Content "$env:USERPROFILE\.ssh\kfota_deploy" -Raw | Set-Clipboard`

## 5. Test with a dry run

Repo → **Actions → Deploy to Secure by Design → Run workflow** (leave
**Dry run** ticked). Open the run log: the "Copy site to server" step lists
every file it *would* copy or delete, without changing anything.

If the list looks right, run it again with **Dry run** unticked, or merge to
`main`. Every later push to `main` deploys automatically.

## Troubleshooting

| Error in the log | Likely cause |
|---|---|
| `Permission denied (publickey)` | Public key not installed for that user, or wrong `DEPLOY_USER` |
| `Host key verification failed` | `DEPLOY_KNOWN_HOSTS` missing or doesn't match the server |
| `Connection timed out` | Wrong host or port, or their firewall blocks GitHub's IP addresses |
| `Access failed` / `No such file` | `DEPLOY_PATH` is wrong. On SFTP-only accounts the path is often relative to the login folder (e.g. `/public_html` or `public_html`) |
| `Permission denied` while writing files | Deploy user can't write to `DEPLOY_PATH` |

## Changing or revoking access

To revoke: ask Secure by Design to remove the public key, and delete the
`DEPLOY_SSH_KEY` secret. To rotate: repeat steps 1, 2 and 4 with a new key.
