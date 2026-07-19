# Kickoff Prompts — Growth Workflow

Run these in Claude Code from the repo root, one stage at a time. Each stage ends at a human checkpoint — don't chain stages in one session.

## Stage 0 — every session, automatic

CLAUDE.md already instructs Claude to critique your prompt before executing and to explain in plain English. If it doesn't, say: "First critique this prompt like a strategist — list missing context and propose a sharper version before doing anything."

## Stage 1 — Market research

> Use the market-signal-researcher agent to produce a fresh demand brief. Focus this cycle on: [e.g., "validating the Student Portfolio Pack segments in Ghana and picking the first expansion market"]. When done, run the evaluator agent on growth/demand-brief.md.

Then: **Checkpoint A** — read the brief, correct anything that contradicts what you know from real users, mark it "APPROVED <date>" at the top.

## Stage 2 — Offer refinement

> Use the offer-architect agent to refine the offer ladder based on the approved demand brief. This cycle, pay special attention to: [e.g., "fixed pricing for the Facilitator Pack" / "PPP prices for expansion market X"]. Then run the evaluator agent on growth/offer-spec.md.

Then: **Checkpoint B** — you approve prices. Mark "APPROVED <date>".

## Stage 3 — Distribution + conversion (parallel)

> Run the distribution-strategist and conversion-system-builder agents in parallel: the strategist produces growth/channel-plan.md from the approved offer spec; the builder drafts revised funnel assets in growth/funnel/. Then run the evaluator agent on both outputs.

Then: **Checkpoint C** — final taste pass. Only after your approval:

> Apply the approved funnel changes from growth/funnel/ into marketing/, showing me each diff before writing.

## Stage 4 — Ship and measure

Launch. Each week, record actuals in growth/metrics.md (visits, lead-magnet conversion, email opens/clicks, sales by market). Then:

> Read growth/metrics.md and identify the weakest stage against the thresholds in CLAUDE.md. Propose which single stage to rerun and why.

## Rules of thumb

- One stage per session — keeps context clean and outputs sharp.
- Never skip the evaluator. Never skip your own checkpoint.
- If an agent's output feels generic, that's a REVISE, not a shrug.
