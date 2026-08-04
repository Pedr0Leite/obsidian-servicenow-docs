# Graph Report - .  (2026-07-31)

## Corpus Check
- 90 files · ~79,790 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 470 nodes · 729 edges · 81 communities (56 shown, 25 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 67 edges (avg confidence: 0.86)
- Token cost: 0 input · 202,353 output

## Community Hubs (Navigation)
- Frontend App Logic
- Seed Data — Allocations & Initiatives A
- Known Bugs & Data Model
- Graphify Skill Reference System
- Seed Data — Allocations & Initiatives B
- package.json Dependencies
- TypeScript Config References
- Capacity REST API Handler
- Team & Headcount Seed Data
- ADO Field Sync Bugs & BR
- App Scope Config
- ACLs, Menu & Roles
- Sync Initiative Fields Business Rule
- Sidebar & New Initiative Panel
- Generated Keys Registry
- Export Button Bug
- Derive Dates on Item Insert BR
- Derive Initiative Dates BR
- Propagate Initiative Changes BR
- Resolve Initiative Link BR
- CreateInitiative Null-Insert Bug
- Duplicate Cross-Scope Privilege Bug
- FinishEdit Null-Guard Bug
- RawData Partial-Failure Reset Bug
- Hardcoded Role-Teams Bug
- SaveAllocations No-Validation Bug
- SelectedSS Shared-Set Bug
- SetPlanStatus No-Trim Bug
- Steerco Status Half-Removed Bug
- XLSX CDN CSP-Block Bug
- XLSX Filename Hardcoded-Year Bug
- Graphify MCP/Benchmark Exports
- Allocation Table Definition
- Headcount Table Definition
- Initiative Table Definition
- Period Table Definition
- Team Table Definition
- UI Page Definition
- Client HTML Doctype
- Agent Orchestration Efficiency Rationale
- Browser Test Token Efficiency Rationale

## God Nodes (most connected - your core abstractions)
1. `renderDetail()` - 27 edges
2. `renderSidebar()` - 18 edges
3. `activeMos()` - 16 edges
4. `renderOvTable()` - 16 edges
5. `getTA()` - 14 edges
6. `renderPipeline()` - 14 edges
7. `Graphify Full Pipeline (/graphify)` - 14 edges
8. `renderHeatmap()` - 13 edges
9. `refreshViews()` - 12 edges
10. `renderTeamDetail()` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Project graphify Integration Rules` --conceptually_related_to--> `Graphify Full Pipeline (/graphify)`  [INFERRED]
  CLAUDE.md → .claude/skills/graphify/SKILL.md
- `README: "React app in ServiceNow"` --conceptually_related_to--> `SPA Views (projects/heatmap/team/overview/pipeline/allplanitems)`  [AMBIGUOUS]
  README.md → capacity-planner.md
- `Task 44: Convert de-facto string choice fields to ChoiceColumn` --conceptually_related_to--> `x_u4bsh_capmgmt_initiative (Capacity Plan Item)`  [INFERRED]
  todo.md → capacity-planner.md
- `Task 39: Restore field-deny ACLs for u_start/u_end` --conceptually_related_to--> `derive-initiative-dates Business Rule`  [INFERRED]
  todo.md → capacity-planner.md
- `Task 43: Propagate external Initiative changes to linked Plan Items` --conceptually_related_to--> `sync-initiative-fields Business Rule`  [INFERRED]
  todo.md → capacity-planner.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Graphify Skill + Reference File System** — claude_skills_graphify_skill_graphify_pipeline, claude_skills_graphify_references_add_watch_graphify_add, claude_skills_graphify_references_exports_wiki_export, claude_skills_graphify_references_extraction_spec_subagent_prompt, claude_skills_graphify_references_github_and_merge_clone, claude_skills_graphify_references_hooks_post_commit_hook, claude_skills_graphify_references_query_bfs_dfs_traversal, claude_skills_graphify_references_transcribe_whisper, claude_skills_graphify_references_update_incremental_update [EXTRACTED 1.00]
- **Multi-Year Period Migration Debt Cluster** — capacity_planner_multi_year_migration_debt, bugs_multi_year_period_overwrite, bugs_activemos_cross_year_truncate, todo_task17, todo_task20, todo_task31, todo_task38 [INFERRED 0.90]
- **Date-Derivation & Initiative-Sync Business Rule Pipeline** — capacity_planner_derive_initiative_dates_br, capacity_planner_derive_dates_on_item_insert_br, capacity_planner_sync_initiative_fields_br, capacity_planner_propagate_initiative_changes_br, capacity_planner_resolve_initiative_link_br [EXTRACTED 1.00]

## Communities (81 total, 25 thin omitted)

### Community 0 - "Frontend App Logic"
Cohesion: 0.06
Nodes (94): aCls(), activeMos(), activeToYear, activeYear, addTeamChip(), addToPlanner(), AREA_CLR, AREA_CLS (+86 more)

### Community 1 - "Seed Data — Allocations & Initiatives A"
Cohesion: 0.04
Nodes (74): init_0, init_1, init_10, init_11, init_12, init_13, init_14, init_15 (+66 more)

### Community 2 - "Known Bugs & Data Model"
Cohesion: 0.07
Nodes (37): BUG: activeMos() silently truncates cross-year month ranges, BUG (fixed): derive-initiative-dates DELETE leaves stale dates, BUG: Multi-year period map overwrite (loadPeriodMaps), BUG (fixed): N+1 GlideRecord queries in derive-initiative-dates BR, BUG: saveToServiceNow sends raw month keys, bypasses period resolution, x_u4bsh_capmgmt_allocation (Capacity Allocation), Cross-Scope Integration (initiative-intake + cmdb_ci_business_app), derive-dates-on-item-insert Business Rule (+29 more)

### Community 3 - "Graphify Skill Reference System"
Cohesion: 0.06
Nodes (33): /graphify Trigger Rule (.claude/CLAUDE.md), Project graphify Integration Rules, graphify add <url>, graphify --watch (auto-rebuild), FalkorDB Export / Push, Neo4j Export / Push, Wiki Export (graphify export wiki), Confidence Score Rubric (EXTRACTED/INFERRED/AMBIGUOUS) (+25 more)

### Community 4 - "Seed Data — Allocations & Initiatives B"
Cohesion: 0.08
Nodes (25): init_63, init_66, init_67, init_68, init_71, init_72, init_73, init_74 (+17 more)

### Community 5 - "package.json Dependencies"
Cohesion: 0.10
Nodes (19): dependencies, xlsx, description, devDependencies, @servicenow/glide, @servicenow/sdk, imports, #now:* (+11 more)

### Community 6 - "TypeScript Config References"
Cohesion: 0.11
Nodes (18): DOM, ES2022, node_modules, src/fluent/generated/**, src/**/*.ts, src/**/*.tsx, compilerOptions, esModuleInterop (+10 more)

### Community 7 - "Capacity REST API Handler"
Cohesion: 0.24
Nodes (12): addInitiative(), createInitiative(), getAvailableInitiatives(), getData(), loadPeriodMaps(), MONTHS, PLAN_STATUSES, saveAllocations() (+4 more)

### Community 8 - "Team & Headcount Seed Data"
Cohesion: 0.32
Nodes (10): team_ai_engineering, team_architecture, team_ba_businessanalyst, team_erp, team_integrations, team_internal_apps, team_pm, team_sales (+2 more)

### Community 9 - "ADO Field Sync Bugs & BR"
Cohesion: 0.24
Nodes (10): BUG (fixed): field-level write ACLs missing for u_ado_ref/u_ado_status, BUG (fixed): sync-initiative-fields BR does not sync u_ado_ref/u_ado_status, propagate-initiative-changes Business Rule, resolve-initiative-link Business Rule, sync-initiative-fields Business Rule, Task 23: Add missing field-level write ACLs for u_ado_ref/u_ado_status, Task 24: Sync u_ado_ref/u_ado_status in sync-initiative-fields BR, Task 43: Propagate external Initiative changes to linked Plan Items (+2 more)

### Community 10 - "App Scope Config"
Cohesion: 0.25
Nodes (7): dependencies, x_u4bsh_initiati_0, name, scope, scopeId, tables, x_u4bsh_initiati_0_initiative

### Community 11 - "ACLs, Menu & Roles"
Cohesion: 0.48
Nodes (4): capmgmt_menu, capmgmt_admin, capmgmt_planner, capmgmt_viewer

### Community 12 - "Sync Initiative Fields Business Rule"
Cohesion: 0.43
Nodes (5): mapPriority(), mapSize(), SIZE_MAP, STATE_BUCKET, syncInitiativeFields()

### Community 13 - "Sidebar & New Initiative Panel"
Cohesion: 0.50
Nodes (4): BUG (fixed): Absences type missing from new-initiative dropdown, New Initiative Panel (ni-name/ni-area/ni-priority/ni-size/ni-type), Sidebar Plan-Item List + New Initiative Panel, Task 30: Add Absences option to new-initiative type dropdown

### Community 14 - "Generated Keys Registry"
Cohesion: 0.50
Nodes (3): Internal, Keys, Now

### Community 15 - "Export Button Bug"
Cohesion: 1.00
Nodes (3): NOTE: export-btn is labeled Save Changes, correctly calls saveToServiceNow, export-btn ("Save Changes" button), Task 25: Fix export button wired to save instead of export

## Ambiguous Edges - Review These
- `README: "React app in ServiceNow"` → `SPA Views (projects/heatmap/team/overview/pipeline/allplanitems)`  [AMBIGUOUS]
  README.md · relation: conceptually_related_to

## Knowledge Gaps
- **128 isolated node(s):** `scope`, `scopeId`, `name`, `x_u4bsh_initiati_0_initiative`, `name` (+123 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `README: "React app in ServiceNow"` and `SPA Views (projects/heatmap/team/overview/pipeline/allplanitems)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `buildXLSX()` connect `Frontend App Logic` to `package.json Dependencies`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Why does `xlsx` connect `package.json Dependencies` to `Frontend App Logic`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **What connects `scope`, `scopeId`, `name` to the rest of the system?**
  _128 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Frontend App Logic` be split into smaller, more focused modules?**
  _Cohesion score 0.06425438596491229 - nodes in this community are weakly interconnected._
- **Should `Seed Data — Allocations & Initiatives A` be split into smaller, more focused modules?**
  _Cohesion score 0.04350877192982456 - nodes in this community are weakly interconnected._
- **Should `Known Bugs & Data Model` be split into smaller, more focused modules?**
  _Cohesion score 0.06606606606606606 - nodes in this community are weakly interconnected._