# Security Policy

## Supported Versions

Security fixes apply to the latest published release only.

## Reporting a Vulnerability

Do not post API keys, private journal entries, or exploit details in a public issue.

Report security concerns through the private contact channel listed on the paid storefront or by opening a GitHub issue that describes the general area without sensitive details.

Include:

- Version or commit SHA.
- Operating system.
- Python version.
- Reproduction steps using non-sensitive sample data.
- Whether the issue affects local files, installation, optional API use, or release packaging.

## Security Model

AI Learner's Journal Kit is local-first software. The core app reads and writes files in the configured journal directory.

The optional AI workflow sends prompts to OpenAI only when the user configures an API key and runs `ai-journal ask`.

## Secret Handling

Users should store API keys in environment variables or a local config file and should never commit keys to this repository or share keys in screenshots.

The release process should never package local journals, `.env` files, virtual environments, `.pytest_cache`, or generated test directories.

## Dependency Checks

Before paid release, run:

```bash
python -m pip install -r requirements-dev.txt
pip-audit -r requirements.txt
bandit -r scripts/ --severity-level medium
```
