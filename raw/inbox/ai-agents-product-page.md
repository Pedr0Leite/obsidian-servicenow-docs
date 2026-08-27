<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/products/ai-agents.html -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked with 403 via defuddle/WebFetch, real browser succeeded, no login required) -->
<!-- Marketing/product overview page, not technical documentation. -->

# ServiceNow AI Agents (product page)

"Put AI Agents to work for you — ServiceNow AI Agents act autonomously to get work done. They proactively solve problems and drive exponential productivity in IT, customer service, HR, and every corner of your business."

**Announcement**: Meet ServiceNow Otto, the AI assistant for work — "You ask. ServiceNow Otto handles it end to end, following how your business operates. It works across every system, every department, and every workflow that keeps your business moving." (Confirms the Now Assist → ServiceNow Otto rebrand seen elsewhere in this batch is a full product-line rename, not just a UI label change.)

## How ServiceNow AI Agents work (concept glossary from the page)

- **Agentic workflows** — the overall business objective (the *why*). E.g. triaging cases or categorizing incidents.
- **AI Agent Orchestrator** — coordinates collaboration among teams of AI agents to achieve goals; agent teams outperform single agents on simple-to-complex workflows.
- **AI Agent Studio** — development tool to build/customize AI agents: specialized agents, guardrails, task automation via natural-language interface.
- **ServiceNow AI Control Tower** — central intelligent hub connecting AI strategy, governance, and management across the enterprise (works with internally-built or 3rd-party AI).
- **Roles** — an AI agent's role defines purpose, objectives, behavior, interaction with users — set in natural language, not code.
- **Tools** — technologies/resources agents use to perform tasks (flow actions, subflows, scripts, skills).
- **ServiceNow Otto** — ask via chat/voice/mobile/web; handles work on the platform that already runs the business.
- **AI Agent Fabric** — embeds Agent2Agent (A2A) protocol for ServiceNow ↔ third-party agent communication; agents get context from external tools/data/systems via Model Context Protocol (MCP).
- **Data** — agents use business data (knowledge articles, historical incidents/cases, CMDB CIs, other systems via Workflow Data Fabric) for personalization.
- **AI Agent Advisor** — analyzes business data, surfaces highest-impact opportunities, builds/proves agents before deployment.
- **Autonomous Workforce** — AI specialists assigned to roles with business context/permissions, orchestrating teams of AI agents to deliver outcomes start-to-finish (positioned as scaling teams on-demand).

## FAQ (from the page)

**What is an AI agent?** Can make decisions, take actions, interact with environment without continuous human intervention; adapts to new info, learns over time, manages tasks beyond traditional automation. ServiceNow AI Agents work as teams guided by the AI Agent Orchestrator.

**How do AI agents work?** Define goals/plan tasks within an agentic workflow → gather data from various sources → reason/decide → use tools (scripts, flows, generative AI skills) to execute → monitor results, incorporate feedback, adapt → continuous learning/improvement over time.

**Types of AI agents**: two fast-growing categories — **voice agents** (fluent, human-like conversation, real-time collaboration) and **web agents** (automate work by interacting with web interfaces like a human in the browser — unlocks automation for hard-to-reach 3rd-party apps without APIs, removes integration overhead).

**How are AI agents built?**
1. Define role, goals, success metrics
2. Select an LLM + orchestration framework for logic/workflows
3. Equip with tools: APIs for actions, knowledge bases; MCP (via AI Agent Fabric) for external tools/resources; RAG for contextual understanding
4. Test rigorously for safety/reliability, then deploy
5. Monitor performance, gather feedback, iterate to enhance skills/business impact

**How can I get ServiceNow AI Agents?** Embedded in the ServiceNow AI Platform, business-ready from day one. Build custom agents via natural language in AI Agent Studio, or deploy prebuilt agents — all secured/governed by AI Control Tower.

## Why this might matter to this vault

Mostly marketing framing rather than technical detail, but the **web agents** concept ("interacting with web interfaces like a human, unlocking automation for hard-to-reach 3rd-party apps without APIs") is a notably different capability than anything in [[Proactive Customer Case Communicator]] or [[partner-case-summary-agent]] — both of those stay entirely inside ServiceNow's own data model. Confirms the AI Agent Fabric / MCP / A2A concepts already referenced in the [[Now Assist Readiness Evaluation - Architecture Deep Dive]] licensing section and the SDK guide's tool-type table are current, actively-marketed platform capabilities, not experimental.
