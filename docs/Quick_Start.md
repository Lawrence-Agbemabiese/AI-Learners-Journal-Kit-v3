# AI Learner's Journal Kit v3.0 Quick Start

This guide covers the features currently implemented in v3.0.

## Install

### macOS or Linux

```bash
git clone https://github.com/Lawrence-Agbemabiese/AI-Learners-Journal-Kit-v3.git
cd AI-Learners-Journal-Kit-v3
chmod +x installers/install_ai_journal_v3.sh
./installers/install_ai_journal_v3.sh
```

Restart your terminal if `~/bin` was not already in your `PATH`.

### Windows

```cmd
git clone https://github.com/Lawrence-Agbemabiese/AI-Learners-Journal-Kit-v3.git
cd AI-Learners-Journal-Kit-v3
installers\Installer.bat
```

Use `%USERPROFILE%\AI-Journal\ai-journal.bat` directly, or add `%USERPROFILE%\AI-Journal` to your user `PATH`.

## Optional AI Setup

The core `new`, `append`, `list`, `search`, and `open` commands use only the Python standard library.

The `ask` command needs the OpenAI package and an API key:

```bash
python3 -m pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key"
```

By default, `ask` uses `gpt-4o-mini`. Override it with `AI_JOURNAL_OPENAI_MODEL` if you want another OpenAI chat model.

Claude, Gemini, and multi-source comparison are planned features. For now, use `--source chatgpt` for API-backed AI capture.

## First Entry

Always quote topics and content that contain spaces or shell-special characters.

```bash
ai-journal new "Python Learning Session" python coding
ai-journal append latest "Today I learned about list comprehensions."
ai-journal list --limit 5
ai-journal search "python"
ai-journal open latest
```

## AI-Assisted Entry

```bash
ai-journal ask "What is React useEffect?" --source chatgpt
```

The command shows the response, a quality estimate, risk metadata, and a curation menu:

```text
/save     - Save response to journal
/edit     - Edit response before save
/verify   - Add verification notes
/reflect  - Add critical thinking reflection
/discard  - Do not save this response
```

## Data Location

Entries are stored as Markdown files under:

- macOS/Linux: `~/AI-Journal/entries/YYYY/MM/`
- Windows: `%USERPROFILE%\AI-Journal\entries\YYYY\MM\`

The searchable index lives at `~/AI-Journal/index.json` or `%USERPROFILE%\AI-Journal\index.json`.
