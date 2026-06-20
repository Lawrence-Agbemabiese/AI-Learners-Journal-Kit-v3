# Privacy Policy

AI Learner's Journal Kit is local-first software. The core journal features create and edit Markdown files on the user's computer and do not send journal entries to the project owner.

## Data Stored Locally

The app stores these files in the user's journal folder:

- Markdown journal entries.
- `index.json` metadata for search and listing.
- Optional copied scripts and launchers installed by the setup scripts.

Default locations:

- macOS/Linux: `~/AI-Journal`
- Windows: `%USERPROFILE%\AI-Journal`

## Optional AI Requests

The `ai-journal ask` command is optional. It runs only when the user starts it.

When an OpenAI API key is configured, the question entered by the user is sent to OpenAI's API. OpenAI's handling of that request is governed by OpenAI's own terms and privacy policies.

The project owner does not receive or store the user's prompts, API key, responses, or journal entries.

## API Keys

API keys are read from environment variables or an optional local config file. Users should not share API keys in workshop chat, screenshots, support tickets, or journal examples.

Supported environment variable:

```bash
OPENAI_API_KEY
```

The code also checks for older optional variables used during development, but the current documented AI workflow uses OpenAI only.

## Workshop Data Guidance

Workshop facilitators should ask attendees to use sample topics or non-sensitive learning notes during training. Attendees should not paste private, medical, legal, financial, employment, school, or client-confidential information into the optional AI workflow.

## Support Data

If a user asks for support, they may choose to share logs, screenshots, error messages, or sample journal files. Users should remove personal information and API keys before sharing support material.

## Data Deletion

Users can delete the local journal folder at any time. This removes local entries and metadata created by the app.

Deleting local files does not delete data that a user separately sent to OpenAI or shared through support channels.
