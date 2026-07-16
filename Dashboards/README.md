---
aliases: [Dashboards]
area: dashboard-index
tags: [dashboard, bases]
---
Live Bases dashboards (core `bases` plugin — no Dataview installed). Each `.base` file is a set of filtered views over the vault, built on the `area`/`tags`/`source` frontmatter already in use. Open the file in Obsidian; views are tabs along the top.

## The dashboards

- [[Wiki Health.base|Wiki Health]] — structural health of `wiki/`, computed live. Views: **Needs expansion** (thinnest page first), **Weakly linked**, **Going stale** (untouched 30+ days), **Broken convention** (missing `area`/`tags`), **All pages** with metrics.
- [[CTA Study.base|CTA Study]] — the 89-note CTA certification track. Views: **Exam review queue** (the `TO REVIEW FOR EXAM` folder), **By week**, **Capstone**, **Case studies**, **All exam prep**.
- [[Notion Reference.base|Notion Reference]] — the 285-note Notion corpus. Views: **Raw bulk by topic** (grouped by `area` — shows which topics have accumulated material), **My own writing** (`source: custom`, 21 hand-written notes vs. 263 exports), plus per-topic and recency views.
- [[Wiki.base|Wiki]] — plain `wiki/` browser split by `area` (concept/entity/query/synthesis).
- [[Applications.base|Applications]] — `Applications/` split per app.

## Two things worth knowing

**Wiki Health replaces part of `lint.py`, not all of it.** The `Needs expansion` view reproduces lint's sparse-article check exactly — it flags the same 33 pages — but for free and live, where `lint.py` costs an LLM call. It does *not* replace lint's *semantic* checks (cross-article contradictions, stale-vs-newer-source detection), which still need `uv run python scripts/lint.py`.

**Wiki Health deliberately has no "orphans" view.** Lint's orphan check means "no other *wiki article* links here." Bases' `file.backlinks` counts inbound links from anywhere in the vault — including `wiki/index.md` and the Notion notes — so by that measure only the two append-only logs are orphans, and pages lint calls orphaned (e.g. `ciwf`, 5 backlinks) look fine. Bases can't filter backlinks by source folder, so the check isn't reproducible here. **Keep using `lint.py` for orphans.** `Weakly linked` is the softer live proxy.

## Caveats

- `words` is an estimate: `(file.size - 195) / 7.28`, a linear fit against actual word counts from this vault's pages (`acls` → 52 est. vs. 50 actual). Good for ranking, not exact. Bases can't read file contents.
- Notion filenames carry export hash suffixes, so views show the `aliases` title via a `title` formula instead of `file.name`.
- These are read-only views, not content. They don't replace `wiki/index.md`, `Notion/INDEX.md`, or `ServiceNowOfficialDocs/INDEX.md` — those stay the curated, described entry points.

## What the dashboards surface

`Raw bulk by topic` next to `Wiki Health → Needs expansion` shows the vault's real synthesis debt: CTA has **89** raw notes behind a **40-word** concept page; AI & VA has **40** behind two ~60-word pages. 33 of 35 wiki pages are stubs. That gap is the backlog — the dashboards make it visible, per CLAUDE.md's "propose first, don't fix silently."
