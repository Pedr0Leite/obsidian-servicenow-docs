<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/virtual-agent-forum/ai-agent-to-fetch-data-from-custom-table-and-return-couple/m-p/3429630 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# AI Agent to fetch data from custom table and return a couple results based on the query

AlpUtkuM, Mega Sage — 11-18-2025

**Question**: wants AI Agent(s) to query a couple of custom tables and return results based on the query — e.g. a user wants to see approval levels/approvers defined for a specific division/region. Wants users interacting via Virtual Agent.

**Reply (JK9903, Giga Guru)**: An AI agent can't do this automatically on its own — create a tool (script, flow, or action) that returns what's needed. The AI agent acts as a bridge between the user and the tool: takes user input, invokes the tool, shows the result. Once the AI agent is configured, use the AI connector in VA to call it (make sure VA is enabled on the AI agent).

**Reply (warren_chan, ServiceNow Employee)**: Confirms yes, an AI agent tool can do this — but pushes back on whether Agentic AI is even the right approach:

> I would just argue that it's a poor use case for Agentic AI as what you're seeking is maybe not fully deterministic, but pretty close to it. You will do just fine with conventional tools like scripting or AI search. For Agentic AI to be truly powerful, you want to leverage its ability to think/plan/reason.

0 Helpfuls · 1,032 Views

## Why this might matter to this vault

Directly relevant design-justification data point for [[partner-case-summary-agent]]: this is nearly the same shape of ask ("fetch data from a table based on a query, return results to the user via a conversational surface"), and a ServiceNow employee explicitly argues that pattern alone is a "poor use case for Agentic AI" — better served by scripting/AI Search — unless there's real reasoning/planning value. This is a useful sanity check: Partner Case Summary Agent's *data retrieval* step (case/account lookup) is indeed close to deterministic and could arguably be plain scripting, but its **summarization** step (turning raw case data into a 2-3 line prose summary judging status/next-steps/blockers) is exactly the "think" part that justifies the LLM/agent framework rather than a plain script or report. Worth citing this tension explicitly if the design is ever challenged on "why use an AI Agent for this at all."
