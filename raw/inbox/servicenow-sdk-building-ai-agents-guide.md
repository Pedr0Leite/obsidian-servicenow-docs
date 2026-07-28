<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://servicenow.github.io/sdk/guides/building-ai-agents-guide -->
<!-- Fetched: 2026-07-23 via defuddle CLI -->
<!-- Fetched as part of a batch of 27 URLs; this is one of 4 that succeeded (23 blocked by ServiceNow's CDN/WAF with 503s, or JS-only with nothing extractable — see blocked-urls-2026-07-23.md in this folder). -->

Version: Latest (4.9.0)

Build and configure ServiceNow AI Agents and AI Agentic Workflows using the Fluent SDK. AI Agents perform tasks with tools (CRUD, script, OOB, reference-based), while AI Agentic Workflows orchestrate multiple agents as a team. This guide covers end-to-end creation: authentication, tool configuration, instructions authoring, triggers, ACL deployment, and editing existing agents. Requires SDK 4.4.0 or higher.

> **Branding note:** "Now Assist" has been rebranded to "ServiceNow Otto." These names refer to the same product. All technical identifiers (table names, field names, string literals like `"Now Assist Panel"`, `now_assist_deployment`) remain unchanged — use them exactly as-is in code.

---

## When to Use

- Creating a new AI Agent in ServiceNow
- Creating AI Agentic Workflows that orchestrate multiple agents
- Modifying existing agents or agentic workflows (adding tools, changing auth, updating instructions)
- Configuring agent authentication and security (Dynamic User vs AI User)
- Selecting and configuring agent tools (CRUD, script, OOB tools)
- Setting up triggers for agents or agentic workflows
- Defining team members for agentic workflows

---

## Workflow vs Single Agent Decision Tree

```markdown
User Request
    |
Does it involve multiple tasks? (AND, THEN, followed by)
    | NO  -> USE SINGLE AI AGENT
    | YES
        |
    Do the tasks require DIFFERENT capability types?
    (e.g., search + summarize, fetch from table A + update table B)
        | NO  -> USE SINGLE AI AGENT (multiple tools, one agent)
        | YES -> USE AI AGENTIC WORKFLOW
```

**Pattern Recognition:**

| User Says | Type | Why |
| --- | --- | --- |
| "Fetch X AND do Y" (different capabilities) | Workflow | Different capability types working together |
| "Get data THEN process it" (different agents) | Workflow | Sequential operations needing different specializations |
| "Look up and update an incident" | Single Agent | Same table, same capability type (CRUD), multiple tools |
| "Search for incidents by priority" | Single Agent | Single task |

**Key distinction:** Multiple *tools* on the same table or same capability type = single agent with multiple tools. Multiple *capability types* requiring different specializations = workflow with multiple agents.

---

## AI Agent vs AI Agentic Workflow

| Feature | AI Agent | AI Agentic Workflow |
| --- | --- | --- |
| Purpose | Single agent performing tasks | Multiple agents working as a team |
| Import | `AiAgent` from `@servicenow/sdk/core` | `AiAgenticWorkflow` from `@servicenow/sdk/core` |
| Configuration | `tools` array | `team: { $id, name, members: [...] }` |
| Version array | `versionDetails` | `versions` |
| Record identity | `$id` (explicit ID) | `$id` (explicit ID) |
| Security | `securityAcl` (mandatory, auto-generates ACL) | `securityAcl` (mandatory, auto-generates ACL) |
| Run-as user | `runAsUser` | `runAs` |
| Execution mode | `executionMode` on tools | `executionMode` at workflow level (default: `'copilot'`) |
| Trigger channel | `'nap'` / `'nap_and_va'` (agent-level `channel`) | `"Now Assist Panel"` (trigger-level, mandatory) |
| Processing messages | `processingMessage`, `postProcessingMessage` | Not available |
| Protection policy | `protectionPolicy` (optional) | `protectionPolicy` (optional) |

---

## Protection Policy

Both `AiAgent` and `AiAgenticWorkflow` support `protectionPolicy` (inherited from `Now.Internal.WithIdAndMetadata`). This sets the `sys_metadata` protection policy on the generated record, controlling whether other developers can edit the record after the application is installed.

| Value | Effect |
| --- | --- |
| `'read'` | Others can see the configuration but **cannot change** it |
| `'protected'` | Others **cannot change** this record |
| *(omitted)* | Others can fully customize this record |

You can also use `$override` to set properties not directly supported by the API:

```typescript
AiAgent({
  $id: Now.ID['my_agent'],
  name: 'My Agent',
  protectionPolicy: 'read',
  $override: { custom_field: 'value' },
  // ...
})
```

---

## Security ACL (securityAcl)

`securityAcl` is **mandatory** on both `AiAgent` and `AiAgenticWorkflow`. It controls **who can invoke** the agent/workflow and auto-generates the `sys_security_acl` and `sys_security_acl_role` records. It is a discriminated union on the `type` field — each variant also requires a `$id` to identify the generated ACL record.

### Access Types

| `type` | Who can invoke | Extra fields |
| --- | --- | --- |
| `'Any authenticated user'` | Any logged-in user | None |
| `'Specific role'` | Only users with listed roles | `roles: [...]` (required) |
| `'Public'` | Anyone, no auth required | None |

```typescript
// Any authenticated user
securityAcl: {
    $id: Now.ID['my_agent_acl'],
    type: 'Any authenticated user',
}

// Specific roles only
securityAcl: {
    $id: Now.ID['my_agent_acl'],
    type: 'Specific role',
    roles: [
        '282bf1fac6112285017366cb5f867469',  // itil role sys_id
        'b05926fa0a0a0aa7000130023e0bde98',  // user role sys_id
    ]
}
```

> **Important distinction:** `securityAcl` controls *who can invoke* the agent. `runAsUser` (agent) / `runAs` (workflow) and `dataAccess` are separate — they control *which user identity the agent runs under* when executing.

### Execution Identity (runAsUser / dataAccess)

Set **either** `runAsUser` (agent) or `dataAccess` — not both:

- **`runAsUser`** — agent always runs as the specified sys_user sys_id regardless of invoker
- **`dataAccess.roleMap`** (role names) or **`dataAccess.roleList`** (role sys_ids) — agent runs as the invoking user, restricted to the listed roles. **Required when `runAsUser` is not set.** For workflows, use `dataAccess` when `runAs` is not set.

### Role Discovery

1. Identify target tables from the agent's CRUD tools
2. Query `sys_security_acl_role` for each table (encodedQuery: `sys_security_acl.nameLIKE<table_name>`)
3. Add discovered role **names** to `dataAccess.roleMap`, or role **sys_ids** to `dataAccess.roleList` and `securityAcl.roles`

### Common Role sys_ids

| Role | sys_id |
| --- | --- |
| admin | `2831a114c611228501d4ea6c309d626d` |
| itil | `282bf1fac6112285017366cb5f867469` |
| user | `b05926fa0a0a0aa7000130023e0bde98` |

---

## Tool Types and Selection

### Selection Priority

1. **OOB tools** when available (e.g., Web Search, RAG, Knowledge Graph)
2. **Reference-based tools** (action, subflow, capability, catalog, topic)
3. **CRUD tools** for database operations
4. **Script tools** only when no other tool type fits

Never use CRUD tools for journal fields (`work_notes`, `comments`). Always use Script tools with `GlideRecordSecure`.

### Tool Selection Guide

| Need | Tool Type | Why |
| --- | --- | --- |
| Read/search records | CRUD (`lookup`) | Direct table query |
| Create new records | CRUD (`create`) | Maps inputs to columns |
| Modify records | CRUD (`update`) | Query + field update |
| Custom logic | Script | Full JavaScript control |
| Web information | OOB (`web_automation`) | Auto-linked OOB tool |
| Semantic/keyword search | RAG (`rag`) | Structured search with ValueLabelType inputs |
| Graph-based search | OOB (`knowledge_graph`) | Knowledge Graph tool |
| File ingestion | OOB (`file_upload`) | File Uploader tool |
| In-depth research | OOB (`deep_research`) | Deep Research tool |
| Desktop tasks | OOB (`desktop_automation`) | Desktop Automation tool |
| MCP integration | OOB (`mcp`) | MCP tool |
| Flow Designer action | Action (`action`) | Triggers existing flows |
| AI skill | Capability (`capability`) | Links to skills |

### inputs Format by Tool Type

| Tool type | `inputs` format | Has `script` field? |
| --- | --- | --- |
| `crud` | **Object** (`ToolInputType`) with `operationName`, `table`, `inputFields`, etc. | No (auto-generated) |
| `rag` | **Object** (`RagInputType`) with `searchType`, `searchProfile`, `sources`, etc. (all using `ValueLabelType`) | No (auto-generated) |
| `script` | **Array** of `[{ name, description, mandatory, value? }]` | Yes |
| `web_automation` | Omit (plugin provides defaults) | No |
| Reference types | Omit (platform resolves at runtime) | No |
| Other OOB types | Omit (plugin provides defaults) | No |

### Required Tool Properties

Every tool **must** have `name` and `type`. `preMessage` and `postMessage` are strongly recommended. Every agent **must** have `processingMessage` and `postProcessingMessage` (not available on workflows).

---

## CRUD Tools

### Operations

| Operation | Required Fields |
| --- | --- |
| `create` | `table`, `inputFields` with `mappedToColumn` |
| `lookup` | `table`, `queryCondition`, `returnFields` (mandatory) |
| `update` | `table`, `queryCondition`, `inputFields` with `mappedToColumn` |
| `delete` | `table`, `queryCondition` |

### queryCondition Syntax

Format: `"column_name=={{input_field_name}}"`. Always verify column names by querying `sys_dictionary` before writing tools.

| Operator | Syntax | Example |
| --- | --- | --- |
| Equals | `field=value` | `state=1` |
| Not equals | `field!=value` | `state!=7` |
| Contains | `fieldLIKEvalue` | `short_descriptionLIKEnetwork` |
| Is empty | `fieldISEMPTY` | `assigned_toISEMPTY` |
| OR | `^OR` | `priority=1^ORpriority=2` |

### Lookup Best Practices

- **Always include `{ name: 'sys_id' }` in `returnFields`** — without it, the agent cannot chain operations (e.g., pass the record's sys_id to another tool)
- Use `LIKE` operator for text-based searches
- Use multiple keyword inputs with `OR` for natural language
- Prefer `number` over `sys_id` as primary filter: `number={{id}}^ORsys_id={{id}}`
- For reference fields in `returnFields`, include `referenceConfig`: `{ table: "sys_user", field: "name" }`

### Create Operation — Mandatory Columns

For `create` operations, query `sys_dictionary` to discover mandatory columns: `now-sdk query sys_dictionary -q 'name=<table>^mandatory=true' -f 'column_label,element' -o json`. Ensure ALL mandatory columns are captured in `inputFields` with `mandatory: true`.

### mappedToColumn Self-Check (create/update tools)

After writing each create or update tool, run this check before proceeding:

1. Parse `queryCondition` and list every `{{field_name}}` variable — these are query-only fields
2. For each entry in `inputFields`:
	- Is the field in the queryCondition variables? → It is a query field. Confirm it does **NOT** have `mappedToColumn` ✓
		- Is the field NOT in queryCondition? → It is a write field. Confirm it **HAS** `mappedToColumn` set to a valid column name. If missing, add it now
3. For `create` tools (no queryCondition): every `inputField` MUST have `mappedToColumn` — no exceptions
4. Do NOT proceed to the next tool until this check passes

---

## Script Tools

All script inputs are **strings** at runtime. Parse with `parseInt()`, `JSON.parse()`, etc. The `inputs` field for script tools is a **simple array** of input field definitions (unlike CRUD tools which use an object).

```javascript
(function(inputs) {
    var impact = parseInt(inputs.impact, 10);
    var urgency = parseInt(inputs.urgency, 10);
    // ... logic
    return { priority: result, status: 'success' };
})(inputs);
```
- Always use `GlideRecordSecure` (not `GlideRecord`)
- Do NOT add CDATA tags (plugin handles automatically)
- `inputSchema` is auto-generated from `inputs` — do not specify it manually
- Use module imports for server-side script files (or `Now.include()` for legacy scripts)

### Calling Existing Script Includes

If a script include with a matching method exists, call it from within the Script tool instead of re-implementing logic:

```javascript
(function(inputs) {
    var util = new MyAppUtils();
    var result = util.calculatePriority(inputs.impact, inputs.urgency);
    return { priority: result, status: "success" };
})(inputs);
```

### Journal Field Updates (work_notes, comments)

`work_notes` and `comments` are journal fields backed by `sys_journal_field` — they are not columns on the target table. CRUD update tools cannot write to them. Always use a Script tool:

```javascript
(function(inputs) {
    var gr = new GlideRecordSecure(inputs.table_name);
    if (!gr.get(inputs.record_sys_id)) {
        return { status: "error", message: "Record not found: " + inputs.record_sys_id };
    }
    if (inputs.field === "work_notes") {
        gr.work_notes = inputs.note_text;
    } else if (inputs.field === "comments") {
        gr.comments = inputs.note_text;
    } else {
        return { status: "error", message: "Invalid journal field: " + inputs.field };
    }
    gr.update();
    return { status: "success", message: "Journal field updated" };
})(inputs);
```

---

## Reference-Based Tools

Each requires a type-specific reference field containing the target record's sys_id. Do NOT add `inputs`.

| Tool Type | Required Field | Target Table |
| --- | --- | --- |
| `action` | `flowActionId` | `sys_hub_action_type_definition` |
| `capability` | `capabilityId` | `sn_nowassist_skill_config` |
| `subflow` | `subflowId` | `sys_hub_flow` |
| `catalog` | `catalogItemId` | `sc_cat_item` |
| `topic` | `virtualAgentId` | `sys_cs_topic` |
| `topic_block` | `virtualAgentId` | `sys_cs_topic` |

---

## OOB Tools

OOB tools only require `type` and `name`. The plugin auto-links to the existing OOB tool record.

```typescript
{
    type: 'web_automation',
    name: 'AIA Web Search',
    preMessage: 'Searching the web...',
    postMessage: 'Web search results retrieved.'
}
```

Other supported OOB types: `'rag'`, `'knowledge_graph'`, `'file_upload'`, `'deep_research'`, `'desktop_automation'`, `'mcp'`.

---

## RAG (Search Retrieval) Tools

RAG tools enable semantic search and document retrieval from ServiceNow tables. The `type` for RAG tools is `'search_retrieval'` and requires structured `inputs` configuration.

### Search Types

| Type | Description | Required Fields |
| --- | --- | --- |
| `'keyword'` | Simple text matching | None |
| `'semantic'` | Semantic search using embeddings | `semanticIndexes` (array of ValueLabelType) |
| `'hybrid'` | Combines keyword and semantic | `semanticIndexes` (array of ValueLabelType) |

**Note:** The `query` description is generated using the `searchProfile.label`. `semanticIndexes` and `documentMatchThreshold` are only included in the generated schema for `semantic` and `hybrid` search types. `fields` and `searchResultsLimit` apply to all search types.

### RAG Tool Example (Semantic Search)

```typescript
{
    name: 'Semantic Knowledge Search',
    description: 'Searches knowledge articles using semantic search',
    type: 'search_retrieval',
    recordType: 'custom',
    executionMode: 'autopilot',
    preMessage: 'Performing semantic search...',
    postMessage: 'Semantic search completed.',
    inputs: {
        searchType: {
            type: 'semantic',
            semanticIndexes: [
                { value: 'kb_knowledge_text_index', label: 'Knowledge Base Text Index' }
            ],
            documentMatchThreshold: 0
        },
        searchProfile: {
            value: 'quick_action_kb_search_profile',
            label: 'Quick Action - KB Search Profile'
        },
        sources: [
            { value: 'kb_knowledge', label: 'Knowledge Articles' }
        ],
        fields: [
            { value: 'kb_knowledge.short_description', label: 'Short description [kb_knowledge]' },
            { value: 'kb_knowledge.text', label: 'Article body [kb_knowledge]' },
            { value: 'kb_knowledge.number', label: 'Number [kb_knowledge]' }
        ],
        searchResultsLimit: 5
    }
}
```

### Search Type Comparison

| Property | `keyword` | `semantic` | `hybrid` |
| --- | --- | --- | --- |
| `searchType.type` | `'keyword'` | `'semantic'` | `'hybrid'` |
| `semanticIndexes` | Not applicable | Required | Required |
| `documentMatchThreshold` | Not applicable | Optional (default: 0) | Optional (default: 0) |
| `searchProfile` | Required | Required | Required |
| `sources` | Optional | Optional | Optional |
| `fields` | Optional | Optional | Optional |
| `searchResultsLimit` | Optional | Optional | Optional |

---

## Instructions Authoring

### Three Key Fields

Each field has a distinct purpose — do not duplicate content across them.

| Field | Purpose | Answers |
| --- | --- | --- |
| `description` | Scope — what it DOES | "What problem does this agent solve?" |
| `agentRole` | Identity — what it IS (agents only) | "Who am I?" |
| `instructions` | Behavior — what it SHOULD DO | "How should I act and use my tools?" |

### Writing Principles

- **Clarity**: Use specific action verbs (`Fetch`, `Retrieve`, `Filter`, `Analyze`, `Update`). Add explicit conditions: `"If priority = High, then escalate immediately"`
- **Actionable steps**: Every step MUST bind to a tool action, agent delegation, or concrete output. Avoid vague verbs without tool binding: `"Understand the request"` — prefer `"Use [Tool Name] to retrieve X"`
- **Explicit tool references**: Name tools explicitly in instructions. Update instructions whenever a tool is renamed
- **Contingencies**: Handle failures with gates: `"DO NOT PROCEED if details are missing"`
- **Coherence**: Each step builds on the previous step's results. Use consistent terminology throughout
- **Trigger context**: Use "from the task" or "from the context" — NOT "from the triggering record"
- **Output format is mandatory**: Tools return raw data (JSON, integer codes, sys_ids). Every instructions block MUST include a presentation step telling the agent how to format results in plain English

### Output Format Guidance

Tools return raw data — JSON objects, integer choice codes (e.g., `state: 1`), and reference sys_ids. The agent surfaces this verbatim unless instructions explicitly tell it to reformat.

Every instructions block that returns data to the user MUST include a presentation step:

```markdown
Step N: Present Results.
- Format the results in plain English as a bulleted list.
- Use readable labels instead of field names (e.g., "Priority" not "priority").
- Replace numeric state/priority codes with their labels (e.g., state 1 = Open, state 6 = Resolved).
- Do NOT display sys_ids, internal field names, or raw JSON to the user.
```

For reference fields, include `referenceConfig` on `returnFields` entries so the tool resolves display values.

| Output type | Minimum instruction required |
| --- | --- |
| Single record, few fields | `"Present the details in plain English."` |
| Multiple records | `"List each record with a numbered heading and its key fields as sub-bullets."` |
| Records with numeric choice codes | `"Replace state/priority codes with their text labels before presenting."` |
| Records with reference fields | `"Use the display name from reference fields, not the sys_id."` |

### Trigger-Initiated Instructions

When an agent or workflow has a trigger, the triggering record's data is available through `task` and `context` — NOT by querying the triggering table directly.

**WRONG** — agent cannot process "triggering record":

```markdown
Step 1: Gather data from the triggering record.
```

**CORRECT** — reference task/context:

```markdown
Step 1: Extract Incident Details.
- Extract the incident number, priority, and short description from the task.
- Use the context to identify the assignment group and category.
```

Rules:

- Use "from the task" or "from the context" to reference incoming trigger data
- The first step should extract/parse needed fields from `task` / `context`, not fetch them from a table
- Subsequent steps CAN use tools to fetch *additional* data not already in the trigger context
- For workflows, use `contextProcessingScript` to shape trigger data before agents use it

### Agent-to-Agent Data Flow (Workflows)

Agents in a workflow share data through the orchestration context. Instructions must explicitly state what data to pass between steps:

- **State what to retrieve**: `"Use [Agent A] to retrieve the incident's number, priority, state, and assigned_to."`
- **Reference previous results**: `"Using the incident details from Step 1, use [Agent B] to search for similar resolved incidents."`
- **Handle missing data**: `"If [Agent A] returns no results, skip [Agent B] and proceed directly to Step N."`
- **Aggregate across agents**: `"Combine the incident details from Step 1 with the resolution suggestions from Step 2 and present a unified summary."`

### Tool Description Guidance

| Quality | Description | Problem |
| --- | --- | --- |
| **Bad** | `"Looks up incidents"` | Too vague — agent won't know when to pick this tool over another |
| **Good** | `"Searches for incidents by number, priority, or assignment group. Returns number, short description, state, priority, and assigned_to."` | Specifies inputs, outputs, and scope |

### Scaling by Complexity

| Complexity | Tools/Agents | Instructions Length |
| --- | --- | --- |
| Simple | 1-2 tools | 5-10 lines |
| Moderate | 3-4 tools | 10-20 lines |
| Complex | 5+ tools | 20-30 lines |
| Workflow | 2-10 agents | 15-30 lines |

If instructions exceed ~30 lines, split into multiple agents orchestrated by a workflow.

---

## Agent Decomposition for Workflows

When building a workflow, decompose the request into individual agents. Each agent should have a single clear responsibility.

### Decomposition Patterns

| Pattern | When to Use | Example |
| --- | --- | --- |
| **By capability** | Agents need different tool types | Lookup Agent (CRUD) + Analysis Agent (Script) + Search Agent (OOB) |
| **By table/domain** | Work spans multiple tables | Incident Agent + Change Agent + Problem Agent |
| **By workflow phase** | Clear sequential phases | Gather Agent → Process Agent → Act Agent |

### Rules of Thumb

1. **One capability per agent** — if an agent needs tools that serve fundamentally different purposes, split into separate agents
2. **Split at >5 tools** — an agent with more than 5 tools becomes unfocused
3. **Each agent gets a clear name** — `"Incident Lookup Agent"`, not `"Helper Agent"`
4. **Non-overlapping responsibilities** — no two agents should answer the same question
5. **Match agent count to complexity** — 2-3 agents for most workflows; 4+ only for genuinely complex multi-phase processes

---

## Advanced Patterns

### Tool Composition

| Scenario | Tools Needed | Why |
| --- | --- | --- |
| Read/write database records | CRUD only | Direct table operations |
| Read records + calculate/transform | CRUD + Script | Script processes CRUD output |
| Read records + external info | CRUD + OOB | Web Search supplements DB data |
| Read, transform, and enrich | CRUD + Script + OOB | Full pipeline: fetch → process → enrich |

Composition rules:

- Each tool should do ONE thing
- Instructions must define the ORDER tools are used
- Name tools clearly so instructions can reference them unambiguously
- Use `outputTransformationStrategy` on tools whose output feeds into other tools

### Multi-Tool Instructions Pattern

```markdown
Step 1: Gather Data.
- Use [CRUD Lookup Tool] to fetch records matching the user's criteria.
- NEVER skip this step — all subsequent steps depend on its output.
- DO NOT PROCEED if no records are found.

Step 2: Process Results.
- Use [Script Tool] to analyze/aggregate the data from Step 1.
- Present computed results to the user.

Step 3: Enrich (if needed).
- Use [OOB Web Search] to find supplementary information.
- Combine with Step 2 results and present the final summary before taking any action.
```

---

## Memory Categories

AI Agents can access long-term memory categories. Set `memoryCategories` to an array of category strings. Only include categories relevant to the agent's purpose — omit the property entirely if the agent doesn't need long-term memory.

| Category | Description |
| --- | --- |
| `"device_and_software"` | Devices and software used by the user |
| `"meetings_and_events"` | Meetings, events, and calendar items |
| `"projects"` | Projects and initiatives |
| `"workplace"` | Workplace and organizational information |

---

## Trigger Configuration

Triggers are optional. Agents/workflows can operate without them via ServiceNow Otto Panel.

### Trigger Types

| Type | Description |
| --- | --- |
| `record_create` | On new record creation |
| `record_update` | On record update |
| `record_create_or_update` | On both |
| `email` | On email receipt |
| `scheduled` | On a repeating interval |
| `daily` / `weekly` / `monthly` | Scheduled at specific times |
| `ui_action` (workflows only) | From a UI action button |

### Key Differences: Agent vs Workflow Triggers

| Property | Agent trigger | Workflow trigger |
| --- | --- | --- |
| `channel` | `"nap"` or `"nap_and_va"` | `"Now Assist Panel"` (mandatory) |
| `triggerCondition` | Optional | Mandatory for record-based |
| `objectiveTemplate` | Required (defaults to `""`) | Required |

### Scheduled Trigger Fields

The `schedule` object is used when `triggerFlowDefinitionType` is `'scheduled'`, `'daily'`, `'weekly'`, or `'monthly'`.

| Type | Required Fields (inside `schedule` object) |
| --- | --- |
| `daily` | `schedule.time` |
| `weekly` | `schedule.runDayOfWeek` (1=Sun to 7=Sat), `schedule.time` |
| `monthly` | `schedule.runDayOfMonth` (1-31), `schedule.time` |
| `scheduled` | `schedule.repeatInterval` (e.g., `'1970-01-05 12:00:00'` = every 5 days) |

Time format: `"1970-01-01 HH:MM:SS"`.

The `schedule.triggerStrategy` field controls repeat behavior. Values differ by entity type:

| Entity | Valid `triggerStrategy` values |
| --- | --- |
| AI Agent | `'every'`, `'once'`, `'unique_changes'`, `'always'` |
| AI Agentic Workflow | `'every'`, `'immediate'`, `'manual'`, `'once'`, `'repeat_every'`, `'unique_changes'` |

### Email Trigger Required Fields

| Field | Required? | Description |
| --- | --- | --- |
| `targetTable` | Yes | The table where email records are processed |
| `triggerCondition` | Yes | Filter condition for selective email processing |

### Run-As Configuration

Configuring who the trigger executes as is **mandatory** for all trigger types.

**For record-based triggers — discover user-reference columns first:**

1. Query `sys_dictionary` with: `now-sdk query sys_dictionary -q 'name=<targetTable>^internal_type=reference^reference=sys_user' -f 'column_label,element' -o json`
2. Present the discovered columns to the user and ask which user the trigger should run as
3. If the user picks a column → set `runAs: "<column_name>"` (do NOT generate `runAsScript`)
4. If the user picks "Other user" or for scheduled/email triggers → generate `runAsScript`

**Option A — Column-based (`runAs`):**

```typescript
{
  runAs: "assigned_to",   // column name, not label
}
```

**Option B — Script-based (`runAsScript`):**

Resolve the user sys_id first: `now-sdk query sys_user -q 'user_name=<username>' -f 'sys_id,user_name' -o json`

```typescript
{
  runAsScript: `/**
 * Script to be evaluated at runtime when the trigger is executed.
 * @param {GlideRecord} current - Target record that executed this trigger.
 * @returns {string}
 */
(function(current) {
  var result = "<resolved_sys_id>"; // sys_id of the user
  return result;
})(current);`,
}
```

**Option C — Fixed user (`runAsUser`):**

```typescript
{
  runAsUser: "6816f79cc0a8016401c5a33be04be441",  // specific user sys_id
}
```

**Priority:** If both `runAs` and `runAsScript` would apply, prefer `runAs` (simpler). Only use `runAsScript` when a specific user is needed that cannot be derived from a record column.

### Safety Considerations

1. **Triggers are deployed inactive** — users must manually activate triggers in ServiceNow after testing
2. **Test thoroughly** before activating triggers
3. **Monitor first executions** after activation
4. **Document trigger conditions** for maintainability
5. **Security Testing**: Verify ACLs and role masks are properly configured before activating triggers
6. **Audit Trail**: Ensure `runAsScript` returns the appropriate user for audit purposes

### Trigger Activation Workflow

1. Create workflow/agent with triggers
2. Deploy to ServiceNow instance
3. Test thoroughly in development/test environment
4. Manually activate trigger in ServiceNow after validation
5. Monitor first few executions

---

## ACL Deployment

Both AI Agents and AI Agentic Workflows use `securityAcl`. The plugin **automatically generates** `sys_security_acl` and `sys_security_acl_role` records — no manual two-step deployment is needed.

The generated ACL name follows the format: `{domain}.{scope}.{name}`

```typescript
// Works the same for both AiAgent and AiAgenticWorkflow
securityAcl: {
    $id: Now.ID['my_agent_acl'],
    type: 'Specific role',
    roles: [
        '282bf1fac6112285017366cb5f867469',  // itil
        'b05926fa0a0a0aa7000130023e0bde98'   // user
    ]
}
```

---

## Workflow Configuration

### Team Structure

Workflows use `$id` for record identity (just like agents). The `team` object also requires its own `$id`.

```typescript
team: {
    $id: Now.ID["workflow_team"],  // MANDATORY on team
    name: "Workflow Team",
    // description is auto-populated from workflow.description — do not set it
    members: [
        "62826bf03710200044e0bfc8bcbe5df1"  // Agent sys_id from sn_aia_agent table
    ]
}
```

Team members can also be specified using the `Record` API (recommended for portability across instances):

```typescript
import { AiAgenticWorkflow, Record } from '@servicenow/sdk/core'

const lookupAgent = Record({ table: 'sn_aia_agent', $id: Now.ID['lookup_agent'], data: { name: 'Lookup Agent' } })
const analysisAgent = Record({ table: 'sn_aia_agent', $id: Now.ID['analysis_agent'], data: { name: 'Analysis Agent' } })

AiAgenticWorkflow({
    // ...
    team: {
        $id: Now.ID['my_team'],
        name: 'My Team',
        members: [lookupAgent, analysisAgent],
    },
})
```

Agents **must** be deployed before creating workflows.

### Workflow-Level Fields

| Field | Type | Default | Notes |
| --- | --- | --- | --- |
| `executionMode` | `'copilot' \| 'autopilot'` | `'copilot'` | Execution mode for the workflow |
| `memoryScope` | `string` | `'global'` | Memory scope for team members |
| `active` | `boolean` | `true` | Omit if active (default) |
| `sysDomain` | `string` | `'global'` | Omit if global (default) |

Only specify fields that differ from their defaults — the plugin suppresses default values in the transform output.

### Deployment Order

1. Create and deploy AI Agents (with `securityAcl`)
2. Retrieve the agent sys_ids by querying `sn_aia_agent` (see the `query-guide` topic)
3. Create and deploy workflow with `securityAcl` and agent sys_ids
4. Query `sn_aia_usecase` to verify the workflow was created

### contextProcessingScript

Supports inline scripts or `Now.include()` for external files:

```javascript
(function(task, user_utterance, workflow_id, context) {
    return {
        pageContext: context?.pageContext,
        triggerContext: context?.triggerContext
    };
})(task, user_utterance, workflow_id, context);
```
```typescript
// Preferred: external file
contextProcessingScript: Now.include('./context-processing-script.js')
```

---

## Complete AI Agent Example

```typescript
import { AiAgent } from "@servicenow/sdk/core";

export const incidentHelperAgent = AiAgent({
    $id: Now.ID["incident_helper_agent"],
    name: "Incident Helper Agent",
    description: "Retrieves incident details and searches for resolution guidance.",
    agentRole: "You are an ITSM incident specialist.",

    // Security — auto-generates ACL records
    securityAcl: {
        $id: Now.ID['incident_helper_agent_acl'],
        type: 'Specific role',
        roles: [
            '282bf1fac6112285017366cb5f867469',  // itil
            'b05926fa0a0a0aa7000130023e0bde98'   // user
        ]
    },

    agentDescriptor: 'created_by_build_agent',
    channel: 'nap_and_va',
    recordType: 'custom',
    processingMessage: "Analyzing your incident request...",
    postProcessingMessage: "Incident analysis complete.",

    versionDetails: [{
        name: "V1",
        number: 1,
        state: "published",
        instructions: `Step 1: Extract the incident number from the user's request.
Step 2: Use the Lookup Incident tool to fetch details.
Step 3: Present details in bullet-point format.
Step 4: Use AIA Web Search for resolution guidance.
Step 5: Recommend next steps. NEVER modify without user approval.`
    }],

    tools: [
        {
            active: true,
            name: "Lookup Incident",
            description: "Searches for incidents by number",
            executionMode: "autopilot",
            type: "crud",
            recordType: "custom",
            preMessage: "Searching for the incident...",
            postMessage: "Incident details retrieved.",
            inputs: {
                operationName: "lookup",
                table: "incident",
                inputFields: [
                    { name: "incident_number", description: "Incident number", mandatory: false }
                ],
                queryCondition: "number={{incident_number}}",
                returnFields: [
                    { name: "number" },
                    { name: "short_description" },
                    { name: "state" },
                    { name: "priority" },
                    { name: "assigned_to", referenceConfig: { table: "sys_user", field: "name" } }
                ]
            }
        },
        {
            type: "web_automation",
            name: "AIA Web Search",
            active: true,
            preMessage: "Searching the web...",
            postMessage: "Web search results retrieved."
        }
    ],

    triggerConfig: []
});
```

## Complete Workflow Example

```typescript
import { AiAgenticWorkflow } from "@servicenow/sdk/core";

export const incidentAnalysisWorkflow = AiAgenticWorkflow({
    $id: Now.ID["incident_analysis_workflow"],
    name: "Incident Analysis Workflow",
    description: "Orchestrates two agents to retrieve and analyze incidents.",
    recordType: "custom",

    // Security — auto-generates ACL records (mandatory)
    securityAcl: {
        $id: Now.ID['incident_analysis_workflow_acl'],
        type: 'Specific role',
        roles: [
            '282bf1fac6112285017366cb5f867469',  // itil
            'b05926fa0a0a0aa7000130023e0bde98'   // user
        ]
    },

    // dataAccess required when runAs is omitted (dynamic user identity)
    // Use roleMap (role names) or roleList (role sys_ids)
    dataAccess: {
        roleMap: ['itil', 'user']
    },

    team: {
        $id: Now.ID["incident_analysis_team"],
        name: "Incident Analysis Team",
        // description is auto-populated from workflow description
        members: [
            "62826bf03710200044e0bfc8bcbe5df1",
            "274b465a7d5f42e581664209557b2b18"
        ]
    },

    versions: [{
        name: "V1",
        number: 1,
        state: "published",
        instructions: `Step 1: Use the Incident Lookup Agent to fetch details.
Step 2: Use the Analysis Agent to examine patterns.
Step 3: Present findings. NEVER modify without user approval.`
    }],

    triggerConfig: [{
        name: "high_priority_incident",
        channel: "Now Assist Panel",
        targetTable: "incident",
        triggerFlowDefinitionType: "record_create",
        triggerCondition: "priority<=2",
        objectiveTemplate: "Analyze high priority incident ${number}",
        showNotifications: true,
        runAsScript: `(function(current) {
            return current.assigned_to || "6816f79cc0a8016401c5a33be04be441";
        })(current);`
    }]
});
```

---

## Editing Existing Agents/Workflows

### Auto-Computed Fields

The following fields are auto-generated by the plugin and should **not** be specified in `.now.ts`:

`internalName`, top-level `instructions`, `base_plan`, `inputSchema`, `targetDocumentTable`, `targetDocument`, CRUD `script`, `team.description`, trigger `usecase`

### Safe Edit Workflow

1. Locate the `.now.ts` file
2. Read the entire current configuration
3. Identify scope of changes (see Change Impact Matrix)
4. Apply only the requested changes
5. Redeploy and query to verify

### Change Impact Matrix

| Change | Also Update |
| --- | --- |
| Add CRUD tool | Verify columns, update instructions, check executionMode |
| Remove tool | Remove instruction references, check dependencies |
| Change auth mode | Update `securityAcl.type`, add/remove `roles` as needed |
| Add trigger | Add to `triggerConfig`, verify target table |
| Add team member (workflow) | Deploy agent first, get sys_id, update instructions |
| Update instructions | Ensure all referenced tool/agent names still exist |

### Rollback

Set current published version to `state: "withdrawn"`, set previous version to `state: "published"`, redeploy.

---

## Plugin Transformation Notes

These notes describe how the plugin converts Fluent config values to ServiceNow record fields.

### Common to Both Agents and Workflows

- **Script fields** (`contextProcessingScript`, `runAsScript`, tool `script`): Auto-wrapped in CDATA by the plugin. Never add CDATA tags manually.
- **`securityAcl`**: Auto-generates `sys_security_acl` and `sys_security_acl_role` records. The ACL name is derived from the internal name: `{domain}.{scope}.{name}`. ACL type is `gen_ai_agent` for agents and `gen_ai_agentic_usecase` for workflows.
- **`dataAccess.roleMap`**: Role names are resolved to sys_ids via `sys_user_role` table at build time, then written to `sys_agent_access_role_mapping` records.
- **`dataAccess.roleList`**: Role sys_ids are written directly to `sys_agent_access_role_configuration.role_list` as a comma-separated list.
- **`inputSchema`**: Auto-generated from `inputs` — never set manually.
- **Schedule fields**: `runDayOfWeek` and `runDayOfMonth` are numbers in Fluent but stored as strings in ServiceNow. The plugin handles the conversion.

### AI Agent–Specific

- **`channel`**: String values (`'nap'`, `'nap_and_va'`) are resolved by the plugin to sys_ids during transform.
- **CRUD tool `inputs`**: Fluent uses `ToolInputType` object (`{ operationName, table, inputFields, queryCondition, returnFields }`). The plugin transforms this into ServiceNow's `crudInputs` JSON format with `operation`, `table.value`, `fieldValues`, and `query`.
- **`queryCondition`**: Maps to ServiceNow's `query` field on the tool — Fluent uses `queryCondition` to avoid confusion with encoded query syntax.
- **`memoryCategories`**: Each category creates a record in `sn_aia_ltm_category_mapping` linking the agent to the category.
- **`versionDetails`**: Published version's `instructions` become the active agent instructions.
- **Tool `sysOverrides`**: Overrides the tool definition record (`sn_aia_tool`). **`m2mSysOverrides`**: Overrides the agent-tool M2M record (`sn_aia_agent_tool_m2m`). These are separate properties targeting different tables.

### AI Agentic Workflow–Specific

- **`team.description`**: Auto-populated from the workflow's `description` field. Never set it manually — it will be overwritten.
- **`team.name`**: Auto-generated from the workflow name if omitted.
- **`internalName`**: Auto-generated as `{domain}.{scope}.{name}` — never specify it manually.
- **`channel`** (triggers): Workflow triggers use `'Now Assist Panel'` (plain string). The plugin resolves this to a sys_id from `messaging_channel`. Do NOT use `Record<'messaging_channel'>` — the workflow plugin rejects Record references for `channel`.
- **`useCase`**: Automatically set to the parent workflow's record ID. Can be overridden to point to a different use case.
- **Default value suppression**: During `toShape` (ServiceNow → Fluent), fields matching their defaults are omitted to keep generated code clean.

---

## Validation and Enums

### Required Fields

| Entity | Mandatory Fields |
| --- | --- |
| AI Agent | `$id`, `name`, `description`, `agentRole`, `securityAcl` |
| AI Agentic Workflow | `$id`, `name`, `description`, `securityAcl`, `team.$id` |
| CRUD tool | `name`, `type`, `inputs.operationName`, `inputs.table`, `inputs.inputFields` |
| Script tool | `name`, `type`, `script` |

### Valid Enums

| Property | Valid Values |
| --- | --- |
| `recordType` (agent) | `"custom"`, `"template"`, `"aia_internal"`, `"promoted"` (default: `"template"`) |
| `recordType` (workflow) | `"custom"`, `"template"`, `"aia_internal"` (default: `"template"`) |
| `executionMode` (tool) | `"autopilot"`, `"copilot"` |
| `executionMode` (workflow) | `"autopilot"`, `"copilot"` (default: `"copilot"`) |
| `state` (version) | `"draft"`, `"committed"`, `"published"`, `"withdrawn"` (default: `"draft"`) |
| `tool.type` | `"script"`, `"crud"`, `"capability"`, `"subflow"`, `"action"`, `"catalog"`, `"topic"`, `"topic_block"`, `"web_automation"`, `"rag"`, `"knowledge_graph"`, `"file_upload"`, `"deep_research"`, `"desktop_automation"`, `"mcp"` |
| `securityAcl.type` | `'Any authenticated user'`, `'Specific role'`, `'Public'` |
| `agentDescriptor` | `"require_caller_id"`, `"created_by_ai_agent_advisor"`, `"created_by_build_agent"`, `""` (default: `""`) |
| `agentType` | `"internal"`, `"external"`, `"voice"`, `"aia_internal"` |
| `channel` (agent) | `"nap"`, `"nap_and_va"` (default: `"nap_and_va"`) |
| `schedule.triggerStrategy` (agent) | `"every"`, `"once"`, `"unique_changes"`, `"always"` |
| `schedule.triggerStrategy` (workflow) | `"every"`, `"immediate"`, `"manual"`, `"once"`, `"repeat_every"`, `"unique_changes"` |
| `outputTransformationStrategy` | `"abstract_summary"`, `"custom"`, `"none"`, `"paraphrase"`, `"summary"`, `"summary_for_search_results"` |

### Common Hallucinations to Avoid

| Wrong | Correct |
| --- | --- |
| `"standard"` | `"custom"` (recordType) |
| `"automatic"` | `"autopilot"` (executionMode) |
| `"active"` | `"published"` (state) |
| `"database"` | `"crud"` (tool.type) |
| `versions` (for agents) | `versionDetails` |
| `versionDetails` (for workflows) | `versions` |
| `runAs` (for agents) | `runAsUser` |
| `"nap"` (for workflow triggers) | `"Now Assist Panel"` |
| `acl: "..."` (for agents or workflows) | `securityAcl: { $id, type, roles? }` (mandatory for both) |
| Missing `securityAcl` on workflows | `securityAcl` is mandatory for workflows too, not just agents |
| `securityAcl: { userAccess: 'dynamic_user' }` | `securityAcl: { $id, type: 'Any authenticated user' \| 'Specific role' \| 'Public' }` |
| Missing `$id` at workflow top level | Workflows use `$id` just like agents — always include it |
| `processingMessage` on workflows | Agent-only field — not valid on `AiAgenticWorkflow` |
| `postProcessingMessage` on workflows | Agent-only field — not valid on `AiAgenticWorkflow` |
| `team.description` set manually | Auto-populated from workflow `description` — do not set |
| Manual `inputSchema` | Auto-generated from `inputs` — never set manually |
| `inputs: {...}` for script tools | `inputs: [...]` (array, not object) for script tools |
| `dataAccess` omitted when `runAs` absent (workflow) | `dataAccess` is mandatory for workflows when `runAs` is not set |
| `searchProfile: "profile_name"` (RAG) | `searchProfile: { value: "profile_name", label: "Display Name" }` (ValueLabelType required) |
| `sources: ["table1", "table2"]` (RAG) | `sources: [{ value: "table1", label: "Label1" }, ...]` (ValueLabelType array required) |
| `semanticIndexes: ["index1"]` (RAG) | `semanticIndexes: [{ value: "index1", label: "Label1" }]` (ValueLabelType array required) |
| `fields: ["field1", "field2"]` (RAG) | `fields: [{ value: "field1", label: "Label1" }, ...]` (ValueLabelType array required) |

### Property Naming

Always use camelCase in Fluent config — the plugin converts to snake_case for ServiceNow tables.

| Wrong (snake_case) | Correct (camelCase) |
| --- | --- |
| `memory_scope` | `memoryScope` |
| `sys_domain` | `sysDomain` |
| `run_as_user` | `runAsUser` |
| `role_list` | `roleList` |
| `target_table` | `targetTable` |
| `objective_template` | `objectiveTemplate` |

---

## Error Recovery

| Error Pattern | Category | Resolution |
| --- | --- | --- |
| `dataAccess must have at least one of roleList or roleMap` | Missing roles | Add `dataAccess.roleMap` (role names) or `dataAccess.roleList` (role sys_ids) — required when `runAsUser` / `runAs` is not set |
| `Table not found` | Bad table name | `now-sdk query sys_db_object -q 'name=<table>' -f 'name,label' -o json`. Try `nameLIKE<partial>` to find similar names |
| `Record not found` / `Invalid reference` | Bad sys_id | Query the appropriate table: `now-sdk query sn_aia_agent -q 'name=<name>' -f 'sys_id,name' -o json` (or `sys_user_role`, `sys_user`) |
| `Duplicate name` | Name collision | `now-sdk query sn_aia_agent -q 'nameLIKE<name>' -f 'sys_id,name' -o json` and `now-sdk query sn_aia_usecase -q 'nameLIKE<name>' -f 'sys_id,name' -o json`. Ask user: rename or update existing? |
| ACL / permission error | ACL misconfiguration | Verify `securityAcl` is set correctly. `now-sdk query sys_security_acl -q 'nameLIKE<agent_name>' -f 'sys_id,name,operation' -o json` to verify ACL was generated |
| Build/compile TypeScript error | Code syntax | Read build output for line number. Common: missing comma, wrong type, unmatched brackets |
| Agent deploys but queries return 0 results | Phantom role | `Now.ID` in `roleList` hashes to non-existent sys_id. `now-sdk query sys_user_role -q 'name=<role_name>' -f 'sys_id,name' -o json` to get actual sys_id |

### Rollback via Versioning

1. Set current published version's `state` to `"withdrawn"`
2. Set previous version's `state` to `"published"`
3. Redeploy — agent/workflow uses previous version's instructions

Only one version can be `state: "published"` at a time. For workflows, the published version's `instructions` are automatically written to `base_plan`.

---

## Deployment Checklist

### ACL Configuration

`securityAcl` is **mandatory** on both agents and workflows. The plugin automatically generates `sys_security_acl` and `sys_security_acl_role` records — no separate ACL file or deployment step is needed.

Checklist:

- Set `securityAcl` inline on the agent/workflow — do NOT create a separate ACL file
- Do NOT use the `acl` skill for agent/workflow access control
- Do NOT query `sys_security_acl` to get an ACL sys_id for the agent/workflow
- NEVER leave `securityAcl` empty or omit it

### Deployment Order (Workflows)

1. Create and deploy AI Agents (with `securityAcl`)
2. Retrieve agent sys_ids: `now-sdk query sn_aia_agent -q 'name=<agent_name>' -f 'sys_id,name' -o json`
3. Create and deploy workflow with `securityAcl` and agent sys_ids in `team.members`
4. Verify: `now-sdk query sn_aia_usecase -q 'name=<workflow_name>' -f 'sys_id,name' -o json`

### Post-Deployment Summary

After the final deploy, query for values and provide a summary:

1. **Get instance URL**: `now-sdk query sys_properties -q 'name=instance_name' -f 'value' -o json` → URL is `https://<value>.service-now.com`
2. **Get agent sys_id**: `now-sdk query sn_aia_agent -q 'name=<agent_name>' -f 'sys_id,name' -o json` (use exact match, not `nameLIKE`)
3. **Get workflow sys_id** (if applicable): `now-sdk query sn_aia_usecase -q 'name=<workflow_name>' -f 'sys_id,name' -o json`
4. Generate 2-4 test prompts targeting different tools/instruction steps, including at least one error handling prompt

---

## Avoidance

- **Never use `Now.ID` for roles in `roleList`** — always use `now-sdk query sys_user_role -q 'name=<role>' -f 'sys_id,name' -o json` to get the actual sys_id. `Now.ID` can hash to a sys_id that doesn't match the deployed role's actual sys_id ("phantom role" problem)
- **Never use agent names in workflow `team.members`** — always use agent sys_ids from `now-sdk query sn_aia_agent -q 'name=<agent>' -f 'sys_id,name' -o json`
- **Never add CDATA tags manually** — the plugin handles CDATA wrapping automatically for script fields
- **Never omit `securityAcl`** — it is mandatory on both agents and workflows
- **Never omit `mappedToColumn` on CRUD create/update inputs** — without it, the update silently changes nothing
- **Never omit `returnFields` on CRUD lookup tools** — it is mandatory for lookup operations
- **Never use `runAs` for agents or `runAsUser` for workflows** — agents use `runAsUser`, workflows use `runAs`
- **Never use `versions` for agents or `versionDetails` for workflows** — agents use `versionDetails`, workflows use `versions`
- **Never use `"nap"` for workflow trigger channel** — workflow triggers require `"Now Assist Panel"` (plugin resolves to sys_id)
- **Never use `Record<'messaging_channel'>` for workflow trigger channel** — workflow plugin rejects Record references for `channel`; use plain strings only
- **Never set `team.description` manually on workflows** — auto-populated from workflow `description`
- **Never set `inputSchema` manually** — auto-generated from `inputs`
- **Never omit `recordType: "custom"` on user-created agents, workflows, and tools** — plugin defaults to `"template"` which is reserved for system-managed records
- **Never use CRUD update tools for journal fields** (`work_notes`, `comments`) — these are backed by `sys_journal_field`; always use a Script tool
- **Never pass full sentences to lookup tool search fields** — add keyword extraction guidance in agent instructions
- **Never omit the output format step in instructions** — tools return raw JSON/codes; without a formatting step, raw data is shown to the user
- **Never write "gather from the triggering record" in instructions** — use "from the task" or "from the context" instead
- **Never create a workflow before deploying its agents** — workflow `team.members` requires agent sys_ids which are only available after agent deployment

---

## Database Tables

| Table | Purpose |
| --- | --- |
| `sn_aia_agent` | AI Agent records |
| `sn_aia_agent_config` | Agent configuration and settings |
| `sn_aia_usecase` | AI Agentic Workflow records |
| `sn_aia_usecase_config_override` | Configuration overrides for workflows |
| `sn_aia_team` | Team configuration |
| `sn_aia_team_member` | Team member records |
| `sn_aia_version` | Version information |
| `sn_aia_tool` | Tool definitions |
| `sn_aia_agent_tool_m2m` | Agent-to-tool relationships |
| `sn_aia_trigger_configuration` | Trigger configuration |
| `sn_aia_trigger_agent_usecase_m2m` | Trigger-agent-usecase mappings |
| `sys_agent_access_role_configuration` | Role-based data access controls |
| `sys_security_acl` | ACL records (auto-generated by `securityAcl`) |
| `sys_user_role` | Role records |

---

## Related (from source page)

- query-guide.md — `now-sdk query` syntax for looking up sys_ids, verifying deployments, and resolving role references
- aiagent-api.md — AI Agent API reference (coalesce keys, field mappings, defaults)
- aiagenticworkflow-api.md — AI Agentic Workflow API reference (coalesce keys, field mappings, defaults)
