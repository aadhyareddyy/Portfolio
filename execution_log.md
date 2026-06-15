# Execution Log — Cold Outreach Research Pipeline

## Started: 2026-06-15

---

### LinkedIn Collection (updated 2026-06-15 — rescrape)

| Expert | URL Used | Posts Retrieved | Retrieval Method | Status |
|--------|----------|-----------------|------------------|--------|
| Alex Berman | https://www.linkedin.com/in/alexanderberman | 5 + viral | Direct profile + post page scrape | Done |
| Belal Batrawy | https://www.linkedin.com/in/belbatrawy/ | 5 + viral | Direct profile + post page scrape | Done |
| Jason Bay | https://www.linkedin.com/in/jasondbay/ | 5 + viral | Direct profile + post page scrape | Done |
| Will Aitken | https://www.linkedin.com/in/justwillaitken/ | 5 + viral | Direct profile + post page scrape | Done |
| Nick Abraham | https://www.linkedin.com/in/nick-abraham/ | 5 + viral | Direct profile + post page scrape | Done |
| Matthew Putnam | https://www.linkedin.com/in/matthewrichardputnam/ | 5 + viral | Direct profile + post page scrape | Done |
| Kris Rudeegraap | https://www.linkedin.com/in/rudeegraap/ | 5 + viral | Direct profile + post page scrape | Done |
| Ricky Pearl | https://www.linkedin.com/in/rickypearl/ | 5 + viral | Direct profile + post page scrape | Done |
| Sam Nelson | https://www.linkedin.com/in/realsamnelson/ | 5 + viral | Direct profile + post page scrape | Done |
| Morgan J Ingram | https://www.linkedin.com/in/morganjingramamp/ | 5 + viral | Direct profile + post page scrape | Done |

Engagement metrics (likes/comments) scraped from public LinkedIn post HTML via `scrape_engagement_v2.py`.

---

### YouTube Collection

| Expert | Video 1 Title | Video 2 Title | Transcript Method | Status |
|--------|--------------|--------------|-------------------|--------|
| Alex Berman | The Insane Psychology Behind Cold Email | My Favorite Cold Email Scripts of All Time | Auto captions | Done |
| Jason Bay | Improve Your Cold Calls in 2024 - Jason Bay | Cold Email: Ignore this webinar if you don't want to double your reply rates | Auto captions | Done |
| Will Aitken | How to nail video outreach (with Will Aitken) | No Nonsense Sales roleplay (S1:E4) | Auto captions | Done |
| Nick Abraham | How To Fix Your Cold Email Deliverability | Use THESE Cold Email Tools to Book More Calls | Auto captions | Done |
| Sam Nelson | Prospecting With Empathy: Sam Nelson | Why Cold Outreach Isn't Working For You | Auto captions | Done |
| Morgan J Ingram | How to Build a LinkedIn Sales Strategy | Confessions of an SDR (video prospecting) | Auto captions | Done |

---

### Failures and Fallbacks Used

| Step | What Failed | Fallback Used | Outcome |
|------|-------------|---------------|---------|
| LinkedIn direct fetch | Login wall on all profiles | Web search `site:linkedin.com` + expert name | Partial post text retrieved |
| @OutboundSquad /videos | No videos tab | yt-dlp `ytsearch` for Jason Bay cold email | 2 videos selected |
| @WillAitken /videos | HTTP 404 | yt-dlp `ytsearch` for Will Aitken cold email SDR | 2 videos from interview channels |
| @leadbird /videos | No videos tab | yt-dlp `ytsearch` for Nick Abraham cold outreach | 2 videos from Nick Abraham channel |
| Nick Abraham video h2j0gFz9RH4 | Video not available | Used q95kdUtzddw + wYMtt4ZTa3Y instead | Success |
| Git not in PATH | `git` command not found | Installed Git for Windows via winget | Success |
| Python not in PATH | `pip`/`python` not found | Installed Python 3.12 via winget | Success |
| clean_transcript.py print | UnicodeEncodeError on Windows console | Set PYTHONIOENCODING=utf-8 | Files written successfully |
| Jason Bay video 2 duration | 55 min exceeds 30 min rule | Kept video; transcript available via auto captions | Documented in sources.md |

---

### Completion Summary
- LinkedIn files created: 10/10
- YouTube transcript files created: 12/12
- sources.md: Done
- README.md: Done
- Total commits: 20
- Completed: 2026-06-15
