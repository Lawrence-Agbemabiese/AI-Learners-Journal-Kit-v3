#!/usr/bin/env python3
"""
AI Journal Entry Saver v3.0
Enhanced with AI integration metadata and connoisseurship features.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import re

def get_journal_dir():
    """Get the AI Journal directory path."""
    return Path.home() / "AI-Journal"

def load_index():
    """Load the journal index."""
    index_path = get_journal_dir() / "index.json"
    try:
        with open(index_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Create default index if it doesn't exist
        default_index = {
            "version": "3.0",  # Updated version for AI integration
            "created": datetime.now().isoformat() + "Z",
            "entries": [],
            "tags": {},
            "ai_stats": {  # New AI-specific statistics
                "total_ai_assisted": 0,
                "sources_used": {},
                "avg_quality_rating": 0.0
            },
            "stats": {
                "total_entries": 0,
                "last_modified": datetime.now().isoformat() + "Z"
            }
        }
        save_index(default_index)
        return default_index

def save_index(index_data):
    """Save the journal index."""
    index_path = get_journal_dir() / "index.json"
    index_data["stats"]["last_modified"] = datetime.now().isoformat() + "Z"
    with open(index_path, 'w') as f:
        json.dump(index_data, f, indent=2)

def create_slug(topic):
    """Create a URL-friendly slug from a topic."""
    # Convert to lowercase, replace spaces and special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '', topic.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def create_entry(topic, content=None, tags=None, ai_metadata=None):
    """Create a new journal entry with optional AI metadata."""
    if tags is None:
        tags = []
    
    now = datetime.now()
    slug = create_slug(topic)
    
    # Create entry filename with date and slug
    entry_filename = f"{now.strftime('%Y%m%d')}-{slug}.md"
    
    # Create year/month directory structure
    entry_dir = get_journal_dir() / "entries" / now.strftime('%Y') / now.strftime('%m')
    entry_dir.mkdir(parents=True, exist_ok=True)
    
    entry_path = entry_dir / entry_filename
    
    # Handle duplicate entries intelligently
    if entry_path.exists():
        print(f"Entry already exists: {entry_path}")
        
        # If it's a similar topic, suggest variations
        base_topic = topic.lower()
        variations = [
            topic.replace("what is", "what is an").replace("what is an an", "what is an"),
            topic.replace("what is an", "what is"),
            topic + " detailed",
            topic + " advanced",
            topic.replace("?", " explained?") if "?" in topic else topic + " explained"
        ]
        
        for variation in variations:
            var_slug = create_slug(variation)
            var_filename = f"{now.strftime('%Y%m%d')}-{var_slug}.md"
            var_path = entry_dir / var_filename
            
            if not var_path.exists():
                print(f"✅ Created new entry: {var_path}")
                print(f"📝 Topic: {variation}")
                print(f"🏷️  Tags: {', '.join(tags) if tags else 'untagged'}")
                return create_entry(variation, content, tags, ai_metadata)
        
        return str(entry_path)
    
    # Create enhanced entry content with AI metadata
    content_sections = []
    
    # Header
    content_sections.append(f"# {topic}")
    content_sections.append("")
    
    # Metadata section
    metadata_lines = [
        f"**Date:** {now.strftime('%B %d, %Y')}",
        f"**Time:** {now.strftime('%I:%M %p')}",
        f"**Tags:** {', '.join(tags) if tags else 'untagged'}"
    ]
    
    # Add AI metadata if present
    if ai_metadata:
        if ai_metadata.get('source'):
            metadata_lines.append(f"**AI Source:** {ai_metadata['source']}")
        if ai_metadata.get('quality_rating'):
            metadata_lines.append(f"**Quality Rating:** {ai_metadata['quality_rating']}/10")
        if ai_metadata.get('confidence'):
            metadata_lines.append(f"**Confidence:** {ai_metadata['confidence'].title()}")
        if ai_metadata.get('risk_level'):
            risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}
            emoji = risk_emoji.get(ai_metadata['risk_level'], "")
            metadata_lines.append(f"**Risk Level:** {emoji} {ai_metadata['risk_level'].title()}")
    
    content_sections.extend(metadata_lines)
    content_sections.append("")
    
    # Main content or template
    if content:
        content_sections.append(content)
    else:
        # Default template
        template = """## Key Points
- [Add your key insights here]

## Questions & Answers

[Add your Q&A content here]

## Follow-up Actions
- [ ] [Add any next steps]

---

## Full Session Content

[Add your detailed content here]

---

## Reflection
[Add your thoughts and reflections here]"""
        content_sections.append(template)
    
    entry_content = "\n".join(content_sections)
    
    # Write the entry
    with open(entry_path, 'w') as f:
        f.write(entry_content)
    
    # Update index with enhanced metadata
    index_data = load_index()
    
    entry_record = {
        "id": len(index_data["entries"]) + 1,
        "topic": topic,
        "slug": slug,
        "filename": str(entry_path.relative_to(get_journal_dir())),
        "created": now.isoformat() + "Z",
        "tags": tags,
        "word_count": len(entry_content.split())
    }
    
    # Add AI metadata to entry record
    if ai_metadata:
        entry_record["ai_sources"] = [ai_metadata.get('source', 'unknown')]
        entry_record["quality_rating"] = ai_metadata.get('quality_rating', 0)
        entry_record["confidence"] = ai_metadata.get('confidence', 'medium')
        entry_record["risk_level"] = ai_metadata.get('risk_level', 'low')
        entry_record["verification_status"] = ai_metadata.get('verification_status', 'untested')
        
        # Update AI statistics
        if "ai_stats" not in index_data:
            index_data["ai_stats"] = {
                "total_ai_assisted": 0,
                "sources_used": {},
                "avg_quality_rating": 0.0
            }
        
        index_data["ai_stats"]["total_ai_assisted"] += 1
        source = ai_metadata.get('source', 'unknown')
        if source in index_data["ai_stats"]["sources_used"]:
            index_data["ai_stats"]["sources_used"][source] += 1
        else:
            index_data["ai_stats"]["sources_used"][source] = 1
        
        # Update average quality rating
        total_ai = index_data["ai_stats"]["total_ai_assisted"]
        current_avg = index_data["ai_stats"]["avg_quality_rating"]
        new_rating = ai_metadata.get('quality_rating', 5)
        index_data["ai_stats"]["avg_quality_rating"] = ((current_avg * (total_ai - 1)) + new_rating) / total_ai
    
    index_data["entries"].append(entry_record)
    index_data["stats"]["total_entries"] += 1
    
    # Update tag counts
    for tag in tags:
        if tag in index_data["tags"]:
            index_data["tags"][tag] += 1
        else:
            index_data["tags"][tag] = 1
    
    save_index(index_data)
    
    print(f"✅ Created new entry: {entry_path}")
    print(f"📝 Topic: {topic}")
    print(f"🏷️  Tags: {', '.join(tags) if tags else 'untagged'}")
    
    # Show AI metadata if present
    if ai_metadata:
        if ai_metadata.get('source'):
            print(f"🤖 AI Source: {ai_metadata['source']}")
        if ai_metadata.get('quality_rating'):
            quality_bar = "★" * ai_metadata['quality_rating'] + "☆" * (10 - ai_metadata['quality_rating'])
            print(f"⭐ Quality: {quality_bar} ({ai_metadata['quality_rating']}/10)")
    
    return str(entry_path)

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python entry_saver.py '<topic>' [tags...]")
        print("Example: python entry_saver.py 'Terminal Commands' tmux bash")
        sys.exit(1)
    
    topic = sys.argv[1]
    tags = sys.argv[2:] if len(sys.argv) > 2 else []
    
    # Read content from stdin if available
    content = None
    if not sys.stdin.isatty():
        content = sys.stdin.read().strip()
    
    entry_path = create_entry(topic, content, tags)
    
    # Optionally open the entry in default editor
    if "--open" in sys.argv:
        os.system(f"open '{entry_path}'")

if __name__ == "__main__":
    main()
