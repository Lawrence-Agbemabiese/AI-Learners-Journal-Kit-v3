# Evaluator Review — growth/demand-brief.md (Cycle 1, rev. 2)

**Artifact:** `growth/demand-brief.md` (Demand Brief, 2026-07-02, rev. 2 after evaluator REVISE)
**Evaluator pass date:** 2026-07-02 (second pass)
**Rubric:** `.claude/skills/evaluator-rubric/SKILL.md` (all criteria must score ≥4/5)

## Verdict: PASS

All eight rev. 1 revision requirements were implemented and independently re-verified — not taken on the reviser's word. New content introduced in rev. 2 (revenue arithmetic, rebuilt WTP case, verification column) was adversarially checked; arithmetic was recalculated by hand and the newly load-bearing citations were re-fetched. One non-blocking nit remains (below). Ready for Checkpoint A.

---

## Rubric scorecard (rev. 2)

| # | Criterion | Score | Justification |
|---|-----------|-------|---------------|
| 1 | Pain urgency | 4 | All pain-point quotes (Techlabari registrant, both Kolawole/DEV quotes) verified verbatim by fetching; Ghana-local learner voice is still absent, honestly flagged as Unknown #4 (cross-reference now correct), which caps this at 4. |
| 2 | Promise believability | 4 | The reframed promise — "portfolio evidence OMCP's certificate doesn't give you" — is concrete, falsifiable, and no longer contradicted by the GBC source; not a 5 because the portfolio-output mechanism depends on 12-week pack materials the offer-spec has not yet defined. |
| 3 | Differentiation | 5 | Rev. 2 now names the rubric's canonical free alternative — "ChatGPT plus an ordinary notebook or Google Doc, which costs nothing and requires no install" — and states the dimensions to beat (structure, searchability, portfolio output), each matching real v3.0.1 capabilities (JSON-index search, structured Markdown entries). |
| 4 | Economics | 4 | Three-scenario revenue table recalculated and correct (1,000 × 2% × GHS 49 = GHS 980 ≈ USD 86 at 11.34; Scenario C ≈ USD 1,729; 49/11.34 = 4.32; one USD 100 license ≈ 23 student sales; 13 × 100 = 1,300), with the honest and conservative implication that the student tier alone is modest revenue; not a 5 because Scenario B's 10k-visit reach and Scenario C's 5% visit rate are labeled assumptions rather than sourced figures. |
| 5 | Global fit | 5 | GHS anchor with verified minimum-wage arithmetic (49 / 21.77 ≈ 2.3 days), PPP framing for all three expansion markets, cedi/MoMo rails via verified Selar GHS pricing, and no US idioms. |
| 6 | Product truth | 5 | Product-truth paragraph and §3 item 5 unchanged from rev. 1 and re-checked against `README.md`: beginner menu, JSON-index search, local Markdown, optional BYO-key AI, structure-only AI review score, offline Starter Guide, and the explicit absence claims (no cloud sync/mobile/spaced repetition) all match; no AI-accuracy guarantees anywhere. |
| 7 | Slop check | 5 | Typo fixed, retraction notes are specific and dated, cross-references corrected, verification-status column adds real information; nothing generic or interchangeable — publishable under Lawrence's name. |

---

## Rev. 2 verification log (fix-by-fix)

| Rev. 1 requirement | Status | Evidence |
|---|---|---|
| 1. Remove Selar GHS 40–250 | **Done** | Row deleted; retraction note in §2; WTP rebuilt on verified ALX USD 5/mo + the ₵30 example (both match my rev. 1 fetches); table now shows "₵30 only — Verified on page (single example, not a market band)". |
| 2. Remove Selar NGN 3,000–20,000 | **Done** | Row deleted; covered by the same retraction note; §6 logs both retractions explicitly. |
| 3. Narrow certificates claim | **Done** | §1 now quotes GBC's "globally recognized certifications" (verified in my GBC fetch) and scopes the gap to portfolios/process documentation; H2 copy updated to match. |
| 4. Trim partner list | **Done** | Now "Huawei, MTN, AWS, and Oracle" — exactly what the Techlabari fetch showed; Google/Microsoft removed. |
| 5. Soften 3MTT "requires" | **Done** | §3 and §5 now say "incentivized — not mandated," name the 10GB MTN data reward condition, disclose the KB 403s, and mark video/prize specifics unverified — matching my corroboration exactly. |
| 6. Reconcile university count | **Done** | Both figures now shown side by side ("4–12 institutions pending direct confirmation"), flagged in §1, §3-facilitator, §6, and Unknown #3. |
| 7. Add revenue arithmetic | **Done** | §2 scenario table + facilitator asymmetry; all six calculations recomputed and correct; assumption inputs labeled; 1% falsification floor stated. |
| 8. Fix typo; mark Gumroad unverified | **Done** | "reworked" fixed; USD 25.98 removed and logged in §6 as a search-snippet artifact; Gumroad row marked Unverified. |

**Fresh adversarial checks on new/newly load-bearing claims:**

- **Mastercard Foundation / ALX 32,000+ incl. Accra** (now the WTP case's second leg): fetched and verified — "over 32,000 new tech learners in eight African countries," Accra named among the eight Karibu cities.
- **ALX Pathway Foundations USD 5/mo (USD 40 / 8 months):** the figure is corroborated by multiple independent sources (GreenEconomy.Media, FutureSA: "$5 USD monthly fee... total of $40 USD over 8 months"), **but the cited alxafrica.com/how-it-works URL now returns 404**, so the row's "Verified on page" label is not currently reproducible — see nit below.
- **No previously verified claim was broken by the edits:** OMCP figures (90k/48h, 12,623 by 30 May 2026, 859 pilot, 130 centers, 400k target), quotes, minimum wage, FX arithmetic, and the Nigeria-workshop Facilitator-Pack framing (still correctly caveated, twice) all carried over intact.

## Remaining issues (non-blocking — fold into the next cycle, do not hold Checkpoint A)

1. **ALX Pathway row:** change "Verified on page" to "corroborated via press; primary URL currently 404" or re-source to a live ALX page. The number is sound; the label overstates current verifiability.
2. **Ghana-local learner quotes** (Unknown #4) remain the single biggest evidence gap before conversion copy is written — already correctly gated in the brief.
3. **Scenario B/C reach assumptions** must be replaced with observed numbers in `growth/metrics.md` after the first test cycle.

---

## Appendix — Rev. 1 review summary (audit trail, 2026-07-02 first pass)

**Verdict: REVISE.** Scores: Pain urgency 4, Promise believability 4, Differentiation 4, **Economics 2**, Global fit 4, Product truth 5, Slop check 4.

Key refutations (all found by fetching cited sources): (1) Selar Ghana ebook guide contained no "GHS 40–250" band (only a ₵30 example) — used in Segment 2 WTP, pricing table, and H1 basis; (2) Selar 2026 guide contained no "NGN 3,000–20,000" Notion-template pricing; (3) §1/§6's "no press mention of certificates" was contradicted by the brief's own GBC source quoting the Minister on "globally recognized certifications"; (4) Techlabari partner list padded with Google and Microsoft (not in the article); (5) 3MTT "requires weekly reflections" overstated — sources describe incentivized behavior (10GB MTN data reward), and both KB pages return 403; (6) GBC "at least four" vs Ecofin "twelve" universities unreconciled; (7) Gumroad "USD 25.98" unverified; (8) typo "rewowrked"; plus no price × conversion × audience arithmetic despite the rubric requiring it. Claims that survived attack: all headline OMCP figures, both learner quotes verbatim, ALX All Access USD 5/mo, minimum wage GHS 21.77, FX/wage arithmetic, product-truth compliance, and the correct Facilitator-Pack framing of the Nigeria workshop. Eight numbered revision requirements were issued; all are verified Done above.

---

*Next step: Checkpoint A (Lawrence). On approval, offer-architect consumes `growth/demand-brief.md` to produce `growth/offer-spec.md`. Rev. 2's remaining issues 1–3 above should be inherited as open items, not silently dropped.*
