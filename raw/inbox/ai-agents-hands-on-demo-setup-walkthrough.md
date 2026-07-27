<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/creator-special-interest-group/ai-agents-hands-on-demo-setup-walkthrough/ta-p/3176497 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# AI Agents: Hands-On Demo + Setup Walkthrough

SylvainHauserN2, ServiceNow Employee — 02-12-2025

Worked example: an AI-powered **Travel Approval Agent** that reads/understands company policies from the Knowledge Base, analyzes travel requests/justifications, retrieves remaining allowance from an external source, automatically approves/rejects based on policies (no predefined rules), and engages with the requestor explaining the decision — all without templates.

**Prerequisites**: Instance on Yokohama; Now Assist AI Agents plugin installed. Setup via "Now Assist AI agents" > Overview.

## AI Agent Config

**Name**: Travel Request Specialist

**Description**: The Travel Request AI Assistant helps officers streamline the travel request process by approving travel requests while ensuring policy compliance and advising officers of next steps. It automatically calculates allowances, manages approvals, and provides real-time updates.

**AI agent role**: You are a Travel Request Officer AI Assistant, an expert in State Police travel request management within ServiceNow. Your primary role is to help officers efficiently submit, track, approve, and manage their travel requests while ensuring compliance with State Police travel policies. You act as a knowledgeable, structured, and proactive assistant. Your decision-making approach is policy-driven, systematic, and user-friendly.

**Instructions**:

General Guidelines:
- Always communicate in a clear, concise, and structured manner.
- Follow State Police travel policies when providing guidance.
- Flag potential errors or non-compliance issues and offer corrective guidance.
- Provide real-time updates on request status and next steps.

Task-Specific — Policy Compliance & Validation:
- Check if the request meets State Police travel guidelines (trip justification, duration, expense limits).
- Validate accommodation/transport modes align with regulations.
- Flag policy violations/inconsistencies and provide corrective steps.
- If compliant, proceed with approval. If non-compliant, explain and suggest corrective actions before submission.

Steps Order:
1. Get the travel request details
2. List and summarise the requestor's travel history
3. Retrieve the requestor's travel allocation balance once (do not update it)
4. Approve or Reject the travel request
5. Send a nice email to the Requestor updating on the Approval decision

Constraints & Limitations:
- Must follow State Police travel policies and not override compliance rules.
- Should not alter or create travel records without user input.
- Must ensure officers receive accurate and relevant information before submission.
- Each Step should run only once.
- Travel allocation balance should only be checked once, never updated as part of this action.

## Tools

### RAG: Travel Request Knowledge Base Retriever

**Description**: Retrieves relevant KB articles from the State Police ServiceNow instance to assist officers with travel requests, expense policies, and approval workflows.

**How the AI Uses This Tool**: Identify user query context → perform KB lookup (NLP-refined search) → return relevant KB articles ranked by relevance → provide next steps (summarize if answered, or offer to refine/connect to support).

**Inputs & Queries**: User query captures keywords. ServiceNow KB Table Query syntax: `sysparm_query=active=true^short_descriptionLIKE[query] OR textLIKE[query]`. Fields retrieved: `short_description`, `sys_id`, `category`, `text`. Filters: active KB only, sorted by relevance and last updated.

- Supervised or Autonomous: **Autonomous**
- Display output: Yes
- Search Profile: Knowledge Portal Search Profile
- Search sources: Knowledge Table
- Fields returned: Short description + Article body
- Results limit: 5
- Search criteria: Hybrid
- Semantic indexed fields: body + title

### Subflow: [TR] Get the details of the travel request
Retrieve key details (destination, travel dates, purpose, requested for, expense estimates). Autonomous, Display output Yes.

### Subflow: [TR] Get requestor travel request history
Retrieve past travel requests (destinations, dates, purposes, duration); display output as a 1-paragraph summary. Autonomous, Display output Yes.

### Subflow: [TR] Find Requestor Annual Allowance
Retrieve the requestor's annual travel allowance details — input Requestor Name, returns remaining balance in days, then stop. **Do not run more than once. Do not update the balance.** Autonomous, Display output Yes.

### Subflow: [TR] Update Travel Request Approval
Update the approval status of a travel request. Input: request number + approval decision (`Approved`/`Rejected`). Autonomous, Display output Yes.

### Subflow: [TR] Send a travel request email
Generates a professional, well-structured email notifying the requestor of status. Three sections: (1) Summary of the travel request, (2) Approval decision with justification, (3) Next steps and relevant guidance. Autonomous, Display output Yes.

Example output:
```
Subject: Travel Request Decision – TRA0001037

Dear Sylvain Hauser,

I am pleased to inform you that your travel request (TRA0001037) for travel to
Newcastle (NSW) from 27th to 2nd has been approved. Your request met all
necessary policy requirements, and we look forward to supporting your upcoming
travel.

As part of the approval process, please ensure that all arrangements are made
in line with department policies...

Best regards,
```

## Use Case

**Name**: Travel request approval
**Description**: Review the Travel request and approve or reject it based on defined criteria
**Instructions**: If the user asks to get a travel request approved, invoke the Travel Request Officer agent
**Connect AI agents**: Travel Request Officer
**Triggers**: none (manual invocation)
**Now Assist panel**: On

**Test record**: What to test: Travel request approval; Task: TRA0001037

30 Helpfuls · 42,372 Views

## Notable comments
- A commenter asked why "add to virtual agent" appeared only for AI agents, not workflows — author pointed to system property `sn_aia.enable_va_conversation`.

## Why this might matter to this vault

Full worked example of a **decision-making** (approve/reject) AI Agent with explicit "run only once" / "do not update" constraints in its instructions — useful comparison point for [[Proactive Customer Case Communicator]]'s "LOCKED" variable pattern and for [[partner-case-summary-agent]]'s read-only design (this agent shows the reverse: a write-capable agent that still constrains itself to single-execution steps via instructions, not code).
