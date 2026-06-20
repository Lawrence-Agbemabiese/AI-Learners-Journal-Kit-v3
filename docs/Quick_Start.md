# AI Learner's Journal Kit v3.0 Quick Start

For the easiest path, use the beginner menu instead of direct terminal commands.

## Install

### macOS

Double-click `installers/Installer.command`, then open:

```text
~/AI-Journal/Start AI Journal.command
```

### Windows

Double-click `installers\Installer.bat`, then open:

```text
%USERPROFILE%\AI-Journal\Start AI Journal.bat
```

### Linux

```bash
chmod +x installers/install_ai_journal_v3.sh
./installers/install_ai_journal_v3.sh
ai-journal
```

## Menu

Run `ai-journal` with no arguments, or use the double-click launcher.

```text
1. Create a new journal entry
2. Add to latest entry
3. Ask AI and save answer
4. Search my journal
5. Open latest entry
6. Run setup check
7. Quit
```

## Direct Commands

These are optional for users who prefer the command line:

```bash
ai-journal new "Python Learning Session" python coding
ai-journal append latest "Today I learned about list comprehensions."
ai-journal list --limit 5
ai-journal search "python"
ai-journal open latest
```

You can also omit text arguments and let the app prompt you:

```bash
ai-journal new
ai-journal append latest
ai-journal search
```

## Optional AI Setup

The core `new`, `append`, `list`, `search`, and `open` commands use only the Python standard library.

The `ask` command needs the OpenAI package and an API key:

```bash
python3 -m pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key"
ai-journal ask "What is React useEffect?"
```

AI Journal shows a review score for structure and completeness. It is not a factual accuracy score. Verify high-stakes topics with a trusted expert or source.

Use plain terminal output when needed:

```bash
ai-journal ask "What is Docker?" --plain
```

## Data Location

Entries are stored as Markdown files under:

- macOS/Linux: `~/AI-Journal/entries/YYYY/MM/`
- Windows: `%USERPROFILE%\AI-Journal\entries\YYYY\MM\`

The searchable index lives at `~/AI-Journal/index.json` or `%USERPROFILE%\AI-Journal\index.json`.

## Support And Privacy

For workshop or paid-product distribution, include `SUPPORT.md`, `PRIVACY.md`, `REFUND_POLICY.md`, and `SECURITY.md`.

The core journal stores entries locally. The optional AI workflow sends prompts to OpenAI only when the user configures an API key and runs `ai-journal ask`.
