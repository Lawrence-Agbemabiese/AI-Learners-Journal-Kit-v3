# Workshop Facilitator Guide

This guide helps facilitators run AI Learner's Journal Kit in a training workshop.

## Audience

Use this workshop for:

- Students learning how to capture AI-assisted learning.
- Professionals building a local knowledge base.
- Beginners who need a menu-driven experience before direct terminal commands.

## Pre-Workshop Checklist

- Share the release ZIP, not a random source snapshot.
- Ask attendees to install Python 3.9 or newer.
- Ask attendees to confirm they can open Terminal, Command Prompt, or PowerShell.
- Decide whether optional OpenAI use is in scope.
- Prepare non-sensitive sample prompts and learning notes.

## Recommended Agenda

1. Explain the local journal folder and Markdown storage.
2. Install the product.
3. Run `ai-journal setup`.
4. Open the beginner menu with `ai-journal`.
5. Create a first entry.
6. Append notes to the latest entry.
7. Search by tag or topic.
8. Open the latest entry.
9. Optional: configure `OPENAI_API_KEY` and demonstrate `ai-journal ask`.

## Sample Exercise

Ask attendees to create an entry with this topic:

```text
What I learned about responsible AI today
```

Suggested tags:

```text
ai learning ethics
```

Then ask them to append:

```text
One idea I want to remember is that AI answers should be verified before use.
```

Finally, ask them to search:

```text
ethics
```

## Safety Guidance

Do not ask attendees to paste private, medical, legal, financial, student-record, employer, or client-confidential information into the app or optional AI workflow.

Use sample content during training.

## Troubleshooting Script

Ask attendees to run:

```bash
ai-journal setup
```

If that fails, confirm:

- Python is installed.
- The installer copied files into the journal folder.
- A new terminal was opened after PATH changes.
- The user can run the launcher directly from the journal folder.

## Workshop Success Criteria

Every attendee should leave with:

- One created journal entry.
- One appended note.
- One successful search.
- A clear understanding that entries are stored locally as Markdown.
