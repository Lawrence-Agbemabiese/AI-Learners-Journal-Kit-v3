# Channel Plan — 2026-07-19 (Cycle 1) — rev. 2, 2026-07-19 (post-evaluator)

**Prepared by:** distribution-strategist
**Status:** DRAFT rev. 2 — all five revision requirements in `growth/reviews/review-channel-plan-2026-07-19.md` (verdict REVISE, Economics 3) addressed; ready for evaluator re-review (see end of file)
**Scope ruling honored:** Ghana ONLY. Nigeria/3MTT is the noted next facilitator market and is deliberately NOT spec'd or scheduled anywhere in this plan.
**Inputs:** `growth/offer-spec.md` (APPROVED 2026-07-19, Checkpoint B — rulings honored throughout), `growth/demand-brief.md` (approved Checkpoint A), `growth/pending-corrections.md`, `marketing/ghana-launch/social-content-scripts.md`, `marketing/ghana-launch/email-whatsapp-sequence.md` (existence noted as an inventory asset), live web research 2026-07-19, and direct verification of the shipped artifacts in `dist/` (see §0). **Note:** `CLAUDE.md` is cited as an input by upstream documents but does not exist in the repo at write time — all CLAUDE.md-derived targets (2% visitor→buyer, ≥25% opt-in, 1,000-visit test volume) are taken as quoted in the approved demand brief and offer spec. Flagged for Lawrence.

**Product-truth boundary for every hook and calendar item below (verified 2026-07-19 by opening the shipped files):**
- The shipped bundle is **v3.3.0** (built 2026-07-19, `dist/release-manifest.json`, 77 files). The Student Portfolio Pack ZIP (`dist/ghana-launch/`, 1.16 MB) now contains the full v3.3.0 bundle — L2 is closed.
- **`ai-journal import` IS shipped**: `scripts/session_import.py` is in the v3.3.0 ZIP and `scripts/journal_cli.py` wires the `import` subcommand ("Import a Claude Code session as a draft entry"); `docs/Release_Notes_v3.3.0.md` documents it. Pending-corrections §4 ("not in any shipped bundle") is now stale. Hooks may therefore reference it — but only for developer/power-user audiences, Claude Code history only, offline, no API key. It is NOT a hook for the OMCP-learner mass audience.
- Everything else promised = v3.0.1 core (local CLI + web UI, Markdown journal, JSON-index search, optional BYO-key AI, offline) plus the launch PDFs. No cloud sync, no mobile app, no spaced repetition, no MoMo checkout claim (Gumroad is card/USD — see §7 handoff flag).

---

## 0. Gate status — verified today, and it governs the whole sequence

**The L1 precondition is NOT yet met (checked 2026-07-19):**
- `dist/ghana-launch/AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip` was rebuilt today (07:29) but its `facilitator-cohort-license-guide.pdf` **still prints the superseded GHS 300 / 750 / 1,500 / 3,000 table** (text extracted and read this morning).
- The live landing page (agenticppa.com/ghana-ai-coding-journal, fetched 2026-07-19) **still displays the same superseded table** in its facilitator section, and its Student Pack bullet still says "v3.0.1 release bundle" (the bundle is now v3.3.0).

Per the Checkpoint B ruling, **no facilitator outreach (H3) and no Experiment 2 quoting may launch until both surfaces show the approved pricing** (per-cohort opener GHS 950, floor GHS 450, ceiling GHS 1,500; institution annual anchor GHS 4,500). This plan therefore runs on a relative clock: **Day 0 = the day the regenerated license-guide PDF + updated landing page ship.** Student-side channel work (P2, TikTok) does NOT touch facilitator pricing and may start immediately — the student funnel's own gate (L2) is already closed.

---

## 1. Assigned research: Unknown #2 — can OMCP learners be reached at funnel scale?

**Question (demand brief, Top Unknown #2; offer-spec §8 routed it here):** where do OMCP Phase-Two learners congregate online, and can the lead magnet reach them at the 10k–20k-visit scale assumed in demand-brief Scenarios B/C?

**Finding: NO open, direct channel to OMCP learners at funnel scale exists today. Reach is mediated — by episodic registration announcements, university allocations, and centers/facilitators.** Evidence, gathered 2026-07-19:

1. **No public learner groups found.** Searches for OMCP WhatsApp/Telegram learner groups surface only official portals and press ([onemillioncoders.gov.gh](https://onemillioncoders.gov.gh/), [moc.gov.gh/one-million-coders](https://moc.gov.gh/one-million-coders/)). The portal remains JS-rendered with no public community links. Cohort/center WhatsApp groups almost certainly exist (see #4) but are private — you enter them through a facilitator, not a link. (Absence of evidence after directed search; consistent with the demand brief's own failed attempt, §6.)
2. **Reach moment #1 — registration pushes and institution-level windows (re-sourced, rev. 2).** General Phase 2 registration opened in **late April 2026**, and the cited coverage describes it as **ongoing with no published close date** ([GhCampus, 26 Apr 2026](https://ghcampus.com/tech-news/registration-opens-for-phase-2-of-one-million-coders-programme/) — "registration is now open," prior applicants told not to reapply; [TechFocus24, 1 May 2026](https://techfocus24.com/ministry-of-communications-opens-online-registration-for-one-million-coders-programme/) — "currently ongoing," no dates) — treat it as an open-ended intake punctuated by announcement spikes, not a scheduled calendar of windows. What IS dated and time-boxed happens at the **institution level**: GCTU's 2,000-slot allocation **runs 15–20 July 2026, first-come, first-served** ([GCTU announcement](https://site.gctu.edu.gh/announcements/one-million-coders-programme-registration-now-open.aspx) — the page is JS-rendered and would not render on direct fetch; wording verified 2026-07-19 via its search-indexed text: "Registration runs from 15 July to 20 July 2026… first-come, first-served basis") — i.e., one institution-level intake is live this very week. Each such moment — a Ministry push or a campus allocation announcement — is when applicants actively search "how to register," share portal links in WhatsApp, and follow campus announcements. This remains the only moment OMCP learners are publicly visible and searchable at scale, but it arrives as **episodic announcements to react to, not windows to plan around**.
3. **Reach moment #2 — institutional allocation.** Slots are allocated through institutions — e.g., **GCTU received 2,000 slots for this cohort** and announced it on its own site ([GCTU announcement](https://site.gctu.edu.gh/announcements/one-million-coders-programme-registration-now-open.aspx)); phase one runs through **~130 centers (50 laptops each) in all 16 regions and 12 universities including KNUST, University of Ghana, and University of Cape Coast** ([Ecofin](https://www.ecofinagency.com/news-digital/1304-54603-ghana-scales-up-one-million-coders-program-nationwide); [TechAfrica News](https://techafricanews.com/2026/04/13/ghana-launches-nationwide-one-million-coders-programme-with-laptop-distribution/)). The learner lists live inside institutions — exactly where Prof. B. Amenu (KNUST) sits.
4. **The ambient channels are known and huge, but generic (citations repaired, rev. 2).** WhatsApp is Ghana's most-used platform: **93% of internet users** used it as of Q3 2024, with **TikTok second at 81% of internet users, having overtaken Facebook** ([Statista, "Social media platforms as a share of internet users in Ghana as of 3rd quarter 2024"](https://www.statista.com/statistics/1171534/leading-social-media-platforms-ghana/) — We Are Social / DataReportal / Meltwater survey data, published 3 Mar 2025; **both figures visible in the page's own text**, verified 2026-07-19). Caveats stated plainly: these are Q3 2024 platform-use shares of internet users, not 2026 figures and not monthly-active counts; and the [DataReportal Digital 2026: Ghana](https://datareportal.com/reports/digital-2026-ghana) article carries **no WhatsApp or TikTok sections at all** (confirmed against the 2025 edition too) — from DataReportal we cite only what its article text verifiably states: **26.3M internet users, 74.6% penetration**. Independent of any usage rate, the Ministry itself courted a **TikTok STEM-feed partnership specifically to publicize OMCP** (June 2025 meeting, Minister Sam George × TikTok West Africa — [Ecofin](https://www.ecofinagency.com/news/2706-47462-ghana-eyes-tiktok-partnership-to-train-one-million-coders); [Pulse Ghana](https://www.pulse.com.gh/articles/news/sam-george-meets-tiktok-team-demands-fair-pay-for-ghanaian-creators-2025062812381795838) — cited for the courtship only, which is all it contains). So the *platforms* reach OMCP learners; what's missing is any *OMCP-specific aggregation point* on them that we can post into.
5. **Delivery happens inside closed platforms.** The 12,623 completions were recorded "across its learning platforms" ([Ghana Business News](https://www.ghanabusinessnews.com/2026/05/30/more-than-12000-learners-complete-courses-under-one-million-coders-programme/)) — learner attention during training is inside partner LMSes, not open communities.

**Verdict and consequences for this plan:**
- **Scenario B/C reach assumptions (10k–20k visits) remain unvalidated and should be treated as NOT currently achievable organically.** Budget the 90 days for **~1,000–2,500 engineered visits** — shown as an assumption chain, not an assertion (rev. 2; every number below is a labeled assumption, logged for the retro, replaced by observed UTM data at Day 45):
  - **P2 WhatsApp:** seeded surfaces = Kwaku S.'s cohort group (assume 50–100 members — centers run 50 laptops each, so 50–100 is the plausible group size; existence unverified, §7.3), the KNUST pilot cohort once live (~30–60), 2–4 club/community shares (GDG chapters; DevCongress's 1,000+ members, of whom assume 200–400 see any single announcement), plus status posts to the existing tester/free-pack contact list (~100–200 viewers). Unique reach per push ≈ **400–1,200**. Assume **5–10% link-click** on a forwarded card/status (no Ghana WhatsApp CTR benchmark found — pure assumption) × **8–12 non-overlapping pushes** over 12 weeks (each group tolerates roughly one ask per fortnight) ⇒ **~300–1,400 visits**.
  - **E1 TikTok:** 24 clips (2/wk × 12 wks) × **300–1,000 median views/clip** for a new account (assumption) = 7k–24k views × **0.5–1.5% bio-link tap-through** (assumption) ⇒ **~50–350 visits** — which is exactly why E1's Day-45 threshold (§6) is stated in views/link-taps, not conversions.
  - **Registration-moment package + evergreen post + direct shares:** ~100–500 episodic visits (spiky, announcement-driven — §1.2).
  - **Sum: ~450–2,250.** With midpoint assumptions holding, **~1,000–2,500 is the plausible ceiling; the low case is ~500** — enough for Experiment 3 (2×500 visits) in all cases, enough for Experiment 1's 1,000 visits only in the mid/high case, and nowhere near the ceiling scenarios. The P2 shortfall fallback is stated in §6.
- **This finding independently confirms the facilitator-first ruling.** The facilitator is not just the better buyer (H3 arithmetic) — the facilitator is the *only reliable distribution channel to OMCP learners*. One licensed cohort = a private WhatsApp group we could never reach from outside.
- **The registration moment is the one open-funnel moment — and it is episodic, not scheduled (rev. 2).** The plan keeps a small, always-ready "registration moment" content package (§4) to fire whenever the Ministry announces a push or an institution announces a dated allocation window (like GCTU's 15–20 July FCFS window, §1.2), instead of a continuous OMCP-targeting content grind that has nowhere to land.

---

## 2. Channel ranking (ruthless: 2 primary + 1 experimental; everything else parked)

| Rank | Channel | Audience presence (evidence) | Cost | Effort | Fit with the offer | Verdict |
|---|---|---|---|---|---|---|
| **P1** | **Direct facilitator outreach** (email + LinkedIn touches + warm intros) | The buyer universe is *countable*: ~130 OMCP centers, 12 partner universities, named bootcamps (Codetrain Accra/Kumasi, IIPGH), club networks ([Ecofin](https://www.ecofinagency.com/news-digital/1304-54603-ghana-scales-up-one-million-coders-program-nationwide)); two warm doors already open (Prof. B. Amenu/KNUST confirmed pilot access; Kwaku S., enrolled OMCP learner + AMBASSADOR-FREE ambassador); §1 shows facilitators gatekeep learner reach | ~0 cash | High per contact, but only 20 contacts (H3) | GHS 950-opener / GHS 4,500-institution deals justify manual, named outreach in a way GHS 49 never can; also the §1 verdict makes this the learner channel too | **Primary — the H3 motion. Gated on L1 (Day 0).** |
| **P2** | **WhatsApp** (shareable free-pack card + status posts + the existing `email-whatsapp-sequence.md` asset + group seeding via ambassadors/pilot cohorts) | Most-used platform in Ghana — **93% of internet users, Q3 2024** ([Statista / We Are Social / DataReportal / Meltwater](https://www.statista.com/statistics/1171534/leading-social-media-platforms-ghana/), figure visible in page text); market scale from [DataReportal](https://datareportal.com/reports/digital-2026-ghana): 26.3M internet users, 74.6% penetration; the free 7-day ZIP is natively forwardable | ~0 cash | Low–medium | Perfect for a GHS 49/free-lead product: zero ad cost, offline-friendly audience, and the private cohort groups (§1) are WhatsApp groups | **Primary — the student motion feeding Experiments 3 then 1. No gate; starts Week 1.** |
| **E1** | **TikTok short-form** (the 10 scripts in `social-content-scripts.md`, 2 clips/week) | **81% of internet users, #2 platform ahead of Facebook — Q3 2024 survey** ([Statista](https://www.statista.com/statistics/1171534/leading-social-media-platforms-ghana/), figure visible in page text; no current-year Ghana usage figure could be verified, so E1 is sized as an experiment, not a reach assumption); Ministry actively courting TikTok's STEM feed to publicize OMCP ([Ecofin](https://www.ecofinagency.com/news/2706-47462-ghana-eyes-tiktok-partnership-to-train-one-million-coders); [Pulse Ghana](https://www.pulse.com.gh/articles/news/sam-george-meets-tiktok-team-demands-fair-pay-for-ghanaian-creators-2025062812381795838)) — OMCP content is institutionally pushed onto the platform | ~0 cash | Medium (filming) | Unproven for converting a deliberate GHS 49 purchase (2.3 days of minimum wage — not impulse); treat strictly as top-of-funnel supply for the H2/H1 landing tests | **Experimental — kill/scale decision Day 45.** |

**Parked, with reasons (do not spread thin):** X/Twitter (no Ghana-scale audience evidence vs. WhatsApp/TikTok); LinkedIn *as a content channel* (used only as an outreach surface inside P1); YouTube long-form (high effort, no distribution advantage yet); SEO/blog (slow; exception: one evergreen "OMCP registration + first-week checklist" post kept ready for registration moments, §4); paid ads (USD 4.50 price × 2% target conversion cannot clear ad CPCs; facilitator deals don't need ads).

---

## 3. P1 — Facilitator outreach plan (H3: 20 named targets, 60 days, gated on L1)

**Posture (per approved rulings):** open per-cohort at **GHS 950**; hold floor **GHS 450**; ceiling **GHS 1,500** (a negotiation bound only — never an opening quote); offer institution annual **GHS 4,500** when a buyer mentions multiple cohorts. KNUST pilot: **50% off first cohort = GHS 475**. Carry the offer-spec §6 discovery questions into every call (Unknowns #1/#3/#4 are still uncollected) — question 3's *unprompted* fair-price ask, posed before any number is named, is now the primary clean absolute-WTP instrument. **L3 boundary applies to every noncommercial target: lead with materials/workshop value; never "you need this license."**

**Experiment 2 — redesigned (rev. 2) to remove the self-contradiction the evaluator caught (review requirement 4).** The spec's §7 two-arm design (GHS 950 to half the list, GHS 1,500-with-pilot-50% to the other half) predates the Day-0 requirement that **GHS 950 be publicly printed** in the regenerated license-guide PDF and on the landing page. Once 950 is public, any GHS 1,500 quote is contaminated the moment the prospect opens the site or the one-pager — the same standing-counter-offer failure the L1 ruling exists to kill. **Fix (recommended default = review option (a)): both arms quote the published list price, GHS 950; the experimental variable becomes the concession, not the list price.** Arm A (half the 17 non-warm targets): straight GHS 950, no concession. Arm B (the other half): GHS 950 list with a 50%-off-first-cohort pilot concession (= GHS 475), KNUST-style. This reads whether the pilot concession moves reply→call→close rates, keeps every quote consistent with the public price, and still logs every objection verbatim. The GHS 1,500 ceiling survives only as the upper negotiation bound if a buyer bids upward (e.g., a commercial bootcamp bundling multiple runs). **Because this amends the approved spec's §7 experiment design (without touching any approved price), it is flagged for Lawrence's confirmation at the Day-0 check-in.** Alternatives considered and rejected: quoting 1,500 only to prospects reached before they see the site (review option (b) — fragile; one shared link breaks the arm) and knowingly accepting a contaminated 1,500 reading (option (c) — produces worthless data). What is lost: no cross-arm read on absolute price level — that intel now comes from §6 question 3's unprompted answers and from logged negotiation movement, verbatim.

### Wave sequence (Day 0 = L1 ships)

- **Day 0–7 — Gate week.** Lawrence ships regenerated license-guide PDF + landing-page pricing update (+ facilitator ZIP rebuild). Meanwhile (allowed — no outreach yet): build the named 20-target list, prep the two concession variants (Arm A / Arm B per the redesigned Experiment 2 above), prep the one-page facilitator PDF/link kit (which must show only the public GHS 950 / GHS 4,500 list prices).
- **Wave 1, Days 7–14 (warm, 3 targets).** (1) **KNUST pilot via Prof. B. Amenu** — the anchor deal: 50%-off first cohort at GHS 475; agree pilot success criteria (cohort size, journal completion count) so it produces the cycle's first real paid data point AND a private student-cohort WhatsApp group for P2. (2) **Kwaku S.** — activate as ambassador (AMBASSADOR-FREE): ask for one intro to his OMCP center's coordinator and one share of the free pack into his cohort group (this is also the §1 reach test). (3) One GDG/DevCongress organizer intro from existing network.
- **Wave 2, Days 14–42 (12 targets).** Cold-but-named outreach across the five org types below; email first, LinkedIn touch second, one follow-up each; book discovery calls.
- **Wave 3, Days 42–60 (5 targets + follow-ups).** Fill remaining slots using whatever §6 intel arrived; escalate any multi-cohort conversation to the GHS 4,500 institution anchor.

### Five org types for the Facilitator Pack, with outreach angle

| # | Org type (named examples) | Outreach angle (all honest, L3-compliant) |
|---|---|---|
| 1 | **OMCP training centers** (~130 across 16 regions; start with centers in Accra/Kumasi + Kwaku S.'s center) | "Your learners finish with a certificate; this gives them the portfolio evidence beside it — printable day-one materials, a 2-hour workshop flow, and a rubric, ready before your next cohort starts." Free-noncommercial eligibility stated plainly; the pack sells on ready materials + support, never license necessity. |
| 2 | **OMCP partner universities / CS & IT departments** (12 incl. KNUST — pilot venue, University of Ghana, UCC; GCTU holds 2,000 Phase-2 slots) | "KNUST-style pilot: one cohort, half-price first license (GHS 475-equivalent), success criteria agreed up front — you get a portfolio clinic your students keep offline after the semester." (Use the KNUST name in other-university outreach **only after** the pilot has actually started.) |
| 3 | **Private bootcamps & paid trainers** (Codetrain Africa — Accra & Kumasi; IIPGH coding programs) | The ONLY segment where commercial-use rights are part of the pitch: "One license covers your whole paying cohort — materials, workshop flow, and the commercial-use rights the noncommercial license withholds." Opener GHS 950. |
| 4 | **Campus developer clubs** (GDG on Campus chapters — e.g., Accra Institute of Technology, Takoradi Technical University; DevCongress community, 1,000+ members; GDG Kumasi/DevFest organizers as the route into Kumasi campuses — no KNUST-specific GDG chapter could be verified) | "Run a portfolio clinic for your members" — free 7-day pack for the club, ambassador codes for leads; clubs are noncommercial, so this is a seeding/reach channel first and a licensing channel only if a club runs paid training. This is also the dev audience where the shipped `ai-journal import` (Claude Code sessions → draft entries) is an honest, differentiated talking point. |
| 5 | **NGO / nonprofit training orgs & workshop conveners** (Ghana Code Club — 22 centers, 7,000 teachers; GirlCode Ghana; TEA-LP/UPH-model conveners) | "A facilitator runbook + assessment rubric your volunteer teachers can run tomorrow" — free-noncommercial eligibility up front; paid pack positioned as convenience, printables, and support (per `SUPPORT.md`), not rights. |

**P1 success metric (H3 thresholds):** ≥3 discovery calls AND ≥1 paid license at ≥GHS 450 within 60 days of Day 0. **Falsified if** <2 replies from 20 contacts → deprioritize the Facilitator Pack this cycle. **Review dates:** Day 30 checkpoint; Day 60 verdict (if Day 0 = 2026-07-26, reviews ≈ 2026-08-25 and 2026-09-24 — restate when L1 actually ships).

---

## 4. 90-day content calendar (weekly cadence per channel)

Calendar clock: **student channels start Week 1 = week of 2026-07-20** (no gate). **Facilitator track starts at Day 0 = L1 ship** (target inside Week 1–2; the calendar assumes Day 0 lands by 2026-07-26 and must slip with it).

| Weeks | P1 Facilitator outreach (cadence: 4–6 touches/wk once gated open) | P2 WhatsApp (cadence: 2 posts/wk + sequence sends) | E1 TikTok (cadence: 2 clips/wk) | Experiment tie-in |
|---|---|---|---|---|
| 1–2 | Gate week → Wave 1 (KNUST via Prof. Amenu; Kwaku S. ambassador activation; 1 network intro) | Launch shareable free-pack card; status posts from scripts #1 (course vs portfolio) and #4 (weekly proof); ask testers/ambassador to forward into cohort groups | Film + post scripts #1, #3, #6; all CTAs → lead-magnet landing (H2 variants) | **Experiment 3 (H2 A/B) opens Week 1**: two landing variants, 500 visits each, traffic from P2 + E1 |
| 3–4 | Wave 2 begins: 6 cold-named contacts (org types 1–3); discovery calls with §6 questions; Experiment 2 concession split (Arm A/B, §3) starts | Scripts #5 (interview prep), #10 (scholarship); first sequence sends to new free-pack emails/numbers | Scripts #2, #5; 1 "day in the journal" screen-capture clip (real product only) | H2 read at ~500+500 visits → winning frame becomes the buy-page headline |
| 5–8 | Wave 2 completes (12 total); follow-ups; escalate multi-cohort talks to GHS 4,500 anchor; Day-30 review | **Experiment 1 window:** all CTAs point to the ONE clean GHS 49 page (no GHANALEARNERS code — retired per ruling); scripts #6, #7, #8 rotation; Day-7 upsell messages fire on free-pack completers | Scripts #7 (Ghana learner), #10; retire weakest 2 clips, double down on best performer | **Experiment 1 (H1)**: accumulate toward 1,000 visits at GHS 49 clean; conversion logged excluding TESTER/AMBASSADOR-FREE redemptions |
| 9–12 | Wave 3 (5 targets) + follow-ups; Day-60 H3 verdict; KNUST pilot mid-cohort check-in (collect verbatim retention quotes — Unknown #4) | Pilot-cohort story content (only with consent, only true numbers); continue 2/wk; final push toward 1,000-visit H1 line | Day-45 kill/scale decision executed at Week 9 boundary; if scaled: 3/wk repurposing WhatsApp-proven hooks | H1 read at 1,000 visits; Experiment 2 objection log closed at Day 60 |
| Standing | — | **Registration-moment package (fire on trigger, any week):** the moment the Ministry announces a registration push OR an institution announces a dated allocation window (like GCTU's 15–20 July 2026 FCFS window, §1.2), post the prepared "Registering for One Million Coders? Start your evidence file before class 1" card + the one evergreen blog/SEO post (independent-resource disclaimer mandatory) | Same trigger: 1 prepared registration-moment clip | Registration announcements are the only open OMCP funnel moment (§1) — episodic and unscheduled, so the package stays ready year-round |

---

## 5. Hooks — 10 per primary channel, each mapped to a demand-brief pain point

Honesty rules applied: nothing beyond the shipped v3.3.0 bundle; no income promises; certificate framing complements, never attacks, OMCP; "independent resource, not an official government product" disclaimer on anything OMCP-adjacent; `ai-journal import` appears only in dev-audience hooks (verified shipped, §0).

### P1 — Facilitator outreach (email subject lines / call openers)

| # | Titled hook | Mapped demand-brief pain point |
|---|---|---|
| 1 | **"Your learners get a certificate. Do they leave with proof?"** | §1: "the gap is the *evidence of learning* — process documentation and portfolio — not the credential" |
| 2 | **"The cohort materials you'd otherwise build from scratch"** | §1 Segment 3: trainers "have no reflection/portfolio system — they'd have to build worksheets, rubrics, and templates from scratch" |
| 3 | **"When the portal went dark, learners with journals kept their record"** | §3.3: "We were told we'd start classes soon after the launch… Then—nothing." (portal offline by Nov 2025) |
| 4 | **"Printable journals for rooms where laptops are shared"** | §3.5: hardware scarce/contested (GHS 14,000/laptop controversy; 20,000 laptops for 130 centers) |
| 5 | **"A 2-hour workshop flow, timed to the minute, ready for your next intake"** | §1 Segment 3 (no provided system) — references the verified 0–120-min flow actually in the shipped pack |
| 6 | **"'A command or a syntax has just vanished from your head' — your trainees, one month out"** | §3.1: Mangabo Kolawole quote on skill evaporation |
| 7 | **"Forgetting isn't a discipline problem. Give the cohort a system."** | §3.2: re-forgetting needs an external system, not more studying |
| 8 | **"Free for noncommercial use — here's what the paid pack adds"** | §3.5 cost constraints + L3 honesty: leads with the PolyForm noncommercial grant, sells materials/support value only |
| 9 | **"Your paying students expect portfolio-ready graduates"** (commercial bootcamps ONLY) | §1 Segment 3: bootcamps charge real money (Codetrain; IIPGH GHS 200–300, dated) — the segment where commercial-use rights framing is permitted |
| 10 | **"Your dev learners' AI sessions vanish. The new import turns them into journal entries."** (dev bootcamps/GDG audiences ONLY) | §3.1 evaporation + pending-corrections §2 (session-history tools trend); honest: Claude Code history only, offline, shipped in v3.3.0 |

### P2 — WhatsApp (status/broadcast card titles)

| # | Titled hook | Mapped demand-brief pain point |
|---|---|---|
| 1 | **"Finished the week. Kept nothing?"** | §3.1: "a command or a syntax has just vanished from your head… You lose it" |
| 2 | **"A certificate says you attended. Your journal shows what you built."** | §1 / H2: evidence-of-learning gap (complements the certificate) |
| 3 | **"If classes pause, your journal doesn't."** | §3.3: program stop-start ("Then—nothing.") — supportive tone, never mocking OMCP |
| 4 | **"7 days. One page a day. Proof you can show."** | §3.1 capture-system prescription ("Have a learning journal…") — free lead magnet CTA |
| 5 | **"Works offline. No subscription. Yours forever."** | §3.5: device/data constraints — verified product truth (offline, local Markdown) |
| 6 | **"Stop losing the prompt that finally worked."** | §3.1 + prompt-log mechanism (judgment, not copying) |
| 7 | **"Registering for One Million Coders? Start your evidence file before class 1."** | §3.3 hedge + §1 fit; fires only when a registration push or dated institutional window is live (§1.2); carries the independent-resource disclaimer |
| 8 | **"Interviewers ask what you built, not what you watched."** | §3.1/§1: evidence gap at hiring time (mirrors script #5) |
| 9 | **"Scholarship forms love evidence: projects, screenshots, reflections."** | §1 fit (internship/scholarship tracker is verified pack content; mirrors script #10) |
| 10 | **"GHS 49. Once. About the price of a month of ALX — but you keep it offline forever."** | §2: verified ALX USD 5/month anchor; deliberate-purchase honesty (no impulse/get-rich framing) |

---

## 6. Per-channel success metrics and review dates

| Channel | Metric | Threshold | Review date(s) |
|---|---|---|---|
| P1 Facilitator | Replies / discovery calls / paid licenses from 20 named contacts | ≥3 calls AND ≥1 license ≥GHS 450 by Day 60; falsified <2 replies | Day 30 + Day 60 from L1 ship (≈2026-08-25 / ≈2026-09-24 if Day 0 = 07-26); restate on actual Day 0 |
| P2 WhatsApp | UTM'd landing visits from wa links; lead-magnet opt-in; H1 conversion | Opt-in ≥25% on winning H2 variant; contribute ≥60% of Experiment 1's 1,000 visits (= 600 — inside the §1 chain's 300–1,400 WhatsApp range if its assumptions hold); ≥2% visitor→buyer at GHS 49 (falsified <1%) | H2 read ≈2026-08-10; mid ≈2026-08-18; H1 read at 1,000 visits; if not reached by 2026-10-17, apply the shortfall fallback below — do NOT read H1 early on a small sample |
| E1 TikTok | Views, profile→link taps, cost of production time | ≥20,000 cumulative views OR ≥300 link taps by Day 45, else kill; if passed, scale to 3/wk | Kill/scale decision 2026-09-02; final 2026-10-17 |
| Plan-level | All numbers logged to `growth/metrics.md` (file does not exist yet — recommend Lawrence or conversion-system-builder create it; not this agent's file) | — | Cycle retro 2026-10-17 |

**Excluded from all conversion metrics:** TESTER and AMBASSADOR-FREE redemptions (per Checkpoint B ruling and pending-corrections §6).

**P2 shortfall fallback (rev. 2, per review requirement 5):** the §1 chain's low case (~500 total visits) would leave H1 short of its 1,000-visit line by 2026-10-17. If the Day-45 re-forecast (observed UTM click-throughs replacing the §1 assumptions) projects a shortfall: (a) extend the H1 window into the next cycle at the same clean GHS 49 price rather than reading early — a small-sample read would be worse than a late one; (b) report visits-to-date and observed CTRs at the cycle retro; (c) shift effort to the reach mechanism §1 actually validated — each licensed facilitator cohort (P1) adds a private WhatsApp group of ~30–100 learners to P2's seeded surfaces, so P1 wins compound directly into H1 traffic. Do not buy traffic to force the read (paid ads remain parked, §2).

---

## 7. Honest limits and handoff flags (not findings; not edited elsewhere — outside this file's scope)

1. **Payment-rails risk (flag to conversion-system-builder / Lawrence):** checkout is Gumroad in USD by card; the demand brief's cedi/MoMo evidence sits on Selar-type rails. No hook in this plan promises MoMo. If H1 underperforms, test rails before concluding price failure.
2. **Landing page also still says "v3.0.1 release bundle"** while the shipped pack contains v3.3.0 — bundle-version copy should update in the same L1 pass (surface list in pending-corrections §3).
3. **Unverified:** existence/size of OMCP center-level WhatsApp groups (inferred, §1); a KNUST-specific GDG on Campus chapter (route via GDG Kumasi instead); TikTok's ability to convert a deliberate GHS 49 purchase (that's why it's experimental); Scenario B/C reach (treat as not achievable this cycle, §1).
4. **`CLAUDE.md` missing from the repo** at write time (see header) — targets used here come from its quotations in approved upstream docs.
5. **KNUST social proof** ("KNUST is piloting this") may be used in outreach only after the pilot cohort has actually started, and pilot-story content only with Prof. Amenu's consent and true numbers.

---

**Rev. 2 changelog (2026-07-19, post-evaluator — maps 1:1 to the review's five revision requirements):**
1. Registration claim re-sourced (§1.2, §1 verdict, §4 Standing row, hook P2 #7): general Phase 2 registration reframed as open-ended since late April 2026 per what GhCampus/TechFocus24 actually say; the 15–20 July 2026 FCFS window correctly attributed to GCTU's institution-level 2,000-slot allocation (GCTU's own announcement); "windows to plan around" replaced with "announcements to react to."
2. TikTok figure re-cited (§1.4, §2 E1 row): 81% — of internet users, Q3 2024 — now cited to the Statista page that visibly carries it (We Are Social/DataReportal/Meltwater data); Pulse Ghana retained only for the STEM-feed courtship it actually reports; E1 explicitly sized as an experiment, not a reach assumption.
3. WhatsApp figure corrected (§1.4, §2 P2 row): 93% of internet users, Q3 2024, same Statista page; DataReportal now cited only for its verified 26.3M users / 74.6% penetration; the unsourced "leads observed markets" line deleted.
4. Experiment 2 redesigned around the public GHS 950 list price (§3, §4): both arms quote 950; the concession (none vs. 50%-off first cohort) is the variable; ceiling GHS 1,500 demoted to negotiation bound; amendment flagged for Lawrence at Day 0.
5. The ~1,000–2,500-visit budget now carries a labeled per-channel assumption chain (§1 verdict) plus a P2 shortfall fallback (§6).

Nothing the review passed was weakened: §0 gate status, the wave plan and five org types, all 20 hooks, the metric exclusions, and the §7 flags are unchanged except where the five fixes required it.

---

*This plan (rev. 2) is ready for the evaluator re-review. Evaluator: rev. 2 addresses revision requirements 1–5 of `growth/reviews/review-channel-plan-2026-07-19.md`; please re-check (a) the repaired citations in §1.2/§1.4/§2, (b) the redesigned Experiment 2 in §3 against the Checkpoint B rulings, and (c) the §1 reach-budget arithmetic and §6 fallback. On PASS, Wave 1 outreach awaits only the L1 ship (Day 0).*
