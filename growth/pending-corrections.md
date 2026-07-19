# Pending corrections and inputs for the next growth-cycle pass

Logged 2026-07-19 (Lawrence + Claude session). Feed these into the owning agents when their stage next reruns. Nothing here is shipped marketing copy.

## For market-signal-researcher (next demand-brief revision)

1. **Factual error to correct:** the demand brief states the Facilitator Pack has "no published price." False — the shipped facilitator license guide PDF and the live landing page (agenticppa.com/ghana-ai-coding-journal) both publish GHS 300 / 750 / 1,500 / 3,000 cohort pricing. Error originated in CLAUDE.md's "Contact / license" line. (Found by evaluator pass 1 on the offer spec, 2026-07-05.)
2. **Alternatives table addition:** "AI session history viewers" as an adjacent category — e.g. Claude Code History Viewer (free, offline desktop app, ~1.9K GitHub stars, reads local session history of Claude Code + 8 other AI coding tools; searchable transcripts + analytics; covered by Joe Njenga, Medium, 2026-07-18). Assessment: retrieval tool, not a reflection/portfolio system; serves the developer segment only; erodes the manual prompt-log component for CLI users. Watch item: if such tools add "summarize sessions into a learning reflection," differentiation narrows to the portfolio/meaning layer.

## For offer-architect / Checkpoint B (L1 scope widening)

3. The shipped GHS 300–3,000 facilitator pricing is not only in the PDF — it is **publicly displayed on the live landing page**. If Checkpoint B rules "supersede," the update must cover: license-guide PDF, landing page pricing section, and any other surfaces, before the first facilitator outreach (H3) or Experiment 2 quoting.

## Product note (truth boundary for all future copy)

4. **New feature exists in the repo but is NOT in any shipped bundle yet:** `ai-journal import` (scripts/session_import.py) — imports a local Claude Code session as a draft journal entry (prompts pre-filled, Reflection left to the learner). Offline, stdlib-only, read-only on session files. Rationale: turns session-history tools from a competitive threat into a feed; targets the intermediate/power-user segment (validated interest: tester Kwaku S., private machine, terminal-motivated). Do NOT mention in sales/marketing copy until it ships in a release bundle (requires build_release.py rebuild + dist refresh). Update docs/Paid_Product_Checklist.md at next release.

## Checkpoint B agenda additions

5. Record the L2 correction: the "live refund trigger" was narrower than assessed — the website ZIP (June 20 build) always contained the full v3.0.1 bundle; the broken 13.6 KB ZIP existed only in dist/ and never reached buyers. Gumroad now hosts the complete rebuilt ZIP directly (uploaded 2026-07-05-session; 0 sales at the time).
6. TESTER discount code (100% off, 25 uses, Student Portfolio Pack) created on Gumroad for tester distribution; AMBASSADOR-FREE (25 uses) also live. Tester redemptions are not organic sales — exclude from H1 conversion metrics.
