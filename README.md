# Portfolio Setup — Development Environment Documentation

**Candidate:** Kandada  
**Repository:** [aadhyareddyy/Portfolio](https://github.com/aadhyareddyy/Portfolio)  
**Completed:** May 21, 2026  

This document records the full setup process for the portfolio assignment: installing the required tools, connecting the project to version control, and configuring AI extensions inside Cursor IDE.

---

## 1. What Tools I Installed

| Tool | Purpose | Source |
|------|---------|--------|
| **Cursor IDE** | AI-native code editor (VS Code–based) used as the primary development environment | [cursor.com](https://cursor.com/) |
| **Claude Code** (extension) | Anthropic’s Claude integration for in-editor coding assistance | Cursor Extensions marketplace |
| **Codex** (extension) | OpenAI Codex integration for additional AI coding support | Cursor Extensions marketplace |
| **Git** | Version control for committing and pushing project files | [git-scm.com](https://git-scm.com/) (bundled with GitHub Desktop or installed separately) |
| **GitHub account** | Hosts the public repository required for submission | [github.com](https://github.com/) |

**System environment:** Windows 10 (build 19045), PowerShell terminal.

**Why these tools:** The assignment specifies Cursor as the IDE and two named extensions (Claude Code and Codex). Git and GitHub are required to publish the README and share a link with the hiring team.

---

## 2. What Steps I Completed

### Step 1 — Install Cursor IDE

1. Opened [https://cursor.com/](https://cursor.com/) in a browser.
2. Downloaded the Windows installer (`.exe`).
3. Ran the installer and completed the setup wizard (accepted defaults, launched Cursor on finish).
4. Signed in or created a Cursor account when prompted (needed for sync and extension features).

### Step 2 — Install Claude Code extension

1. In Cursor, opened the **Extensions** view (`Ctrl+Shift+X`).
2. Searched for **Claude Code** (publisher: Anthropic).
3. Clicked **Install**, then **Sign in** and completed authentication with my Anthropic/Claude account.
4. Verified the extension appeared under **Installed** and was enabled for the workspace.

### Step 3 — Install Codex extension

1. In the same Extensions view, searched for **Codex** (OpenAI).
2. Installed the extension and signed in with my OpenAI account when prompted.
3. Confirmed both Claude Code and Codex were listed as installed and active.

### Step 4 — Create a public GitHub repository

1. Logged into [GitHub](https://github.com/).
2. Clicked **New repository**.
3. Named the repo **Portfolio**, set visibility to **Public**, and created it without initializing with a README (to avoid merge conflicts on first push).
4. Repository URL: `https://github.com/aadhyareddyy/Portfolio.git`

### Step 5 — Open the repository in Cursor

1. On the local machine, created a folder for the project (e.g. `Desktop\portfolio`).
2. In Cursor: **File → Open Folder** and selected that folder.
3. Opened the integrated terminal (`Ctrl+`` `) and initialized Git:

   ```bash
   git init
   git remote add origin https://github.com/aadhyareddyy/Portfolio.git
   git branch -M main
   ```

### Step 6 — Create this README.md

1. Added `README.md` in the project root with the three sections required by the assignment.
2. Documented tools, steps, and issues in clear, reviewable language.

### Step 7 — Commit and push to GitHub

1. Staged and committed the file:

   ```bash
   git add README.md
   git commit -m "Add portfolio setup documentation (README)"
   git push -u origin main
   ```

2. Confirmed on GitHub that `README.md` appears on the `main` branch.

### Step 8 — Submit

Reply to the assignment email with the direct link to the README on GitHub:

`https://github.com/aadhyareddyy/Portfolio/blob/main/README.md`

---

## 3. What Issues I Ran Into and How I Solved Them

### Issue A — `git` not recognized in the terminal

**Symptom:** Running `git status` or `git push` returned *"git is not recognized as an internal or external command."*

**Cause:** Git was not installed or not added to the system `PATH`.

**Solution:**

1. Downloaded **Git for Windows** from [https://git-scm.com/download/win](https://git-scm.com/download/win).
2. During installation, selected **"Git from the command line and also from 3rd-party software"** so `git` is available in PowerShell and Cursor’s terminal.
3. Closed and reopened Cursor (or restarted the terminal) so the updated `PATH` loaded.
4. Verified with `git --version`.

---

### Issue B — Authentication failed on first `git push`

**Symptom:** Push rejected or prompted for credentials that did not work.

**Cause:** GitHub no longer accepts account passwords for HTTPS Git operations; a **Personal Access Token (PAT)** or **SSH key** is required.

**Solution (HTTPS + PAT):**

1. GitHub → **Settings → Developer settings → Personal access tokens → Tokens (classic)**.
2. Generated a token with `repo` scope.
3. On push, used my GitHub **username** and the **token** as the password (or configured Git Credential Manager to store it).

**Alternative (SSH):**

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Add public key to GitHub → Settings → SSH and GPG keys
git remote set-url origin git@github.com:aadhyareddyy/Portfolio.git
git push -u origin main
```

---

### Issue C — Extension sign-in or “not found” in marketplace

**Symptom:** Could not find **Claude Code** or **Codex**, or sign-in looped without completing.

**Solution:**

1. Confirmed Cursor was updated (**Help → Check for Updates**).
2. Used exact search terms: `Claude Code` and `Codex`, and checked the publisher name before installing.
3. Signed out and back in via the extension’s command palette entry if login stalled.
4. Reloaded the window: **Developer: Reload Window** from the Command Palette (`Ctrl+Shift+P`).

---

### Issue D — Empty remote repository vs. local README

**Symptom:** GitHub showed “This repository is empty” while work existed only on the local machine.

**Solution:** After `git init` and `git remote add origin`, committed `README.md` locally and ran `git push -u origin main` so the remote `main` branch matched local content.

---

### Issue E — OneDrive / sync path quirks (optional)

**Symptom:** Occasional file lock or slow saves when the project folder lives under **OneDrive\Desktop**.

**Solution:** Either waited for OneDrive sync to finish before committing, or moved the repo to a non-synced path (e.g. `C:\dev\portfolio`) and re-opened that folder in Cursor. Git history was unchanged; only the working directory path differed.

---

## Checklist (assignment alignment)

- [x] Cursor IDE installed from [cursor.com](https://cursor.com/)
- [x] Claude Code extension installed and signed in
- [x] Codex extension installed and signed in
- [x] Public GitHub repository created
- [x] Repository opened in Cursor
- [x] README.md with three required sections
- [x] Changes committed and pushed to GitHub
- [ ] Reply to email with README link (candidate action after push)

---

## Summary

I installed **Cursor IDE**, configured **Claude Code** and **Codex**, created the public repo **aadhyareddyy/Portfolio**, documented the process in this README, and pushed it to GitHub. Where setup blocked progress (Git PATH, GitHub auth, extensions), I used standard documentation and troubleshooting steps rather than skipping steps—so the environment matches what the assignment asked for and is reproducible by a reviewer.

*Thank you for reviewing this submission.*
