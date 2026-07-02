---
name: todo-fixer
description: Finds and fixes issues listed in a todo.md file in the current project. Use this skill whenever the user mentions "fix todos", "work on the todo list", "resolve todo.md issues", "tackle the todo file", or any request to address outstanding tasks, bugs, or improvements tracked in a todo.md. Also trigger when the user says things like "fix what's in the todo", "handle the pending issues", or "clean up the todo". This skill should be used proactively any time a todo.md file is referenced in a fix/resolve/work-on context.
---
 
# Todo Fixer Skill
 
This skill reads the project's `todo.md` file, parses the outstanding issues, and systematically fixes them one by one.
 
## Workflow
 
### 1. Locate the todo.md
 
Search for `todo.md` (case-insensitive) starting from the project root:
 
```bash
find . -maxdepth 3 -iname "todo.md" | head -5
```
 
If multiple are found, prefer the one at the project root. If none is found, tell the user and stop.
 
### 2. Read and parse the todo list
 
Read the file and identify actionable items. These are typically:
- `- [ ] ...` checkboxes (unchecked)
- Numbered items like `1. Fix ...`
- Lines with `TODO:`, `BUG:`, `FIXME:`, `ISSUE:` prefixes
- Section headers followed by bullet points describing issues
**Skip already-completed items** — checked boxes `- [x]`, items marked `✅`, `DONE`, or `~~strikethrough~~`.
 
### 3. Triage and plan
 
Before touching any code:
1. List all open items you found, numbered clearly
2. Group them by type if helpful (bugs, refactors, missing features)
3. Note any items that are ambiguous or require user input — ask upfront, don't get blocked mid-fix
4. Confirm with the user if the list is long (10+ items): "I found N open todos — should I fix all of them or prioritize certain ones?"
### 4. Fix each item systematically
 
For each item:
1. **Understand the issue** — read relevant source files before changing anything
2. **Make the fix** — targeted, minimal changes; don't refactor unrelated code
3. **Verify** — run relevant tests or checks if available (`npm test`, `pytest`, `cargo test`, etc.)
4. **Mark as done** — update the todo.md item to `- [x]` or add `✅` once confirmed working
If a fix reveals a deeper problem that can't be resolved quickly, note it clearly and move on rather than getting stuck.
 
### 5. Summary report
 
After working through the list, provide a concise summary:
- ✅ Fixed: list of resolved items
- ⚠️ Skipped / needs input: anything blocked or ambiguous
- 🔁 Follow-up suggested: items that need more work
## Guidelines
 
- **Read before writing** — always understand the existing code before modifying it
- **One item at a time** — complete and verify each fix before moving to the next
- **Preserve intent** — fix what's described, don't over-engineer
- **Update todo.md** — keep it in sync as you go so progress is visible
- **Ask once, not repeatedly** — gather all clarifying questions upfront in step 3
## Edge Cases
 
- **No todo.md found**: Report the search paths checked and ask if it's elsewhere
- **All items already done**: Tell the user the todo list is clean
- **Item references unknown file/module**: Note it, skip it, mention in summary
- **Conflicting or duplicate items**: Consolidate and fix once