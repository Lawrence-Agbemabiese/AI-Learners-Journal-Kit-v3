# Demo Run-Sheet — Ashesi University Lecturer Session

**Format:** ~25–30 min video call, tomorrow afternoon · **Product:** AI Learner's Journal Kit v3.4.0
**Audience:** one lecturer *evaluating for his students* — not a student learning. He is asking two silent questions the whole time: *"Will this actually help my students learn?"* and *"How much of my time will it cost me?"* Every segment below answers one of those.

**The one idea to land:** Learning evaporates. His students finish a course with a certificate and no evidence of *understanding*. AILJK makes their learning permanent, searchable, and provable — locally, offline, at no running cost — and gives *him* a window into what actually confused them.

---

## Tonight (15 min prep)

- [ ] Journal is already reset to a clean state — do NOT add test entries; the empty "Write one line today to start your streak" screen is your opening shot.
- [ ] Dry-run once: double-click **START HERE - AI Journal.command**, confirm the browser opens, then Ctrl-C and close.
- [ ] Bump your terminal font size (⌘+ twice) and browser zoom to 125% for screen-share legibility.
- [ ] Upload the zip to Google Drive and test the link **in a private/incognito window** (this proves it works for someone who isn't you).
- [ ] Have `docs/Workshop_Facilitator_Guide.md` open in a tab — you'll offer it at the close.
- [ ] Close Slack/mail/notifications. Nothing kills a "your students' data stays private" pitch like a notification popping up mid-demo.

## Backup plans (decide now, not live)

- Internet dies mid-call → keep going: the entire product works offline. Say so out loud; it becomes a selling point.
- Browser UI won't launch → fall back to `ai-journal menu` in the terminal; the beginner menu shows the same flows.
- He asks something you can't answer → "Good question — I'll journal it and follow up," then literally do it on screen with **Add to today**. Turns a stumble into a demo.

---

## Run of show

### 0:00–0:03 — The hook (talk, no screen yet)

Ask him the tutorial-plan question, adapted: *"When a student finishes your course, what can they show you — six months later — of what they actually understood?"* Let the pause happen. Then: *"Certificates say they finished. I want to show you what evidence of understanding looks like."*

### 0:03–0:08 — First capture (screen share starts)

1. Double-click **START HERE** → browser opens to the clean journal. One sentence on what he's seeing: *"This is a student's day one. Runs on their laptop, plain files, no account, no cloud."*
2. Click **New entry** → topic: "Binary search trees" (or something from *his* department's curriculum — ask what he teaches and use that). Write two honest lines including one *"what confused me"* line.
3. Point at the streak/heatmap tiles for five seconds only: *"Habit mechanics, same psychology as Duolingo — but the artifact it produces is a study record, not a score."*

### 0:08–0:12 — The daily ritual

1. Click **Add to today** → add a quick thought. Narrate the design: *"Zero friction matters. A stray insight after class goes into today's entry — students never file, never organize."*
2. Click **Ask the Guide** → ask "What is an API?" → answer appears **offline**. Say the important sentence: *"No API key, no internet, no cost — beginner questions are answered locally. With a free key, it becomes a full AI tutor that builds on the student's own notes — and every answer is saved and labeled with its source."*

### 0:12–0:17 — The payoff: search + proof

1. Click **Search my journal** → search a word from the entry you just made. *"Week 9, a student searches week 2. It's all theirs, all findable."*
2. Open the entry → show **Delete** → move it to trash → mention it's recoverable. Small moment, but it signals a finished, safe product.
3. The git bridge, 90 seconds, terminal: `cd ~/AI-Journal && git log --oneline` (or `git init` + first commit if you reset the repo). *"Plain Markdown means the professional toolchain works out of the box. A semester of commits is a portfolio artifact an internship interviewer can actually read."*

### 0:17–0:22 — What's in it for HIM (the segment most demos skip)

Talk over the journal folder in Finder — plain files, year/month folders:

- *"The 'what confused me' lines are formative-assessment gold. Students can share an entry or a folder with you — you see misconceptions while there's still time to fix them."*
- *"It's AI-transparent by design: AI answers are labeled with their source and a review score, and the reflection sections can only be written by the student. This is the honest middle path on AI use — not banning it, not pretending it isn't happening."*
- *"Zero infrastructure for you or the university: no server, no accounts, no data protection headache. Python 3.9+, which every CS lab machine already has."*

### 0:22–0:27 — Q&A

Likely questions, honest answers:

- **"What does it cost?"** — The kit is a one-time purchase (mention your current pricing / cohort packs); running cost is zero. Optional full-AI answers use the student's own free-tier key (Groq — no card needed).
- **"Privacy / where does data go?"** — Nowhere. Local files only. Optional AI questions go straight to the provider the student chose, never through you.
- **"Does it work without internet?"** — Yes, everything except live AI answers. (If your connection hiccuped earlier, point back to it.)
- **"Isn't this just letting them lean on AI?"** — Opposite framing: the journal *documents* their AI use and forces reflection on it. The Reflection section can't be generated — that's the pedagogy.
- **"Windows or Mac labs?"** — Both, plus Linux. Same double-click start.
- **"Can I see it at scale / with a class?"** — the bridge to the close ↓

### 0:27–0:30 — The close (one specific ask)

Don't end with "so, what do you think?" End with: *"Would you pick one course and try it with a small group — even 5–10 students — for two weeks? I'll handle setup with them directly, and I have a facilitator guide and ready-made day-one materials, so it costs you one announcement."* Then send, in the call chat, while still talking: the Drive download link + the facilitator guide offer + your WhatsApp/email. Agree a specific follow-up date before you hang up.

---

## After the call (5 min, same day)

- Journal the session itself with **Add to today** — what he asked, what landed, what confused *you*. (You now have a product for exactly this.)
- Send the recap message within the hour: link again, one-line summary of what he saw, the agreed follow-up date.
- Log the outcome for your experiment tracking (attendance-equivalent, objections heard, pilot yes/no) — this is a live data point for the facilitator channel alongside the KNUST conversation.

## Product truth guardrails (never overpromise)

Local-first, offline, plain Markdown, JSON-index search, optional BYO-key AI, Python 3.9+ required. No cloud, no sync, no bundled API access. If he asks for something it doesn't do: *"It doesn't do that today — I keep a public changelog; tell me why you need it and it may be why v3.5 exists."*
