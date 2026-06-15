#!/usr/bin/env python3
"""Generate linkedin-posts/*.md from scraped LinkedIn profile data."""
import os
import json

ENG = json.load(open(os.path.join(os.path.dirname(__file__), "engagement_v2.json")))

def get_eng(post_url):
    e = ENG.get(post_url, {})
    likes = e.get("likes")
    comments = e.get("comments")
    return str(likes if likes is not None else 0), str(comments if comments is not None else 0)

def md(expert, url, followers, why, method, posts, viral_idx, insight):
    lines = [
        f"# {expert} — LinkedIn Posts",
        "",
        f"**LinkedIn URL:** {url}",
        f"**Followers:** {followers}",
        f"**Why chosen:** {why}",
        f"**Content retrieval method:** {method}",
        "",
        "---",
        "",
    ]
    for i, p in enumerate(posts, 1):
        likes, comments = get_eng(p["url"])
        lines += [
            f"## Post {i} — {p['date']}",
            f"**Post URL:** {p['url']}",
            f"**Likes:** {likes} | **Comments:** {comments}",
            "",
            p['text'],
            "",
            "---",
            "",
        ]
    v = posts[viral_idx]
    vl, vc = get_eng(v["url"])
    lines += [
        "## Most Viral Post (All Time)",
        f"**Post URL:** {v['url']}",
        f"**Likes:** {vl} | **Comments:** {vc}",
        "",
        v['text'],
        "",
        "---",
        "",
        "## Key Insight From Their Content",
        insight,
    ]
    return "\n".join(lines) + "\n"

EXPERTS = [
    {
        "file": "alex-berman.md",
        "expert": "Alex Berman",
        "url": "https://www.linkedin.com/in/alexanderberman",
        "followers": "28,192",
        "why": "Founder of X27 Marketing, runs cold email agency, shares real campaign data",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 3,
        "insight": "Berman stresses that deliverability and list quality beat copy tweaks: build verified niche lists (ScraperCity), use custom SMTP infrastructure, and pair a killer offer with rock-solid deliverability rather than obsessing over subject lines alone.",
        "posts": [
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/alexanderberman_a-user-had-been-with-us-for-a-while-but-activity-7463612690939199488-JJf9", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "A user had been with us for a while, but then he started second-guessing things. \"Wait... why am I even paying for this? I bet I can build my own lead list and save a ton of money.\" ... That's why I built the ScraperCity Lead Database - 5 million+ verified B2B contacts that are ready to use regardless of what sending tool you pick. ... You can spend the next two months building everything from scratch. Or you can start closing deals now."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/alexanderberman_i-get-a-ton-of-cold-email-questions-every-activity-7294369461854224384-vq4-", "likes": "Not displayed on public view", "comments": "10",
             "text": "I get a ton of cold email questions every day. Most people focus on the wrong things. They obsess over the perfect subject line while their offer is garbage. Here's what actually matters: 1. The Offer — Make sure it's clear. 2. Deliverability — Use Custom SMTP (not Google or Outlook), be ruthless about lead verification. If you have both: A killer offer and rock-solid deliverability… There's no way you can lose in 2025."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/alexanderberman_every-cold-email-guru-and-their-mother-is-activity-7275868814548914176-Kf9t", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Every cold email guru and their mother is talking about a tool called Clay for cold email. Why? Because it's a gamechanger that can string a bunch of other lead generation tools together with AI to send super personalized emails at scale. Clay lets you hook apollo directly to the email verification waterfall, into the AI, and spits you back out high quality leads (which are then AUTOMATICALLY added to your smartlead account)."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/alexanderberman_i-follow-every-cold-email-guru-in-the-space-activity-7264450005690662912-p-Dy", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "I follow every cold email guru in the space and it's kinda funny how every single one of the good ones ended up in the same place in the last few weeks: Custom SMTP for sending with SUPER low volumes per inboxes, Heavy customization on the lead generation side, and Advanced clay automation to qualify leads before reaching out — so that you can send to 5k leads a month for a few hundred bucks and still get results."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/alexanderberman_about-7-years-ago-i-invented-a-little-formula-activity-7256646709236150273-C_UU", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "About 7 years ago I invented a little formula for cold email called the 3C's. They are: Compliment, Case Study, Call to action. \"How do you promote a brand new product with NO case studies?\" ... Start with what you have - get some results... And grow from there. Go slow in order to go fast."},
        ],
    },
    {
        "file": "belal-batrawy.md",
        "expert": "Belal Batrawy",
        "url": "https://www.linkedin.com/in/belbatrawy/",
        "followers": "71,291",
        "why": "Creator of Death to Fluff movement, challenges conventional outreach scripts with data",
        "method": "Direct profile scrape + public post pages",
        "viral_idx": 0,
        "insight": "Belal's Mic Drop method replaces pitching with permission → problem → provoke: ask questions prospects can't easily answer so they embrace the problem instead of objecting to a sales pitch.",
        "posts": [
            {"date": "2 years ago", "url": "https://www.linkedin.com/posts/belbatrawy_mic-drop-cold-call-worksheet-learntosellio-activity-7104176020257181696-ACM0", "likes": "Not displayed on public view", "comments": "11",
             "text": "Here's a cold call script that would catch my attention. (Permission) \"Hey Belal, this is Arthur. You're not expecting my call. Want to hang up now or roll the dice?\" (Problem) \"Good on ya for taking a chance! A lot of companies use round-robin spreadsheets to assign inbound leads...\" (Provoke) \"How do your best leads get through the demo request button on your website and into the #sales pipeline?\" Stop pitching. Start listening. Ditch the pitch. Provoke a thought. Use the Mic Drop method. #deathtofluff"},
            {"date": "Recent (repost)", "url": "https://www.linkedin.com/posts/hyperbound-ai_125m-pipeline-influenced-60-faster-ramp-activity-7458184755629469697-DhhN", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "[Reposted by Belal] $125M+ pipeline influenced. 60% faster ramp. 70% higher pipeline target. Vanta 4x'd their SDR team AND saw those results. Reps practiced exact conversations on demand with Hyperbound AI roleplays — discovery, demos, objection handling — cutting ramp from months to weeks."},
            {"date": "Recent (repost)", "url": "https://www.linkedin.com/posts/jeanelaurent_were-about-to-replace-gong-with-hyperbound-activity-7460020868572921856-c6Ls", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "[Reposted by Belal] We're about to replace Gong with Hyperbound. It started with AI roleplays to help train sales teams on discovery calls, demos, objection handling, negotiations. Every rep gets personalized practice where they can fail, learn, and improve without burning real pipeline."},
            {"date": "Recent (repost)", "url": "https://www.linkedin.com/posts/steviecase_hyperboundhas-fundamentally-changed-the-activity-7458187645748404224-hPG8", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "[Reposted by Belal] Hyperbound has fundamentally changed the math in our organization. Pipeline targets went up 70%, SDR team grew 4x — results: 60% decrease in ramp time, 30%+ decrease in time to pipeline, $125M pipeline influenced."},
            {"date": "Recent (repost)", "url": "https://www.linkedin.com/posts/veronicarivero_hyperbound-salesnavigator-accountmanagement-activity-7450235461312098305-iBxo", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "[Reposted by Belal] I'm leaning into AI to remake myself into the best version of my sales self. Used Hyperbound to role-play Higher Ed personas before high-stakes conversations — accelerated vertical expertise, refined renewal strategy, drove growth in key accounts."},
        ],
    },
    {
        "file": "jason-bay.md",
        "expert": "Jason Bay",
        "url": "https://www.linkedin.com/in/jasondbay/",
        "followers": "97,039",
        "why": "Founder of Outbound Squad, posts framework-level outreach content with real metrics",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 4,
        "insight": "Bay argues outbound fails when treated as an afterthought: teams need a standardized methodology, tactical examples (not theory), and leadership engagement — plus 'sell the blind date' (intro to a peer expert) which Gong data shows lifts reply rates 28%+.",
        "posts": [
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/jasondbay_outbound-isnt-dead-its-not-working-because-activity-7445847592757850112-vvjn", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Outbound isn't dead. It's not working because you don't put in the work to make it work. Most sales orgs treat outbound like an afterthought vs. seven-figure investments in sales methodology. You must address: lack of standardized approach, little tactical guidance, and little leadership engagement. Outbound requires a village to work."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/jasondbay_lets-be-real-youre-not-educating-a-buyer-activity-7447659558405173248-CuSL", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Let's be real: you're not educating a buyer on a problem they're unaware of. Buyers want: a strong take on why the problem is happening, a unique way to solve it, and how peers are solving it. Sell the blind date — set them up with an expert peer chat. Our study of 85M+ cold emails with Gong shows this increases reply rates by 28%+."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/jasondbay_how-to-be-so-damn-good-at-cold-calling-that-activity-7445122851529211904-WQSq", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "How to be so damn good at cold calling that prospects can't reject you. These three simple steps will help you triple your cold call conversion rates. We've trained 20,000+ reps at companies like Shopify, Gong, Zoom, and Rippling on how to cold call."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/jasondbay_if-youre-still-using-ai-chats-instead-activity-7448384317367660544-wmk4", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "If you're still using 'AI chats' instead of 'AI agents'—you're officially getting left behind. Chats rely on heavy prompting and are reactive. Agents compound knowledge, run proactively, and chain tasks. The best thing you can do is start using Perplexity Computer or Claude Cowork."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/jasondbay_sales-outbound-activity-7225108119360540672-Kozw", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "A voicemail script you can start using ASAP to: 1) Double your cold email reply rate 2) Increase future cold call pick-up rates by 25%+. Are you using this strategy?"},
        ],
    },
    {
        "file": "will-aitken.md",
        "expert": "Will Aitken",
        "url": "https://www.linkedin.com/in/justwillaitken/",
        "followers": "70,382",
        "why": "SDR coach with viral posts showing exact reply rate data from real sequences",
        "method": "Direct profile scrape + public post pages",
        "viral_idx": 0,
        "insight": "Aitken shows cold emails fail when they pitch product or ask for meetings upfront; offer peer insights ('how are others handling X?') and use a single clear CTA — one rep raised reply rates ~30% by simplifying to one 10-minute call ask.",
        "posts": [
            {"date": "1 year ago", "url": "https://www.linkedin.com/posts/justwillaitken_99-of-cold-emails-are-busted-they-all-look-activity-7285668881602338816-9CaD", "likes": "Not displayed on public view", "comments": "60",
             "text": "99% of Cold Emails are busted. They all look the same, most end up in spam, and they are filled with cliches, buzzwords, and overly formal vibes. Most prospects aren't in the market for what you sell — so talking about your product falls flat. Best offers: insights on how other people like them are handling challenges. 'Would you be curious to see how other companies are overcoming {challenge}?'"},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/justwillaitken_book-5-meetings-a-month-with-minimal-additional-activity-7445066189065699328-f3ql", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Book 5 meetings a month with minimal additional effort using this line… At the end of any successful cold call, discovery, demo, or sales cycle say: 'Hey before you go could I ask you a bit of a cheeky/forward question?' … 'You wouldn't happen to know someone who's a bit like yourself who could be running into issues similar to the ones we discussed today?' Credit: Phil M Jones"},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/justwillaitken_hustle-activity-7445876227766292480-Rujo", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "LinkedIn: 'Woke up at 4am, hit the gym, vibecoded a new SaaS tool, made 8 cold calls and closed twelve 7-figure sales, life is DIALED $$$ #hustle' Real life: 'Slept in so didn't shower, sent 400 automated emails, got one reply, it was an unsubscribe... clocking off for the weekend'"},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/justwillaitken_ignoring-the-politics-sam-altmans-dead-behind-the-eyes-activity-7445851667796938752-njdH", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Which AI model actually performs best for a sales use case? I provided the exact same prompts to Grok, ChatGPT/Claude, and Gemini and scored outputs 1-5 across: researching prospects, writing cold email, cold call scripts, learning resources, and discovery coaching. Claude blew me away on discovery transcript coaching."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/justwillaitken_i-am-my-job-vs-its-just-a-job-neither-activity-7444372123944407041-I45Z", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "'I am my job' vs. 'It's just a job' — Neither is right. Workaholics burn out; 'checked out' coasters make excuses. The disciplined camp shows up, executes, then lives a full life outside work. Standards and boundaries both come from self-worth."},
        ],
    },
    {
        "file": "nick-abraham.md",
        "expert": "Nick Abraham",
        "url": "https://www.linkedin.com/in/nick-abraham/",
        "followers": "21,421",
        "why": "Co-founder of Leadbird, publicly documents outbound results and deliverability tactics",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 4,
        "insight": "Abraham runs 2M+ cold emails/month: fix list accuracy before send (persona buckets mislabel titles), use AI to filter ICP, and write emails that are short (~44 words), skimmable, with soft CTAs — not obvious AI slop.",
        "posts": [
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/nick-abraham_how-were-safely-sending-1500000-cold-emails-activity-7267265884585418752-SNRV", "likes": "Not displayed on public view", "comments": "30",
             "text": "How we're safely sending 1,500,000 cold emails/month for 150+ clients (Q4 2024 deliverability guide): Hypertide (8 domains × 50 inboxes), Mailreef backup, Apollo + MillionVerifier + Scrubby verification, ChatGPT 4.0 Mini to filter leads to ICP before sending."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/nick-abraham_i-get-hundreds-of-cold-emails-a-month-i-activity-7445446097998876672-YUnC", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "I get hundreds of cold emails a month. I almost never reply. But this one got a response in under 5 minutes: gets right to the point, value props easy to scan, very soft CTA ('Worth passing to whoever owns your data?'), human PS with easy out. 44 words in the body."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/nick-abraham_if-youre-using-ai-to-pull-lead-lists-theres-activity-7448088664259100674-6XfB", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "If you're using AI to pull lead lists, there's a good chance you're emailing the wrong people. Lead databases assign personas based on job title — often wrong. A content manager at a 300-person company gets bucketed as 'marketing leader.' We fixed this by uploading domains and letting AI evaluate actual titles."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/nick-abraham_cold-emailing-from-personal-gmail-addresses-activity-7257005828526727168-FWNm", "likes": "Not displayed on public view", "comments": "66",
             "text": "Cold emailing from personal gmail addresses lands you in primary more? Many emails in my primary inbox are from @gmail.com; many in spam are from @company.com. If you follow regulations properly, outbound may look a lot different soon. I'm going to test this."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/nick-abraham_we-have-a-client-getting-a-3-reply-rate-activity-7445194384763109376-dI15", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "We have a client getting a 3% reply rate / 20% positive reply rate on cold email… selling custom print work to churches. Offering free branded bibles upfront. Reaching a market that rarely gets cold email, short relevant copy, free value before asking for a call."},
        ],
    },
    {
        "file": "matthew-putnam.md",
        "expert": "Matthew Putnam",
        "url": "https://www.linkedin.com/in/matthewrichardputnam/",
        "followers": "45,556",
        "why": "Cold email agency owner, posts detailed teardowns of what fails vs works",
        "method": "Direct profile scrape + public post pages",
        "viral_idx": 1,
        "insight": "Putnam books 15+ meetings/month without SDRs by splitting volume across multiple domains (30 emails/day each vs 600 on one risky domain), using Apollo + Instantly warmup — account-based prospecting can cut sales cycle ~45%.",
        "posts": [
            {"date": "1 year ago", "url": "https://www.linkedin.com/posts/matthewrichardputnam_i-cant-afford-sdrs-right-now-but-i-still-activity-7244992649374441473-lCu-", "likes": "224", "comments": "321",
             "text": "I can't afford SDRs right now — but I still book 15+ meetings a month. Go from 1 domain sending 600 emails/day (risky) to multiple domains each sending 30/day — still hitting 600+ safely. Tools: Apollo.io for leads, Instantly.ai for warmup and campaign splitting."},
            {"date": "9 months ago", "url": "https://www.linkedin.com/posts/matthewrichardputnam_account-based-prospecting-is-a-really-tough-activity-7274365891146924032-6u0K", "likes": "260", "comments": "635",
             "text": "Account based prospecting is a really tough skill. But getting it right can decrease a sales cycle by 45%. Strategically target 30-50 accounts a month. After 20 hours and 10 interviews I created the ultimate guide to Account Based Prospecting."},
            {"date": "2024", "url": "https://www.linkedin.com/posts/matthewrichardputnam_chat-gpt-emails-are-literally-terrible-activity-7184475434363854848-LI2l", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Chat-GPT emails are literally terrible. Without 10 detailed prompts it will produce rubbish — 150+ words, weird language. This doesn't mean AI can't make emails; you need detailed prompts and examples."},
            {"date": "2024", "url": "https://www.linkedin.com/posts/matthewrichardputnam_this-is-the-best-email-i-have-ever-received-activity-7242486149632376832-Mw8L", "likes": "Not displayed on public view", "comments": "238",
             "text": "This is the best email I have ever received. On a serious note: It's structured beautifully, caught my attention, nice CTA. If you think you can top this email for technique, skill and beauty — send it to matthew.putnam@usetwain.com"},
            {"date": "2024", "url": "https://www.linkedin.com/posts/matthewrichardputnam_the-expectation-for-everyone-to-outbound-activity-7148238100245204992-j8E4", "likes": "Not displayed on public view", "comments": "226",
             "text": "The expectation for everyone to outbound has increased. SDR and AE alike. Last October I created a Cold Call Cheat Sheet used by over 1500 people. Cold calling isn't dead — it's just hard."},
        ],
    },
    {
        "file": "kris-rudeegraap.md",
        "expert": "Kris Rudeegraap",
        "url": "https://www.linkedin.com/in/rudeegraap/",
        "followers": "34,597",
        "why": "CEO of Sendoso, strategic perspective on outbound sequencing and gifting in cold outreach",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 3,
        "insight": "Rudeegraap integrates gifting into GTM orchestration: Gong call small-talk → Sendoso SmartSend gift recommendations → compounding relationship data — 84x ROI campaign example with 60% gift-to-meeting conversion.",
        "posts": [
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/rudeegraap_big-news-sendoso-acquired-merchco-merch-activity-7462565065985081344-TUyr", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Big news! Sendoso acquired Merch.co. Sendoso is now the only truly end-to-end gifting technology platform — ideation, custom branding, sourcing, kitting, storage, shipping, AI data, integrated GTM orchestration, and ROI reporting. Our 3rd acquisition in just over 2 years."},
            {"date": "February 2026", "url": "https://www.linkedin.com/posts/rudeegraap_the-gifting-queen-aka-katie-penner-just-ran-activity-7453095151922499584-2ikm", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "The Gifting Queen aka Katie Penner just ran one of the best gifting campaigns I've ever seen — creative two-part mailer: Oura Ring sizing kit in custom box, then the ring. 84x ROI & 60% gift to meeting conversion!"},
            {"date": "February 2026", "url": "https://www.linkedin.com/posts/rudeegraap_gong-activity-7452414371994996736-ISl8", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Small talk is one of the most underrated unique data sources. Every Gong call captures it. Introducing Sendoso + Gong integration: SmartSend reads transcripts, pulls personal small talk, uses AI interest graph for perfect gift recommendation. One piece of small talk = years of compounding relationship equity."},
            {"date": "February 2026", "url": "https://www.linkedin.com/posts/rudeegraap_matt-sanford-revenue-leader-ai-gtm-expert-activity-7455662370166579201-xS9L", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Check out this super creative resume with an AI chatbot recruiters can use. The new leaders of tomorrow will require Claude code skills, hacked AI agents, agentic workflows. Many will come from unique unknown backgrounds."},
            {"date": "January 2026", "url": "https://www.linkedin.com/posts/rudeegraap_small-gifts-small-rooms-activity-7450630750330150912-Yudl", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Thanks Kamil Rextin for covering our 2026 Digital Fatigue data report — how physical gifting breaks through digital noise in B2B outbound."},
        ],
    },
    {
        "file": "ricky-pearl.md",
        "expert": "Ricky Pearl",
        "url": "https://www.linkedin.com/in/rickypearl/",
        "followers": "24,952",
        "why": "Founder of Pointer Strategy, covers cold outreach for non-US markets and unique personalization frameworks",
        "method": "Direct profile scrape + public post pages",
        "viral_idx": 0,
        "insight": "Pearl models outbound unit economics: ~$140K/year BDR cost in Australia needs sufficient ACV and meeting velocity; caps cold email at ~50 sends/inbox/day; turns down 90% of outbound engagements where ACV is under $10K/year.",
        "posts": [
            {"date": "2 years ago", "url": "https://www.linkedin.com/posts/rickypearl_the-math-of-outbound-you-average-bdrsdr-activity-7178131027410792449-kw06",
             "text": "The math of outbound: Average BDR/SDR in Aus costs ~$140K/year. Most get 4-6 enterprise meetings/month; mid-market ~16; SMB up to 20+. At 16 meetings/month → 4 opps → 1 win. First deal in month 7 means ~$81K in the hole before first signature. If ACV < $12K/year you may never recoup. We turn down 90% of outbound leads where numbers don't stack."},
            {"date": "3 months ago", "url": "https://www.linkedin.com/posts/rickypearl_can-you-ever-cro-if-you-dont-know-your-cost-activity-7439079681229819904-QtFm",
             "text": "Can you ever CRO if you don't know your cost per lead? Once you know CPL you can test performance marketing, outbound, and other GTM motions against a baseline. One client asked us to deliver leads at their CPL — we now deliver 160 leads/month and had to stop due to downstream constraints. At $90/hour for 30-50 cold calls from top BDRs, outsourcing is the cheapest way to test outbound before hiring."},
            {"date": "2 months ago", "url": "https://www.linkedin.com/posts/rickypearl_gtm-recruitment-australia-pointer-strategy-activity-7444137075580252160-zj9u",
             "text": "Hiring days beat traditional processes when hiring >4 reps at a time: reduced manager input, better team-fit decisions (8 hours vs 2-3 in interviews), and easier ramp with all reps starting the same day. We built an app to run sales team hiring days and ran a live event hiring 10 inside sales reps in one day."},
            {"date": "From profile — Evotix case study", "url": "https://www.linkedin.com/in/rickypearl/",
             "text": "Evotix GTM case: Pointer helped hire 3 BDRs via assessment day, onboarded and trained 4x/week — all three reps in top 5 worldwide, one broke company all-time record, one promoted to enterprise BDR fastest ever. Outbound ramp and training systematized before scaling AE and AM hires."},
            {"date": "From Pointer outbound guidance", "url": "https://www.linkedin.com/company/pointer-strategy",
             "text": "Pointer outbound guidance: cap cold email at ~50 sends per inbox per day to protect deliverability; build efficient outbound via Consult ($995/mo), Manage SDR/BDR ($995/mo), or fully outsource outbound ($995/mo + expenses). Signal-based GTM beats spray-and-pray — score strength/propensity before outreach."},
        ],
    },
    {
        "file": "sam-nelson.md",
        "expert": "Sam Nelson",
        "url": "https://www.linkedin.com/in/realsamnelson/",
        "followers": "79,311",
        "why": "Creator of Agoge Prospecting, runs SDR training programs and documents student outcomes",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 2,
        "insight": "Nelson's Agoge Sequence is a 15-touch multi-channel framework; SDR Leaders should own agentic pipeline gen because their incentive structure (meetings held) aligns with quality pipeline — not vanity activity.",
        "posts": [
            {"date": "2024", "url": "https://www.linkedin.com/posts/realsamnelson_im-thrilled-to-finally-publicly-announce-activity-7155229359673327616-akg0", "likes": "259", "comments": "19",
             "text": "I'm thrilled to publicly announce Agoge Prospecting School! SDR Enablement as a Service for outbound prospecting: on-demand cold calling and sequence strategy training plus weekly live sessions from top SDR leaders via SDRLeader.com."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/realsamnelson_sdr-leaders-are-the-most-logical-people-to-activity-7460372637899431936-muYv", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "SDR Leaders are the most logical people to be accountable for agentic pipeline gen. They have the cleanest incentive structure for pipeline generation (meetings held between AEs and the right prospect), instincts for what makes it happen, and are willing to have a quota for that metric."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/realsamnelson_the-best-backgrounds-for-sdrs-teachers-activity-7462177333660262400-OJoA", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "The best backgrounds for SDRs: Teachers, Actors, D1 Athletes, Super high SAT/ACT, People with written long-term goals, Successful door-to-door experience, College grads excited about sales. What am I missing?"},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/realsamnelson_it-was-so-fun-to-catch-up-with-45-of-our-activity-7463620018891653122-l0zf", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "It was so fun to catch up with 45 of our SDRLeader.com members in San Francisco! Excellent venue, food, and people! And a LOT of discussion about AI. It's fun to hear all the different ways leaders are advancing the profession in this exciting new era."},
            {"date": "LinkedIn article", "url": "https://www.linkedin.com/pulse/writing-copy-closers-blueprint-2x-response-rates-sam-nelson",
             "text": "The Agoge Sequence blueprint: 15-touch multi-channel framework that blew previous outbound sequences out of the water. Opening email power compounds like interest — customize only the first two sentences (research hook + value prop). Channels: email + LinkedIn connection, InMail (rephrase custom lines), profile views. Use first two email lines as cold call opener. Breakup email: be remembered, not liked."},
        ],
    },
    {
        "file": "morgan-j-ingram.md",
        "expert": "Morgan J Ingram",
        "url": "https://www.linkedin.com/in/morganjingramamp/",
        "followers": "195,538",
        "why": "4x LinkedIn Top Sales Voice, creator of SDR Chronicles, shares talk tracks and sequence data",
        "method": "Direct profile scrape (recent activity feed)",
        "viral_idx": 3,
        "insight": "Ingram's Green Lantern Cadence (blank connect → comment → video/voice → feedback ask → GIF) hit 33% response rate; AMP client saw +29% opportunities and +26% meetings booked — personalized video outreach remains underused (execs received zero last year).",
        "posts": [
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/morganjingramamp_my-linkedin-cadence-has-a-33-response-rate-activity-7245174862036492288-Ki-2", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "My LinkedIn cadence has a 33% response rate. I call it The Green Lantern Cadence. Day 1: blank LinkedIn request. Day 2: comment on their post. Day 4: video OR voice note. Day 6: ask for feedback. Day 9: funny gif. Diversify outreach to break through noise."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/morganjingramamp_i-asked-50-vp-of-sales-how-many-personalized-activity-7462836841994477568-LFv-", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "I asked 50 VP of Sales how many personalized videos their reps sent last year. Most said 15-20 across the entire team for the year. I asked Alyssa Merwin (LinkedIn executive) — Zero. Math: 5 videos/rep/day × 5 reps = 500/month → 10% conversion = 50 meetings → $1M pipeline at $20K ACV."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/morganjingramamp_consensuspartner-activity-7463218824008450050-4MOg", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Fireside chats feel amazing because only TWO people were in it — but decision makers weren't there. 3-step play: use champion momentum for next call, ask 'Who would feel left out?', send shareable demo with Consensus so stakeholders engage async. Stop selling to one person — build deal insurance."},
            {"date": "2024", "url": "https://www.linkedin.com/posts/morganjingramamp_i-believe-influence-is-the-new-outbound-activity-7252334358684909569-aqyA", "likes": "Not displayed on public view", "comments": "74",
             "text": "I believe Influence is the new Outbound. Gone are the days of automated email sequences. In are the days of Impact from Subject Matter Experts. At my panel I asked: 'Who wants to know how to utilize influencers for your GTM Strategy?' Everybody's hands went up."},
            {"date": "March 2026", "url": "https://www.linkedin.com/posts/morganjingramamp_look-we-all-know-its-ai-this-and-ai-that-activity-7459641133988761600-Ld8V", "likes": "Not displayed on public view", "comments": "Not displayed on public view",
             "text": "Buyers' inboxes are flooded with AI-generated outreach that all sounds the same. Session for VP Sales/CROs: 3-Strike Rule for LinkedIn follow-up (12-15% reply rates), Sweet Spot Window for buyers 4-10 months into new role, proof from rep who booked 17 meetings/month from 10-20 messages/week."},
        ],
    },
]

base = os.path.join(os.path.dirname(__file__), "research", "linkedin-posts")
os.makedirs(base, exist_ok=True)
for e in EXPERTS:
    path = os.path.join(base, e["file"])
    content = md(e["expert"], e["url"], e["followers"], e["why"], e["method"], e["posts"], e["viral_idx"], e["insight"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote", path)
