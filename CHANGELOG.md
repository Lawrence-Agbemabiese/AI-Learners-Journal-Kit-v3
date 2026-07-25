# Changelog

All notable product-facing changes should be documented here before a paid release is published.

## v3.4.2 (2026-07-25)

- Added "The daily ritual: Learn → Capture → Prove" card to the web UI home screen, with links to recommended practice platforms (Coddy.tech, Codédex) and a one-line description of each step. Links are plain recommendations for now; the card carries an inline placeholder for partner links + disclosure text once an affiliate arrangement is approved.

## v3.4.1 (2026-07-24)

- Added an **Edit** button to the web UI's entry view: open any entry, click Edit, change the full text, Save. The search index and word counts update immediately. (Terminal users can keep editing the file directly — `ai-journal open <entry>` shows its path.)

## v3.4.0 (2026-07-23)

- Added safe entry deletion: soft delete moves the entry to `<journal>/trash/` (with a restore log) after confirmation, in both the CLI (`ai-journal delete`) and the web UI. Permanent removal is explicit via `ai-journal delete --purge` with a typed confirmation. JSON and SQLite search indexes stay consistent after either.
- "Add to today" now really means today: appends go to today's entry (a new one is started automatically when the day has none), never to an older "latest" entry. The web dialog also lets you pick any recent entry; the CLI accepts `today`, `yesterday`, a date (`2026-07-23`), an id, or a topic.
- Fixed same-day duplicate topics: entries are renamed predictably ("Topic (2)") instead of grammar-mangled variations, and a fully colliding save can no longer be silently discarded.
- Fixed the web UI "Make it simpler" button stacking its prefix onto the question when clicked twice.
- Fixed installers not copying the web interface: `ai-journal web` now works from an installed copy (installers ship `web/` + the web launcher, and the server falls back to the journal's own `web/` folder).
- Fixed entry and index files being written without an explicit UTF-8 encoding, which could crash saves containing accents or emoji on Windows.
- Fixed a nameless `YYYYMMDD-.md` file being created when a topic was empty or symbols-only (now "Untitled entry").
- Fixed `ai-journal import` accepting out-of-range session numbers (e.g. `0` silently importing the last session).
- Fixed `ai-journal backup` including the rebuildable search database's WAL sidecar files and temp files in backups.
- The beginner menu no longer exits entirely when an action fails; it returns to the menu.

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
