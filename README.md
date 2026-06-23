# AI Learner's Journal Kit v3.0

AI Learner's Journal Kit turns useful AI conversations, class notes, workshop exercises, and learning moments into a searchable Markdown journal.

The current product is a local-first command-line tool with a beginner menu. It is suitable for training workshops, self-paced learners, and paid digital product distribution when packaged from a verified release artifact.

## Quick Start

### macOS

1. Download the release ZIP or clone this repository.
2. Right-click `installers/Installer.command`.
3. Choose `Open`, then follow the prompts.
4. Start the beginner menu:

```bash
ai-journal
```

You can also double-click `~/AI-Journal/Start AI Journal.command` after installation.

### Windows

1. Download the release ZIP or clone this repository.
2. Double-click `installers\Installer.bat`.
3. Open a new Command Prompt and run:

```cmd
ai-journal
```

If the new terminal does not recognize `ai-journal`, use:

```cmd
%USERPROFILE%\AI-Journal\ai-journal.bat
```

You can also double-click `%USERPROFILE%\AI-Journal\Start AI Journal.bat`.

### Linux

```bash
chmod +x installers/install_ai_journal_v3.sh
./installers/install_ai_journal_v3.sh
ai-journal
```

## Installation

The installers copy the CLI wrapper and Python scripts into `~/AI-Journal` on macOS/Linux or `%USERPROFILE%\AI-Journal` on Windows. Existing journal entries are preserved.

For paid distribution, use the versioned ZIP created by the release build script instead of asking customers to download a source snapshot.

## Features

- Beginner menu for non-coders: create, append, search, open, and check setup.
- Direct CLI commands for workshop facilitators and power users.
- Plain Markdown journal entries stored locally on the user's computer.
- Search by topic or tag through a small JSON index.
- Optional OpenAI workflow through `OPENAI_API_KEY`.
- AI review score that estimates structure and completeness, not factual correctness.
- Cross-platform installers for macOS, Windows, and Linux.
- Release packaging script for customer-ready ZIP and tar.gz artifacts.

## Beginner Menu

Run `ai-journal` with no arguments:

```text
1. Create a new journal entry
2. Add to latest entry
3. Ask AI and save answer
4. Search my journal
5. Open latest entry
6. Run setup check
7. Quit
```

The menu asks for topics, notes, and search terms interactively, so users do not need to know terminal quoting rules.

## Commands

```bash
ai-journal new "My First Learning Session" learning
ai-journal append latest "A useful insight I want to remember"
ai-journal search "docker"
ai-journal list --limit 10
ai-journal open latest
ai-journal setup
```

You can also run commands without text arguments and let the app prompt you:

```bash
ai-journal new
ai-journal append latest
ai-journal search
```

## If your computer blocks the app the first time

Because this app is downloaded from the internet and is not yet signed by Apple
or Microsoft, your computer may warn you the first time you open the launcher.
Nothing is wrong with the file - this is the normal warning for new downloads.

**macOS** ("Apple could not verify..."): click **Done** (not "Move to Trash"),
then open **System Settings -> Privacy & Security**, scroll to the Security
section, and click **Open Anyway** next to "Start AI Journal.command". Enter your
password if asked, then click **Open**. After this, double-clicking works.

**Windows** ("Windows protected your PC"): click **More info**, then **Run
anyway**.

### Still stuck on macOS? Run it from the Terminal

This always works, even when the launcher is blocked:

1. Open the **Terminal** app (press Cmd+Space, type `Terminal`, press Return).
2. Type `cd ` (with a trailing space) but do **not** press Return yet.
3. Drag the `ai-coding-journal-starter` folder onto the Terminal window - its
   path is filled in for you - then press Return.
4. Run:

   ```bash
   python3 scripts/journal_cli.py menu
   ```

Power-user shortcut to clear the quarantine flag once, then double-click as
normal:

```bash
xattr -dr com.apple.quarantine ai-coding-journal-starter
```

## Turn on AI answers

The journal works fully without AI, and beginner questions like "what is an
API?" are answered offline by the built-in **Starter Guide** - no key needed.
To get AI answers to *any* question, switch on full AI once by pasting a
provider key. Recommended order for learners:

- **Groq** - free, no card needed. The best option if you don't have a card.
- **Claude** or **ChatGPT** - paid; need credits on your provider account.
- **Gemini** - has a free tier, but Google now requires linking a billing card
  to your Google account before it will work (otherwise you get a quota error).

Then install the optional package and set your key:

```bash
python3 -m pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
ai-journal ask "Explain photosynthesis for a beginner"
```

For Windows Command Prompt:

```cmd
set OPENAI_API_KEY=your-api-key-here
ai-journal ask "Explain photosynthesis for a beginner"
```

AI Journal does not include an API key. Users are responsible for their own API
usage and costs. The offline Starter Guide always works for free.

## Workshop Use

This repository includes a workshop guide for facilitators: `docs/Workshop_Facilitator_Guide.md`.

Recommended workshop setup:

- Distribute the release ZIP before the session.
- Ask attendees to install Python 3.9 or newer before the workshop.
- Start with the beginner menu, then show direct commands.
- Use the optional AI workflow only after the core journal flow works.

## Paid Product Use

Use `docs/Paid_Product_Checklist.md` before publishing to Payhip, Gumroad, Lemon Squeezy, or another digital storefront.

Minimum paid-product package:

- Versioned release ZIP.
- `README.md`
- `docs/Quick_Start_v3.md`
- `SUPPORT.md`
- `PRIVACY.md`
- `REFUND_POLICY.md`
- `SECURITY.md`
- `CHANGELOG.md`
- SHA256 checksums from the release build.

## Journal Storage

Entries are stored as Markdown in `~/AI-Journal`:

```text
~/AI-Journal/
  entries/
    2026/
      05/
        20260523-my-topic.md
  media/
  scripts/
  index.json
```

Because entries are plain Markdown, users can read, edit, back up, or export them with ordinary tools.

## Documentation

- `docs/Quick_Start_v3.md` - step-by-step beginner guide.
- `docs/Workshop_Facilitator_Guide.md` - training workshop runbook.
- `docs/Paid_Product_Checklist.md` - storefront and release checklist.
- `docs/Release_Checklist.md` - engineering release gate.
- `docs/Release_Notes_v3.0.1.md` - corrected release note template.
- `OPTIONAL_READING_command-line.md` - command-line background.
- `demo/usage-examples.md` - copy-paste examples.

## Support

See `SUPPORT.md` for workshop and paid-customer support expectations.

## Privacy

See `PRIVACY.md`. The core journal stores data locally. Optional AI prompts are sent to OpenAI only when the user configures an API key and runs `ai-journal ask`.

## License

MIT. See `LICENSE`.
