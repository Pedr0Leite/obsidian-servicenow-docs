---
aliases: [Token Improvement Ideas]
area: session-log
tags: [performance, token-optimization, todo]
---

Ideas from a 2026-07-27 session on reducing token/time cost of navigating this vault. Three items from that session are already done — per-folder `INDEX.md` for leaf dirs >100 files, the frontmatter search tool (`scripts/frontmatter_search.py`), and the root `llms.txt`. The rest are queued here, not yet built. Run one at a time; each is independent.

## 1. ~~Global `llms.txt` at vault root~~ — DONE 2026-07-27

Built `llms.txt` at repo root: 55 category one-liners generated from `ServiceNowOfficialDocs/INDEX.md`'s `## ` headers, plus a hand-written section for everything outside `ServiceNowOfficialDocs/` (Notion, Applications, wiki, ClaudeAgents, etc.) and a Tools section (semantic_search, frontmatter_search.py, obsidian-cli). 9.2KB vs. `INDEX.md`'s 96.5KB — roughly 10x cheaper for the "which top-level area do I want" step. Generator script left in scratchpad only (one-off, category headers rarely change); rerun by hand if categories are added/removed.

## 2. Backfill empty `description:` frontmatter in `support-and-troubleshooting/`

Spot-checked during the frontmatter-cache build: many KB-article files under `support-and-troubleshooting/*` have `description:` blank in frontmatter (title is usually fine — it's the article title). This weakens both the sub-indexes generated this session and the new `frontmatter_search.py` tool, since both key off that field.

**Action:** for files with blank description, generate a 1-sentence summary (would require reading the body — do this in batches per subfolder, it's a real per-file cost, not free like the other items here).

## 3. Collapse/archive `delta-*` release-changelog dirs

`delta-washingtondc-australia/`, `delta-yokohama-australia/`, `delta-zurich-australia/` — ~400 files each, ~1,200 total. Mostly redundant with `release-notes/release-notes/` (272 files) — per-product changelogs for old release-pair upgrades. If old delta pairs aren't queried often, moving stale ones (e.g. keep the newest, archive the rest) out of the default glob path shrinks what agents scan by default. Also noted: `delta-washingtondc-australia/` has 19 zero-byte files — a scrape gap, separate from the token question but worth a look while in there.

**Action:** confirm with user which delta pairs are actually still relevant before archiving anything (this one is a judgment call, not mechanical).

## 4. `.smart-env/` is committed to git — 3.2GB, 51,322 tracked files (URGENT, confirmed)

Checked this session, not hypothetical: `git ls-files .smart-env | wc -l` → 51,322. `du -sh .smart-env` → 3.2GB. It's the Smart Connections plugin's generated embedding index — bigger than the entire `ServiceNowOfficialDocs` corpus (~46k files) combined, and it's all sitting in git history. This is almost certainly the single largest token/clone/disk cost in the repo, dwarfing everything folder-indexing touches.

**Action (needs your sign-off, this is destructive):**
1. Add `.smart-env/` to `.gitignore` (safe, do first).
2. Remove it from the current tree: `git rm -r --cached .smart-env`.
3. It'll still bloat `.git` history until history is rewritten (`git filter-repo` or similar) — that's the destructive part, and rewrites history for anyone else with a clone, so don't do it without confirming no one else is relying on the current history.
4. Confirm the Smart Connections plugin can rebuild `.smart-env` locally from the vault (it should — that's the whole point of it being a generated index) before removing anything.

---
*Filed 2026-07-27. Delete or check off items as they're completed.*
