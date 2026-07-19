# Paid Product Checklist

Use this checklist before publishing a paid digital product.

## Novice-first onboarding

- The product ZIP contains `START_HERE.md`.
- The ZIP contains `START HERE - AI Journal.command`.
- The ZIP contains `START HERE - AI Journal.bat`.
- `README.md` leads with the browser interface, not Terminal.
- `README.txt` gives the same browser-first instructions.
- `docs/Quick_Start_v3.md` assumes no coding knowledge.
- AI setup is explained through **Ask the Guide → Manage AI**.
- Terminal commands are labeled advanced or optional.
- A clean Mac user can reach the browser UI without reading command-line instructions.
- A clean Windows user can reach the browser UI without opening Command Prompt manually.

## Product truth

- README describes only features in the current release.
- Screenshots match the current browser UI.
- Sales copy does not promise bundled API access.
- Product page explains that AI providers may require the customer's own key and usage credits.
- Product page explains that notes are stored locally.
- Product page explains that the local launcher opens a browser interface.

## Package

- Release archive was created with `scripts/build_release.py`.
- Do not upload GitHub's automatic source archive to a storefront.
- ZIP includes launchers, web UI, scripts, docs, support files, license, and policies.
- ZIP excludes `.git`, virtual environments, caches, local journals, secrets, and test output.
- ZIP excludes internal strategy and agent folders (`growth/`, `.claude/`).
- Session import is described as Claude Code-only and optional; no other tools are advertised.
- SHA256 checksums are generated.
- `python3 scripts/verify_customer_package.py <release.zip>` passes.
- Package was tested after downloading the exact storefront file.

## Storefront

- The uploaded file is the versioned customer release ZIP.
- Product description begins with “No coding required” or equivalent.
- The first instruction says to double-click the START HERE launcher.
- At least one current browser-interface screenshot is shown.
- Version number is visible.
- Support, refund, privacy, and license information are visible.
- Download instructions do not point customers to GitHub unless intended.

## Delivery test

For every platform—Gumroad or any future store:

1. Upload the versioned release ZIP.
2. Purchase or download it through a test customer account.
3. Compare its SHA256 hash with `dist/SHA256SUMS.txt`.
4. Extract it into a new folder.
5. Confirm the START HERE files are visible at the top level.
6. Launch the browser UI.
7. Create a test entry.
8. Ask an offline or configured AI question.
9. Confirm no developer files or private journal data are included.

## Support readiness

- `SUPPORT.md` is included.
- Known setup issues have short canned responses.
- Support instructions tell users not to share API keys.
- A current screenshot of the home screen is available for support.

## Launch gate

Do not publish unless:

- Local tests pass.
- CI passes.
- Customer ZIP passes `verify_customer_package.py`.
- A clean install succeeds from the exact ZIP uploaded to the store.
- Store listing and screenshots match the included version.
