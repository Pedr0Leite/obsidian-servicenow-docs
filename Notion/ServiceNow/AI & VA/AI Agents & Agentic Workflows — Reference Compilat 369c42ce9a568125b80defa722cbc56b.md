---
aliases:
  - "AI Agents & Agentic Workflows — Reference Compilat"
tags:
  - ai-agents
  - agentic-workflow
  - genai
  - ai-agent-studio
  - now-intelligence
---

# AI Agents & Agentic Workflows — Reference Compilation

# Sources

- [Gen AI Skills, AI Agents & Agentic Workflows for FSO](https://www.servicenow.com/community/fso-articles/gen-ai-skills-ai-agents-amp-agentic-workflows-for-fso/ta-p/3500995) — ServiceNow Community (FSO-specific)
- [Deep Dive into AI Agents & Agentic Automation in the Zurich Release](https://www.servicenow.com/community/upgrades-and-patching-forum/deep-dive-into-ai-agents-amp-agentic-automation-in-the/m-p/3444288) — ServiceNow Community
- [Exploring Now Assist AI Agents](https://www.servicenow.com/docs/r/xanadu/intelligent-experiences/exploring-ai-agents.html) — Official Docs (Xanadu)

---

# Core Concepts

## Gen AI Skill

A purpose-built, prompt-driven capability using generative AI to assist agents within their workspace. Designed for **focused, single-step tasks** — surfacing a summary, drafting a response, or generating a recommendation — without autonomous multi-step reasoning.

> Skills reduce cognitive load on agents by delivering the right information at the right moment, keeping humans firmly in control.
> 

## AI Agent

An autonomous capability that can **reason, take actions, and produce outcomes** on behalf of a user for a specific task or decision point. Unlike a Gen AI Skill, an AI Agent doesn't just surface information — it actively evaluates context and executes actions.

Key characteristics:

- Operates independently, focused on a single domain or step
- Can investigate, classify, recommend, or communicate
- Building blocks of more complex agentic workflows
- In Zurich: capable of **perceiving** (NL, data, signals), **reasoning** (constraints, dependencies), **acting** (cross-system execution), and **learning** (adapting from feedback)

## Agentic Workflow

Multiple AI Agents coordinated by an **orchestrator** to complete a broader, multi-step process end-to-end. The orchestrator determines which agents to invoke, in what sequence, and how to pass context between them.

> **Key distinction:** If there's an orchestrator directing a team of agents → Agentic Workflow. If a single agent is acting on its own → individual AI Agent.
> 

---

# Platform Architecture (Zurich Release)

## AI Agent Studio

Visual + conversational development environment for building agents.

- Define goals → agents pioneer the workflows
- Provide governance → ensure safe boundaries
- Integrate skills across ITSM, HRSD, CSM, SecOps, etc.

## Vibe Coding (Natural Language Workflow Generation)

Users describe what they want in plain language → the agent builds the workflow → users refine → platform secures it. Results in rapid AI delivery cycles with reduced technical complexity.

## AI Agent Fabric & Collaboration Layer

Agents can pass tasks between each other, negotiate execution routes, re-plan if conditions change, and form **agent teams** — analogous to cross-functional squads. Enables digital workforce management.

## AI Control Tower

Governance cockpit for autonomous operations:

| Capability | Benefit |
| --- | --- |
| Behavioral insights | Transparency into decision pathways |
| Guardrails & policies | Compliance, safety, and impact control |
| Lifecycle governance | Enterprise-scale rollout management |
| Auditability | Every machine action is traceable |

## Process + Task Mining Integration

AI agents get visibility into real operational flows: detect bottlenecks, identify improvement opportunities, execute optimization actions, and validate impact through closed-loop learning.

---

# Trust & Security

- Data boundary enforcement
- Agent role-based identity (Machine Identity Console)
- Ethical AI guardrails
- Change tracking + forensic auditability
- Sandboxing to prevent data leakage

---

# FSO-Specific: Out-of-the-Box Gen AI Skills

> FSO is built on top of CSM — customers automatically inherit all Now Assist for CSM capabilities. These are FSO-specific additions.
> 

## Dispute Case Summarization

Condenses a dispute record into a concise, high-level summary for agents to understand a case at a glance. Uses a tailored prompt covering a wide array of dispute categories, surfaced within the agent workspace.

## Claims Case Summarization

Condenses a claim record into a brief, high-level summary to help claims adjusters quickly find information. Addresses specific lines of business via tailored inputs and prompts. Accessible from the Now Assist panel.

## Disputes Intake via Virtual Agent

Enables cardholders to report a dispute through conversational AI. Key capabilities:

- Asks contextually appropriate questions; rephrases if customer response is unclear
- Navigates card network rules and issuer policies to determine required information
- Pulls transaction data from core banking systems
- Accepts supporting files (photos, emails)
- Flags ineligible deflection cases based on network rules
- Collects required customer consents before proceeding
- Stores full conversation log on the case for auditability
- Model is grounded in pre-defined intake requirements — cannot go off-topic

---

# FSO-Specific: Out-of-the-Box Agentic Workflows

## Resolving Friendly Fraud Disputes

Automated workflow for friendly fraud dispute resolution:

- Automatically gathers transaction and customer data
- Applies predefined decision rules to validate the dispute
- Supports **Visa CE 3.0** compliance — gathers and validates qualified transaction data (prior eligible transactions, device/IP data, matching payment credentials) to contest first-party misuse and shift dispute liability from issuer to merchant
- Initiates refund processing or case escalation when required
- Provides notifications and reporting throughout

## Resolving ACH Disputes (4-Agent Team)

Orchestrated team of four AI agents for ACH dispute resolution. Architecture is **extensible** to other payment types (wire transfers, P2P, check disputes).

| Agent | Responsibility |
| --- | --- |
| Merchant Analysis for Disputes | Investigates the merchant; produces merchant credibility outcome |
| Nacha Operating Guidelines Check | Applies Nacha guidelines to determine eligibility and compliance |
| ACH Dispute Return Recommendation | Draws on merchant analysis, Nacha check, and similar past cases to recommend dispute outcome |
| Dispute Communication | Communicates outcome to customer or merchant's bank; creates tracking task |

The workflow auto-gathers ACH transaction, authorization, and customer account data; applies regulatory criteria; initiates provisional credit issuance, return processing, or escalation; and produces full audit trails.

---

# Enterprise Use Cases by Domain (Zurich)

| Domain | AI Agent Capabilities | Business Impact |
| --- | --- | --- |
| ITSM | Root-cause resolution, change conflict prediction, self-healing tickets | Prevent outages, reduce MTTR |
| HRSD | Eligibility automation, policy interpretations, validated case handling | Lower case volume, improved SLA |
| CSM | Autonomous customer case triage & fulfillment | 24/7 digital-first CX |
| Security | Automated alert investigation & remediation | Stronger security posture |
| Operations | Predictive resource optimization | Reduced ops cost + downtime |

---

# Further Reading

- [Now Assist for CSM: Agentic Workflows and AI Agents](https://www.servicenow.com/community/csm-articles/now-assist-for-csm-agentic-workflows-and-ai-agents/ta-p/3341816)
- [Introducing AI Agents and Quick Start Guide](https://www.servicenow.com/community/now-assist-articles/introducing-ai-agents-and-quick-start-guide/ta-p/3200447)
- [When to Use AI Agents: Rationalizing Use Cases](https://www.servicenow.com/community/now-assist-articles/when-to-use-ai-agents-rationalizing-uses-cases-for-workflows/ta-p/3340584)
- [Create Your Own AI Agent: Walkthrough Using AI Agent Studio](https://www.servicenow.com/community/now-assist-articles/create-your-own-ai-agent-a-walkthrough-on-creating-an-ai-agent/ta-p/3208901)
- [AI Agents FAQ and Troubleshooting](https://www.servicenow.com/community/now-assist-articles/ai-agents-faq-and-troubleshooting/ta-p/3200454)
- [Now Assist for FSO — Store App](https://store.servicenow.com/store/app/191caf2e1b246a50a85b16db234bcbeb)

## Related

- [[Agentic Workflow & AI Agents]]
- [[Get Familiar with Agentic Workflows & AI Agent]]
- [[Best Practices for Creating AI Agent Workflows]]
- [[Introducing AI Agents and Quick Start Guide]]
- [[GAF]]
- [[Now Assist]]