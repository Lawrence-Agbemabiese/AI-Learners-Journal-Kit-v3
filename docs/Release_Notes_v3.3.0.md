# AI Learner's Journal Kit v3.3.0 Release Notes

Use these notes for the v3.3.0 public release.

## Summary

This release adds session import: learners who use Claude Code (Anthropic's terminal coding assistant) can turn a real coding session into a draft journal entry in one command. The draft pre-fills their actual prompts; the Reflection stays theirs to write. The journal keeps owning what the session meant, not just what was said.

## What Is New In v3.3.0

- `ai-journal import` lists your recent Claude Code sessions and imports the one you pick (`--latest` skips the menu). Also available as option 6 in the beginner menu.
- Imported drafts pre-fill the AI Prompt Log with your real prompts and session facts (project, time span, exchange counts).
- The Reflection questions are printed in the terminal after import so the next step is obvious.
- Sessions are remembered after import: importing the same session again points you to the existing entry instead of creating a duplicate.
- Everything runs offline using only the Python standard library. The importer only reads local session files and never modifies them.

## What Works In This Release (carried from v3.0.1-v3.2.0)

- Beginner menu for creating, appending, searching, opening, and checking journal setup.
- Local Markdown journal entries with a searchable JSON index.
- Browser-based friendly UI and direct CLI commands.
- Optional OpenAI-powered `ask` command when the user configures `OPENAI_API_KEY`.
- Cross-platform installers for macOS, Windows, and Linux.
- Customer-ready release ZIP and tar.gz artifacts with SHA256 checksums.
- Support, privacy, refund, and security documentation.

## Important Notes

- The core journal does not require an API key.
- Session import requires no API key and works fully offline.
- Session import currently supports Claude Code history only; other tools (Gemini CLI, Cursor, Aider) are not yet supported and are not advertised.
- The optional AI workflow uses the customer's own OpenAI API key.
- Review scores estimate answer structure and completeness, not factual correctness.

## Suggested GitHub Release Assets

- `ai-learners-journal-kit-v3.3.0.zip`
- `ai-learners-journal-kit-v3.3.0.tar.gz`
- `SHA256SUMS.txt`
- `release-manifest.json`

## Suggested Storefront Description

AI Learner's Journal Kit is a local-first learning journal for students, professionals, and workshop participants who want to turn AI conversations and class notes into a searchable Markdown knowledge base. New in v3.3.0: if you code with Claude Code in the terminal, one command turns a real session into a draft journal entry — your prompts pre-filled, your reflection to write. Includes a beginner menu, a friendly browser UI, cross-platform installers, optional OpenAI integration, and customer-ready documentation.
