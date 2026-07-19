# Offer Spec — 2026-07-05 (Cycle 1, rev. 2)

**APPROVED 2026-07-19 (Lawrence, Checkpoint B).** Rulings:
1. **L1 — SUPERSEDE.** The shipped GHS 300/750/1,500/3,000 table (license-guide PDF + landing page) is superseded by this spec's pricing. Hard precondition before ANY facilitator outreach or Experiment 2: regenerate the license-guide PDF and update the landing-page pricing section to match.
2. **Facilitator per-cohort opener: GHS 950** (A2; floor GHS 450, ceiling GHS 1,500). Institution tiers per §3 (B2 GHS 4,500 anchor). Still provisional against real WTP data — first real negotiations may move it.
3. **KNUST pilot: 50% off first cohort** (GHS 475 at the opener) — list price preserved, produces the cycle's first real paid data point.
4. **Student tier: GHS 49, retire the GHANALEARNERS 20% code** from draft copy so H1 measures one clean price. TESTER and AMBASSADOR-FREE codes remain for tester/ambassador distribution and are excluded from H1 metrics.
- **L3 confirmed:** OMCP centers/universities qualify for free noncommercial use under PolyForm per README.md; facilitator sales to them lead with materials/workshop value, never "you need this license."
- **L4 approved:** both copy tasks routed to conversion-system-builder in Stage 3.
- **Conversation intel (July 19):** Kwaku S. is enrolled in OMCP and positioned as a genuine ambassador (AMBASSADOR-FREE code fits); Prof. B. Amenu (KNUST) confirms access to a potential student cohort — the H3 pilot venue. Unprompted facilitator WTP, procurement mechanics, and verbatim retention quotes are still UNCOLLECTED — carry the §6 discovery questions into the next conversations.
- **Product note:** the shipped bundle is now v3.3.0 (adds `ai-journal import`); the 13.6 KB broken-ZIP issue (L2) was resolved 2026-07-19 — Gumroad and agenticppa.com both serve complete bundles.

**Prepared by:** offer-architect
**Status:** APPROVED at Checkpoint B (see above); Stage 3 (distribution-strategist + conversion-system-builder) is unlocked, gated on the L1 precondition
**Inputs:** `CLAUDE.md`, `growth/demand-brief.md` (approved Checkpoint A, 2026-07-05), `marketing/ghana-launch/*`, `docs/Paid_Product_Checklist.md`, `docs/Workshop_Facilitator_Guide.md`, `REFUND_POLICY.md`, `README.md` (license summary), and — **newly verified for rev. 2 by opening the shipped ZIPs and extracting the PDFs** — `dist/ghana-launch/AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip` (13.6 KB) and `dist/ghana-launch/AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip` (11.8 KB), including `facilitator-cohort-license-guide.pdf`. `growth/metrics.md` does not exist yet — there are zero live funnel numbers; every threshold below comes from `CLAUDE.md` targets, not observed rates.

**Checkpoint A decisions honored:** facilitator-first is the primary motion; student tier stays GHS 49 pending H1; scope is Ghana only; Nigeria/3MTT noted as next facilitator market but NOT spec'd. **All facilitator pricing in this document is PROVISIONAL** pending willingness-to-pay and procurement intel expected ~2026-07-10 from the KNUST professor and the mentee conversations (demand-brief header, Unknowns #1/#3/#4). Final pricing is Lawrence's decision at Checkpoint B.

**Product truth (v3.0.1 only):** offers below promise nothing beyond what ships — local-first Python CLI + web UI, Markdown journal, JSON-index search, optional BYO-API-key AI, offline Starter Guide, the launch PDFs actually inside the `dist/ghana-launch/` ZIPs (verified this revision), and the facilitator guide (`docs/Workshop_Facilitator_Guide.md`). No cloud sync, no mobile app, no spaced repetition, no analytics dashboard, no delivered training services. **Rev. 2 correction:** the shipped Student ZIP does NOT currently contain the v3.0.1 release bundle its own README promises — see Lawrence action item L2; no copy may claim the bundle until the ZIP is repackaged.

---

## 0. Lawrence action items surfaced by this revision (outside the spec itself)

- **L1 — Facilitator pricing reconciliation (blocks all H3 outreach and Experiment 2).** The shipped license-guide PDF already publishes cohort prices (GHS 300/750/1,500/3,000 — see §3) that contradict every provisional SKU below. Decide at Checkpoint B: supersede the shipped table (then regenerate/withdraw the PDF **before** any facilitator is contacted) or anchor new SKUs to it. §3 presents both paths with a recommendation.
- **L2 — Student ZIP packaging gap (blocks H1 traffic; live refund trigger).** The shipped `AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip` (13.6 KB, verified) contains three PDFs, three policy files, and a README — no v3.0.1 release bundle. Its own `README.txt` tells the buyer to "unpack the included v3.0.1 release bundle," and the Gumroad copy promises the same. Under `REFUND_POLICY.md`, "the release ZIP is corrupted or missing required files" and "the product page materially misrepresented the current feature set" are both refund-eligible. **Fix before any H1 traffic:** either repackage the ZIP to include the bundle, or change the README/Gumroad copy to match what ships. Recommendation: repackage — the CLI journal is the product's core.
- **L3 — PolyForm licensing boundary ruling (Checkpoint B).** Per `README.md`, the PolyForm Noncommercial 1.0.0 license grants free noncommercial use to "educational institutions, nonprofits, public research organizations, and government bodies." Lawrence to confirm whether OMCP centers (government program, free to learners) and partner universities need a paid license at all, or whether the Facilitator Pack sells to them purely on materials/support value (§1 Premium is now written on that assumption).
- **L4 — Two copy tasks routed to conversion-system-builder (Lawrence sign-off):** (a) replace the conflicting refund text in `gumroad-product-copy.md` with the `REFUND_POLICY.md` storefront text (§4); (b) add the facilitator→student reverse-upsell line, which does not exist today (§5).

Note: L1 and L2 can share one `dist/` rebuild pass — the Student ZIP must be regenerated regardless, so regenerating the license-guide PDF in the same pass costs little extra.

---

## 1. Positioning statements per tier

### Free — Ghana 7-Day AI Coding Journal
- **Who:** Ghanaian learners in coding/AI/data/cyber tracks — OMCP Phase-Two trainees first (12,623 completions by 30 May 2026; 400k 2026 target — demand-brief §1).
- **One problem:** you finish a week of training with nothing you can show or search — "a command or a syntax has just vanished from your head" (demand-brief §3.1).
- **Why it beats ChatGPT + a notebook:** it's a *structured* 7-day capture ritual (what you learned / built / prompted / what confused you / what proof to save) that works offline on paper or as a local app — no account, no data cost, and the record survives when a program's portal goes dark (demand-brief §3.3: OMCP portal offline by Nov 2025). A blank notebook gives you pages; this gives you the questions.

### Core — Student Portfolio Pack (sharpened to H2 framing)
- **New headline positioning:** **"The portfolio evidence OMCP's certificate doesn't give you."**
- **Who:** OMCP trainees and campus tech-club / self-taught learners (GDG, DevCongress) who will receive — or hope to receive — a certificate but have no documented proof of process (demand-brief §1: the gap is *evidence of learning*, not the credential; positioning complements, never attacks, the certificate).
- **One problem:** a certificate says you attended; it cannot show an employer what you understood, built, fixed, and can explain. (This is already the strongest line in `marketing/ghana-launch/email-whatsapp-sequence.md` Message 2 — H2 promotes it from email #2 to the tier's headline.)
- **Why it beats ChatGPT + a notebook:** the free default produces scattered chats and dead pages. The pack converts 12 weeks of learning into named artifacts — project case study, GitHub README, prompt log, internship/scholarship tracker (all verified inside the shipped `02-student-portfolio-pack.pdf`) — plus, **once L2 is fixed**, a local, searchable Markdown journal (JSON-index search) the learner owns forever, offline, with AI optional on their own free-tier key. Structure, searchability, portfolio output: exactly the three axes the demand brief says we must win on (§2 key takeaway). *Until L2 is fixed, copy may promise only the PDFs and policies that actually ship.*

### Premium — Facilitator Cohort Pack (primary motion this cycle)
- **Who:** the countable Ghana facilitator universe — ~130 OMCP centers across 16 regions, 4–12 partner universities (count unreconciled — demand-brief §1), private bootcamps (Codetrain, IIPGH), and workshop conveners of the UPH/TEA-LP type (demand-brief §1 Segment 3).
- **One problem:** trainers are expected to produce employable, portfolio-ready graduates but have no reflection/portfolio system — they'd have to build worksheets, rubrics, and templates from scratch (existing landing copy) while the program itself provides none (demand-brief §1: no press coverage describes any OMCP portfolio system).
- **Why it beats ChatGPT + a notebook (or DIY):** one license gives every learner in the cohort the same structured system on day one — printable PDFs for low-device settings (demand-brief §3.5: hardware is scarce/contested), a step-by-step facilitator runbook with a recommended agenda, sample exercise, troubleshooting script, and safety guidance (`docs/Workshop_Facilitator_Guide.md` — **no stated duration**; verified), and a **2-hour timed workshop flow** (0–120 min table in the shipped license-guide PDF; verified). And, **for commercial trainers only** (private bootcamps, paid instructors — the Codetrain/IIPGH-type paid classes), the commercial-use rights the PolyForm Noncommercial license otherwise withholds.
  **Licensing boundary (rev. 2 correction):** per `README.md`, educational institutions, nonprofits, public research organizations, and government bodies already qualify for **free noncommercial use** — so for OMCP centers and universities, the spec's primary targets, the pack sells on ready-made day-one cohort materials, printables, the workshop flow, and facilitator support — **not legal necessity**. Do not use "you need this license" framing with those buyers. (Checkpoint B item: Lawrence confirms where the boundary actually falls — see L3.)
- **What the license legally is:** a rights grant + the pack files. It does NOT include delivered training, customization, or support beyond `SUPPORT.md` — those remain "contact us" services.

---

## 2. Tier table with PPP price points

Anchor: USD/GHS ≈ 11.34 (demand-brief §2, 1 Jul 2026). Ghana daily minimum wage GHS 21.77.

| Tier | Contents (verified against shipped ZIPs, 2026-07-05) | Ghana (anchor) | USD | Nigeria (indicative — NOT spec'd this cycle) | Kenya (indicative — NOT spec'd this cycle) |
|---|---|---|---|---|---|
| Free 7-Day Journal | Fillable 7-day PDF + starter app (local CLI journal) + README | Free | Free | Free | Free |
| Student Portfolio Pack | 12-week tracker, prompt log, project case-study template, GitHub README starter, internship/scholarship tracker (all inside `02-student-portfolio-pack.pdf`), 7-day journal PDF, facilitator-notes preview PDF, policies, README. **v3.0.1 release bundle: promised by the ZIP's own README but NOT currently shipped — do not claim in copy until L2 is fixed** | **GHS 49** (unchanged, per Checkpoint A — H1 tests it) | USD 4.50 | USD 4.50; **no verified NGN conversion exists in the brief** (the NGN price-band claim was retracted, §6) — set NGN sticker only after a rate/rails check next cycle | ~KES 600 (derived from the brief's Moringa figures, KES 174,000 ≈ USD 1,300 → ~134 KES/USD, §5 — verify before use) |
| Facilitator Cohort Pack | License guide PDF (contains suggested pricing + 2-hour workshop flow — see §3), student pack PDF, 7-day journal PDF, workshop facilitator guide (untimed runbook: agenda steps, sample exercise, safety guidance, troubleshooting), README; commercial-use rights where the license requires them (see §1 licensing boundary) | **See §3 — PROVISIONAL options, reconciliation pending** | see §3 | Next facilitator market (3MTT: 300k fellows already incentivized to reflect weekly, §5) — do not spec until next cycle | not assessed |

Rationale for holding GHS 49: it is within ~10% of the only *verified* comparable (ALX All Access, USD 5/month, §2), ≈ 2.3 days of minimum wage — deliberate-purchase territory, not impulse — and H1 exists precisely to test it (falsified if <1% buy after 1,000 visits). Changing the price before the test destroys the test.

**One flag, not a change:** the GHANALEARNERS 20% launch code in `gumroad-product-copy.md` takes the effective price to ~GHS 39. If it runs during the H1 test, H1 measures GHS 39, not GHS 49. Recommendation: pick one — either test at list price with no code, or declare the test price GHS 39. (Experiment 1, §7.)

---

## 3. Facilitator tier — pricing reconciliation, then provisional SKUs

### 3.0 The shipped product already publishes prices (rev. 2 — verified)

`dist/ghana-launch/AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip` → `facilitator-cohort-license-guide.pdf` contains a **"Suggested cohort pricing"** table (text extracted and verified 2026-07-05):

| Shipped tier | Shipped price | Learner cap | Per learner |
|---|---|---|---|
| Starter cohort | **GHS 300** | up to 25 | GHS 12.00 |
| Growth cohort | **GHS 750** | up to 100 | GHS 7.50 |
| Institution cohort | **GHS 1,500** | up to 250 | GHS 6.00 |
| Large program | **GHS 3,000** | up to 750 | GHS 4.00 |

This contradicts two things: (a) `CLAUDE.md`'s "Contact / license" tier description, and (b) the demand brief's §2 line that "the Facilitator Pack has no published price" — the brief inherited that from `CLAUDE.md` without opening the ZIP; rev. 1 of this spec repeated the error. Consequence at the draft SKUs below: a 100-learner deal at A2 + overflow = GHS 950 + 70×20 = **GHS 2,350** vs. the shipped **GHS 750** — a buyer who opens the PDF they just bought sees they were quoted ~3× the printed price.

**Experiment 2 (§7) is INVALID until this is resolved:** any facilitator holding the pack can see GHS 300, so no quoted A2/A3 price yields a clean willingness-to-pay reading.

### 3.1 Two resolution paths for Checkpoint B (pricing is Lawrence's decision)

**Path (a) — Supersede the shipped table.** Adopt the SKU structure below (or Lawrence's own numbers); treat the PDF's table as an unreviewed artifact that predates this growth cycle.
- **Hard precondition:** regenerate the license-guide PDF (and rebuild the Facilitator ZIP) with the table removed or replaced **before any H3 outreach, Experiment 2 quoting, or new downloads**. Until then, every shipped copy is a standing counter-offer.
- For: the shipped numbers trace to no documented pricing logic and no demand-brief evidence; they collapse to GHS 4–7.50/learner at scale, which undercuts the entire facilitator-first arithmetic (13 centers × GHS 300 = GHS 3,900 ≈ USD 344 — versus the brief's USD ~100/cohort anchor logic); and there are zero live funnel numbers (`growth/metrics.md` doesn't exist), so essentially no copies are in buyers' hands yet — the cost of superseding is near zero today and grows with every download.
- Against: requires the dist rebuild before outreach (mitigated: L2 already forces a rebuild pass).

**Path (b) — Anchor to the shipped table.** Make GHS 300/750/1,500/3,000 the official list prices; drop SKUs A/B below; restate the license guide's caps as the SKU boundaries.
- For: zero repackaging risk; the table's steep volume discounts are friendly to the big-cohort OMCP centers; honors whatever thinking originally produced those numbers.
- Against: locks in prices that were never evidence-derived *either*, at levels the brief's own arithmetic says make the facilitator motion barely worth running; forfeits the July 10 WTP intel before it arrives.

**Recommendation: Path (a), decided at Checkpoint B after the ~July 10 conversations.** Reasoning: nothing has shipped to real buyers yet, the L2 packaging fix already forces a dist rebuild, and the July 10 intel is the first real evidence either way — if it says Ghana facilitator WTP really is GHS 300-territory, Lawrence simply picks numbers near the shipped table at Checkpoint B and Path (a) still holds (the point is that the *spec*, not a forgotten PDF, is the source of truth). Whichever path is chosen, the PDF and the spec must say the same thing before the first facilitator email goes out.

### 3.2 Provisional SKUs (valid only under Path (a); everything PROVISIONAL)

Evidence base is thin by the brief's own admission: no published Codetrain fees, IIPGH's GHS 200–300/learner is 2021-stale, center procurement authority is "pure assumption pending direct outreach" (§6), and the USD 100/cohort figure in §2 was arithmetic-only. The July 10 conversations (questions in §6 below) are the gate. Final numbers = Checkpoint B, after that intel.

#### Pricing logic (traceable)
1. **Retail-stack ceiling:** SKU A covers up to 30 learners; 30 × GHS 49 = **GHS 1,470**. A per-cohort license must land clearly below that to read as a deal. (Reference point at the shipped table's 25-learner cap: 25 × 49 = GHS 1,225.)
2. **Ghana paid-training floor:** learners individually paid IIPGH GHS 200–300 for instructor-led coding (stale but the only Ghana instructor-market datum, §2). A whole-cohort license priced near *one or two learners' worth* of that old fee is defensibly cheap for an institution.
3. **Brief's arithmetic anchor:** USD 100 ≈ GHS 1,134/cohort makes one license ≈ 23 student sales (§2) — the asymmetry that justified facilitator-first (H3).

#### SKU A — Per-Cohort License (one named cohort, up to 30 learners, one training run)

| Option | Price | ≈ USD | ≈ per learner (30) | Reasoning |
|---|---|---|---|---|
| A1 — Velocity floor | **GHS 450** | ~40 | GHS 15 | Low enough for an individual trainer to pay by MoMo out of pocket if centers have no budget authority (hedges Unknown #3). ~9× one student pack. Risk: anchors the product low — though still 1.5× the shipped Starter price. |
| A2 — Anchor (recommended opener) | **GHS 950** | ~84 | GHS 32 | Just under the brief's USD-100 arithmetic anchor; per-learner cost (GHS 31.70) lands near the one verified Selar price point (₵30, single example — §2); **~35% below the 30-learner retail stack of GHS 1,470**. Caution: the shipped license-guide PDF currently suggests GHS 300 for a 25-learner cohort — that conflict (§3.0/L1) must be resolved before this number is quoted to anyone. |
| A3 — Value ceiling | **GHS 1,500** | ~132 | GHS 50 | Tests whether "ready workshop + cohort materials (+ commercial rights where they apply)" carries premium over the retail stack logic. Use as the opener ONLY if July 10 intel says institutions, not individuals, pay. Equals the shipped Institution-tier (≤250 learners) price for a 30-learner cohort — untenable while the PDF circulates. |

Overflow: +GHS 20 per learner beyond 30 (keeps 100-learner center deals possible without a new SKU). Note: at 100 learners this totals GHS 2,350 vs. the shipped GHS 750 Growth tier — another reason §3.0 must be resolved first.

#### SKU B — Per-Institution Annual License (one center/campus, unlimited cohorts, 12 months)

| Option | Price | ≈ USD | Break-even vs. SKU A2 | Reasoning |
|---|---|---|---|---|
| B1 | **GHS 2,500** | ~220 | ~2.6 cohorts/yr | Easy yes for a center running 3+ cohorts; sized for OMCP centers if ministry/center money is tight. |
| B2 — Anchor | **GHS 4,500** | ~397 | ~4.7 cohorts/yr | For universities (4–12 OMCP partners) and multi-track centers; still < 4 learners' worth of a Moringa-class bootcamp month, and trivially small vs. institutional budgets implied by GHS 14,000/laptop procurement (§3.5). |
| B3 | **GHS 8,000** | ~705 | ~8.4 cohorts/yr | Only if July 10 intel reveals real procurement budgets at centers/universities. |

**Recommended negotiation posture for H3 outreach (20 facilitators, 60 days) — contingent on §3.0 resolution:** open per-cohort at A2 (GHS 950), hold a floor at A1 (GHS 450), and offer B2 (GHS 4,500) when a buyer mentions multiple cohorts. A pilot concession — e.g., 50% off the first cohort license — is preferable to lowering list price, and doubles as Experiment 2 (§7).

**Revenue check against the brief's own arithmetic:** 10% of the ~130 verified centers at A2 = 13 × GHS 950 = GHS 12,350 (~USD 1,090) — same order as the brief's Scenario B–C student revenue, from a 13-buyer motion instead of a 10,000-visit motion (§2). The same 13 buyers at the shipped GHS 300 Starter price = GHS 3,900 (~USD 344) — the gap between the two is the monetary size of the L1 decision.

**What I could NOT support from the brief:** any evidence that a specific cedi figure clears; whether the buyer is trainer, center owner, or ministry; whether invoicing/requisition is even possible at OMCP centers. Missing research = exactly Unknowns #1 and #3; do not treat A2/B2 as validated. And the shipped GHS 300–3,000 table is *also* unvalidated — neither table has evidence behind it yet; July 10 is the first real signal.

---

## 4. Guarantee and refund framing (consistent with REFUND_POLICY.md)

- **Storefront text (both paid tiers), verbatim from `REFUND_POLICY.md`:** "Refunds are available within 7 days if you cannot access the download, the release package is incomplete, or the documented installer fails on a supported platform and we cannot provide a workaround. Because this is a digital download, refunds are not offered for change-of-mind purchases or third-party AI API behavior."
- **Live exposure (rev. 2):** until L2 is fixed, the Student Pack is *itself* refund-eligible under this policy ("release package is incomplete" — the ZIP omits the bundle its README promises). This is why L2 blocks H1 traffic.
- **Positive framing (allowed, promises nothing new):** "Works offline. No subscription. Your journal is plain Markdown on your own machine — if you stop using the Kit, you keep every entry." This is a product-truth guarantee, stronger than a money-back gimmick for this audience (demand-brief §3.3/§3.5). *Applies to the CLI journal — gate this copy on L2 like everything else bundle-dependent.*
- **Facilitator tier:** same 7-day access/functionality window on the license files. Do NOT offer outcome guarantees ("your learners will retain more") — unverifiable and off-policy. Use the pilot discount (§3) as the risk-reducer instead of a broader guarantee.
- **Consistency fix needed (not edited here — outside my file scope):** `marketing/ghana-launch/gumroad-product-copy.md` currently states a *different* refund rule ("...purchased by mistake and has not been downloaded") that conflicts with `REFUND_POLICY.md`. Conversion-system-builder should replace it with the storefront text above; `docs/Paid_Product_Checklist.md` requires the refund policy be visible and accurate. (Routed as L4a.)

---

## 5. Upsell path

**Free → Student ("Day 7 trigger"):**
- Moment: completion of the 7-day journal — the learner has just produced 7 days of evidence and hits the wall of "now what?"
- Mechanism (all already in inventory): final page of the free PDF + `README-free.txt` "WANT THE FULL SYSTEM?" block + email/WhatsApp Message 2. Reframe all three to H2: "You now have 7 days of proof. Your certificate won't hold the next 12 weeks — the Portfolio Pack will."
- Secondary trigger from the brief: program stall (§3.3). "If classes pause, your journal doesn't." Use sparingly; supportive, never mocking OMCP.

**Student → Facilitator ("teaches-others trigger"):**
- Moment: any student-pack buyer who runs or helps run a club/cohort — the pack already seeds this with `03-facilitator-notes-preview.pdf` inside the Student ZIP (verified).
- Mechanism: one line in the student README + email Message 3: "Training others? A cohort license covers your whole class — from GHS [A-price, post-L1]." (Fixed price replaces "ask about a cohort license," cutting the contact-us friction the Checkpoint A decision targets. Mention commercial-use rights only to commercial-trainer audiences, per §1 licensing boundary.)
- **Facilitator → Student reverse upsell (rev. 2 correction):** this path exists in structure but not yet in copy. The shipped license-guide PDF's only CTA is "email info@agenticppa.com with your cohort size…" — it says nothing about learners buying personal packs. **Routed copy task (L4b, conversion-system-builder):** add one line to the license guide and the facilitator README — "your learners can buy personal Portfolio Packs after the cohort ends" — ideally in the same dist rebuild pass as L1/L2. One line of copy converts every licensed cohort into a student-tier audience.

---

## 6. Discovery questions for the July 10 conversations (max 6 — targets Unknowns #1, #3, #4)

Capture verbatim quotes — Unknown #4 explicitly needs 5–10 exact phrases before copy is written.

1. **(U4 — retention voice)** "When people you teach or mentor finish a coding or AI course, what do they say a month later about what they've kept — or lost? What exact words do they use?"
2. **(U1 — student WTP)** "If a trainee wanted a 12-week portfolio journal system like this near the end of their course — GHS 49, one-time — is that an easy yes, a stretch, or a no? What would they compare it against?"
3. **(U3 — facilitator WTP + budget owner)** "Suppose you ran a 25-person cohort with this pack. What would a fair one-time license price be — and who would actually pay it: you personally, the center, or the institution?" *(Do NOT show the license-guide PDF or name any price first — unprompted answers are the only clean WTP data we can still collect; see §3.0.)*
4. **(U3 — procurement mechanics)** "When a training center or department here buys supplementary materials, how does the money actually move — MoMo from the trainer, an invoice, a requisition? How long does it take?"
5. **(U3 — university list)** "Do you know which universities are actually in OMCP Phase Two — closer to four or twelve? Can you name any, or someone inside one?" *(KNUST professor is the prime source here.)*
6. **(U4/U1 — evidence gap)** "Have you seen any trainee keep a portfolio or learning journal on their own? What happened to their record when a program paused or a platform went down?"

---

## 7. Three pricing experiments (with success thresholds)

| # | Experiment | Design | Success threshold | Falsified / rework if |
|---|---|---|---|---|
| 1 | **H1 — GHS 49 live test (student)** | Run the Gumroad/landing funnel to 1,000 visits at ONE price (decide: list GHS 49 with no discount code, or declare GHS 39 the test price — do not mix). **Precondition: L2 packaging fix shipped.** | ≥2% visitor→buyer (CLAUDE.md target) | <1% after 1,000 visits → rework price/framing first, not channel (demand-brief H1) |
| 2 | **Facilitator two-point WTP test — INVALID until L1 is resolved** (any respondent holding the pack can see the shipped GHS 300 price; under Path (a) the PDF must be regenerated first, under Path (b) the quoted prices must BE the shipped table). Design, once valid: within H3's 20-facilitator outreach, quote A2 (GHS 950/cohort) to half and A3 (GHS 1,500 with pilot-50%-off = GHS 750 first cohort) to half; log every objection verbatim. | (as designed) | ≥3 discovery calls and ≥1 paid license at ≥GHS 450 within 60 days (H3 thresholds + A1 floor) | <2 replies total → deprioritize Facilitator Pack this cycle (H3 falsification); all acceptances only below GHS 450 → SKU A repriced at Checkpoint B rerun |
| 3 | **H2 — portfolio-gap framing A/B** | Two lead-magnet landing variants: "portfolio evidence the certificate doesn't give you" vs. current generic "journal your AI learning"; 500 visits each. Framing drives price tolerance, so it gates Experiment 1's copy. | Portfolio-gap variant ≥25% opt-in AND beats generic (CLAUDE.md / demand-brief H2) | Parity or worse → H2 falsified; revert headline positioning in §1 to generic and rerun Offer stage |

Sequencing: Experiment 3 before or alongside 1 (framing gates the buy page); Experiment 2 runs on the facilitator track and is the cycle's primary motion — but it cannot start until the L1 reconciliation decision lands and (under Path (a)) the PDF is regenerated.

---

## 8. What the demand brief could not support (carried forward honestly)

- Any validated Ghana facilitator price point — all §3 numbers (both the provisional SKUs *and* the shipped GHS 300–3,000 table) are constructed, not evidenced; the SKUs trace to the retail stack, one stale IIPGH datum, and the brief's arithmetic placeholder.
- Nigeria pricing in NGN (rev-1 band retracted; no verified rate in evidence) and any Kenya demand signal beyond ecosystem scale.
- Whether OMCP learners can even be reached at funnel scale (Unknown #2 — untouched by this spec, belongs to distribution-strategist).
- Ghana-local retention quotes for copy (Unknown #4 — §6 questions exist to fix this).
- One correction the spec owed the brief: the brief's §2 statement that the Facilitator Pack "has no published price" is contradicted by the shipped license-guide PDF (§3.0). Market-signal-researcher should note this for the brief's next revision; the error originated in `CLAUDE.md`'s "Contact / license" line.

---

## Checkpoint B request

Lawrence — pricing is your decision; nothing above is final. Requested at Checkpoint B (after the ~July 10 conversations):

1. **Rule on the pricing reconciliation (L1):** Path (a) supersede the shipped GHS 300/750/1,500/3,000 table (then the license-guide PDF is regenerated before any outreach) or Path (b) adopt the shipped table as list price. Recommendation: Path (a) — see §3.1. Experiment 2 stays frozen until you rule.
2. **Pick facilitator numbers** (if Path (a)): per-cohort opener (A1/A2/A3 or your own) and per-institution anchor (B1/B2/B3), or send offer-architect back with the new intel.
3. **Rule on the PolyForm licensing boundary (L3):** confirm that OMCP centers/universities are treated as free-noncommercial-eligible (pack sells on materials value) and that commercial-license framing is reserved for private bootcamps/paid trainers — or correct that boundary.
4. **Confirm the L2 packaging fix** (Student ZIP rebuilt with the v3.0.1 bundle, or copy corrected to match the ZIP) before any H1 traffic.
5. **Confirm** Student Pack stays GHS 49 for H1, and rule on the GHANALEARNERS-code conflict (test at 49 or at 39 — one or the other).
6. **Approve** the H2 headline ("the portfolio evidence OMCP's certificate doesn't give you") as the student tier's lead positioning.
7. **Approve** the two copy tasks routed to conversion-system-builder (L4): refund-text fix + facilitator→student reverse-upsell line.
8. **Confirm** the §6 discovery questions before the July 10 calls.
