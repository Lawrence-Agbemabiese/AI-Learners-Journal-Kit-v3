# Release Notes — v3.4.0 (2026-07-23)

## What's new for learners

### Add to today — now it really is today

The **Add to today** button (and `ai-journal append`) now always lands your note in *today's* entry. If you haven't written anything yet today, a fresh "Notes - <date>" entry is started for you automatically — a quick thought never gets lost, and it never gets buried in an entry from three days ago.

You can also aim a note at any entry:

- **Web:** the "Add to today" dialog has an *Add to which entry?* picker listing your recent entries.
- **CLI:** `ai-journal append today "..."`, or target `yesterday`, a date like `2026-07-23`, an entry number, or a topic name.

### Delete entries — safely

You can now delete an entry from the web UI (open it, click **Delete**) or the terminal (`ai-journal delete <entry>`). Deletion is *soft by default*: the note moves to a visible `trash` folder inside your journal, with a `trash-index.json` log that makes restoring easy. Search and stats update immediately.

Truly permanent deletion exists only in the terminal, on purpose:

```bash
ai-journal delete <entry> --purge   # asks you to type DELETE to confirm
```

## Fixes

- Saving the same topic twice in one day now produces "Topic (2)" instead of oddly reworded titles — and a colliding save can no longer be silently discarded.
- The web UI's "Make it simpler" button no longer stacks its phrasing onto the question when clicked more than once.
- Installers now ship the browser interface with the installed copy, so `ai-journal web` works after installation (not just from the unzipped download).
- Notes containing accents, emoji, or non-Latin scripts now save reliably on Windows (all files are read and written as UTF-8).
- An empty or symbols-only topic no longer creates a nameless file; it becomes "Untitled entry".
- `ai-journal import` no longer accepts out-of-range session numbers.
- `ai-journal backup` no longer includes rebuildable search-database sidecar files.
- The beginner menu returns to the menu after a failed action instead of quitting.

## Upgrading an existing install

Re-run the installer from the new bundle (`installers/Installer.command` on macOS, `installers/Installer.bat` on Windows). Your entries and index are never overwritten; only the app scripts, web interface, and launchers are refreshed.
