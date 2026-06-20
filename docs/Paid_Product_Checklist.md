# Paid Product Checklist

Use this checklist before publishing a paid digital product.

## Product Truth

- README describes only features that exist in the current release.
- Release notes do not advertise unsupported multi-AI comparison.
- Screenshots and sales copy match the current beginner menu and command set.
- Product page explains that Python 3.9 or newer is required.
- Product page explains that OpenAI usage is optional and requires the customer's own API key.

## Package

- Release ZIP was created from a clean working tree.
- ZIP includes installers, scripts, launchers, docs, demo content, license, and policies.
- ZIP excludes `.git`, virtual environments, caches, local journals, and test output.
- SHA256 checksums are generated.
- Package was installed on a clean macOS or Linux test account.
- Package was smoke-tested on Windows before paid launch.

## Storefront

- Product title and subtitle are specific and current.
- Refund policy is visible.
- Support channel and response expectation are visible.
- Privacy summary is visible.
- Download file is the release ZIP, not a GitHub auto-generated source archive.
- Version number is shown on the storefront.

## Support Readiness

- `SUPPORT.md` is included in the package.
- Known setup issues have short canned responses.
- A non-sensitive sample journal entry is available for troubleshooting.
- The support workflow tells users not to share API keys.

## Legal And Trust

- `LICENSE` is included.
- `PRIVACY.md` is included.
- `REFUND_POLICY.md` is included.
- `SECURITY.md` is included.
- The product page avoids guarantees about AI factual accuracy.

## Launch Gate

Do not publish a paid release unless:

- Local tests pass.
- CI passes on the release commit.
- The release artifact exists.
- Release notes match the artifact.
- A clean install smoke test passes from the artifact.
