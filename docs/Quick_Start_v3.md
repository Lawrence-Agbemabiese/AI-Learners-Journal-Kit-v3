# AI Learner's Journal Kit v3.0 Quick Start

This guide is for people who want the easiest path first. You can use AI Journal from a double-click menu and do not need to memorize terminal commands.

## 1. Install

### macOS

1. Open the downloaded folder.
2. Open the `installers` folder.
3. Right-click `Installer.command`.
4. Choose `Open`.
5. Choose `Open` again if macOS shows a security warning.
6. Follow the prompts.

After installation, double-click:

```text
~/AI-Journal/Start AI Journal.command
```

### Windows

1. Open the downloaded folder.
2. Open the `installers` folder.
3. Double-click `Installer.bat`.
4. Follow the prompts.

After installation, double-click:

```text
%USERPROFILE%\AI-Journal\Start AI Journal.bat
```

### Linux

Open a terminal in the downloaded folder and run:

```bash
chmod +x installers/install_ai_journal_v3.sh
./installers/install_ai_journal_v3.sh
ai-journal
```

## 2. Use The Menu

When AI Journal starts, choose a number:

```text
1. Create a new journal entry
2. Add to latest entry
3. Ask AI and save answer
4. Search my journal
5. Open latest entry
6. Run setup check
7. Quit
```

The menu asks for the topic, notes, and search words. This avoids common terminal problems with quotes, spaces, question marks, and dollar signs.

## 3. Create Your First Entry

Choose `1. Create a new journal entry`.

Example topic:

```text
What I learned about responsible AI today
```

Example tags:

```text
ai learning ethics
```

The entry is saved as a Markdown file inside `~/AI-Journal/entries`.

## 4. Add Notes Later

Choose `2. Add to latest entry`.

Paste or type your note. Finish with a blank line.

## 5. Search Your Journal

Choose `4. Search my journal`.

Search by topic or tag, such as:

```text
ethics
docker
lesson plan
```

## Optional: Ask AI From The Journal

The journal works without an API key. To use the `ask` option with OpenAI:

1. Get an API key from `https://platform.openai.com/api-keys`.
2. Install the optional package:

```bash
python3 -m pip install -r requirements.txt
```

1. Set the key for your terminal session:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Then choose `3. Ask AI and save answer` from the menu, or run:

```bash
ai-journal ask "What is a learning objective?"
```

AI Journal shows a review score for structure and completeness. It is not a factual accuracy score. For medical, legal, financial, security, or other high-stakes topics, verify with a trusted expert or source.

## Optional: Direct Commands

If you are comfortable in a terminal, these commands still work:

```bash
ai-journal new "My First Learning Session" learning
ai-journal append latest "A useful insight"
ai-journal search "learning"
ai-journal list --limit 10
ai-journal open latest
ai-journal setup
```

You can also leave off the text and let AI Journal prompt you:

```bash
ai-journal new
ai-journal append latest
ai-journal search
```

## Troubleshooting

### The command `ai-journal` is not found

On macOS, double-click:

```text
~/AI-Journal/Start AI Journal.command
```

On Windows, double-click:

```text
%USERPROFILE%\AI-Journal\Start AI Journal.bat
```

You can also run the setup check from the installed menu.

### AI does not answer

Check that the optional package is installed and the API key is set:

```bash
python3 -m pip install -r requirements.txt
echo $OPENAI_API_KEY
```

If no key is configured, AI Journal creates a manual entry instead of stopping.

### I prefer plain terminal output

Use:

```bash
ai-journal ask "What is Docker?" --plain
```

## Support And Privacy

For workshop or paid-product distribution, include these files with the download:

- `SUPPORT.md`
- `PRIVACY.md`
- `REFUND_POLICY.md`
- `SECURITY.md`

The core journal stores entries locally. The optional AI workflow sends prompts to OpenAI only when the user configures an API key and runs `ai-journal ask`.
