---
aliases: [Scoped Apps, Scoped Applications]
area: concept
tags: [concept, scoped-app, packaging]
---
Scoped app structure, namespacing (`x_vendor_appname`), update-set packaging, cross-scope access.

## Sources
- [[capacity-planner]] — real scoped app (`x_u4bsh_capmgmt`), built with Fluent/now-sdk.
- `Notion/ServiceNow/Applications/` — Anonymize Data, Update Set Mover, "Update sets - Full Applications".
- `ServiceNowOfficialDocs/application-development/servicenow-sdk/` — official SDK/local-dev tooling reference.

## now-sdk local dev gotcha (zsh + nvm)
`now-sdk` uses `#!/usr/bin/env node` — resolves whichever `node` is first on `$PATH`. If nvm is only loaded in `~/.bashrc` (not `~/.zshrc`), zsh sessions fall back to system Node (v12), causing `Unexpected token '?'` errors in subcommands that use modern JS (e.g. `now-sdk init` with inquirer). `--help` survives because it avoids modern syntax. Fix: add the nvm loader block to `~/.zshrc`.

Source: [[raw/sessions/2026-07-14#Session 12:25 — pedro]]

## Related concepts
- [[acls]]
- [[sn-instance-scan]] — real scoped app in design

## Related
- [[wiki/index|Wiki Index]]
