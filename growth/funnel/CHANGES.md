# growth/funnel/ CHANGES — 2026-07-19, rev. 2 (post-evaluator) (conversion-system-builder)

Drafts only. Nothing in marketing/, scripts/, web/, or dist/ has been touched; applying any of this to live assets requires the evaluator pass and Lawrence's Checkpoint C approval. All citations are to `growth/offer-spec.md` (APPROVED 2026-07-19), `growth/pending-corrections.md`, and — new at rev. 2 — `growth/channel-plan.md` (2026-07-19) and `growth/reviews/review-funnel-2026-07-19.md` (verdict REVISE).

## Rev. 2 changes (2026-07-19, post-evaluator) — mapped to the review's revision requirements

1. **Requirement 1 — demarcation leak, `landing-page-pricing-v2`: FIXED.** The "Removed from the live page" section (GHANALEARNERS / TESTER / AMBASSADOR-FREE names, GHS 300–3,000 table) moved ABOVE the site-ready line into a block headed "INTERNAL — NOT SITE COPY, DO NOT TRANSCRIBE," together with the transcriber notes (verbatim-refund sourcing, fine-print placement). Below the line is now pure site copy; the demarcation sentence states that a literal transcription is safe to publish. Refund text unchanged, verbatim.
2. **Requirement 2 — demarcation leak, `license-guide-v2`: FIXED.** The "Product-truth guardrails" block moved ABOVE the "full PDF content" line and marked INTERNAL — NOT PDF CONTENT. The floor/ceiling instruction now reads "do not print the private negotiation bounds recorded in offer-spec ruling 2 (the floor and ceiling)" — no bounds numerals below the content line (the header still names the superseded shipped table's prices, correctly, above the line in the INTERNAL region). Below the line: list prices only (950 / +20 / 4,500 / 475).
3. **Requirement 3 — one-pager vs. Experiment 2: initially reconciled against a superseded design; CORRECTED at one-pager rev. 3 (2026-07-19, per `review-funnel-rev2-2026-07-19.md` requirements 1–3).** An earlier revision of this item falsely recorded that channel-plan §3 designs Arm B at list GHS 1,500 (pilot GHS 750). The actual governing design (`channel-plan.md` §3 rev. 2, amending offer-spec §7, flagged for Lawrence's Day-0 confirmation): **both arms quote the published list price, GHS 950; the experimental variable is the concession** — Arm A = straight GHS 950 (+ GHS 4,500 institution anchor), no pilot line; Arm B = identical plus the 50%-off-first-cohort pilot (= GHS 475). GHS 1,500 survives only as an internal negotiation bound (offer-spec ruling 2), never printed, never quoted as an opener. Fix applied at rev. 3: both GHS 1,500 Arm B blocks deleted (the numeral now appears nowhere in the one-pager); Arm A blocks lose the pilot line; Arm B blocks carry it (V2 per-learner math recomputed — pilot ≈ GHS 16/learner at 30); the header reconciliation paragraph rewritten to state the governing design; the defunct "Arm B contamination ruling" guardrail replaced with an exposure-covariate note; KNUST re-labeled warm / non-experimental — a Wave 1 target outside the 17-target Arm A/B split, receiving the pilot per Checkpoint B ruling 3 (GHS 475, list GHS 950 preserved), the same concession Arm B's pages carry as the treatment. **Open rulings for Lawrence (re-scoped):** (a) Day-0 confirmation of the §7 experiment-design amendment flagged in channel-plan §3; (b) non-blocking — the public pilot-line question: the landing page and Touch 6 mention the 50%-off pilot, so an Arm A prospect can discover and request it; either hold the public pilot line until Experiment 2 closes, or accept it and log exposure (had seen the pricing page; raised the pilot unprompted) as covariates. Everything public stays at the GHS 950 list price either way.
4. **Requirement 4 — Touch 6 L3 gap: FIXED.** Touch 6 (email and WhatsApp renderings) now carries the free-noncommercial eligibility sentence mirroring one-pager V1: schools/universities/nonprofits/government already qualify for free noncommercial software use; the license is priced for materials, workshop system, and support; commercial providers also receive commercial-use rights.
5. **Requirement 5a — diaspora section: RESTORED (decision recorded).** Rev. 1 dropped the live "For the diaspora" gift/sponsor block silently — that was an accident, not a decision. Decision now: KEEP the angle (it is live revenue and a distribution path that matches the facilitator-first motion), REWRITE the copy to approved pricing — gift a pack at GHS 49/USD 4.50; "sponsor a classroom" now maps to the per-cohort license at GHS 950 (about USD 84) instead of the old framing, so diaspora money feeds the primary facilitator motion. Restored in `landing-page-v2` between the facilitator offer and the FAQ.
6. **Requirement 5b — email-gated free download: ADDED to blocking to-dos (item 4 below).** The v2 primary CTA converts the live direct download into email-gated delivery; the capture form and automated delivery email do not exist yet and gate the ≥25% opt-in metric and Touch 1.
7. **Also applied (non-blocking review items):** the evaluator's three sentence rewrites adopted verbatim — one-pager V2 headline, storefront long-description opener (following paragraph de-duplicated), Touch 5 closing line; Touch 4 now links the full refund policy next to its paraphrase (review item 12). Nothing the review passed was weakened: verbatim refund text intact in all three places, all prices unchanged, product-truth blocks untouched.

All revised files are stamped "rev. 2, 2026-07-19 (post-evaluator)" except the one-pager, stamped rev. 3 after the re-review correction (item 3 above); filenames unchanged.

## Files in this drop (build/apply in this order)

1. `license-guide-v2-2026-07-19.md` — L1 deliverable (a): corrected source for regenerating `facilitator-cohort-license-guide.pdf`.
2. `landing-page-pricing-v2-2026-07-19.md` — L1 deliverable (b): replacement pricing section for agenticppa.com/ghana-ai-coding-journal.
3. `landing-page-v2-2026-07-19.md` — full landing page copy, 3 headline variants.
4. `email-whatsapp-sequence-v2-2026-07-19.md` — 6-touch sequence (was 4 messages).
5. `storefront-copy-v2-2026-07-19.md` — Gumroad copy incl. L4a refund fix.
6. `facilitator-outreach-onepager-2026-07-19.md` — new asset, two L3-compliant versions.
7. This CHANGES.md.

## Verification findings (done before writing any copy)

- **`ai-journal import` SHIPS — the spec header is right, pending-corrections §4 is stale.** Verified by inspection 2026-07-19: `dist/ghana-launch/AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip` (rebuilt today 07:29, 1,155,015 bytes) contains `04-ai-learners-journal-kit-v3.3.0.zip`, which contains `scripts/session_import.py` and a `journal_cli.py` with the `import` subcommand wired ("Import a Claude Code session as a draft entry"). Copy therefore MAY mention it, and does — constrained per `docs/Paid_Product_Checklist.md`: "Claude Code-only and optional; no other tools are advertised." Pending-corrections §4 was logged before today's rebuild; market-signal-researcher/next pass should mark it resolved.
- **Bundle claims allowed:** the Student ZIP genuinely includes the full v3.3.0 release bundle (L2 resolved per spec header + pending-corrections §5). Copy updated from "v3.0.1 release bundle" to v3.3.0.
- **L1 is NOT yet fixed in dist/:** today's rebuilt `AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip` still contains a license-guide PDF printing GHS 300/750/1,500/3,000 (text extracted and read). The generator source is `scripts/generate_ghana_launch_assets.py` `facilitator_pack()` lines ~336–342 — outside my write scope. **The PDF regeneration and Facilitator ZIP rebuild remain a blocking to-do before any facilitator outreach** (spec header ruling 1). File 1 is the exact replacement content.
- **`CLAUDE.md` does not exist at the repo root** despite being cited by my agent definition and the offer-spec inputs. All targets referenced from it (2% visitor→buyer, H2 25% opt-in) were taken via the offer-spec's citations instead.
- **`growth/channel-plan.md` does not exist yet** (distribution-strategist running in parallel) — *superseded at rev. 2: the channel plan landed 2026-07-19 and rev. 2 reconciles against it (Experiment 2 arms, gate sequencing). Remaining sync points listed below.*

## Decision: floor/ceiling stay OUT of print

Offer-spec ruling 2 gives GHS 950 as opener with floor GHS 450 / ceiling GHS 1,500 as negotiation bounds. **Decision applied: list prices only (GHS 950 / +20 overflow / GHS 4,500 / pilot GHS 475) appear in the PDF, landing page, and one-pager; floor and ceiling appear nowhere public.** Rationale: (a) §3.0 showed exactly what a printed price table does — it becomes a standing counter-offer against every future quote; printing a floor recreates that bug on purpose; (b) §3.2's posture is "open at A2, hold a floor at A1" — a floor you've published is not a floor you hold; (c) Experiment 2 needs clean WTP readings at quoted prices (§7). The bounds are recorded in the one-pager's internal-guardrails block only.

## Diff vs. live assets, file by file

### 1. license-guide-v2 vs. shipped `facilitator-cohort-license-guide.pdf`
- REPLACED "Suggested cohort pricing" (GHS 300 up-to-25 / 750 up-to-100 / 1,500 up-to-250 / 3,000 up-to-750) with per-cohort GHS 950 (≤30, one run), +GHS 20/learner overflow, institution annual GHS 4,500, pilot 50% off first cohort. [spec header rulings 1–3; §3.2]
- ADDED "What is in the pack" section leading with materials value, and an in-PDF licensing note that educational/nonprofit/government buyers already qualify for free noncommercial software use — the PDF circulates to L3-protected audiences, so it must never read as "you need this license." [§1 licensing boundary; ruling L3]
- ADDED "After the cohort" reverse-upsell line — learners can buy personal Portfolio Packs (GHS 49). The shipped PDF's only CTA was the info@agenticppa.com email. [L4b; §5]
- REVISED CTA to name the fixed prices (email becomes a confirmation, not a quote request) and note invoice/MoMo. [Checkpoint-A friction goal cited in §5]
- PRESERVED verbatim: subtitle, trust note, best-use-cases list, the 2-hour workshop flow table (0–120 min), assessment rubric.

### 2. landing-page-pricing-v2 vs. live pricing display
- REMOVED the public GHS 300/750/1,500/3,000 facilitator table from the site copy. [pending-corrections §3; ruling 1]
- REMOVED any GHANALEARNERS display; GHS 49 shown as one clean price. [ruling 4; §2 flag]
- ADDED facilitator pricing block (950 / +20 / 4,500 / pilot 475), the verbatim refund text near the buy buttons [§4], the "works offline / keep every entry" product-truth guarantee [§4 positive framing, now permitted since the bundle ships], and payment-surface notes (card + PayPal + MoMo contact) per my checkout principles.

### 3. landing-page-v2 vs. `marketing/ghana-launch/landing-page-copy.md`
- Hero: was the generic "Turn your coding training into portfolio proof." Now 3 variants — A = approved H2 headline ("The portfolio evidence OMCP's certificate doesn't give you"), B = evidence-loss angle (demand-brief §3.1 voice via spec §1), C = the old generic line kept as the Experiment 3 control. [ruling 6; §7 Exp. 3]
- ADDED proof section listing only shipped artifacts (no testimonials exist; product truth §1) incl. one line on `ai-journal import` (verified above).
- Paid offer: "USD 4.50, approximately GHS 49" flipped to GHS-first [checkout principles]; bundle updated to v3.3.0.
- Facilitator block: "use the cohort license" → named GHS 950/30-learner price. [§5]
- FAQ: kept all four live questions (official-status answer extended to "complements, never replaces"); ADDED certificate-objection, AI-cost/BYO-key, program-pause, and refund questions [demand-brief objections via spec §1/§4; agent-definition FAQ requirement]. Python answer now states 3.9+ explicitly.
- Free-offer copy now states "no account, no data cost after download, entries stay on your device." [§1 Free positioning]

### 4. email-whatsapp-sequence-v2 vs. `marketing/ghana-launch/email-whatsapp-sequence.md`
- 4 messages → 6 touches, each with email + WhatsApp renderings (agent contract: 5–7 touch).
- Old M1 → Touch 1 (delivery reframed to opt-in confirmation). NEW Touch 2 (mid-week nudge, §3.1 forgetting-voice). Old M2 → Touch 3, promoted to the Day-7 conversion moment with the §5 approved reframe ("You now have 7 days of proof. Your certificate won't hold the next 12 weeks — the Portfolio Pack will."). NEW Touch 4 (objections/product truth: certificate-complement, offline/no-subscription, BYO-key + no-accuracy-guarantee). Old M4 → Touch 5 but REWRITTEN: GHANALEARNERS removed, closes at list GHS 49. [ruling 4] Old M3 → Touch 6: "Ask about a cohort license" → "GHS 950 for up to 30 learners" fixed price. [§5 teaches-others trigger]
- Program-stall trigger used once, supportively ("If a program portal ever goes dark, your record doesn't") per §5 "use sparingly."

### 5. storefront-copy-v2 vs. `marketing/ghana-launch/gumroad-product-copy.md`
- **L4a:** refund section was "…refunds available within 7 days only if the files cannot be accessed or the product was purchased by mistake and has not been downloaded" — conflicts with REFUND_POLICY.md. REPLACED with the verbatim storefront text. [§4; ruling L4]
- REMOVED the entire "Launch discount" section (GHANALEARNERS, 20% first 100). [ruling 4]
- Bundle line updated v3.0.1 → v3.3.0 (verified shipping). ADDED "How the app works" product-truth block: local Markdown storage, browser interface via START HERE, Python 3.9+, BYO API key + provider-credits note, no AI-accuracy guarantee, `ai-journal import` as optional/Claude-Code-only. [Paid_Product_Checklist "Product truth" + "Storefront" rules]
- Short description now opens "No coding required to start" and the long description gives the START HERE double-click as the first instruction; version visible in title and footer. [checklist storefront rules]
- ADDED outcomes disclaimer (artifacts, not job guarantees) and the facilitator cross-sell at GHS 950. [§4; §5]
- Subtitle now carries the H2 positioning in program-neutral wording ("your certificate") since Gumroad reaches beyond OMCP.

### 6. facilitator-outreach-onepager (new; no live counterpart)
- Two versions enforcing L3: V1 (OMCP centers/universities) leads with materials/workshop value, includes the free-noncommercial acknowledgment, zero commercial-rights framing; V2 (private bootcamps/paid trainers) adds commercial-use rights + per-learner economics. [§1 licensing boundary; ruling L3]
- Pilot: 50% off first cohort = GHS 475, positioned as the risk-reducer; no outcome guarantees anywhere. [ruling 3; §4]
- Internal guardrails block records the floor/ceiling, B2-only-on-multi-cohort posture, verbatim objection logging for Experiment 2, and the do-not-send-old-PDF rule. [§3.2; §7]

## Conflicts hit and how resolved

1. **Spec header vs. pending-corrections §4 on `ai-journal import`:** resolved by ZIP inspection — it ships (see Verification). Spec header wins; correction note is stale.
2. **Approved H2 headline names OMCP vs. "independent, not official" trust note:** kept the approved headline verbatim on the landing page (ruling 6) with the trust note directly present; used program-neutral "your certificate" wording on Gumroad and in emails, which reach non-OMCP audiences. Flag for evaluator: confirm naming OMCP in a paid-product headline is acceptable alongside the disclaimer.
3. **Floor/ceiling in print:** resolved as documented above — internal only.
4. **Checklist says support email in bundle docs is `agbe@udel.edu` (free README) while marketing uses `info@agenticppa.com`:** copy standardized on info@agenticppa.com (the spec's CTA address); flag the free-README support line for the next dist pass.

## Sync points with `growth/channel-plan.md` (2026-07-19 version — rev. 2 reconciliation done; these remain open)

Reconciled at rev. 2: Experiment 2's two-arm design (plan §3) now has matching one-pager pricing blocks; the plan's Day-0/L1 gate matches this file's blocking to-dos 1–2; the plan's §7 flag 2 (landing page still says "v3.0.1 bundle") is fixed in `landing-page-v2`. Still open — revisit with distribution-strategist:

- **Experiment 2 open rulings** (item 3 above, as corrected): Lawrence's Day-0 confirmation of the §7 design amendment, and the non-blocking public-pilot-line visibility question (hold it until Experiment 2 closes, or keep it and log exposure). If the plan revises Experiment 2's design again, the one-pager's arm blocks must be re-matched.
- Touch spacing/timing and the WhatsApp broadcast mechanics in `email-whatsapp-sequence-v2` (channel ownership, opt-in source, send windows) — the plan assigns WhatsApp to P2 but does not fix send-day mechanics.
- Which headline variant serves which channel: plan §4 sends P2 + E1 traffic to the H2 variants Week 1 — matches Experiment 3's A/C split here; confirm C-variant traffic allocation.
- Whether the facilitator one-pager is delivered as email attachment, WhatsApp PDF, or print — formatting pass may be needed; the plan's "one-page facilitator PDF/link kit" (Gate week) should be built from this file.
- Social scripts (`marketing/ghana-launch/social-content-scripts.md`) were NOT revised here — script 9's "Ask about the cohort license" CTA also needs the GHS 950 update at Checkpoint C, and script CTAs should map to the channel plan first.
- The plan's §7 flag 1 (Gumroad is card/USD; no MoMo rail) is consistent with our copy ("contact us if you need a mobile-money option") — if H1 underperforms, test rails before concluding price failure.
- `growth/metrics.md` still does not exist (plan §6 recommends creating it) — needed before any experiment reads.

## Blocking to-dos outside my scope (for Lawrence / next dist pass)

1. Transcribe `license-guide-v2-2026-07-19.md` into `scripts/generate_ghana_launch_assets.py` and rebuild the Facilitator ZIP — the shipped PDF still prints GHS 300–3,000 as of today's 07:29 build. No facilitator outreach until done (ruling 1).
2. Apply `landing-page-pricing-v2-2026-07-19.md` to the live site pricing section (same precondition).
3. Remove/expire the GHANALEARNERS code on Gumroad so the page and checkout agree at GHS 49.
4. **Build the email-gated free-download mechanism (added at rev. 2, evaluator requirement 5/Refutation 10):** the v2 landing page's primary CTA promises "just your email — the download link comes straight to your inbox," but the live page is a direct download with no capture. Needs: an opt-in form on the landing page, automated delivery of the free-pack link (Touch 1), and consent-compliant storage of the address for Touches 2–6. This gates the H2 ≥25% opt-in metric and the whole sequence — without it, ship the v2 page with the direct-download CTA and mark Experiment 3's opt-in metric unreadable.
5. **Confirm Experiment 2's amended design at Day 0 (decision owner Lawrence, with distribution-strategist):** channel-plan §3 rev. 2 amends offer-spec §7 (both arms quote the published GHS 950 list; the concession is the variable) and flags it for confirmation at the Day-0 check-in. Related, non-blocking: rule on the public pilot-line question (item 3 above) — hold the landing-page/Touch 6 pilot mention until Experiment 2 closes, or keep it and log exposure per prospect.
