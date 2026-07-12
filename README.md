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
2. Click **Ask the Guide** and ask a complete question, such as “What does grep do?”
3. Leave **Use my journal as context** checked when you want the Guide to build on your notes.
4. Click **Search my journal** to find earlier learning.
5. Use **Manage AI** to choose Groq, OpenAI, Claude, or Gemini when available.

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
- New entries, quick additions, search, progress, and badges
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
