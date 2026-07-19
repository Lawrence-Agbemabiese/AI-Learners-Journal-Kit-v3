# Changelog

All notable product-facing changes should be documented here before a paid release is published.

## v3.3.0 (2026-07-19)

- Added `ai-journal import`: turn a local Claude Code session into a draft journal entry with your real prompts pre-filled and the Reflection left for you to write. Offline, read-only on session files; also available as beginner menu option 6.
- Import remembers which sessions were already imported and refuses duplicates.
- After import, the Reflection questions are printed in the terminal so the next step is obvious.
- Fixed a duplicate "Created new entry" message when an entry name collision triggered the automatic rename.
- Release packaging now explicitly excludes internal working folders (`growth/`, `.claude/`) from customer archives.

## Unreleased

- Added buyer-facing privacy, support, refund, and security documentation.
- Added workshop and paid product readiness checklists.
- Added release packaging support for versioned ZIP and tar.gz artifacts.
- Made Python CLI output safer for captured and Windows terminal output.
- Aligned README claims with the current product feature set.

## v3.0.0

- Added optional OpenAI-powered `ask` workflow.
- Added beginner-oriented journal commands.
- Added cross-platform installer scripts.
- Added Markdown journal storage with JSON index.
- Added CI, lint, and security workflow coverage.
