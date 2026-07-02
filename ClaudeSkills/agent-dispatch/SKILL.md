# Agent Dispatch Skill

Invoke this skill with `/agent-dispatch` before writing any agent prompt. It enforces lean prompts and prevents token waste.

---

## Step 1 — Pick the right agent

| Task | Agent |
|---|---|
| 1–3 file edits, pattern already known | `developer` |
| Doc / todo / story rewrite | `ba-agent` (no SDK lookups) |
| Multi-artifact feature, new tables, ACLs | `orchestrator` |
| Browser verification (≤5 named checks) | `tester` |
| Unknown or exploratory | `dispatcher` |

**Never use `orchestrator` for a single-file change.**

---

## Step 2 — Pre-read before you prompt

Read every file the agent will touch **in the main context** now:
- Source files (table definitions, ACLs, list files, app.js sections)
- The relevant todo.md task block

Then paste the excerpts into the prompt. The agent must not re-read what you already have.

---

## Step 3 — Prompt must include

- Exact file paths to create/modify
- Exact line numbers or code blocks to match (from your pre-read)
- All decisions already made — no ambiguity left for the agent to resolve
- The pattern to follow (copy from existing source, not from docs)

---

## Step 4 — Append this constraints block to every implementation prompt

```
Constraints:
- Do NOT create dev-log.md or any other extra files.
- Do NOT run npm run types.
- Do NOT call npx @servicenow/sdk explain unless generating Fluent code that requires it.
- Read files before editing — surgical edits, shortest diff wins.
- Mark the todo.md task [x] when done.
- Do not make unsolicited improvements beyond the stated scope.
- Stop after the final step. Do not make further changes.
```

---

## Step 5 — End the prompt with an explicit stop

Last line of every prompt:
> "Stop after [last step]. Do not make further changes."

---

## Token budget reference (observed costs)

| Agent + task | Lean (pre-read) | Bloated (no pre-read) |
|---|---|---|
| `developer` — 2-file edit | ~25–45k | ~80–95k |
| `ba-agent` — todo rewrite | ~10k | ~70k |
| `tester` — 4 named checks | ~25k | ~90k |
| `orchestrator` — new table | ~45k | ~150k+ |

If your prompt is longer than the code the agent will write, it's too long.
