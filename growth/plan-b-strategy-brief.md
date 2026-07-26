# Plan B Strategy Brief — "What if every partnership application fails?"

*Written 2026-07-26. Purpose: kick off a dedicated strategy task. Start a new task, connect ~/AI-Learners-Journal-Kit-v3, and say: "Read growth/plan-b-strategy-brief.md and think it through with me." Read growth/ailjk-project-primer.md first for full project context (note: primer predates v3.4.3 and the Ekow send — see Current State below).*

## The scenario to plan for

All outbound partnership applications come back negative or are ignored:
Codédex Creator Program (sent 2026-07-25 night; bump email ready in growth/codedex-followup-bump.md), and any future Coddy.tech approach. Affiliate income — the entire monetization engine behind the free-forever decision — never materializes.

## Current state (as of 2026-07-26 morning)

- Product at v3.4.3 (home card now says "The daily **workflow**: Learn → Capture → Prove" — cultural copy fix, Lawrence's call). Repo clean, pushed, dist/ zips built and verified.
- Dr. Ekow (Ashesi) follow-up email SENT 2026-07-25 with working Drive links (v3.4.2 zip + Getting Started PDF, both anyone-with-link). Awaiting response.
- KNUST (via Francis) and University of Port Harcourt replication sessions targeted for the week of 2026-07-27. Experiment 4 (3-hr AILJK + Coddy tutorial) same week.
- Business model of record: journal FREE FOREVER; affiliate income from practice platforms; facilitator cohort packs / portfolio packs leaning paid.

## The four questions, reframed after first-pass critique

1. **Practice platform independence — WITHOUT cloning competitors.**
   Rejected framing: clone Coddy/Codédex (reputational risk while applications pending; huge content/maintenance cost; agents can scaffold the shell but not the pedagogy).
   Adopted framing: evaluate mission-aligned open-source platforms as ritual-card link replacements — freeCodeCamp, Exercism, and similar. Criteria: free for learners, works on low-end hardware / low bandwidth, beginner-appropriate, no account friction, longevity. Deliverable: a swap-ready shortlist so the ritual card can be repointed in one release if affiliates say no.
   (Deferred sub-question, only if a build is ever justified: fresh same-week research on coding agents — Claude Code, OpenAI Codex, Moonshot Kimi, others — not from memory.)

2. **Revenue without affiliates — challenge the "back to direct sales" reflex.**
   Free-forever was chosen because scale IS the strategy; re-paywalling the journal kills the community engine. Preferred candidates to examine: grant funding + paid facilitator cohort packs + paid portfolio/credential packs + institutional licenses (universities pay, learners never do). Direct sales to learners is the fallback of last resort — analyze it honestly, but it must beat the alternatives, not just exist.

3. **Market expansion — urban low-income youth globally.**
   Sequencing question: does expanding beyond Ghana → Nigeria → anglophone SSA strengthen grant applications (bigger impact story) or dilute the beachhead? Fit with social-enterprise framing. What evidence (Experiment 4 metrics, cohort outcomes) must exist first?

4. **Development Impact Prize.**
   Concept: annual prize for AILJK users building apps with clear development impact.
   Consistency fix from first pass: cannot be funded from "subscription proceeds" (no subscriptions exist under free-forever). Candidate funding: a named line in a grant budget, a sponsor (bank/telco/foundation), or a % of facilitator-pack revenue. Also design: judging criteria, evidence-from-journal requirement (the journal itself as the audit trail — unique differentiator), first edition scope (Ghana-only pilot?).

## Research agenda for the strategy task (do fresh web research; do not rely on model memory)

- Open-source practice platforms: current state of freeCodeCamp, Exercism, Odin Project, others; API/deep-link options; offline/low-bandwidth suitability.
- Grant funders plausible for this profile: Mastercard Foundation (Young Africa Works), Fondation Botnar, GIZ/BMZ digital skills programs, Google.org, Co-Impact, Jacobs Foundation, UNICEF innovation funds; typical ticket sizes, open calls, eligibility for Ghana-registered social enterprises.
- Comparable models: freeCodeCamp's donor model, Zindi, ALX/Sand Technologies, Andela's early model — what funded free learning at scale in Africa.
- If reached: current coding-agent landscape comparison (only if the build question survives scrutiny).

## Constraints (non-negotiable product truths)

Local-first, offline, plain Markdown + JSON index (+ rebuildable SQLite FTS), optional BYO-key AI, Python 3.9+, no cloud, no sync, no bundled API access. Never overpromise. Any Plan B must keep the core journal free forever unless this task explicitly concludes otherwise WITH Lawrence's sign-off.

## Decision outputs this strategy task should produce

1. A one-page Plan B decision memo (trigger conditions: e.g. "if no Codédex reply by DATE, then...").
2. Ranked revenue mix for the no-affiliate world.
3. Grant funder shortlist with next actions and deadlines.
4. Prize: go/no-go for a Ghana pilot + funding source.
5. Ritual-card link swap shortlist (question 1 deliverable).

## Working conventions with Lawrence (unchanged)

Show improved prompts before executing. Exact copy-paste commands, one block per command, one-line explanations. Backup before anything destructive. He commits himself (suggest messages). Warm, energetic collaboration; he calls the assistant "Fable 5".
