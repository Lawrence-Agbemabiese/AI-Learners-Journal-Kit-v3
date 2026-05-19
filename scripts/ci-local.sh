#!/bin/bash
set -euo pipefail

# CI Local Reproduction Script
# Reproduces the exact checks that are failing in GitHub Actions

echo "🔍 CI/CD Local Reproduction Script"
echo "=================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print section headers
print_section() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE} $1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Exit on first failure
EXIT_CODE=0

print_section "📚 DOCUMENTATION CHECK"

echo "Testing tools: markdown-link-check, markdownlint-cli2"
echo ""

# Test 1: Markdown Link Check
echo -e "${YELLOW}🔗 Running markdown link check...${NC}"
if command_exists npx; then
    if npx markdown-link-check README.md --config .github/markdown-link-check-config.json; then
        echo -e "${GREEN}✅ Markdown links OK${NC}"
    else
        echo -e "${RED}❌ Markdown links FAILED${NC}"
        echo "First failing lines:"
        npx markdown-link-check README.md --config .github/markdown-link-check-config.json 2>&1 | grep -E "(✖|ERROR)" | head -3
        EXIT_CODE=1
    fi
else
    echo -e "${YELLOW}⚠️  npx not available, skipping markdown-link-check${NC}"
fi

echo ""

# Test 2: Markdownlint
echo -e "${YELLOW}📝 Running markdownlint...${NC}"
if command_exists npx; then
    if npx markdownlint-cli2 "**/*.md"; then
        echo -e "${GREEN}✅ Markdownlint OK${NC}"
    else
        echo -e "${RED}❌ Markdownlint FAILED${NC}"
        echo "First failing lines:"
        npx markdownlint-cli2 "**/*.md" 2>&1 | head -5
        EXIT_CODE=1
    fi
else
    echo -e "${YELLOW}⚠️  npx not available, skipping markdownlint${NC}"
fi

print_section "🔒 SECURITY SCAN"

echo "Testing tools: bandit, pip-audit"
echo ""

# Test 3: Bandit Security Scanner
echo -e "${YELLOW}🛡️  Running Bandit security scan...${NC}"
if command_exists bandit; then
    # Test the exact logic from the failing workflow
    echo "Running scan for medium and high severity issues only..."
    bandit -r scripts/ --severity-level medium -f json -o bandit-medium-high.json --exit-zero

    # Check results using the same Python logic as the workflow
    ISSUE_COUNT=$(python3 -c "
import json
try:
    with open('bandit-medium-high.json', 'r') as f:
        data = json.load(f)
    print(len(data['results']))
except:
    print('0')
")

    echo "Medium/High severity issues found: $ISSUE_COUNT"

    if [ "$ISSUE_COUNT" -eq "0" ]; then
        echo -e "${GREEN}✅ No medium/high severity security issues found${NC}"
    else
        echo -e "${RED}❌ Found $ISSUE_COUNT medium/high severity security issues!${NC}"
        echo "First failing lines:"
        bandit -r scripts/ --severity-level medium | head -10
        EXIT_CODE=1
    fi

    # Clean up
    rm -f bandit-medium-high.json
elif command_exists python3; then
    echo "Installing bandit..."
    python3 -m pip install bandit --user --quiet
    # Retry the test
    echo "Retrying bandit scan..."
    bandit -r scripts/ --severity-level medium -f json -o bandit-medium-high.json --exit-zero
    ISSUE_COUNT=$(python3 -c "
import json
try:
    with open('bandit-medium-high.json', 'r') as f:
        data = json.load(f)
    print(len(data['results']))
except:
    print('0')
")

    if [ "$ISSUE_COUNT" -eq "0" ]; then
        echo -e "${GREEN}✅ Bandit security scan passed${NC}"
    else
        echo -e "${RED}❌ Bandit found $ISSUE_COUNT medium/high severity issues${NC}"
        EXIT_CODE=1
    fi
    rm -f bandit-medium-high.json
else
    echo -e "${YELLOW}⚠️  Python3 not available, skipping bandit${NC}"
fi

echo ""

# Test 4: Dependency vulnerability check
echo -e "${YELLOW}🔍 Running dependency vulnerability check...${NC}"
if command_exists python3; then
    if python3 -m pip list | grep -q pip-audit; then
        echo "pip-audit already installed"
    else
        echo "Installing pip-audit..."
        python3 -m pip install pip-audit --user --quiet
    fi

    if python3 -m pip_audit -r requirements.txt; then
        echo -e "${GREEN}✅ Dependency vulnerability check passed${NC}"
    else
        echo -e "${RED}❌ Dependency vulnerability check failed${NC}"
        EXIT_CODE=1
    fi
else
    echo -e "${YELLOW}⚠️  Python3 not available, skipping pip-audit${NC}"
fi

print_section "🧪 BEHAVIORAL TESTS"

if command_exists python3; then
    if ! python3 -m pytest --version >/dev/null 2>&1; then
        echo "Installing pytest..."
        python3 -m pip install pytest --user --quiet
    fi

    if python3 -m pytest -q; then
        echo -e "${GREEN}✅ Behavioral tests passed${NC}"
    else
        echo -e "${RED}❌ Behavioral tests failed${NC}"
        EXIT_CODE=1
    fi
else
    echo -e "${YELLOW}⚠️  Python3 not available, skipping pytest${NC}"
fi

print_section "📊 RESULTS SUMMARY"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}🎉 All checks passed!${NC}"
else
    echo -e "${RED}❌ Some checks failed (exit code: $EXIT_CODE)${NC}"
    echo ""
    echo -e "${YELLOW}💡 Next steps:${NC}"
    echo "1. Fix the specific issues reported above"
    echo "2. Run this script again to verify fixes"
    echo "3. Commit and push to test on GitHub Actions"
fi

echo ""
exit $EXIT_CODE
