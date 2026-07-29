<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/ai-agents-faq-and-troubleshooting/ta-p/3200454 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# AI Agents FAQ and Troubleshooting

Victor Chen, ServiceNow Employee — updated March 2026, for Yokohama Patch 11 / Zurich Patch 5

## What's an AI Agent at ServiceNow?
Autonomous systems that interact with their environment to gather data, make decisions, and complete tasks that would otherwise need a human.

## Licensing / prerequisites
- License: Pro Plus or Enterprise Plus SKU.
- Yokohama Patch 1+ or Xanadu Patch 7+ (Zurich recommended), with Now Assist for ITSM/HRSD/... and AI Agents store apps installed. Admins need `sn_aia.admin`. AI Search and Now Assist Panel must be enabled. Latest store app version as of March 2026: 6.1.11. Installable via the Now Assist Suite bundle.
- **Is my instance ready?** Use the **Now Assist Readiness Evaluation** store app.

## Terminology
- **Agentic workflow** = the *why* (overall business problem/goal).
- **Agent** = the *who* (virtual worker performing specific tasks).
- **Tools** = operations the agent runs to perform actions.

## LLM
Default: Azure OpenAI's GPT-OSS on ServiceNow-managed Azure servers, orchestration layer. Context window: 128K tokens (exceeding may cause unpredictable behavior). Configurable to NowLLM, Claude, Gemini as of Yokohama Patch 6+/Zurich Patch 1+. Using a ServiceNow-hosted 3rd-party model doesn't create additional charges; BYOK or a separate agent/model not hosted by ServiceNow may.

## Instruction length limits
- AI Agent Role: max 2,000 chars
- AI Agent Instructions: max 8,000 chars

## 3rd-party LLM/agent connections
Via subflows/actions tools as integration. More seamless communication via MCP and A2A also available.

## Assist consumption
Based on number of actions run (not orchestrator/communicator agent actions). Bucketed "Small"/"Medium"/"Large" — see ServiceNow Assists Overview. Sub-prod usage/testing in AI Agent Studio also consumes assists; monitor via AI Agent Studio analytics.

Skills/VA topics/conversational catalog items run *as a tool inside* an agentic workflow do NOT separately consume assists (the workflow run itself still does, per Small/Medium/Large).

## PDI availability
Not available in PDIs.

## Hallucination mitigation
"Human on the loop" model — humans monitor, intervene when necessary (supervisory, not always active). Service agents can review AI-generated plans, provide feedback/explicit approval before execution. Now Assist Guardian provides prompt injection protection. Grounded prompt templates tie prompts to platform data + RAG. Skill Kit supports same grounding; temperature setting affects groundedness. Hallucinations remain possible with any generative AI.

## Triggers
Created via condition/objective when creating an Agent or Agentic Workflow. Can also trigger via database changes or user query.

## Feedback loop
During interaction, agent may ask for feedback/permission to proceed and change approach accordingly.

## Object/field recognition
Yes — AI Agents recognize ServiceNow objects (table names, field names) in instructions.

## Languages
All Now LLM-supported languages.

## GCC/self-hosted
Supported as of July 2025, with NowLLM.

## Domain separation
Yes — `sys_domain` field exists on all agent tables, gets `sys_domain_path` if domain separation is enabled.

## Data passing between tools/agents
Stored in short-term memory, passed via instructions (both within an agent between tools, and between agents). Data transfer is LLM-mediated and may change — instruct agents to be exact when passing data; in Tools UI, set LLM strategy to "None" to minimize.

## OOB agents
ITSM, HRSD, CRM workflows each ship OOB agents.

## "No agents are available at the moment" error
Usually: Agent proficiency not filled/inaccurate, AI Search not enabled, orchestrator token count exceeded, agent prompts not descriptive enough. Check Agents/tools (Skills) are Active.

## "AI Agent states it can no longer execute a tool"
Check `sn_aia.continuous_tool_execution_limit` — controls max continuous, uninterrupted executions for the same tool.

## Virtual Agent + Agentic Workflows/AI Agents
Yes, NA in VA can run AI Agents. You **cannot discover** an agentic workflow in VA by typing e.g. "help resolve INCxxx" — you can only *trigger* a workflow to appear in NA VA (e.g. create an INC, workflow runs in VA). Requires "Agentic Support" toggle in Assistants > Settings. In AI Agent Studio, Virtual Agent experience toggle must be on for the AI Agent. Agent description/role must be detailed enough to match user query. Recommended model provider for the AI Agents skill group: Azure OpenAI.

## NAP 2-hour timeout
Check "Conversation Idle Timeout" for the NAP (`sys_cs_channel` record) and property `com.glide.cs.conversation_idle_timeout` (Global, applies to Virtual Agent as a whole, not just AI Agents).

## Performance
For agents analyzing lots of data, use Skill Kit to build a speed-optimizing skill (limits LLM calls). More tools/agents in a use case may degrade orchestration performance — don't recommend >15.

## Pre-production evaluation
AI Agent Studio includes an **Agentic Evaluation** tool. Create an evaluation job, define a dataset of representative historical records (20–100 recommended), run evaluation. Scores task completeness, tool calling correctness, faithfulness.

## Non-determinism
AI Agents/generative AI are non-deterministic — running the same input twice may give different results.

## Learn more
Documentation link, Now Learning course, "Now Assist AI Agents prompting guide", "Agentic workflows End to End Setup Guide".

## Notable Q&A from comments

- **Token limit / GPT-4.1 constrained to 4,096 tokens in AI Agent Studio (SteveGHarland)**: reports a fatal ReAct-parser error when the response exceeds a 4,096-token limit configured within the system, despite the documented 128K context window — an unresolved discrepancy raised in the comments (no official reply as of fetch). This directly evidences the "long-context / token-limit" risk flagged elsewhere.
- **Requestor-facing Agentic AI via Virtual Agent** (Tae Kyung Lee, 03-2025): asked when AI Agents would be usable from the requestor side (not just agent-facing). Victor Chen confirmed (05-2025) "AI Agents for the Requestor Experience (Now Assist in Virtual Agent) is now available in Yokohama Patch 3/Xanadu Patch 9."
- **Connecting to a live agent from within an AI Agent** (HarshaSeetha): create a Virtual Agent topic containing `vaSystem.connectToAgent()`, add it as a Conversational Topic Tool. Works, but the tool's status indicator can stay "Ongoing" (blue) even after the live-agent conversation ends and the AI agent execution finishes — a cosmetic/state-tracking bug noted but not resolved in-thread.
- **UI Action triggering AI Agents (vermaamit16)**: asked about server-side APIs to trigger an AI Agent from a UI action button click — no direct answer given in this thread (see the companion "Bring AI Agents on the Forms" thread for a fuller answer).
- **Invoking agents from Virtual Agent chat in a portal (samhithdamani / vermaamit16)**: AI Agents are only available within Assistants supporting LLM-based topics — enable via Conversational Interfaces → Assistants → enable default "Now Assist for Virtual Agent", then enable Display for the AI Agent under Select Display, with roles granted access.

19 Helpfuls · 54,218 Views

## Why this might matter to this vault

Confirms/extends several risks already flagged in [[Proactive Customer Case Communicator]] and [[partner-case-summary-agent-architecture]]: the 128K context window ceiling (relevant to PCCC's "large-context / token limits" open risk), the NAP idle-timeout property (`com.glide.cs.conversation_idle_timeout`, matches PCCC's "AIPF_NAP conversation idle timeout" deployment note — this FAQ confirms it's a **Global** property, not agent-specific, meaning changing it for PCCC affects all Virtual Agent conversations instance-wide), and the "Now Assist Readiness Evaluation" store app cross-reference (already covered in [[Now Assist Readiness Evaluation - Architecture Deep Dive]]).
