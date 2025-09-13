#!/bin/bash
# AI Learner's Journal Kit - macOS Installer
# Double-click this file to install the AI Journal system

set -euo pipefail

echo "🚀 AI Learner's Journal Kit Installer"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}❌ This installer is for macOS only. For other platforms, see the documentation.${NC}"
    exit 1
fi

# Function to print colored output
print_status() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Variables
JOURNAL_DIR="$HOME/AI-Journal"
BIN_DIR="$HOME/bin"

print_status "Checking system requirements..."

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not installed."
    print_status "Please install Python 3 from https://python.org or using Homebrew:"
    echo "  brew install python3"
    exit 1
fi

print_success "Python 3 found: $(python3 --version)"

# Check if AI Journal directory already exists
if [ -d "$JOURNAL_DIR" ]; then
    print_warning "AI Journal directory already exists at $JOURNAL_DIR"
    read -p "Do you want to continue? This will not overwrite existing entries. (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_status "Installation cancelled."
        exit 0
    fi
else
    print_status "Creating AI Journal directory at $JOURNAL_DIR"
    mkdir -p "$JOURNAL_DIR"/{entries,media,scripts}
fi

# Create bin directory if it doesn't exist
if [ ! -d "$BIN_DIR" ]; then
    print_status "Creating ~/bin directory"
    mkdir -p "$BIN_DIR"
fi

# Check if ~/bin is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    print_warning "~/bin is not in your PATH"
    print_status "Adding ~/bin to your shell profile..."
    
    # Determine which shell profile to update
    SHELL_PROFILE=""
    if [ -n "${ZSH_VERSION:-}" ]; then
        SHELL_PROFILE="$HOME/.zshrc"
    elif [ -n "${BASH_VERSION:-}" ]; then
        SHELL_PROFILE="$HOME/.bash_profile"
    else
        # Default to .zshrc on macOS (default shell)
        SHELL_PROFILE="$HOME/.zshrc"
    fi
    
    # Add to PATH if not already there
    if [ -f "$SHELL_PROFILE" ] && ! grep -q 'export PATH="$HOME/bin:$PATH"' "$SHELL_PROFILE"; then
        echo 'export PATH="$HOME/bin:$PATH"' >> "$SHELL_PROFILE"
        print_success "Added ~/bin to PATH in $SHELL_PROFILE"
        print_warning "You'll need to restart your terminal or run: source $SHELL_PROFILE"
    elif [ ! -f "$SHELL_PROFILE" ]; then
        echo 'export PATH="$HOME/bin:$PATH"' > "$SHELL_PROFILE"
        print_success "Created $SHELL_PROFILE and added ~/bin to PATH"
    fi
fi

# Get the directory where this installer is located
INSTALLER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="$(cd "$INSTALLER_DIR/.." && pwd)"

# Copy or create the AI Journal files
print_status "Installing AI Journal files..."

# Copy the main ai-journal CLI
if [ -f "$BUNDLE_DIR/ai-journal" ]; then
    cp "$BUNDLE_DIR/ai-journal" "$JOURNAL_DIR/"
    chmod +x "$JOURNAL_DIR/ai-journal"
    print_success "Copied ai-journal CLI to AI Journal directory"
fi

# Copy Python scripts
if [ -f "$BUNDLE_DIR/scripts/entry_saver.py" ]; then
    cp "$BUNDLE_DIR/scripts"/*.py "$JOURNAL_DIR/scripts/"
    chmod +x "$JOURNAL_DIR/scripts"/*.py
    print_success "Copied Python scripts to AI Journal directory"
fi

# Create symlink to make ai-journal globally available
if [ ! -f "$BIN_DIR/ai-journal" ]; then
    # If not copied from installer directory, create symlink to the one we just built
    ln -sf "$JOURNAL_DIR/ai-journal" "$BIN_DIR/ai-journal"
    print_success "Created symlink for ai-journal in ~/bin/"
fi

# Initialize index.json if it doesn't exist
if [ ! -f "$JOURNAL_DIR/index.json" ]; then
    cat > "$JOURNAL_DIR/index.json" << EOF
{
  "version": "1.0",
  "created": "$(date -Iseconds)",
  "entries": [],
  "tags": {},
  "stats": {
    "total_entries": 0,
    "last_modified": "$(date -Iseconds)"
  }
}
EOF
    print_success "Created journal index file"
fi

# Test the installation
print_status "Testing installation..."

# Test if ai-journal command works
if "$BIN_DIR/ai-journal" --help > /dev/null 2>&1; then
    print_success "AI Journal CLI is working!"
else
    print_error "Installation test failed. Please check the setup manually."
    exit 1
fi

echo ""
print_success "🎉 Installation completed successfully!"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Restart your terminal or run: source ~/.zshrc (or ~/.bash_profile)"
echo "2. Create your first journal entry:"
echo -e "   ${YELLOW}ai-journal new \"My First Learning Session\" learning${NC}"
echo "3. List your entries:"
echo -e "   ${YELLOW}ai-journal list${NC}"
echo "4. Get help anytime:"
echo -e "   ${YELLOW}ai-journal --help${NC}"
echo ""
echo -e "${GREEN}Happy learning! 🚀${NC}"

# Optional: Create a sample entry
read -p "Would you like to create a sample journal entry? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Creating sample entry..."
    "$BIN_DIR/ai-journal" new "Getting Started with AI Journal" tutorial learning
    print_success "Sample entry created! Use 'ai-journal open latest' to view it."
fi

echo ""
echo "Installation log saved. You can close this window."

# Keep terminal open on macOS when double-clicked
if [ "$0" = "${BASH_SOURCE[0]}" ]; then
    read -p "Press any key to close this window..."
fi
