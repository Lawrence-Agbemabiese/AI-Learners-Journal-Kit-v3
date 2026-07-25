# AI Learner's Journal Kit

AI Learner's Journal Kit turns useful AI conversations, class notes, workshop exercises, and learning moments into a searchable journal that stays on your own computer.

## Start here — no coding required

The friendly browser interface is the recommended way to use AI Journal.

### macOS

1. Download and unzip the customer release.
2. Open the extracted folder.
3. Double-click **START HERE - AI Journal.command**.
4. Your browser opens automatically.
5. Click **Ask the Guide**, **New entry**, or **Search my journal**.

Keep the small Terminal window open while the journal is running. To stop the journal, return to that window and press **Control + C**.

If macOS blocks the launcher, right-click it, choose **Open**, and approve it. See `docs/Quick_Start_v3.md` for illustrated-style troubleshooting steps.

### Windows

1. Download and unzip the customer release.
2. Open the extracted folder.
3. Double-click **START HERE - AI Journal.bat**.
4. Your browser opens automatically.
5. Click **Ask the Guide**, **New entry**, or **Search my journal**.

Keep the small command window open while the journal is running. Close it when finished.

### Linux

Linux users can run:

```bash
python3 scripts/web_server.py
```

Then open the local address shown in the terminal.

## First five minutes

1. Click **New entry** and write one thing you learned.
2. Click **Add to today** whenever a quick thought lands later — it goes into today's entry (one is started for you if needed), or into any entry you pick.
3. Click **Ask the Guide** and ask a complete question, such as “What does grep do?”
4. Leave **Use my journal as context** checked when you want the Guide to build on your notes.
5. Click **Search my journal** to find earlier learning.
6. Use **Manage AI** to choose Groq, OpenAI, Claude, or Gemini when available.

Deleting is safe by design: open an entry, click **Delete**, and it moves to a `trash` folder inside your journal instead of disappearing. Terminal users get a permanent `--purge` option too.

The core journal stores notes as plain Markdown files on your computer. Optional AI questions are sent only to the provider you configure.

## AI setup for beginners

The web interface is the primary setup path:

1. Open AI Journal.
2. Click **Ask the Guide**.
3. Click **Manage AI**.
4. Choose a provider.
5. Paste that provider's API key.
6. Click the connection test or save button.
7. Ask a simple test question.

Never share an API key in email, screenshots, support tickets, journal entries, or GitHub.

## What is included

- Friendly local browser interface
- Plain-file journal stored on your computer
- New entries, quick additions to today or any entry, search, progress, and badges
- Edit any entry in place from the browser
- Safe entry deletion (trash first, permanent only on request)
- Ask the Guide with optional journal context
- Optional multiple AI providers
- Cross-platform launchers and installers
- Advanced command-line interface for facilitators and power users

## Advanced: Terminal users

Terminal use is optional. See `OPTIONAL_READING_command-line.md`.

Common commands:

```bash
uv run ai-journal doctor
uv run ai-journal find "grep"
uv run ai-journal backup
```

## Paid downloads and storefronts

Customers should receive the versioned release ZIP produced by `scripts/build_release.py`, not GitHub's automatic “Source code” archive.

Before uploading to Gumroad, Payhip, Lemon Squeezy, or another platform, follow:

- `docs/Storefront_Distribution_Checklist.md`
- `docs/Paid_Product_Checklist.md`
- `docs/Quick_Start_v3.md`

The release builder now requires the web-first launchers and onboarding documents, preventing a customer package from being built without them.

## Support, privacy, and safety

See `SUPPORT.md`, `PRIVACY.md`, `SECURITY.md`, and `REFUND_POLICY.md`.

AI answers may be wrong. Verify medical, legal, financial, security, and other high-stakes information with a qualified source.

## More information

### Quick Start

Follow `docs/Quick_Start_v3.md` for the complete browser-first walkthrough.

### Installation

Mac and Windows users should begin with the clearly labeled **START HERE** launcher. Terminal-based installation is optional and documented separately.

### Features

The kit includes a local browser interface, plain-file journal storage, search, learning activity tracking, Ask the Guide, optional AI providers, backups, and advanced command-line tools.

### Workshop Use

Facilitators can use the journal in classes, cohorts, coding clubs, and guided learning workshops. See `docs/Workshop_Facilitator_Guide.md`.

### Paid Product Use

Commercial distribution must use the verified customer release ZIP. See `docs/Paid_Product_Checklist.md` and `docs/Storefront_Distribution_Checklist.md`.

### Support

See `SUPPORT.md` for troubleshooting and help.

### Privacy

See `PRIVACY.md` for data-handling information.

### License

See `LICENSE` for permitted use and distribution terms.
