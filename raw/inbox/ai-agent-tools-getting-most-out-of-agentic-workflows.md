<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/ai-agent-tools-getting-the-most-out-of-your-agentic-workflows/ta-p/3227648 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# AI Agent tools — Getting the most out of your agentic workflows

Victor Chen, ServiceNow Employee — updated as of Yokohama Patch 8

## General tool settings

- **Name and Description** — the orchestrator uses these to decide whether/how to use the tool.
- **Input** — Script/Record operation tools support input variables with a description, referenced in the action.
- **Supervised/Autonomous** — whether to ask the user permission before running.
- **Display Output** — shows the action's output to the end-user.
- **Output transformation strategy** — verbosity control. "None" = raw output (JSON/technical), good for surfacing specific records/IDs. "Verbose" = longer, more eloquent answer.

All tools currently only input/output **String**. Safety mechanism: `sn_aia.continuous_tool_execution_limit` caps how many times a given tool can run. Number of tool (action) executions determines assists consumed.

> **Yokohama Patch 1 gotcha**: duplicating an AI Agent leaves the tools in the new agent still pointing at the **original** agent's tools! To avoid affecting the original, remove the tool and add a new one — screenshot/note the original tool config first.

## Tool types

- **Catalog Item** — only conversational catalog items available (e.g. a holiday-booking agent presenting a visa catalog item).
- **Conversational topic** — only LLM-based Virtual Agent topics/topic blocks that are active and published; setup topics not available.
- **File Upload** — DOC/PDF/TXT read for specialized questions; brief wait while document is extracted after saving.
- **Knowledge Graph** — e.g. Enterprise Graph / Enterprise Graph (Small), for unstructured or personnel-related data.
- **Sub-flow/Flow Action** — from Workflow Studio; description should note expected inputs/outputs; flow inputs/outputs must be String or the orchestrator can't process it. Integration Hub spokes are now also AI Agents (their tools optimized for AI Agent processing).
- **Now Assist skill** — OOB or custom Skill Kit skill; description should note expected inputs/outputs.
- **Record operation** — create/lookup/update/delete. Lookup: select table + condition (similar builder to Workflow Studio); only String output, no record cards; "Verbose" output strategy for better-formatted lists. Update: select table + condition + field/value(s); Inputs let the AI Agent ask the end-user which records/how, referenced via `{{...}}`. **Reference fields, or fields not on the table, are not supported.**
- **Script** — can include end-user or agent-provided inputs (e.g. `inputs.inc_number`).
- **Desktop Action** — repetitive desktop tasks.
- **Search Retrieval** — AI Search/RAG; select Search profile, sources, fields. Recommend "Hybrid" search criteria (semantic + keyword). Semantic indexed fields come from the search source's Indexed sources. If issues: confirm Now Assist in Search store app is updated, AI Search configured, sources indexed, search profile published.
- **Web Search** — auto-configured as of Yokohama Patch 6; calls an external LLM (default Gemini) + tools. Use Output strategy to control result quality/length.
- **MCP** — see "Enable MCP and A2A for your agentic workflows" article.

## Notable Q&A from comments

- **sandeep_singhal**: Record operation "create" doesn't allow `{{ input }}` templating in input field value (unresolved as of fetch, no reply shown).
- **Ash-ITSM**: no official docs page describes "Output Transformation Strategy" option meanings — flagged as a possible documentation gap.
- **stevenatwork / JT8 exchange (script tool output)**: a script tool ran and logged correctly (`gs.info`) but the agent reported the result as empty. Root cause pattern demonstrated by JT8:
  - Just updating agent *instructions* to "display the message that was logged" does NOT work — the agent can't see what `gs.info()` wrote to the system log; it only sees what the script's `return` statement gives back.
  - **Fix**: the script must explicitly build and `return` an `outputs` object containing the value to surface, e.g.:
    ```javascript
    (function(inputs) {
      var logMsg = 'Here are some details about the' + inputs.case_number;
      gs.info(logMsg);
      var outputs = {};
      outputs.log_message = logMsg;
      return outputs; // {"log_message":"Here are some details about theHRC0012345"}
    })(inputs);
    ```
  - stevenatwork's actual root cause turned out to be **hidden zero-width space characters (`​`)** in the source field value, breaking downstream logic/output — fixed with `.trim().split('​').join('')`.
- **Shane Brazeal2**: File Upload tool missing on Yokohama Patch 3 — Victor Chen: update store apps/plugins to latest (update the main "Now Assist for ITSM"/HRSD app, which cascades).
- **vermaamit16**: asked for server-side APIs to trigger AI Agents from a UI action button click (no direct answer in this thread).
- **samhithdamani / vermaamit16**: invoking agents from Virtual Agent chat in a portal — enable "Now Assist for Virtual Agent" default assistant under Conversational Interfaces → Assistants, then enable Display for the AI Agent under Select Display, granting access roles.

18 Helpfuls · 36,365 Views

## Why this might matter to this vault

The **script-tool-output** gotcha (a script can `gs.info()` something but the agent only ever sees what's explicitly `return`ed as an `outputs` object) is directly relevant to any custom Script tool design in [[partner-case-summary-agent-architecture]]'s `PartnerCaseSummaryUtil` Script Include — confirms the design's `{answer, effort}`-style explicit return shape (also seen in the [[Now Assist Readiness Evaluation - Architecture Deep Dive]] question-script pattern) is the *correct*, necessary pattern, not just a style convention. The zero-width-space debugging story is a good concrete "what a silently-empty tool output actually looks like in practice" case study.
