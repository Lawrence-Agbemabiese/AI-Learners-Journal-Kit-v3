# Storefront Distribution Checklist

This checklist ensures that Gumroad and future platforms deliver the novice-friendly browser version.

## Canonical customer artifact

The only customer download should be the versioned ZIP built by:

```bash
python3 scripts/build_release.py --version vX.Y.Z
```

Do not use GitHub's automatically generated “Source code (zip)” file. It is not the customer-tested artifact.

## Files that must be visible after extraction

- `START HERE - AI Journal.command`
- `START HERE - AI Journal.bat`
- `START_HERE.md`
- `README.txt`
- `docs/Quick_Start_v3.md`

## Verify the archive

```bash
python3 scripts/verify_customer_package.py dist/ai-learners-journal-kit-vX.Y.Z.zip
```

The command must finish with:

```text
Customer package verification passed.
```

## Gumroad

1. Open the product's Content or Files area.
2. Remove obsolete ZIPs or label them clearly as old versions.
3. Upload the new versioned release ZIP.
4. Put the version number in the filename and product update note.
5. Add the text from `docs/Storefront_Copy_Template.md`.
6. Add current screenshots of:
   - the browser home screen,
   - Ask the Guide,
   - Manage AI.
7. Use a test purchase or complimentary download.
8. Verify the downloaded file with the package checker.
9. Confirm the customer sees START HERE immediately after extraction.

## Future platforms

Repeat the same procedure on Payhip, Lemon Squeezy, Shopify, Etsy digital delivery, or another platform. The platform may change, but the canonical ZIP and verification steps do not.

## Release record

For each upload, record:

- platform,
- product name,
- version,
- upload date,
- exact ZIP filename,
- SHA256,
- test-download result,
- tester name,
- screenshots updated: yes/no.
