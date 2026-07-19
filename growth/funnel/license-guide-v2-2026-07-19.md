# Facilitator Cohort License Guide — v2 source content (rev. 2, 2026-07-19 (post-evaluator))

**Purpose:** complete replacement source for regenerating `facilitator-cohort-license-guide.pdf` (currently produced by `scripts/generate_ghana_launch_assets.py`, `facilitator_pack()` — I cannot edit scripts/; whoever applies Checkpoint C should transcribe the sections below into that DocSpec and rebuild the Facilitator ZIP).
**Supersedes:** the shipped "Suggested cohort pricing" section (GHS 300 / 750 / 1,500 / 3,000) per offer-spec header ruling 1 (L1 — SUPERSEDE) and rulings 2–3.
**Pricing decision applied:** list prices only in print. Lawrence's private negotiation bounds (offer-spec ruling 2) MUST NOT appear in this PDF or any public asset — see CHANGES.md for rationale.
**Verified today:** the rebuilt Facilitator ZIP (2026-07-19 07:29) still contains the old table, so this PDF remains a standing counter-offer until regenerated. L1 is not yet complete in dist/.

### Product-truth guardrails for whoever regenerates the PDF (INTERNAL — NOT PDF CONTENT, DO NOT TRANSCRIBE)

- Do not add outcome guarantees ("your learners will retain more") — offer-spec §4 forbids them; the pilot discount is the risk-reducer.
- Do not print the private negotiation bounds recorded in offer-spec ruling 2 (the floor and ceiling) anywhere — the PDF carries list prices only, exactly as they appear below the line.
- Do not use "you need this license" framing anywhere in the PDF — it circulates to OMCP centers and universities that qualify for free noncommercial use (ruling L3).
- The app claims below match shipped v3.3.0 (verified 2026-07-19): local Markdown + JSON-index search, offline, BYO API key for AI, Python 3.9+.

Everything below the line is the full PDF content — nothing below the line is internal, and a literal transcription of everything below the line is safe to print. Sections marked **(unchanged)** are preserved verbatim from the shipped PDF/generator.

---

## Title

Facilitator Cohort License Guide

## Subtitle **(unchanged)**

Run coding clubs, bootcamps, and school workshops with a ready-made reflection and portfolio system.

## Footer / trust note **(unchanged)**

Designed for Ghanaian high-school and university learners in coding, AI, data, cybersecurity, and digital-skills programs. Independent resource. Not an official government product.

## Section: Best use cases **(unchanged)**

- 2-hour intro workshop
- 7-day coding challenge
- 4-week club sprint
- 12-week bootcamp or course
- university tech society portfolio clinic

## Section: What is in the pack *(new — sells materials value first, per offer-spec §1 Premium and ruling L3)*

- Printable student materials for day one: the 12-week Student Portfolio Pack PDF and the free 7-day journal PDF — ready to print or share, built for low-device settings.
- A step-by-step workshop facilitator guide: agenda, sample exercise, troubleshooting script, and safety guidance.
- The 2-hour timed workshop flow and assessment rubric in this guide.
- The AI Learner's Journal Kit app (local Markdown journal with search; runs offline; optional AI with the user's own API key; requires Python 3.9 or newer).

## Section: Cohort licensing *(REPLACES "Suggested cohort pricing")*

Per-Cohort License — **GHS 950**. Covers one named cohort of up to 30 learners for one training run. Cohorts larger than 30: add GHS 20 per additional learner.

Per-Institution Annual License — **GHS 4,500**. Covers one center or campus for unlimited cohorts over 12 months.

First-time partner pilot: **50% off your first per-cohort license (GHS 475)** so you can run one full cohort before committing further.

A note on who needs a license: the software itself is licensed PolyForm Noncommercial 1.0.0 — educational institutions, nonprofits, public research organizations, and government bodies already qualify for free noncommercial use. For those organizations, this pack is priced for what it adds: ready-made cohort materials, printables, the timed workshop flow, and facilitator support. Commercial training providers (private bootcamps, paid instructors) additionally receive the commercial-use rights the license otherwise withholds.

## Section: Workshop flow **(unchanged — preserve the full 0–120 min table)**

| Time | Activity |
|---|---|
| 0-10 min | Why portfolio proof matters more than passive course completion. |
| 10-25 min | Show examples of a weak learning note vs a strong project note. |
| 25-45 min | Learners complete their first project reflection. |
| 45-65 min | Prompt log exercise: improve one AI prompt and explain the change. |
| 65-90 min | Pair review: each learner explains one project story. |
| 90-120 min | Commitment: choose one portfolio improvement for the next 7 days. |

## Section: Assessment rubric **(unchanged)**

| Area | What to look for |
|---|---|
| Clarity | Can the learner explain the project problem and outcome? |
| Evidence | Are screenshots, links, code, or notes included? |
| Reflection | Does the learner explain mistakes and improvements? |
| AI use | Does the prompt log show judgment and adaptation? |
| Next step | Is there a clear plan for improving the project? |

## Section: After the cohort *(new — L4b reverse upsell, offer-spec §5)*

Your learners can buy personal Student Portfolio Packs (GHS 49) after the cohort ends, so the journaling habit — and the portfolio — keeps growing after your workshop.

## Section: Facilitator CTA *(revised — keeps the contact channel, adds the fixed opener so the email is a confirmation, not a quote request)*

To license a cohort (GHS 950, up to 30 learners) or an institution (GHS 4,500/year), email info@agenticppa.com with your cohort size, dates, institution or group name, and whether you need printable files, Google Docs, or a live workshop. We can invoice institutions or accept mobile money from individual trainers.
