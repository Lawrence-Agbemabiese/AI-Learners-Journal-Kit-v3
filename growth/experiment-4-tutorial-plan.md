# Experiment 4 — Tutorial Plan: "Learn It. Keep It. Prove It."

**AILJK + Coddy.tech: 3-hour live online tutorial**
Drafted 2026-07-19 for delivery week of 2026-07-27 (date TBD). Cohort: Bettie's 5 confirmed students + up to 5 via Francis (KNUST). Format: video call, all participants on laptops. Tests H4 (pending-corrections #9).

---

## The one idea the session must land

Learning evaporates. Coddy makes practice addictive; AILJK makes it permanent and provable. Participants should leave having *felt* the loop twice, not having been told about it:

**Learn (Coddy) → Capture (AILJK) → Prove (git + portfolio)**

Persuasion frame: Coddy gives you a certificate that says you finished. Your journal is the evidence of what you understood, built, and fixed — the thing an employer or scholarship panel can actually read. The two together are a complete system; either alone is half of one.

## Design principles

- Show, never pitch. Every claim about AILJK is demonstrated live within minutes of being made.
- Two full learn→capture cycles so the ritual feels like a habit by hour 2, not a demo.
- Every participant leaves with real artifacts on their own machine: 2+ journal entries, a git-versioned journal repo, a 7-day plan.
- Product truth: AILJK is local-first, offline, plain Markdown, JSON-index search, optional BYO-key AI. Python 3.9+ required. No cloud, no sync. Never promise otherwise.
- Affiliate honesty: the Coddy link is disclosed in plain language at the moment it's shared (see script §Close). Trust is the asset; the commission is incidental to a genuine recommendation.

---

## Pre-session (send 3–5 days before)

1. **Device + setup check (WhatsApp/email):** confirm laptop, run `python3 --version` (need 3.9+), share a 2-minute install note for the AILJK bundle. Offer a 20-min drop-in help slot the day before for anyone whose install fails — do NOT burn session time on broken installs.
2. **Issue Student Portfolio Packs via TESTER codes** (100%-off, 25-use pool; already excluded from H1 metrics by Checkpoint B ruling 4). Participants get the full 12-week artifact set legitimately, at zero cost, without contaminating the GHS 49 test.
3. **Create the cohort WhatsApp group** — this becomes the day-7 accountability channel and the measurement instrument.
4. **Ask each participant to bring one answer:** "Name one thing you learned in the last month that you could show someone today." (Most can't — that's the opening hook.)
5. Prepare your Coddy affiliate link (coddy.tech/affiliate) with UTM/trackable wrapper if possible; test that clicks register in the affiliate dashboard.

## Run of show (180 min)

### 0:00–0:15 — Hook: the vanishing-knowledge problem
- Round-robin the pre-session question. Expect silence or vague answers — name it kindly: "That's not a you problem. It's how learning works without capture."
- One slide/screen: the Learn → Capture → Prove loop. Promise: "In three hours you'll have run this loop twice, and everything you make today stays on your machine forever."
- Set the frame: Coddy = the gym; AILJK = the training log; git = the receipts.

### 0:15–0:45 — Setup sprint (timeboxed hard)
- Verify AILJK runs (`ai-journal` — first entry screen). Helpers: anyone already working pairs with a neighbor who's stuck.
- Coddy account creation — **share the affiliate link here, with the disclosure script**: "Full transparency: this is an affiliate link — if any of you ever chose their paid plan, a small commission supports this free tutorial series. The free tier is all we use today, and it's genuinely what I recommend you start with."
- Everyone completes Coddy onboarding and lands on the Terminal course (coddy.tech/landing/terminal).

### 0:45–1:20 — Loop 1: Terminal
- 20 min: Coddy Terminal basics — first lessons, in-browser, gamified. Let the streak/XP mechanics do their thing.
- 15 min: first real AILJK entry. Walk the structured prompts together: what I learned / what I built / what I prompted / what confused me / what proof I saved. Insist on the "what confused me" field — that's the one a blank notebook never asks.
- Callback: "You just used the terminal to record what you learned about the terminal."

### 1:20–1:30 — Break (streak plug: "Coddy will nudge you daily. Your journal should ride the same trigger.")

### 1:30–2:05 — Loop 2: Python + the search payoff
- 20 min: Coddy Python fundamentals (variables/first program).
- 10 min: second AILJK entry, now with minimal hand-holding — the ritual should already feel familiar.
- 5 min: **the search demo** — search their own two entries from the CLI. "Forty minutes ago is already findable. Imagine week 9 of a course, searching week 2. No account. No internet. Yours."

### 2:05–2:35 — The git bridge (the aha moment)
- Frame: "Your journal is plain Markdown. That means the professional tool for tracking work — git — works on it out of the box."
- Live, together: `git init` the journal folder, `git add`, first `git commit`. Coddy's git-commands reference (coddy.tech/git-commands) on screen as the cheat sheet; point them to the Coddy Git course as the follow-on.
- Land it: "You have now: learned in a browser, captured locally, and committed evidence with the same tool used at every software company on earth. That commit history *is* a portfolio artifact."

### 2:35–2:55 — Prove it: from 7 days to a portfolio
- Tour the Student Pack artifacts they received (12-week tracker, project case study, GitHub README starter, prompt log, internship/scholarship tracker).
- The certificate frame: "Finish Coddy's Python course and you'll have a certificate for LinkedIn — earn it! But when an interviewer asks *'tell me about something that confused you and how you worked through it'* — that answer lives in your journal, nowhere else."
- Set the 7-day challenge: one Coddy lesson + one journal entry daily; post journal day-count in the WhatsApp group; reconvene check-in at day 7.

### 2:55–3:00 — Close
- 2-min feedback form (link in chat) while everyone's still on the call — do not let this slip to "after."
- Recap links in one message: AILJK download, Coddy (affiliate, re-disclosed: "same link as earlier — affiliate, as I said"), WhatsApp group, day-7 date.
- Thank Bettie/Francis by name. Ask: "Who else do you know who should be in the next one?" (organic waitlist for round 2).

---

## Experiment 4 measurement (defined BEFORE the session; log to growth/metrics.md)

| Metric | Instrument | H4 relevance |
|---|---|---|
| Attendance vs confirmed | roll call | funnel top |
| Setup success rate | count at 0:45 | friction measure — gates everything |
| Entries written live (target: 2/person) | screen-share spot check | product activation |
| Affiliate link clicks / Coddy signups | affiliate dashboard | **H4 core datum** |
| Coddy Pro conversions (any window) | affiliate dashboard | **H4 revenue datum** |
| Day-7 journal streak (target: ≥3 of cohort) | WhatsApp check-in | retention/habit |
| Feedback: verbatim quotes | form, free-text | Unknown #4 copy voice |
| "Would you have paid GHS 49 for the pack?" | form, asked LAST | relocated-WTP probe (asked, not tested) |
| Referrals volunteered at close | count | organic-pull signal |

**Success reading (indicative, small-n honest):** with n≈10, this measures activation and habit, not conversion statistics. Treat any Pro conversion as a strong positive signal; treat affiliate click-through and day-7 streaks as the real read. Zero clicks with high engagement = the pairing persuades but the till doesn't ring → H4 weakens.

## Open items before delivery

1. Date/time (coordinate Bettie + Francis groups; one session or two?).
2. Confirm Coddy's affiliate attribution mechanics (cookie window; whether signup-then-later-upgrade still credits you) — checklist item (c) in pending-corrections #9.
3. Verify current Coddy free-tier limits (energy/lives-style caps could interrupt Loop 1 — test a fresh free account yourself for 30 min beforehand).
4. TESTER code logistics: how many of the 25-use pool to allocate (suggest: 12).
5. Decide recording policy (a recording becomes the seed of the online-tutorial asset H4 envisions — get consent).
6. Dry-run the full setup sprint on a clean machine — the 30-minute timebox is the plan's riskiest assumption.

## Relationship to the loop (unchanged rulings)

This is Experiment 4 running ALONGSIDE the approved cycle: H1/GHS 49, facilitator pricing, and all Checkpoint B rulings remain in force. Participants are TESTER-coded and excluded from H1 metrics. Results feed the H1-vs-H4 checkpoint ruling (pending-corrections #9). KNUST note: Francis's students arriving via this free tutorial is *also* a warm-up for the facilitator conversation — a live demonstration of "ready-made day-one cohort materials" (L3-compliant: materials value, no license talk).
