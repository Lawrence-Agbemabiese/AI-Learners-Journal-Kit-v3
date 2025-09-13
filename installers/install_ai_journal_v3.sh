#!/bin/bash
# AI Journal Kit v3.0 Installation Script
# Installs AI integration features and enhanced CLI

set -euo pipefail

echo "🚀 Installing AI Journal Kit v3.0 - AI Integration Update"
echo "======================================================="

JOURNAL_DIR="$HOME/AI-Journal"
SCRIPTS_DIR="$JOURNAL_DIR/scripts"

# Check if AI Journal is already installed
if [ ! -d "$JOURNAL_DIR" ]; then
    echo "❌ AI Journal not found at $JOURNAL_DIR"
    echo "Please install the base AI Journal Kit first."
    exit 1
fi

echo "✅ Found existing AI Journal installation"

# Create backup of existing files
echo "📦 Creating backup of existing files..."
BACKUP_DIR="$JOURNAL_DIR/backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

if [ -f "$JOURNAL_DIR/../bin/ai-journal" ]; then
    cp "$JOURNAL_DIR/../bin/ai-journal" "$BACKUP_DIR/"
fi

if [ -f "$SCRIPTS_DIR/entry_saver.py" ]; then
    cp "$SCRIPTS_DIR/entry_saver.py" "$BACKUP_DIR/"
fi

echo "✅ Backup created at $BACKUP_DIR"

# Install new CLI wrapper
echo "🔧 Installing enhanced CLI wrapper (v3.0)..."
if [ -f "$HOME/Desktop/ai-journal-v3" ]; then
    cp "$HOME/Desktop/ai-journal-v3" "$HOME/bin/ai-journal"
    chmod +x "$HOME/bin/ai-journal"
    echo "✅ Enhanced CLI installed"
else
    echo "❌ ai-journal-v3 not found on Desktop"
    exit 1
fi

# Install AI integration script
echo "🤖 Installing AI integration module..."
if [ -f "$HOME/Desktop/ai_integration.py" ]; then
    cp "$HOME/Desktop/ai_integration.py" "$SCRIPTS_DIR/"
    chmod +x "$SCRIPTS_DIR/ai_integration.py"
    echo "✅ AI integration module installed"
else
    echo "❌ ai_integration.py not found on Desktop"
    exit 1
fi

# Install enhanced entry saver
echo "📝 Installing enhanced entry saver..."
if [ -f "$HOME/Desktop/entry_saver_v3.py" ]; then
    cp "$HOME/Desktop/entry_saver_v3.py" "$SCRIPTS_DIR/entry_saver.py"
    chmod +x "$SCRIPTS_DIR/entry_saver.py"
    echo "✅ Enhanced entry saver installed"
else
    echo "❌ entry_saver_v3.py not found on Desktop"
    exit 1
fi

# Install OpenAI dependency
echo "📦 Installing required dependencies..."
if command -v pip3 >/dev/null 2>&1; then
    pip3 install openai --user --quiet
    echo "✅ OpenAI library installed"
else
    echo "⚠️  pip3 not found. Please install OpenAI manually:"
    echo "    pip3 install openai"
fi

# Create sample configuration file
echo "⚙️ Creating sample configuration..."
cat > "$HOME/.ai-journal-config.json.example" <<EOF
{
  "api_keys": {
    "openai": "your-openai-api-key-here",
    "anthropic": "your-anthropic-api-key-here",
    "gemini": "your-gemini-api-key-here"
  },
  "settings": {
    "default_ai": "chatgpt",
    "auto_quality_assessment": true,
    "risk_detection": true
  }
}
EOF

echo "✅ Sample config created at ~/.ai-journal-config.json.example"

# Test installation
echo "🧪 Testing installation..."

# Test basic CLI
if "$HOME/bin/ai-journal" --help >/dev/null 2>&1; then
    echo "✅ CLI wrapper working"
else
    echo "❌ CLI wrapper test failed"
    exit 1
fi

# Test AI integration (without API key)
if python3 "$SCRIPTS_DIR/ai_integration.py" --help >/dev/null 2>&1; then
    echo "✅ AI integration module working"
else
    echo "❌ AI integration test failed"
    exit 1
fi

echo ""
echo "🎉 AI Journal Kit v3.0 Installation Complete!"
echo ""
echo "✨ NEW FEATURES:"
echo "  • AI-integrated queries: ai-journal ask \"What is React?\""
echo "  • Interactive curation with /save, /edit, /verify commands"
echo "  • Quality assessment and risk detection"
echo "  • Source tracking and metadata"
echo "  • Enhanced list and search with AI info"
echo ""
echo "🔧 SETUP REQUIRED:"
echo "  1. Get an OpenAI API key: https://platform.openai.com/api-keys"
echo "  2. Set environment variable: export OPENAI_API_KEY='your-key'"
echo "  3. Or edit ~/.ai-journal-config.json.example and rename to .ai-journal-config.json"
echo ""
echo "🚀 TRY IT NOW:"
echo "  ai-journal ask \"What is Docker?\" --source chatgpt"
echo ""
echo "📚 HELP:"
echo "  ai-journal --help    # See all commands"
echo "  ai-journal ask --help # AI integration help"
echo ""
echo "Happy learning with AI connoisseurship! 🧙‍♂️"
