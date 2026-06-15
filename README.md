# Cold Outreach Pipeline Research — B2B SaaS

## What This Is
A curated research repository of 10 high-signal practitioners in B2B SaaS cold outreach,
built to support a future playbook on what actually works in 2025. Every expert here
actively runs outreach campaigns, leads SDR teams, or owns an agency — not just writers.

## Why Cold Outreach
Cold outreach is the most measurable B2B growth channel. Results are directly tied to
message quality, sequence structure, and targeting — not algorithms. This makes it the
best topic to build a data-backed playbook grounded in practitioner content.

## Why These 10 Experts
Each expert was selected based on three filters:
1. They practise what they teach — agency owners, SDR team leads, or founders
2. They post specific data — open rates, reply rates, booked meetings
3. Their content was published or updated in 2024–2025

## How Content Was Collected
- **LinkedIn posts:** Collected from each expert's profile via web retrieval and search-based methods (6 posts per expert including most viral)
- **YouTube transcripts:** Downloaded via yt-dlp CLI, cleaned using clean_transcript.py
- **Total content collected:** 60 LinkedIn post slots + 12 YouTube transcripts across 6 experts
- **Fallback handling:** Where primary URLs failed, fallback profiles and search-based retrieval were used; all fallbacks are documented in each file

## Repository Structure
- `/research/sources.md` — master expert list with links, follower counts, retrieval methods, and key insights
- `/research/linkedin-posts/` — one `.md` file per expert with collected posts
- `/research/youtube-transcripts/` — one `.md` file per video with full cleaned transcript
- `/research/other/` — newsletters and additional materials
- `clean_transcript.py` — script used to strip timestamps from `.vtt` caption files
- `execution_log.md` — automated log of every action taken during data collection

## Tools Used
- yt-dlp (transcript and video metadata download)
- Python 3 (VTT transcript cleaning via clean_transcript.py)
- Web search (LinkedIn content retrieval where direct access was blocked)
