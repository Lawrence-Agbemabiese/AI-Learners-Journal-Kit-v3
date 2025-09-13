# 📘 AI Learner's Journal Kit v3.0 — Quick Start Guide

🎉 **What's New in v3.0**: AI Integration! Query ChatGPT directly from your terminal with built-in connoisseurship training. No more context-switching between browser and terminal.

## 💰 Got a Discount Code?

### **Using Your AMBASSADOR-FREE or PPP Code:**

**Before downloading:**
1. **Go to the product page** on Gumroad
2. **Click "I want this"** or "Add to Cart"
3. **At checkout**, look for **"Discount code"** or **"Coupon code"** field
4. **Enter your code:** `AMBASSADOR-FREE` or your country code (e.g., `NG-PPP-3`)
5. **Click "Apply"** - price should change immediately
6. **Complete your purchase**

**Common codes:**
- `AMBASSADOR-FREE` - Free copy for partners
- `STUDENT-3` - $3 student pricing  
- `NG-PPP-3` - $3 Nigeria pricing (and similar for other countries)

---

## 🚀 Installation (5 minutes to working system)

### Step 1: Open Your Terminal

#### 📱 **macOS Users:**
1. **Press** `Cmd + Space` (opens Spotlight search)
2. **Type** "Terminal" and press Enter
3. **Or** go to Applications → Utilities → Terminal

#### 🪟 **Windows Users:**
1. **Press** `Windows key + R` (opens Run dialog)
2. **Type** "cmd" and press Enter
3. **Or** click Start → type "Command Prompt" → press Enter
4. **Or** press `Windows key + X` → select "Terminal" (Windows 11)

### Step 2: Navigate to Downloaded Files

#### 📱 **macOS:**
```bash
cd ~/Downloads/AI_Learners_Journal_Kit_v3.0
```

#### 🪟 **Windows:**
```cmd
cd %USERPROFILE%\Downloads\AI_Learners_Journal_Kit_v3.0
```

### Step 3: Install the Software

#### 📱 **macOS Installation:**

**Method 1: Use the v3.0 Installer (Recommended)**
```bash
chmod +x installers/install_ai_journal_v3.sh
./installers/install_ai_journal_v3.sh
```

**Method 2: Right-Click Method**
1. **In Finder**, navigate to your downloaded folder
2. **Go to** `installers` folder
3. **Right-click** on `Installer.command`
4. **Select** "Open" from menu
5. **Click** "Open" again in security dialog
6. **Follow** the installer prompts

**If you see security warning "Apple could not verify...":**
- This is normal! The software is safe
- Use the right-click method above to bypass it

#### 🪟 **Windows Installation:**
```cmd
installers\Installer.bat
```

### Step 4: Fix Command Access (macOS Only)

If you get "command not found" after installation:

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Then restart your terminal** and try again.

### Step 5: Set Up AI Integration (Optional but Recommended)

To use the new `ask` command with ChatGPT:

1. **Get an OpenAI API key**: https://platform.openai.com/api-keys
2. **Set environment variable:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

**Or create a config file:**
```bash
cp ~/.ai-journal-config.json.example ~/.ai-journal-config.json
# Edit the file and add your API key
```

### Step 6: Test Your Installation

#### Test the command works:
```bash
ai-journal --help
```

You should see the new v3.0 help menu with `ask` command.

---

## 🚨 CRITICAL: Always Use Quotes Around Your Text!

### **⚠️ Why This Matters:**
The terminal treats certain characters as special commands. **Always wrap your topics and content in quotes** to avoid errors.

### **❌ These Will Break (DON'T DO THIS):**
```bash
ai-journal ask What is Docker?           # ? causes "no matches found"
ai-journal new Cost $50                  # $ tries to expand variables
ai-journal ask File & Directory          # & runs commands in background
```

### **✅ These Work Perfectly (DO THIS):**
```bash
ai-journal ask "What is Docker?" --source chatgpt
ai-journal new "Cost Analysis: $50" finance
ai-journal ask "File & Directory Management" --guided
```

### **🎯 Golden Rule: When in doubt, use quotes!**

**Characters that ALWAYS need quotes:**
`? * $ & ; | ( ) [ ] ! '` and anything with spaces

---

## ✨ NEW: AI-Integrated Learning Workflow

### 🤖 Ask AI Directly (No Context Switching!)

```bash
ai-journal ask "What is React useEffect?" --source chatgpt
```

**What happens:**
1. **ChatGPT responds** directly in your terminal
2. **Quality assessment** shows automatically (8/10 bars)
3. **Risk detection** flags high-stakes topics 
4. **Interactive curation menu** appears:

```
┌─ What would you like to do? ─┐
│ /save     - Save to journal   │
│ /edit     - Edit before save  │
│ /verify   - Add verification  │
│ /reflect  - Add reflection    │
│ /discard  - Don't save        │
└─────────────────────────────┘
```

### 🎯 Connoisseurship Training Built-In

- **Quality Scoring**: Every AI response gets rated 1-10
- **Risk Assessment**: Security/financial topics get special warnings
- **Source Tracking**: Know which AI gave you each answer
- **Verification Prompts**: Critical thinking questions for high-risk content
- **Confidence Levels**: Track how much you trust each piece of information

---

## ✅ Your First AI-Assisted Entry (30 seconds)

### Ask AI and curate the response:
```bash
ai-journal ask "What is the Global Index for Responsible AI?" --source chatgpt
```

### Follow the interactive prompts:
1. **Read the AI response** with quality indicators
2. **Choose /save** to store it in your journal
3. **Add verification notes** if prompted
4. **Done!** - Entry saved with full AI metadata

### View your AI-enhanced entries:
```bash
ai-journal list --limit 5
```

You'll see entries with AI source info and quality ratings!

---

## 🎯 Advanced AI Features

### Compare Multiple AI Sources (Coming Soon):
```bash
ai-journal ask "Explain closures" --compare chatgpt,claude,gemini
```

### Guided Learning Mode:
```bash
ai-journal ask "How to secure JWT tokens?" --guided --topic security
```

### Expert Mode (Minimal Prompts):
```bash
ai-journal ask "Top 5 opensource AI tools for SMEs?" --expert
```

---

## 📚 All Available Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `ask` | **NEW** - Query AI with curation | `ai-journal ask "What is Docker?" --source chatgpt` |
| `new` | Create manual entry | `ai-journal new "Topic" tag1 tag2` |
| `append` | Add to existing entry | `ai-journal append latest "New insight"` |
| `list` | Show all entries | `ai-journal list --limit 10` |
| `search` | Find entries | `ai-journal search "keyword"` |
| `open` | View entry in editor | `ai-journal open latest` |

**Remember: Always use quotes around topics and content!**

---

## 🔧 Troubleshooting

### "Command not found" (macOS):
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Then restart your terminal.

### "No matches found" error:
You forgot quotes! Use: `ai-journal ask "Your question here"`

### AI integration not working:
1. Check your API key: `echo $OPENAI_API_KEY`
2. Install OpenAI library: `pip3 install openai --user`
3. Test with: `ai-journal ask "test" --source chatgpt`

### Security warning on macOS:
- **Right-click** the installer file
- **Select** "Open" 
- **Click** "Open" in security dialog

---

## 🎮 Interactive Curation Commands

When AI responds, you'll see these options:

- **`/save`** - Save response to journal (with metadata)
- **`/edit`** - Edit the response before saving
- **`/verify`** - Add confidence and verification notes  
- **`/reflect`** - Add critical thinking reflection
- **`/compare`** - Get another AI's perspective (coming soon)
- **`/discard`** - Don't save this response

---

## 📁 Where Your Data Lives

Your journal entries are stored as **standard Markdown files**:

**macOS/Linux:** `~/AI-Journal/entries/YYYY/MM/`  
**Windows:** `%USERPROFILE%\AI-Journal\entries\YYYY\MM\`

### New in v3.0:
- **AI metadata** embedded in each entry
- **Quality ratings** and **source tracking**
- **Verification status** and **confidence levels**
- **Enhanced index** with AI statistics

---

## 🚀 Pro Tips for AI Connoisseurship

### 1. **Always question AI responses:**
Use `/reflect` to add critical thinking:
- "What could go wrong with this approach?"
- "How would I verify this information?"
- "What's missing from this explanation?"

### 2. **Track your confidence:**
Use `/verify` to set confidence levels:
- **High**: Ready to use in production
- **Medium**: Needs testing first  
- **Low**: Learning only, don't rely on it

### 3. **Multi-source for important topics:**
```bash
ai-journal ask "Security best practices" --source chatgpt
# Later: ask same question with --source claude
# Compare the responses manually for now
```

### 4. **Use risk warnings:**
When you see 🔴 **High-Risk** warnings, always use `/reflect` or `/verify`

---

## 🆘 Need Help?

### Quick Reference:
- **Ask AI:** `ai-journal ask "your question" --source chatgpt`
- **List with AI info:** `ai-journal list --limit 5`
- **Find entries:** `ai-journal search "topic"`
- **Get help:** `ai-journal --help`

### Most Common Mistakes:
1. **Forgetting quotes!** Always use: `ai-journal ask "Your question"`
2. **No API key set** - AI integration needs OpenAI API key
3. **Not restarting terminal** after installation

---

## 🎉 You're Ready to Build Your AI Knowledge Base!

**Remember: The goal is to become a connoisseur of AI output, not just a consumer!**

### **The Connoisseur Mindset:**
- ✅ **Question everything** - Even AI responses
- ✅ **Compare sources** - Different AIs have different strengths  
- ✅ **Verify important information** - Don't trust blindly
- ✅ **Build understanding** - Don't just collect answers
- ✅ **Track your confidence** - Know what you can rely on

Start building your searchable, curated, AI-enhanced knowledge library today!

**Examples to get you started:**
```bash
ai-journal ask "What is Docker?" --source chatgpt
ai-journal ask "How does React useState work?" --guided
ai-journal ask "JWT security best practices" --topic security
```

**Happy learning with AI connoisseurship! 🧙‍♂️🚀**
