# Pending corrections and inputs for the next growth-cycle pass

Logged 2026-07-19 (Lawrence + Claude session). Feed these into the owning agents when their stage next reruns. Nothing here is shipped marketing copy.

## For market-signal-researcher (next demand-brief revision)

1. **Factual error to correct:** the demand brief states the Facilitator Pack has "no published price." False — the shipped facilitator license guide PDF and the live landing page (agenticppa.com/ghana-ai-coding-journal) both publish GHS 300 / 750 / 1,500 / 3,000 cohort pricing. Error originated in CLAUDE.md's "Contact / license" line. (Found by evaluator pass 1 on the offer spec, 2026-07-05.)
2. **Alternatives table addition:** "AI session history viewers" as an adjacent category — e.g. Claude Code History Viewer (free, offline desktop app, ~1.9K GitHub stars, reads local session history of Claude Code + 8 other AI coding tools; searchable transcripts + analytics; covered by Joe Njenga, Medium, 2026-07-18). Assessment: retrieval tool, not a reflection/portfolio system; serves the developer segment only; erodes the manual prompt-log component for CLI users. Watch item: if such tools add "summarize sessions into a learning reflection," differentiation narrows to the portfolio/meaning layer.

## For offer-architect / Checkpoint B (L1 scope widening)

3. The shipped GHS 300–3,000 facilitator pricing is not only in the PDF — it is **publicly displayed on the live landing page**. If Checkpoint B rules "supersede," the update must cover: license-guide PDF, landing page pricing section, and any other surfaces, before the first facilitator outreach (H3) or Experiment 2 quoting.

## Product note (truth boundary for all future copy)

4. **New feature exists in the repo but is NOT in any shipped bundle yet:** `ai-journal import` (scripts/session_import.py) — imports a local Claude Code session as a draft journal entry (prompts pre-filled, Reflection left to the learner). Offline, stdlib-only, read-only on session files. Rationale: turns session-history tools from a competitive threat into a feed; targets the intermediate/power-user segment (validated interest: tester Kwaku S., private machine, terminal-motivated). Do NOT mention in sales/marketing copy until it ships in a release bundle (requires build_release.py rebuild + dist refresh). Update docs/Paid_Product_Checklist.md at next release.

## For market-signal-researcher / next-cycle Nigeria intel

7. **High-value Nigeria lead (logged 2026-07-19):** Prof. Ogheneruona E. Diemuodeke — Professor of Energy and Thermofluid Systems, Dept. of Mechanical Engineering; Director, Energy Technology Institute, University of Port Harcourt, Rivers State, Nigeria; ardent advocate of AI applications in SME entrepreneurship and sustainable-development policy/planning — downloaded the Student Portfolio Pack at $0 (Gumroad, ogheneruona.diemuodeke@uniport.edu.ng; presumably a 100%-off code — verify which). Implications: (a) $0 redemption → EXCLUDE from H1 conversion metrics per Checkpoint B ruling 4; (b) Nigeria is out of scope this cycle, but a professor/institute director is exactly the institutional-facilitator profile the next-cycle Nigeria motion needs — candidate for §6-style discovery questions (facilitator WTP, procurement mechanics, university reach) when Nigeria is spec'd; (c) note the organic pull from the energy/SME-policy academic segment, outside the demand brief's mapped segments.

## For distribution-strategist / offer-architect — Ghana conversation intel

8. **Second warm KNUST door (logged 2026-07-19; meeting Mon 2026-07-20):** Prof. Francis Kemausuor, KNUST — Bioenergy Technology, Energy Planning, Energy Policy; Visiting Lecturer at PAU–Institute of Energy and Water Sciences (Tlemcen, Algeria) and Ecole Supérieure des Métiers des Énergies Renouvelables (Abomey-Calavi, Benin); member, Ghana Institution of Engineering. Track record of joint work with Lawrence incl. a proposal for Digital Transformation Training and Coaching (SheTrades, UPS Project – Ghana; deadline missed, both open to future collaboration). Implications: (a) second KNUST relationship alongside Prof. B. Amenu — the H3 pilot venue; (b) the SheTrades/UPS angle suggests donor-funded training programs as a possible facilitator-pack buyer class (budget mechanics differ from center/university procurement — probe in discovery); (c) his PAU/Benin affiliations are future non-Ghana channels — out of scope this cycle, note only; (d) meeting occurred BEFORE L1 ship — no pricing shown, §6 unprompted-WTP protocol applies. Capture verbatim quotes.

## For market-signal-researcher / offer-architect — H4 candidate hypothesis (free + affiliate model)

9. **New deployment idea (Lawrence, logged 2026-07-19) — do NOT act on until tested; H1 and all Checkpoint B pricing rulings remain in force.** Proposal: AILJK as a forever-free tool; revenue moves downstream to affiliate income from paired practice platforms (e.g. Coddy), with free online tutorials as the conversion surface — learners study terminal/git/Python on the paired platform while journaling/portfolio-building in AILJK. AILJK = trust engine + funnel; tutorial = conversion surface; affiliate commission = till.
   - **H4 (falsifiable form):** a free AILJK + paired-tool tutorial converts enough attendees into paid-tier affiliate signups that revenue per 100 learners rivals or beats direct GHS 49 sales.
   - **Immediate test bench:** Bettie has confirmed 5 students for an AILJK tutorial (deliberately capped at 5 for testing; more were interested). Run as **Experiment 4** alongside — not instead of — the existing loop. Measure: tutorial completion, affiliate link click-through, actual paid signups, revenue per attendee. Ultimate scale target: OMCP.
   - **Verified so far:** Coddy's affiliate program is real — 30% base commission, 40% at $500/mo sales, 50% at $1,000+/mo, lifetime recurring on renewals (coddy.tech/affiliate, checked 2026-07-19).
   - **Verification checklist before any ruling:** (a) Coddy individual Pro price (family plan is $36/mo; individual unconfirmed); (b) payout rails to Ghana (currency, method, minimums); (c) cookie window / attribution mechanics; (d) whether Ghana-based learners can realistically pay a recurring USD card subscription — the WTP problem is relocated, not eliminated; diaspora/sponsor audiences may be the actual commission source; (e) alternative/parallel affiliate programs worth comparing.
   - **Known interactions:** facilitator motion is orthogonal and unaffected (L3 already sells on materials value, not software access; a free student tool may strengthen it). If H4 is confirmed, it invalidates: GHS 49 tier, Experiment 1, student storefront copy, parts of the email sequence. Decision = a Checkpoint ruling after Experiment 4 data, not before.
   - **Trust rule:** any tutorial containing affiliate links must disclose the affiliate relationship plainly. Credibility with OMCP/institutions is the asset the whole model rests on.

## Checkpoint B agenda additions

5. Record the L2 correction: the "live refund trigger" was narrower than assessed — the website ZIP (June 20 build) always contained the full v3.0.1 bundle; the broken 13.6 KB ZIP existed only in dist/ and never reached buyers. Gumroad now hosts the complete rebuilt ZIP directly (uploaded 2026-07-05-session; 0 sales at the time).
6. TESTER discount code (100% off, 25 uses, Student Portfolio Pack) created on Gumroad for tester distribution; AMBASSADOR-FREE (25 uses) also live. Tester redemptions are not organic sales — exclude from H1 conversion metrics.
