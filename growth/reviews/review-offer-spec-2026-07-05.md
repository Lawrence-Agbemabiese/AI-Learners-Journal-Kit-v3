# Evaluator Review — growth/offer-spec.md (2026-07-05)

**Reviewer:** evaluator agent
**Artifact:** `growth/offer-spec.md` (Cycle 1 draft, Checkpoint B pending)
**Evidence base checked against:** `growth/demand-brief.md` (approved Checkpoint A 2026-07-05), `README.md`, `docs/Paid_Product_Checklist.md`, `REFUND_POLICY.md`, `docs/Workshop_Facilitator_Guide.md`, `marketing/ghana-launch/gumroad-product-copy.md`, `marketing/ghana-launch/email-whatsapp-sequence.md`, and the actual shipped artifacts in `dist/ghana-launch/` (all three ZIPs opened and inspected; license-guide PDF text extracted).

---

## Verdict: REVISE

The spec is well-structured, honestly caveated on pricing, and traceable to the demand brief in most places — but it fails product truth. It promises pack contents the shipped Student ZIP does not contain, asserts a legal claim the product's own license summary contradicts for the primary buyer segment, and — the most consequential miss — never mentions that the shipped Facilitator license-guide PDF **already publishes cohort prices** (GHS 300–3,000) that undercut and contradict every provisional SKU in §3. The spec listed the dist ZIP contents among its inputs, so this is a failure against its own declared evidence, not missing web access.

---

## Rubric scorecard (pass requires every criterion ≥4)

| # | Criterion | Score | Justification |
|---|---|---|---|
| 1 | Pain urgency | 4 | Inherits the brief's cited pains (Mangabo quote, OMCP portal-offline quote) accurately and honestly flags the Ghana-local-voice gap, with §6 questions built to close it — but local primary quotes are still absent, capping this below 5. |
| 2 | Promise believability | 3 | Tier promises are mostly scoped and falsifiable, but a skeptical facilitator who opens the pack can falsify three claims in it (missing v3.0.1 bundle, invented "2–3 hour" agenda attribution, nonexistent license-guide upsell line). |
| 3 | Differentiation | 4 | Every tier names ChatGPT + notebook and states the winning dimension (structure, searchability, portfolio output per brief §2) — but the Premium tier's keystone differentiator ("no free template can offer" the license) is legally overbroad (see Refutation 2). |
| 4 | Economics | 3 | Arithmetic is shown throughout and 14 of 15 recomputed figures check out, but "~78% discount vs. retail stack" is wrong (actual ~22–35%), and the entire §3 pricing logic ignores the already-shipped GHS 300/25-learner price in the product itself. |
| 5 | Global fit | 5 | GHS anchor with dated FX source, minimum-wage framing, MoMo named as the out-of-pocket rail (A1 rationale), Nigeria/Kenya prices explicitly deferred pending rate/rails verification, no US idioms. |
| 6 | Product truth | 1 | Automatic fail per rubric: the Student tier contents claim "full v3.0.1 release bundle" is not true of the shipped ZIP, and the "2–3 hour workshop agenda" is not in the cited guide (details below). |
| 7 | Slop check | 5 | Specific voice, concrete numbers, honest "what I could NOT support" section, nothing generic or wasted. |

**Result: 1 criterion at 1, two at 3 → REVISE.**

---

## Refutations found

### R1 — CRITICAL: the shipped product already publishes facilitator prices that contradict §3 (traceability/consistency failure)
`dist/ghana-launch/AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip` → `facilitator-cohort-license-guide.pdf` contains a **"Suggested cohort pricing"** table: Starter GHS 300 (≤25 learners), Growth GHS 750 (≤100), Institution GHS 1,500 (≤250), Large program GHS 3,000 (≤750). The spec's §3 premise — replacing "Contact / license" with first-ever fixed prices — is false: prices are already shipped inside the deliverable. Consequences the spec never addresses:
- SKU A2 (GHS 950, ≤30 learners) is **3.2×** the shipped price for a comparable cohort (GHS 300/25). A 100-learner deal under the spec's overflow rule costs GHS 950 + 70×20 = **GHS 2,350** vs. the shipped **GHS 750** — a buyer who opens the PDF they just licensed sees they were quoted triple.
- Experiment 2 (two-point WTP test) is contaminated: respondents holding the pack can see GHS 300.
- The brief's §2 line "the Facilitator Pack has no published price (contact/license per CLAUDE.md)" is itself contradicted by the shipped PDF — the spec inherited this without checking the ZIP it lists as an input.

### R2 — Overbroad legal claim (product truth / believability)
§1 Premium: "the PolyForm Noncommercial license means program/bootcamp use *requires* a commercial license — the Facilitator Pack IS that license, which no free template can offer." Per `README.md`, PolyForm Noncommercial 1.0.0 permits free noncommercial use **"including … educational institutions, nonprofits, public research organizations, and government bodies."** OMCP centers (government program, free to learners) and the 4–12 partner universities — the spec's own primary targets — plausibly need no commercial license at all. The claim holds only for private for-profit bootcamps (Codetrain, IIPGH-type paid classes). As written, the Premium tier's core differentiator is false for most of the named buyer list.

### R3 — Product-truth violation: "full v3.0.1 release bundle" is not in the shipped Student ZIP
The §2 tier table lists "full v3.0.1 release bundle" among Student Pack contents "(v3.0.1 truth)". The actual shipped `AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip` (13.6 KB) contains only three PDFs, three policy files, and README.txt — no release bundle. `README-student-pack.txt` even tells the buyer to "unpack the included v3.0.1 release bundle," which is absent. Note: this is simultaneously a packaging bug and a live refund trigger under `REFUND_POLICY.md` ("the release ZIP is corrupted or missing required files") — it must be surfaced to Lawrence, not asserted as truth.

### R4 — Fabricated duration and wrong attribution: "a ready 2–3 hour workshop agenda (`docs/Workshop_Facilitator_Guide.md`)"
The facilitator guide contains an agenda, exercises, and safety guidance but **no stated duration anywhere**. The only timed flow in the product is the license-guide PDF's 0–120-minute (2-hour) workshop table. "2–3 hour" appears in no source.

### R5 — Unsupported claim in §5: "the license guide already tells them learners can buy personal packs after the cohort ends"
The extracted license-guide text contains no such statement; its only CTA is "email info@agenticppa.com with your cohort size…". The reverse-upsell mechanism the spec says "costs nothing to keep" does not currently exist.

### R6 — Arithmetic error: "~78% discount vs. retail stack" (SKU A2)
GHS 950 against the 25-learner stack (GHS 1,225) is a **22.4% discount** (950 is 77.6% *of* the stack — "% of" confused with "% discount"). Against the SKU-consistent 30-learner stack (GHS 1,470) it is **35.4%**. Also note the baseline inconsistency: §3 logic 1 computes the ceiling on 25 learners while SKU A covers "up to 30."

### Arithmetic verified correct (for the record)
GHS 49/11.34 = USD 4.32; 49 ≈ 2.25 days × GHS 21.77 ✓; 25×49 = 1,225 ✓; A1 450 ≈ USD 39.7, GHS 15/learner, 9.2× student pack ✓; A2 GHS 31.7/learner ✓; A3 132.3 USD, GHS 50/learner ✓; B1–B3 USD and break-even multiples (2.63 / 4.74 / 8.42) ✓; 13 × 950 = 12,350 ≈ USD 1,089 ✓; USD 100 ≈ GHS 1,134 ≈ 23.1 student sales ✓; 49 × 0.8 ≈ GHS 39 ✓; KES: 174,000/1,300 ≈ 134/USD, 4.5 × 134 ≈ 603 ✓; A3 pilot 1,500/2 = 750 ✓.

### Traceability spot-checks that PASSED (≥3 required)
- 12,623 completions by 30 May 2026 / 400k target / ~130 centers / 4–12 universities "unreconciled" — all match brief §1 verbatim, with the conflict caveat preserved ✓
- ALX USD 5/month as "the only verified comparable," within ~10% of USD 4.50 — matches brief §2, and the one-time-vs-subscription assumption is correctly carried into H1 rather than asserted ✓
- IIPGH GHS 200–300 flagged 2021-stale; Selar ₵30 flagged single example; NGN band correctly treated as retracted (brief §6) ✓
- OMCP portal offline by Nov 2025; GHS 14,000 laptop; 3MTT "incentivized, not mandated" — all match brief §3/§5 including caveats ✓
- H2 headline lineage to email Message 2 verified: "A certificate says you attended" is in `email-whatsapp-sequence.md` Message 2 ✓

### Refund-policy checks PASSED
The §4 storefront text matches `REFUND_POLICY.md` verbatim, character for character ✓. The spec correctly detected the real conflict in `gumroad-product-copy.md` ("purchased by mistake and has not been downloaded") and routed the fix to conversion-system-builder without editing outside its scope ✓. No outcome guarantees offered ✓.

### Provisional-pricing and Checkpoint B framing PASSED
"PROVISIONAL" appears at the header, §2, §3 (twice), and the Checkpoint B request opens with "pricing is your decision; nothing above is final." July 10 gating is explicit throughout. Compliant.

---

## Revision requirements (addressed to offer-architect)

1. **Reconcile §3 with the shipped pricing.** Open `facilitator-cohort-license-guide.pdf`, quote its Suggested cohort pricing table (GHS 300/750/1,500/3,000 by learner count) in the spec, and rebuild the SKU logic to either (a) supersede it — in which case add an explicit precondition that the PDF is regenerated/withdrawn before any H3 outreach or Experiment 2 quoting, or (b) anchor the provisional SKUs to it. Add the reconciliation decision to the Checkpoint B request list. Also state that Experiment 2 is invalid while the GHS 300 price ships inside the pack.
2. **Fix the discount arithmetic.** Replace "~78% discount vs. retail stack" with the correct figure and a single consistent baseline: GHS 950 is ~35% below the 30-learner retail stack of GHS 1,470 (or ~22% below the 25-learner GHS 1,225 — pick one; SKU A covers 30, so use 1,470 and update §3 logic 1 to match).
3. **Scope the PolyForm claim.** Rewrite the Premium "why it beats" bullet so the commercial-license-required argument applies only to commercial users (private bootcamps, paid trainers), and reframe value for OMCP centers/universities (who may qualify for free noncommercial use per README's license summary) around day-one cohort materials, printables, the workshop flow, and facilitator support — or add "does the license actually bind government/university programs?" as an explicit Checkpoint B ruling for Lawrence.
4. **Remove or condition "full v3.0.1 release bundle"** in the Student tier contents until the shipped ZIP contains it. Add a flagged action item for Lawrence: the current `AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip` omits the bundle that `README-student-pack.txt` and the Gumroad copy promise — a live refund trigger under `REFUND_POLICY.md` that must be fixed before H1 traffic.
5. **Correct the workshop-agenda claim.** State what actually ships: a step-by-step facilitator runbook with exercises and safety guidance (`docs/Workshop_Facilitator_Guide.md`, no stated duration) and a 2-hour timed workshop flow (license-guide PDF). Drop "2–3 hour" or source it.
6. **Fix §5's facilitator→student reverse upsell.** Delete "the license guide already tells them…" and replace with a recommendation: "add one line to the license guide/README telling facilitators that learners can buy personal packs after the cohort" — routed to conversion-system-builder as a copy change, since the line does not exist today.

---

## The 3 weakest sentences (quoted, with rewrites)

1. > "A2 — Anchor (recommended opener) | **GHS 950** | ~84 | GHS 32 | Just under the brief's USD-100 arithmetic anchor; per-learner cost sits at the verified Selar ₵30 example (§2); ~78% discount vs. retail stack."
   **Rewrite:** "Just under the brief's USD-100 arithmetic anchor; per-learner cost (GHS 31.70) lands near the one verified Selar price point (₵30, single example — §2); ~35% below the 30-learner retail stack of GHS 1,470. Caution: the shipped license-guide PDF currently suggests GHS 300 for a 25-learner cohort — that conflict must be resolved before this number is quoted to anyone."

2. > "…and a legal right to distribute commercially (the PolyForm Noncommercial license means program/bootcamp use *requires* a commercial license — the Facilitator Pack IS that license, which no free template can offer)."
   **Rewrite:** "…and, for commercial trainers (private bootcamps, paid instructors), the commercial-use rights the PolyForm Noncommercial license otherwise withholds. Note: educational institutions, nonprofits, and government bodies already qualify for free noncommercial use under the license, so for OMCP centers and universities the pack sells on ready-made cohort materials and the 2-hour workshop flow — not legal necessity. (Checkpoint B: Lawrence to confirm the licensing boundary.)"

3. > "…the license guide already tells them learners can buy personal packs after the cohort ends — facilitator → student is the reverse upsell and costs nothing to keep."
   **Rewrite:** "…facilitator → student is the reverse upsell. It costs one line of copy we have not yet written: conversion-system-builder should add 'your learners can buy personal Portfolio Packs after the cohort ends' to the license guide and facilitator README."

---

*Next step: offer-architect revises against requirements 1–6, then rerun this evaluation. Requirements 1 and 4 also generate action items for Lawrence outside the spec itself (regenerate the license-guide PDF or adopt its prices; repackage the Student ZIP with the v3.0.1 bundle).*

---
---

# SECOND PASS — Evaluator re-review of rev. 2 (2026-07-05)

**Artifact:** `growth/offer-spec.md` rev. 2 (claims all 6 first-pass requirements implemented)
**Method:** every fix re-verified independently against the shipped files — both `dist/ghana-launch/` ZIPs re-listed, `facilitator-cohort-license-guide.pdf` and `02-student-portfolio-pack.pdf` text re-extracted, `docs/Workshop_Facilitator_Guide.md`, `README.md` §License, `REFUND_POLICY.md`, `gumroad-product-copy.md`, `email-whatsapp-sequence.md`, and the free-tier ZIP all re-read. All new/changed arithmetic recomputed by hand. The reviser's claims were not taken on trust.

## Verdict: PASS

All 6 requirements are genuinely implemented, every rev.-2 factual claim I tested matches the shipped artifacts, and all recomputed arithmetic is correct. All rubric criteria now score ≥4. PASS applies to the *document*; it does not clear the funnel to ship — L1 (pricing reconciliation) and L2 (Student ZIP repackaging) remain hard blockers that rev. 2 itself correctly imposes on H3 outreach, Experiment 2, and H1 traffic.

## Rubric scorecard (second pass)

| # | Criterion | Score | Justification |
|---|---|---|---|
| 1 | Pain urgency | 4 | Unchanged: brief-cited pains (Mangabo, OMCP portal quote) carried accurately with caveats, but Ghana-local primary quotes are still absent (Unknown #4) — §6 questions exist to close this, capping at 4. |
| 2 | Promise believability | 5 | The three falsifiable-in-the-box claims from pass 1 are gone; every remaining content claim (pack PDF contents, untimed runbook, 2-hour flow, license terms) now matches what I extracted from the shipped files, and copy is explicitly gated on L2 where the ZIP falls short. |
| 3 | Differentiation | 5 | Every tier names ChatGPT + notebook and the winning dimension; the Premium differentiator is now correctly split — commercial rights for commercial trainers only, materials/workshop value for free-noncommercial-eligible institutions — so it survives a skeptical buyer reading the license. |
| 4 | Economics | 4 | All 20+ recomputed figures check out and the L1 decision is monetarily sized (GHS 12,350 vs 3,900 at 13 buyers), but every facilitator number remains constructed rather than evidenced (honestly flagged; July 10 is the first real signal) — present and conservative, not yet sourced, so 4. |
| 5 | Global fit | 5 | Unchanged: GHS anchor with dated FX, minimum-wage framing, MoMo rail, NGN correctly withheld pending verification, KES flagged derived. |
| 6 | Product truth | 5 | Every feature claim re-verified against shipped artifacts is accurate, the ZIP defect is disclosed rather than papered over (with copy gated on the fix), BYO-API-key stated, no outcome guarantees; no violations found. |
| 7 | Slop check | 5 | Rev.-2 additions (§0, §3.0/§3.1) are load-bearing and specific — the supersede-vs-anchor analysis with a costed recommendation is decision-ready, nothing generic added. |

**Result: all criteria ≥4 → PASS.**

## Fix-by-fix verification log

| Req | Status | Evidence (independently re-verified) |
|---|---|---|
| 1 — Reconcile §3 with shipped pricing | **VERIFIED** | Re-extracted `facilitator-cohort-license-guide.pdf`: "Suggested cohort pricing — Starter GHS 300/25, Growth 750/100, Institution 1,500/250, Large 3,000/750" matches §3.0's table exactly, including per-learner math (12.00/7.50/6.00/4.00 ✓). §3.1 gives both paths with the Path-(a) precondition (regenerate PDF before any outreach/quoting); Experiment 2 marked INVALID in §3.0 and §7; reconciliation is Checkpoint B request #1. |
| 2 — Fix discount arithmetic | **VERIFIED** | "~78%" is gone. A2 now reads "~35% below the 30-learner retail stack of GHS 1,470": (1,470−950)/1,470 = 35.4% ✓. §3.2 logic 1 rebuilt on 30 × 49 = 1,470 with the 25-learner 1,225 explicitly demoted to a reference point — single consistent baseline as required. |
| 3 — Scope the PolyForm claim | **VERIFIED** | `README.md` §License (lines 229–237) confirms free noncommercial use "including … educational institutions, nonprofits, public research organizations, and government bodies." §1 Premium now restricts commercial-rights framing to "commercial trainers only," adds the licensing-boundary paragraph forbidding "you need this license" framing with OMCP centers/universities, and routes the boundary ruling to Lawrence as L3 / Checkpoint B #3. |
| 4 — Remove/condition "full v3.0.1 release bundle" | **VERIFIED** | Re-listed the Student ZIP (13,650 bytes = "13.6 KB" ✓): exactly 3 PDFs + 3 policy files + README.txt, no bundle. ZIP's README.txt says verbatim "unpack the included v3.0.1 release bundle"; `gumroad-product-copy.md` line 41 promises "full AI Learner's Journal Kit v3.0.1 release bundle" — both cited correctly in L2. §2 tier row now flags "NOT currently shipped — do not claim in copy until L2 is fixed"; L2 blocks H1 (Experiment 1 precondition) and is correctly tagged a live refund trigger — both quoted refund clauses appear verbatim in `REFUND_POLICY.md`. |
| 5 — Correct workshop-agenda claim | **VERIFIED** | "2–3 hour" no longer appears. Re-read `docs/Workshop_Facilitator_Guide.md` (identical to the copy inside the Facilitator ZIP): recommended agenda, sample exercise, troubleshooting script, safety guidance, **no stated duration** — matches §1's "untimed runbook" description. Re-extracted PDF confirms the 0–120 min "Workshop flow" table → "2-hour timed workshop flow" is accurately sourced. |
| 6 — Fix §5 reverse upsell | **VERIFIED** | The false "license guide already tells them" line is gone. Re-extracted PDF confirms the only CTA is "email info@agenticppa.com with your cohort size, dates, institution or group name…" — exactly as §5 now states. The one-line addition is routed to conversion-system-builder as L4b, bundled with the L1/L2 dist rebuild. |

## Adversarial check of NEW rev.-2 content — no refutations found

- **§0 action items:** L1–L4 all trace to verified facts (pricing table ✓, ZIP contents ✓, README license text ✓, gumroad refund conflict re-confirmed at line 64 + GHANALEARNERS at line 68 ✓). The "L1+L2 share one dist rebuild" efficiency note is sound.
- **§3.0 arithmetic:** 950 + 70×20 = 2,350 vs shipped 750 ✓; "~3× the printed price" = 2,350/750 = 3.13 ✓. The claim that the brief's "no published price" line originated in `CLAUDE.md` is correct (CLAUDE.md says "Contact / license"; brief §2 cites it).
- **§3.1 supersede-vs-anchor:** 13 × 300 = 3,900 ≈ USD 344 ✓; "collapse to GHS 4–7.50/learner at scale" ✓; "`growth/metrics.md` does not exist" independently confirmed (no such file); "essentially no copies in buyers' hands" is framed as inference, consistent with zero live funnel numbers. Recommendation logic (Path (a), decided after July 10) is internally consistent and leaves pricing to Lawrence.
- **§2 tier contents:** Free ZIP re-listed — fillable 7-day PDF + `ai-coding-journal-starter/` (CLI + web app) + README ✓. Student-pack PDF re-extracted — 12-week tracker, prompt log, project case-study template, GitHub README starter, internship/scholarship tracker all present ✓. `03-facilitator-notes-preview.pdf` inside Student ZIP ✓ (§5 seeding claim). |
- **Revised experiments:** thresholds trace to CLAUDE.md (≥2%/<1%, ≥25%) and brief H3 (≥3 calls/≥1 paid/<2 replies); Experiment 2's added "≥GHS 450" floor is honestly labeled as "H3 thresholds + A1 floor". §6 Q3's "do not name a price first" instruction correctly protects the last uncontaminated WTP source.
- **Storefront text §4:** still verbatim-identical to `REFUND_POLICY.md` ✓.

## Minor notes (non-blocking, no action required for PASS)

1. §2 says GHS 49 ≈ "2.3 days" of minimum wage; 49/21.77 = 2.25 — rounding is slightly generous but immaterial.
2. PASS is a document verdict. Operationally, nothing in the facilitator motion may ship until Lawrence rules on L1 and the dist rebuild lands (L1+L2) — the spec itself says so; Lawrence's Checkpoint B sign-off is still required per the growth workflow.

*Second pass complete: rev. 2 proceeds to Checkpoint B (Lawrence).*
