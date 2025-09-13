# 📘 AI Learner's Journal Kit v2.0 — Quick Start Guide

🎉 **What's New in v2.0**: Real working software! No more placeholders—this is production-ready code that you can use immediately.

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
cd ~/Downloads/AI_Learners_Journal_Kit_v2.0
```

#### 🪟 **Windows:**
```cmd
cd %USERPROFILE%\Downloads\AI_Learners_Journal_Kit_v2.0
```

### Step 3: Install the Software

#### 📱 **macOS Installation:**

**Method 1: Right-Click Method (Recommended)**
1. **In Finder**, navigate to your downloaded folder
2. **Go to** `installers` folder
3. **Right-click** on `Installer.command`
4. **Select** "Open" from menu
5. **Click** "Open" again in security dialog
6. **Follow** the installer prompts

**If you see security warning "Apple could not verify...":**
- This is normal! The software is safe
- Use the right-click method above to bypass it

**Method 2: Terminal Installation (If right-click doesn't work)**
```bash
chmod +x installers/Installer.command
./installers/Installer.command
```

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

### Step 5: Test Your Installation

#### Test the command works:
```bash
ai-journal --help
```

You should see the help menu with available commands.

---

## 🚨 CRITICAL: Always Use Quotes Around Your Text!

### **⚠️ Why This Matters:**
The terminal treats certain characters as special commands. **Always wrap your topics and content in quotes** to avoid errors.

### **❌ These Will Break (DON'T DO THIS):**
```bash
ai-journal new What is MCP?           # ? causes "no matches found"
ai-journal new Cost $50               # $ tries to expand variables
ai-journal new File & Directory       # & runs commands in background
ai-journal append latest Today's work # ' breaks the command
```

### **✅ These Work Perfectly (DO THIS):**
```bash
ai-journal new "What is MCP?" question
ai-journal new "Cost Analysis: $50" finance
ai-journal new "File & Directory Management" bash
ai-journal append latest "Today's work was productive"
```

### **🎯 Golden Rule: When in doubt, use quotes!**

**Characters that ALWAYS need quotes:**
`? * $ & ; | ( ) [ ] ! '` and anything with spaces

---

## ✅ Your First Journal Entry (30 seconds)

### Create your first entry:
```bash
ai-journal new "Python Learning Session" python coding
```

### Add some content:
```bash
ai-journal append latest "Today I learned about list comprehensions: [x*2 for x in range(5)]"
```

### View your entries:
```bash
ai-journal list
```

### Search your knowledge:
```bash
ai-journal search "python"
```

## 🎯 Real-World Usage Examples (With Proper Quoting!)

### Capture AI conversations:
```bash
ai-journal new "How does useEffect work?" react hooks
ai-journal append latest "Q: When does useEffect run? A: After every render by default"
ai-journal append latest "Key insight: Use dependency array to control when it runs"
```

### Daily learning sessions:
```bash
ai-journal new "Docker Tutorial Questions" docker containers
ai-journal append latest "Q: What's the difference between ADD and COPY? A: ADD has extra features like URL downloads"
```

### Technical research:
```bash
ai-journal new "Understanding TypeScript Generics" typescript
ai-journal append latest "Generic syntax: function identity<T>(arg: T): T { return arg; }"
```

## 📚 All Available Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `new` | Create new entry | `ai-journal new "Topic" tag1 tag2` |
| `append` | Add to existing entry | `ai-journal append latest "New insight"` |
| `list` | Show all entries | `ai-journal list --limit 10` |
| `search` | Find entries | `ai-journal search "keyword"` |
| `open` | View entry in editor | `ai-journal open latest` |

**Remember: Always use quotes around topics and content!**

## 🔧 Troubleshooting

### "Command not found" (macOS):
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Then restart your terminal.

### "No matches found" error:
You forgot quotes! Use: `ai-journal new "Your topic here" tags`

### "Command not found" (Windows):
The installer should handle PATH automatically. If not, restart Command Prompt.

### Security warning on macOS:
- **Right-click** the installer file
- **Select** "Open" 
- **Click** "Open" in security dialog

### Installer won't run:
**macOS:**
```bash
chmod +x installers/Installer.command
./installers/Installer.command
```

**Windows:**
Right-click `Installer.bat` → "Run as administrator"

## 📁 Where Your Data Lives

Your journal entries are stored as **standard Markdown files**:

**macOS/Linux:** `~/AI-Journal/entries/YYYY/MM/`  
**Windows:** `%USERPROFILE%\AI-Journal\entries\YYYY\MM\`

### Benefits:
- ✅ **No vendor lock-in** - plain text files
- ✅ **Works with any text editor**
- ✅ **Easy to backup and sync**
- ✅ **Future-proof format**

## 🚀 Pro Tips

### 1. **Always quote everything:**
```bash
ai-journal new "Any topic with spaces or symbols" tags
```

### 2. **Great for questions (super common!):**
```bash
ai-journal new "How does authentication work?" security nodejs
ai-journal new "What is dependency injection?" design-patterns
ai-journal new "Why use async/await?" javascript promises
```

### 3. **Perfect for AI conversations:**
```bash
ai-journal new "ChatGPT: React Best Practices" react
ai-journal append latest "Q: How to optimize re-renders? A: Use React.memo and useMemo"
```

### 4. **Organize by learning sessions:**
```bash
ai-journal new "Day 5: Advanced CSS" css flexbox
ai-journal append latest "Learned about CSS Grid vs Flexbox differences"
```

## 🆘 Need Help?

### Quick Reference:
- **List recent entries:** `ai-journal list --limit 5`
- **Find specific topic:** `ai-journal search "your-topic"`
- **View latest entry:** `ai-journal open latest`
- **Get help:** `ai-journal --help`

### Most Common Mistake:
**Forgetting quotes!** Always use: `ai-journal new "Your topic" tags`

### Still stuck?
1. **Double-check quotes** around all text
2. **Restart your terminal** after installation
3. **Try the manual installation method**
4. **Contact support** with your operating system version

---

## 🎉 You're Ready to Build Your AI Knowledge Base!

**Remember the golden rule: Always use quotes around your text!**

Start capturing insights from your ChatGPT, Claude, and Gemini conversations. Your future self will thank you for building this searchable knowledge library.

**Examples to get you started:**
```bash
ai-journal new "What I learned today" daily-notes
ai-journal new "JavaScript Questions" javascript learning
ai-journal new "Docker Commands Reference" docker cheatsheet
```

**Happy learning! 🚀**
