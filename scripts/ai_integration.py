#!/usr/bin/env python3
"""
AI Journal Integration - AI Query and Curation System
Implements the seamless AI learning workflow with connoisseurship features.
"""

import json
import os
import sys
import argparse
import openai
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

# Import existing modules
sys.path.append(str(Path(__file__).parent))
from entry_saver import create_entry, load_index, save_index

class AIResponse:
    """Represents an AI response with metadata."""
    
    def __init__(self, content: str, source: str, quality_score: int = 0):
        self.content = content
        self.source = source
        self.quality_score = quality_score
        self.confidence = "medium"
        self.risk_level = "low"
        self.verification_status = "untested"
        self.user_reflection = ""
        
class AIIntegration:
    """Main AI integration class."""
    
    def __init__(self):
        self.api_keys = self._load_api_keys()
        self.responses: List[AIResponse] = []
        
    def _load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment or config file."""
        keys = {}
        
        # Try environment variables first
        if os.getenv('OPENAI_API_KEY'):
            keys['openai'] = os.getenv('OPENAI_API_KEY')
        if os.getenv('ANTHROPIC_API_KEY'):
            keys['anthropic'] = os.getenv('ANTHROPIC_API_KEY')
        if os.getenv('GEMINI_API_KEY'):
            keys['gemini'] = os.getenv('GEMINI_API_KEY')
            
        # Try config file
        config_path = Path.home() / '.ai-journal-config.json'
        if config_path.exists():
            try:
                with open(config_path) as f:
                    config = json.load(f)
                    keys.update(config.get('api_keys', {}))
            except Exception:
                pass
                
        return keys
    
    def _query_chatgpt(self, question: str) -> AIResponse:
        """Query ChatGPT via OpenAI API."""
        if 'openai' not in self.api_keys:
            return AIResponse("❌ OpenAI API key not configured. Set OPENAI_API_KEY environment variable.", "error")
            
        try:
            client = openai.OpenAI(api_key=self.api_keys['openai'])
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use GPT-3.5 for cost efficiency
                messages=[
                    {"role": "system", "content": "You are a helpful assistant providing clear, accurate explanations for learning purposes. Be concise but thorough."},
                    {"role": "user", "content": question}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            content = response.choices[0].message.content
            quality_score = self._assess_response_quality(content, question)
            
            return AIResponse(content, "ChatGPT", quality_score)
            
        except Exception as e:
            return AIResponse(f"❌ ChatGPT Error: {str(e)}", "error")
    
    def _query_claude(self, question: str) -> AIResponse:
        """Query Claude via Anthropic API."""
        # Placeholder for Claude integration
        return AIResponse("🚧 Claude integration coming soon. Use ChatGPT for now.", "placeholder")
    
    def _query_gemini(self, question: str) -> AIResponse:
        """Query Gemini via Google API."""
        # Placeholder for Gemini integration  
        return AIResponse("🚧 Gemini integration coming soon. Use ChatGPT for now.", "placeholder")
    
    def _assess_response_quality(self, content: str, question: str) -> int:
        """Basic quality assessment algorithm."""
        score = 5  # Start with middle score
        
        # Length check
        if len(content) < 50:
            score -= 2
        elif len(content) > 300:
            score += 1
            
        # Has examples
        if "example" in content.lower() or "for instance" in content.lower():
            score += 1
            
        # Has structure
        if content.count('\n') > 2 or any(marker in content for marker in ['1.', '2.', '-', '*']):
            score += 1
            
        # Question-specific scoring
        if "?" in question and "?" in content:  # Addresses questions directly
            score += 1
            
        return max(1, min(10, score))
    
    def _detect_risk_level(self, question: str, content: str) -> str:
        """Detect risk level of the topic."""
        high_risk_keywords = ['security', 'password', 'crypto', 'financial', 'medical', 'legal']
        medium_risk_keywords = ['production', 'deploy', 'server', 'database', 'api']
        
        text = (question + " " + content).lower()
        
        if any(keyword in text for keyword in high_risk_keywords):
            return "high"
        elif any(keyword in text for keyword in medium_risk_keywords):
            return "medium"
        else:
            return "low"
    
    def _display_response(self, response: AIResponse, question: str) -> None:
        """Display AI response with quality indicators."""
        print(f"\n🤖 {response.source} Response:")
        print("─" * 60)
        print(response.content)
        print("─" * 60)
        
        if response.source != "error" and response.source != "placeholder":
            # Quality bar
            quality_bar = "█" * response.quality_score + "░" * (10 - response.quality_score)
            print(f"📊 Response Quality: {quality_bar} ({response.quality_score}/10)")
            
            # Risk assessment
            response.risk_level = self._detect_risk_level(question, response.content)
            risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}
            print(f"🔍 Risk Level: {risk_emoji[response.risk_level]} {response.risk_level.title()}")
            
            if response.risk_level == "high":
                print("⚠️  High-Risk Topic Detected: Consider expert verification")
        print()
    
    def _show_curation_menu(self) -> str:
        """Show interactive curation menu."""
        print("┌─ What would you like to do? ─┐")
        print("│ /save     - Save to journal   │")
        print("│ /edit     - Edit before save  │")
        print("│ /compare  - Ask another AI    │")
        print("│ /verify   - Add verification  │")
        print("│ /reflect  - Add reflection    │")
        print("│ /discard  - Don't save        │")
        print("└─────────────────────────────┘")
        
        while True:
            try:
                choice = input("\nYour choice: ").strip().lower()
                if choice.startswith('/'):
                    return choice
                else:
                    print("Please enter a command starting with / (e.g., /save)")
            except (KeyboardInterrupt, EOFError):
                return "/discard"
    
    def _handle_edit_response(self, response: AIResponse) -> AIResponse:
        """Allow user to edit the response."""
        print("\n📝 Edit Response (press Enter on empty line to finish):")
        print("Current content:")
        print("─" * 40)
        print(response.content)
        print("─" * 40)
        print("Enter your edited version:")
        
        lines = []
        while True:
            try:
                line = input()
                if line == "" and len(lines) > 0:
                    break
                lines.append(line)
            except (KeyboardInterrupt, EOFError):
                break
                
        if lines:
            edited_content = "\n".join(lines)
            response.content = edited_content
            response.quality_score = max(response.quality_score, 7)  # Boost quality for edited content
            print("✅ Response updated!")
        
        return response
    
    def _handle_verification(self, response: AIResponse) -> AIResponse:
        """Add verification metadata."""
        print("\n🔍 Verification Notes:")
        print("How confident are you in this information?")
        print("1. High - Ready to use")
        print("2. Medium - Needs testing")
        print("3. Low - Learning only")
        
        try:
            choice = input("Enter choice (1-3): ").strip()
            confidence_map = {"1": "high", "2": "medium", "3": "low"}
            response.confidence = confidence_map.get(choice, "medium")
            
            verification = input("Verification notes (optional): ").strip()
            if verification:
                response.verification_status = verification
                
        except (KeyboardInterrupt, EOFError):
            pass
            
        return response
    
    def _handle_reflection(self, response: AIResponse, question: str) -> AIResponse:
        """Add critical thinking reflection."""
        print("\n🤔 Critical Thinking Reflection:")
        
        if response.risk_level == "high":
            print("⚠️  High-risk topic - critical evaluation recommended!")
            print("Consider these questions:")
            print("• What could go wrong with this approach?")
            print("• How would you verify this information?")
            print("• What's missing from this explanation?")
        
        try:
            reflection = input("Your reflection (optional): ").strip()
            if reflection:
                response.user_reflection = reflection
                print("✅ Reflection added!")
        except (KeyboardInterrupt, EOFError):
            pass
            
        return response
    
    def _save_to_journal(self, response: AIResponse, question: str, tags: List[str] = None) -> None:
        """Save the curated response to journal."""
        if tags is None:
            tags = ["question", "ai-assisted"]
            
        # Add source-specific tag
        if response.source.lower() not in ["error", "placeholder"]:
            tags.append(response.source.lower())
            
        # Add risk-level tag for high-risk content
        if response.risk_level == "high":
            tags.append("high-risk")
            
        # Create structured content
        content_parts = [
            f"**Source:** {response.source}",
            f"**Quality:** {response.quality_score}/10",
            f"**Confidence:** {response.confidence.title()}",
            f"**Risk Level:** {response.risk_level.title()}",
            "",
            "## AI Response",
            "",
            response.content,
            ""
        ]
        
        if response.user_reflection:
            content_parts.extend([
                "## My Reflection",
                "",
                response.user_reflection,
                ""
            ])
        
        if response.verification_status != "untested":
            content_parts.extend([
                "## Verification",
                "",
                f"Status: {response.verification_status}",
                ""
            ])
        
        content = "\n".join(content_parts)
        
        # Create entry
        entry_path = create_entry(question, content, tags)
        
        # Update index with AI metadata
        try:
            index_data = load_index()
            if index_data["entries"]:
                latest_entry = index_data["entries"][-1]
                latest_entry["ai_sources"] = [response.source]
                latest_entry["quality_rating"] = response.quality_score
                latest_entry["confidence"] = response.confidence
                latest_entry["risk_level"] = response.risk_level
                save_index(index_data)
        except Exception:
            pass  # Continue even if metadata update fails
            
        print(f"✅ Saved to journal with AI metadata!")
    
    def ask_ai(self, question: str, source: str = "chatgpt", compare_mode: bool = False) -> None:
        """Main AI query interface."""
        print(f"🤖 Querying {source.title()}...")
        
        # Get AI response
        if source == "chatgpt":
            response = self._query_chatgpt(question)
        elif source == "claude":
            response = self._query_claude(question)
        elif source == "gemini":
            response = self._query_gemini(question)
        else:
            response = AIResponse(f"❌ Unknown AI source: {source}", "error")
        
        # Display response
        self._display_response(response, question)
        
        # Handle errors
        if response.source == "error":
            return
        elif response.source == "placeholder":
            print("Would you like to create a manual entry for this question? (y/n)")
            try:
                if input().strip().lower().startswith('y'):
                    create_entry(question, "", ["question", "manual"])
            except (KeyboardInterrupt, EOFError):
                pass
            return
        
        # Interactive curation
        while True:
            choice = self._show_curation_menu()
            
            if choice == "/save":
                self._save_to_journal(response, question)
                break
            elif choice == "/edit":
                response = self._handle_edit_response(response)
                self._display_response(response, question)
            elif choice == "/verify":
                response = self._handle_verification(response)
            elif choice == "/reflect":
                response = self._handle_reflection(response, question)
            elif choice == "/compare":
                print("\n🔄 Comparison mode coming in next update!")
                print("For now, you can ask the same question with --source claude")
            elif choice == "/discard":
                print("❌ Response discarded.")
                break
            else:
                print("Unknown command. Try /save, /edit, /verify, /reflect, or /discard")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='AI Journal Integration')
    parser.add_argument('question', help='Question to ask the AI')
    parser.add_argument('--source', default='chatgpt', choices=['chatgpt', 'claude', 'gemini'], 
                       help='AI source to query')
    parser.add_argument('--compare', help='Compare multiple sources (comma-separated)')
    parser.add_argument('--guided', action='store_true', help='Beginner mode with extra guidance')
    parser.add_argument('--expert', action='store_true', help='Expert mode with minimal prompts')
    parser.add_argument('--topic', help='Topic category for risk assessment')
    
    args = parser.parse_args()
    
    # Check for API configuration
    ai = AIIntegration()
    if not ai.api_keys:
        print("⚠️  No AI API keys configured!")
        print("\nTo use AI integration:")
        print("1. Set environment variable: export OPENAI_API_KEY='your-key-here'")
        print("2. Or create ~/.ai-journal-config.json with your API keys")
        print("\nFor now, creating a manual entry...")
        create_entry(args.question, "", ["question", "manual"])
        return
    
    # Handle comparison mode
    if args.compare:
        print("🔄 Multi-source comparison coming soon!")
        print("For now, using single source mode.")
        
    # Main AI query
    ai.ask_ai(args.question, args.source)

if __name__ == "__main__":
    main()
