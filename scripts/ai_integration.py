#!/usr/bin/env python3
"""Optional OpenAI query and curation workflow for AI Journal."""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List

from entry_saver import create_entry


class AIResponse:
    """Represents an AI response with metadata."""

    def __init__(self, content: str, source: str, review_score: int = 0):
        self.content = content
        self.source = source
        self.review_score = review_score
        self.confidence = "medium"
        self.risk_level = "low"
        self.verification_status = "untested"
        self.user_reflection = ""


class AIIntegration:
    """Main AI integration class."""

    def __init__(self, plain: bool = False):
        self.plain = plain or not self._supports_rich_output()
        self.api_keys = self._load_api_keys()
        self.openai_model = os.getenv("AI_JOURNAL_OPENAI_MODEL", "gpt-4o-mini")
        self.responses: List[AIResponse] = []

    def _supports_rich_output(self) -> bool:
        """Return true when stdout is likely to support Unicode symbols."""
        if os.getenv("AI_JOURNAL_RICH_OUTPUT") == "1":
            return True
        if os.getenv("AI_JOURNAL_PLAIN_OUTPUT") == "1":
            return False
        encoding = (getattr(sys.stdout, "encoding", None) or "").lower()
        return sys.stdout.isatty() and "utf" in encoding

    def _rule(self, width: int = 60) -> str:
        """Return an ASCII divider."""
        return "-" * width

    def _load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment or config file."""
        keys = {}

        # Try environment variables first
        if os.getenv("OPENAI_API_KEY"):
            keys["openai"] = os.getenv("OPENAI_API_KEY")
        if os.getenv("ANTHROPIC_API_KEY"):
            keys["anthropic"] = os.getenv("ANTHROPIC_API_KEY")
        if os.getenv("GEMINI_API_KEY"):
            keys["gemini"] = os.getenv("GEMINI_API_KEY")

        # Try config file
        config_path = Path.home() / ".ai-journal-config.json"
        if config_path.exists():
            try:
                with open(config_path) as f:
                    config = json.load(f)
                    keys.update(config.get("api_keys", {}))
            except Exception as exc:
                print(
                    f"Warning: Could not read {config_path}: {exc}",
                    file=sys.stderr,
                )
                print(
                    "The app will continue with environment variables only.",
                    file=sys.stderr,
                )

        return keys

    def _query_chatgpt(self, question: str) -> AIResponse:
        """Query ChatGPT via OpenAI API."""
        if "openai" not in self.api_keys:
            return AIResponse(
                "OpenAI API key not configured. Set OPENAI_API_KEY "
                "environment variable.",
                "error",
            )

        try:
            try:
                import openai
            except ImportError:
                return AIResponse(
                    "OpenAI integration requires the optional 'openai' package. "
                    "Install it with: python -m pip install -r requirements.txt",
                    "error",
                )

            client = openai.OpenAI(api_key=self.api_keys["openai"])

            response = client.chat.completions.create(
                model=self.openai_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant providing clear, "
                        "accurate explanations for learning purposes. Be concise "
                        "but thorough.",
                    },
                    {"role": "user", "content": question},
                ],
                max_tokens=800,
                temperature=0.7,
            )

            content = response.choices[0].message.content
            review_score = self._assess_response_completeness(content, question)

            return AIResponse(content, "ChatGPT", review_score)

        except Exception as e:
            return AIResponse(f"ChatGPT Error: {str(e)}", "error")

    def _assess_response_completeness(self, content: str, question: str) -> int:
        """Estimate response completeness, not factual correctness."""
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
        if content.count("\n") > 2 or any(
            marker in content for marker in ["1.", "2.", "-", "*"]
        ):
            score += 1

        # Question-specific scoring
        if "?" in question and "?" in content:  # Addresses questions directly
            score += 1

        return max(1, min(10, score))

    def _detect_risk_level(self, question: str, content: str) -> str:
        """Detect risk level of the topic."""
        high_risk_keywords = [
            "security",
            "password",
            "crypto",
            "financial",
            "medical",
            "legal",
        ]
        medium_risk_keywords = ["production", "deploy", "server", "database", "api"]

        text = (question + " " + content).lower()

        if any(keyword in text for keyword in high_risk_keywords):
            return "high"
        elif any(keyword in text for keyword in medium_risk_keywords):
            return "medium"
        else:
            return "low"

    def _display_response(self, response: AIResponse, question: str) -> None:
        """Display AI response with review indicators."""
        print(f"\n{response.source} Response:".strip())
        print(self._rule())
        print(response.content)
        print(self._rule())

        if response.source != "error" and response.source != "placeholder":
            completeness_bar = "#" * response.review_score + "-" * (
                10 - response.review_score
            )
            print(f"Review Score: {completeness_bar} " f"({response.review_score}/10)")
            print(
                "This score estimates structure and completeness, "
                "not factual correctness."
            )

            # Risk assessment
            response.risk_level = self._detect_risk_level(question, response.content)
            risk_label = {"low": "LOW", "medium": "MEDIUM", "high": "HIGH"}
            if not self.plain:
                risk_label = {"low": "LOW", "medium": "MEDIUM", "high": "HIGH"}
            print(
                f"Risk Level: {risk_label[response.risk_level]} "
                f"{response.risk_level.title()}"
            )

            if response.risk_level == "high":
                print(
                    "Warning: High-risk topic detected. "
                    "Verify with a trusted expert or source before relying on it."
                )
        print()

    def _show_curation_menu(self) -> str:
        """Show interactive curation menu."""
        if self.plain:
            print("What would you like to do?")
            print("/save    - Save to journal")
            print("/edit    - Edit before save")
            print("/verify  - Add verification")
            print("/reflect - Add reflection")
            print("/discard - Don't save")
        else:
            print("What would you like to do?")
            print("/save    - Save to journal")
            print("/edit    - Edit before save")
            print("/verify  - Add verification")
            print("/reflect - Add reflection")
            print("/discard - Don't save")

        while True:
            try:
                choice = input("\nYour choice: ").strip().lower()
                if choice.startswith("/"):
                    return choice
                else:
                    print("Please enter a command starting with / (e.g., /save)")
            except (KeyboardInterrupt, EOFError):
                return "/discard"

    def _handle_edit_response(self, response: AIResponse) -> AIResponse:
        """Allow user to edit the response."""
        print("\nEdit Response (press Enter on empty line to finish):")
        print("Current content:")
        print(self._rule(40))
        print(response.content)
        print(self._rule(40))
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
            response.review_score = max(
                response.review_score, 7
            )  # Edited content has been reviewed by the user.
            print("Response updated!")

        return response

    def _handle_verification(self, response: AIResponse) -> AIResponse:
        """Add verification metadata."""
        print("\nVerification Notes:")
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
        print("\nCritical Thinking Reflection:")

        if response.risk_level == "high":
            print("Warning: High-risk topic - critical evaluation recommended!")
            print("Consider these questions:")
            print("- What could go wrong with this approach?")
            print("- How would you verify this information?")
            print("- What's missing from this explanation?")

        try:
            reflection = input("Your reflection (optional): ").strip()
            if reflection:
                response.user_reflection = reflection
                print("Reflection added!")
        except (KeyboardInterrupt, EOFError):
            pass

        return response

    def _save_to_journal(
        self, response: AIResponse, question: str, tags: List[str] = None
    ) -> None:
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
            f"**Review Score:** {response.review_score}/10",
            "**Review Score Note:** This estimates structure and completeness, "
            "not factual correctness.",
            f"**Confidence:** {response.confidence.title()}",
            f"**Risk Level:** {response.risk_level.title()}",
            "",
            "## AI Response",
            "",
            response.content,
            "",
        ]

        if response.user_reflection:
            content_parts.extend(["## My Reflection", "", response.user_reflection, ""])

        if response.verification_status != "untested":
            content_parts.extend(
                ["## Verification", "", f"Status: {response.verification_status}", ""]
            )

        content = "\n".join(content_parts)

        ai_metadata = {
            "source": response.source,
            "quality_rating": response.review_score,
            "confidence": response.confidence,
            "risk_level": response.risk_level,
            "verification_status": response.verification_status,
        }
        create_entry(question, content, tags, ai_metadata=ai_metadata)

        print("Saved to journal with AI metadata!")

    def ask_ai(self, question: str, source: str = "chatgpt") -> None:
        """Main AI query interface."""
        print(f"Querying {source.title()}...")

        # Get AI response
        if source == "chatgpt":
            response = self._query_chatgpt(question)
        else:
            response = AIResponse(f"Unknown AI source: {source}", "error")

        # Display response
        self._display_response(response, question)

        # Handle errors
        if response.source == "error":
            return
        elif response.source == "placeholder":
            print("Would you like to create a manual entry for this question? (y/n)")
            try:
                if input().strip().lower().startswith("y"):
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
            elif choice == "/discard":
                print("Response discarded.")
                break
            else:
                print(
                    "Unknown command. Try /save, /edit, /verify, /reflect, "
                    "or /discard"
                )


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="AI Journal Integration")
    parser.add_argument("question", help="Question to ask the AI")
    parser.add_argument(
        "--source",
        default="chatgpt",
        choices=["chatgpt"],
        help="AI source to query",
    )
    parser.add_argument(
        "--guided", action="store_true", help="Beginner mode with extra guidance"
    )
    parser.add_argument(
        "--expert", action="store_true", help="Expert mode with minimal prompts"
    )
    parser.add_argument("--topic", help="Topic category for risk assessment")
    parser.add_argument("--plain", action="store_true", help="Use plain ASCII output")

    args = parser.parse_args()

    # Check for API configuration
    ai = AIIntegration(plain=args.plain)
    if not ai.api_keys:
        print("Warning: No AI API keys configured!")
        print("\nTo use AI integration:")
        print("1. Set environment variable: export OPENAI_API_KEY='your-key-here'")
        print("2. Or create ~/.ai-journal-config.json with your API keys")
        print("\nFor now, creating a manual entry...")
        create_entry(args.question, "", ["question", "manual"])
        return

    # Main AI query
    ai.ask_ai(args.question, args.source)


if __name__ == "__main__":
    main()
