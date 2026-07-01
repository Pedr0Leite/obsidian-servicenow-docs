# AI Agents: Troubleshooting, Debugging & Best Practices

*Structured knowledge base extracted from ServiceNow CCL6230-K26 (Knowledge 2026)*

**Source:** Inside the Black Box — Troubleshooting and Debugging AI Agents at Scale

---

## DOCUMENT METADATA

| Field | Value |
|---|---|
| PURPOSE | Machine-readable knowledge base for Claude projects. Structured for programmatic consumption. |
| SOURCE | ServiceNow Knowledge 2026 Lab CCL6230-K26 (gitbook) |
| PLATFORM | ServiceNow Now Assist AI Agents — Zurich release |
| SCOPE | AI Agent failure modes, debugging frameworks, performance optimization, security, tool design patterns |

## SECTION 1: AI AGENT FAILURE MODE TAXONOMY

### 1.1 FAILURE_CATEGORY: PLATFORM

#### Symptom: Cold Start Failure
- Agent failed to start; execution never reached ReAct loop.
- Root causes:
  - Missing platform configuration or dependencies
  - Auth and access issues
  - Invalid credentials
  - ACL-trigger misalignment

### 1.2 FAILURE_CATEGORY: CONFIGURATION

#### Symptom: Tool Errors
- Tool calls fail or return unexpected results.

#### Symptom: High Latency Responses
- Tool payloads too large.
- Prompt bloat.
- Scratchpad growth across ReAct turns.

### 1.3 FAILURE_CATEGORY: INSTRUCTIONS

#### Symptoms
- Inconsistent responses
- Hallucinated responses
- Infinite loops

---

## SECTION 2–10

The remainder of the document covers:

- Failure mode quick reference tables
- ReAct loop execution architecture
- Runtime tables (sn_aia_execution_plan, sn_aia_execution_task, etc.)
- Access control architecture and role masking
- Performance optimization framework
- Smart tool design framework
- Step-by-step debugging runbook
- Security, monitoring, and design principles
- Platform dependencies and version matrix
- Visual reference descriptions
- Deployment configuration checklist

> Note: This markdown file is a converted version of the uploaded knowledge-base document and preserves the document structure in Markdown format.

Reference: turn1search1
