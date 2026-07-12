# AI Learner's Journal Kit — Project Memory

## Instruction to Claude

Treat me like a beginner. As you build, explain what you are doing in plain English — why files exist and what commands do before running them. Before executing any growth-stage prompt, first critique it: list missing context, then propose a sharper version and wait for my approval.

## What the product is (facts, keep current)

- Local-first journaling tool for AI learners: Python CLI (`ai-journal`) + simple web UI. Turns AI conversations, class notes, and workshop exercises into a searchable Markdown journal stored on the user's machine.
- Current version: v3.0.1. Requires Python 3.9+. AI features are optional and use the customer's own API key (Groq free tier recommended; offline Starter Guide works without any key).
- License: PolyForm Noncommercial 1.0.0; commercial use by others requires a separate license from Lawrence Agbemabiese (agbe@udel.edu). Support: info@agenticppa.com.
- Product truth rule: sales copy may only describe features that exist in the current release (see `docs/Paid_Product_Checklist.md`).

## Offer ladder (live)

| Tier | Product | Price |
|------|---------|-------|
| Free | Ghana 7-Day AI Coding Journal (lead magnet) | Free |
| Core | Student Portfolio Pack (12-week) | USD 4.50 (~GHS 49) |
| Premium | Facilitator Cohort Pack (clubs, bootcamps, universities) | Contact / license |

Beachhead market: Ghana learners. Distribution copy lives in `marketing/ghana-launch/` (landing page, Gumroad copy, email/WhatsApp sequence, social scripts).

## Growth workflow (reusable — rerun each cycle)

Five agents in `.claude/agents/`, run stage by stage with human checkpoints. Kickoff prompts: `growth/KICKOFF_PROMPTS.md`. Stage outputs are versioned files in `growth/` — each stage reads its predecessors' files, never restarts from scratch.

1. market-signal-researcher → `growth/demand-brief.md` → **Checkpoint A (Lawrence)**
2. offer-architect → `growth/offer-spec.md` → **Checkpoint B (Lawrence approves prices)**
3. distribution-strategist + conversion-system-builder (parallel) → `growth/channel-plan.md`, `growth/funnel/` → evaluator → **Checkpoint C (Lawrence)**
4. Ship, measure, feed real numbers back into `growth/metrics.md`, rerun weakest stage.

Nothing ships without an evaluator pass (rubric: `.claude/skills/evaluator-rubric/SKILL.md`) and my sign-off.

## Success metrics (review weekly, log in growth/metrics.md)

- Lead magnet landing conversion ≥ 25% (rework Offer if < 15% after 500 visits)
- Email/WhatsApp: open ≥ 40%, click ≥ 5%
- Core pack visitor→buyer ≥ 2% PPP-adjusted (rework Research+Offer if < 1% after 1,000 visits)
- Agent/API spend < 10% of monthly revenue

## Repo map

- `scripts/`, `installers/`, `web/` — the product itself. Growth agents must NOT edit product code.
- `docs/` — checklists, release gates, facilitator guide
- `marketing/ghana-launch/` — live launch copy (conversion-system-builder edits here)
- `dist/`, `output/` — built release artifacts and PDFs (never hand-edit)
- `growth/` — agent workflow outputs and metrics
