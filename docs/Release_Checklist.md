# Release Checklist

Use this checklist for free/beta and paid releases.

## Before Building

- Confirm the working tree is clean or intentionally staged.
- Confirm `README.md` describes the current command set.
- Confirm `CHANGELOG.md` has an entry for the release.
- Confirm `docs/Quick_Start_v3.md` works from a downloaded ZIP.
- Confirm policies are present: `SUPPORT.md`, `PRIVACY.md`, `REFUND_POLICY.md`, `SECURITY.md`.

## Verification

Run:

```bash
python -m pytest -q
python -m black --check --diff scripts tests
python -m isort --check-only --diff scripts tests
python -m flake8 scripts tests --max-line-length=88 --extend-ignore=E203,W503
python -m bandit -r scripts --severity-level medium
python -m pip_audit -r requirements.txt
```

## Build

Create release artifacts:

```bash
python scripts/build_release.py --version v3.0.1
```

Expected outputs:

- `dist/ai-learners-journal-kit-v3.0.1.zip`
- `dist/ai-learners-journal-kit-v3.0.1.tar.gz`
- `dist/SHA256SUMS.txt`
- `dist/release-manifest.json`

## Smoke Test From Artifact

1. Extract the ZIP into a temporary folder.
2. Run the installer for the target platform.
3. Run `ai-journal setup`.
4. Create an entry.
5. Append a note.
6. Search for the note's tag.
7. Open or print the latest entry path.

## GitHub Release

- Attach the ZIP, tar.gz, SHA256SUMS, and manifest.
- Use release notes that match the current feature set.
- Do not claim Claude, Gemini, or compare support unless implemented and tested.

## Paid Storefront

- Upload the same ZIP attached to GitHub Releases.
- Add SHA256 checksum to the product page or receipt email.
- Link to refund, support, and privacy terms.
