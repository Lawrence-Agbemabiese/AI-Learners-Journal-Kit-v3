# AILJK Project Primer — session handoff

*Written 2026-07-25. Purpose: brief a fresh Claude (Cowork) task on everything it needs to continue this work. Start a new task, connect the two folders below, and say: "Read growth/ailjk-project-primer.md and pick up from there."*

## Who and what

Lawrence Agbemabiese is building the **AI Learner's Journal Kit (AILJK)** — a local-first, offline, plain-Markdown learning journal for coding beginners. Core loop and brand promise: **Learn (practice platform) → Capture (AILJK) → Prove (git + portfolio)**.

**Business model (decided 2026-07-25): the core journal is FREE FOREVER.** Monetization is practice-platform affiliate income (Codédex application in flight; Coddy referenced in tutorial materials) — free distribution maximizes community scale, and scale is the affiliate engine. Open sub-question: whether the facilitator cohort packs and student portfolio packs stay paid (leaning yes — they're services/materials, not the journal). Ripple effects NOT yet executed: wind down the GHS 49 willingness-to-pay test in the growth docs, update Gumroad/storefront copy to free, revisit REFUND_POLICY/Paid_Product_Checklist framing (checklist still applies to paid packs), and keep the affiliate disclosure placeholder in the ritual card ready. Product truth (never overpromise): local-first, offline, plain Markdown + JSON index (+ rebuildable SQLite FTS), optional BYO-key AI, Python 3.9+, no cloud, no sync, no bundled API access.

## The two folders

- `~/AI-Learners-Journal-Kit-v3` — the product repo (git). Product code: `scripts/`, `web/index.html` (single-file web UI), `installers/`, `tests/` (pytest, 63 passing), docs in root + `docs/`. Internal/no-ship folders: `growth/`, `marketing/`, `promo/`, `output/`, `.claude/` — excluded from customer bundles by `scripts/build_release.py`.
- `~/AI-Journal` — Lawrence's LIVE personal journal + installed copy of the app (scripts + web/). Recently reset to a clean state; his pre-reset data is doubly backed up (see Safety).

## Current version: v3.4.2 (see CHANGELOG.md for full history)

Recent work (July 23–25, one intensive session):
- v3.4.0: big hardening pass (UTF-8 everywhere, same-day topic collisions now "Topic (2)" instead of silent loss, installers ship web UI, menu resilience, packaging leaks fixed) + **append-to-today/date targets** (`ai-journal append today|yesterday|<date>|<id>|<topic>`; web "Add to today" with entry picker, auto-starts today's entry) + **safe delete** (soft to `<journal>/trash/` with `trash-index.json` restore log; `--purge` behind typed DELETE; web Delete button; indexes stay consistent).
- v3.4.1: **Edit button** in web entry view (`/api/entry/update`), full-body editor.
- v3.4.2: **ritual card** on web home screen (Learn → Capture → Prove) linking Coddy.tech and Codédex — plain links for now; the HTML contains a marked PLACEHOLDER comment for swapping in affiliate links + a disclosure line once approved.

## Build & test commands

- Tests: `python3 -m pytest tests/ -q` from repo root (needs pytest).
- Release: `python3 scripts/build_release.py --version vX.Y.Z` (clean tree; `--allow-dirty` for smoke builds) → `dist/`; then `python3 scripts/verify_customer_package.py dist/<zip>`.
- The customer zip must never contain: `growth/`, `marketing/`, `promo/`, `output/`, `journal-backups/`, `_to_delete/`, `.claude/`, `.git/`, personal journal data.

## Safety / recovery locations

- Verified full backup of pre-reset journal: `~/AI-Learners-Journal-Kit-v3/journal-backups/AI-Journal-backup-20260723-130716.tar.gz` (142 files, checksummed).
- Belt-and-braces copy of the same data: `~/AI-Journal/_pre-reset-20260723-130716/` (Lawrence may delete when ready).
- `~/AI-Learners-Journal-Kit-v3/_to_delete/` holds disposable temp snapshots.

## Partnerships & pipeline (the growth agenda)

- **Vision:** large learning community across sub-Saharan Africa; sequence Ghana → Nigeria → anglophone SSA. Social-enterprise framing.
- **Ashesi University:** demo with **Dr. Ekow** (not CS faculty) went well 2026-07-25; he offered to share the journal + ritual with colleagues/students and provided his email. Cover note drafted (`growth/` or Lawrence's records); follow-up = send v3.4.2 Drive link + Recipient_Setup_Guide, offer live session.
- **KNUST:** student cohort via Francis; facilitator conversation (Dr. Kemausuor prep notes in growth/). Replication target this coming week.
- **University of Port Harcourt (Nigeria):** next replication target this coming week — first Nigeria beachhead.
- **Codédex Creator Program:** persuasive application drafted (to help@codedex.io) around AILJK + continental distribution, updated 2026-07-25 for the free-forever model ("your affiliate program is my business model — our incentives are identical"); status = **SENT 2026-07-25 (night)** — but the sent version predates the free-forever decision (it says "paying learners"). Do NOT send an immediate correction. Plan: if they reply, weave in the free-forever upgrade naturally; if quiet after 5–7 business days, send the prepared bump email (in growth/codedex-followup-bump.md) which announces free-forever as a development + fresh traction (Ekow/KNUST/UPH). Then awaiting approval → on approval, cement affiliate links + disclosure in the ritual card. When approved: swap ritual-card URLs to affiliate links + add the disclosure line (placeholder comment marks the exact spot in web/index.html).
- **Coddy.tech:** referenced as affiliate in the Experiment-4 tutorial plan (`growth/experiment-4-tutorial-plan.md`, 3-hour live tutorial, cohort ~10, delivery week of 2026-07-27). Note: Coddy and Codédex are competitors; in lecturer/university conversations stay platform-agnostic.
- Assets ready: `docs/Recipient_Setup_Guide.md` (novice Mac/PC setup, forwardable), `growth/demo-ashesi-runsheet-2026-07-24.md` (reusable demo run-sheet — adapt for KNUST/UPH), Ghana launch packs in `dist/ghana-launch/`.

## Working conventions with Lawrence

- Show an improved version of his prompt before executing (his standing preference).
- He's a beginner-to-intermediate CLI user actively learning (Terminal → Git → Python roadmap): give exact copy-paste commands with one-line explanations; he enjoys doing git/terminal steps himself under guidance.
- Backup before anything destructive — non-negotiable. Nothing irreversible.
- Warm, energetic collaboration; he calls the assistant "Fable 5"; aviation jokes land well ("Hals- und Beinbruch").
- Deliverables: write files and send them; commit product changes to BOTH the repo and the live install (`~/AI-Journal`) so his daily use matches the shipped product; rebuild + verify the bundle when product code changes; suggest commit messages (he commits himself).

## Likely next work

1. Send Dr. Ekow follow-up (link + guide + cover note), track response.
2. Adapt run-sheet + materials for KNUST and University of Port Harcourt sessions.
3. On Codédex approval: cement affiliate links + disclosure in ritual card; rebuild; update Drive.
4. Tutorial Experiment 4 delivery (week of 2026-07-27) and its measurement log (`growth/metrics.md`).
5. Ongoing: small product improvements arising from Lawrence's own daily use (he files sharp, real-use feature requests — the Edit button came from one).
