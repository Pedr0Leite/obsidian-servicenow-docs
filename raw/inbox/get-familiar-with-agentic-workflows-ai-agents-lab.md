<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/developer-articles/get-familiar-with-agentic-workflows-amp-ai-agent/ta-p/3326559 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Get Familiar with Agentic Workflows & AI Agent (hands-on lab)

Luis Estéfano, ServiceNow Employee — created 11 August 2025

Full hands-on lab exploring OOB AI Agents/Agentic Workflows, then duplicating/modifying them and adding a new agent, culminating in deploying to the Now Assist Panel.

## Prerequisites

- **License**: Now Assist License (Pro Plus/Enterprise Plus)
- **Plugins**: AI Agents store app + all "Now Assist for..." dependency apps, latest versions, "Load demo data" selected. If plugin version conflicts, repair (in order):
  1. Flow designer (20 plugins)
  2. Microsoft Azure OpenAI Generative AI Spoke (`sn_azure_openai`)
  3. Generative AI Controller (`sn_generative_ai`)
  4. Now Assist AI Agent (`sn_aia`)
  5. Now Assist for [Product Name] (e.g. `sn_itsm_gen_ai`)
  6. Now Assist for Spokes (`sn_assist_spokes`)
  7. Now Assist for Platform (`sn_genai_platform`)
  8. Now Assist in AI Search (`sn_ais_assist`)
  9. Now Assist in Virtual Agent (`sn_nowassist_va`)
  10. Now Assist Platform Skills (`sn_nowassist_gs`)
  11. Now Assist for Creator (`sn_now_creator`)
  12. All dependent plugins requiring update
- **AI Search**: enable, check status at AI Search > AI Search Status
- **Now Assist Panel**: Now Assist Admin > Experiences > Applications > Now Assist panel > Summary widget > Turn on. Requires at least one Now Assist product plugin (ITSM/HRSD/CSM/SecOps) active.
- **Roles**: admin user needs `sn_aia.admin`, `sn_nowassist_admin.nsa_admin`
- **Data Quality**: ticket data and knowledge base need accurate, up-to-date info for best results

## Considerations (version pinned)

- Release: YP4 [glide-yokohama-12-18-2024__patch4-05-14-2025]
- Generative AI Controller (`sn_generative_ai`): v10.0.8
- Now Assist in AI Search (`sn_ais_assist`): v11.0.14
- Now Assist AI Agents (`sn_aia`): v4.0.37
- AI Agents Platform Usecase (`sn_aia_uc`): v1.0.5
- Naming note: "Agentic Workflow" replaced the original "Use Case" label used in the first release.

## Lab Goal

Understand how OOB AI Agents generate resolution plans, inspect behavior, familiarize with AI Agent Studio tools. Activate/explore the default "Generate resolution plans" Agentic Workflow, then modify it to write logs and automatically create a Change Request.

## Exercise 1: Exploring the Agentic Workflow

All > AI Agent Studio > Overview > Agentic Workflow sub-tab > select "Generate resolution plans" (OOB, read-only protection policy).

Fields: **Name** (business challenge), **Description** (brief problem summary), **Instructions** (guided actions for the AI agent — this field is AI Instruction, directly tied to LLM input).

**Connect AI agents** section — agents mapped to this workflow:
- **Record management AI agent** — fetch/create/update record with provided details
- **Next action recommendation AI agent** — fetches record details, similar records, relevant KB articles to provide summaries/resolution steps
- **Web research and recommendation AI agent** — analyzes problem and generates resolution steps using web search tools

"Recommend AI agents" section uses Now Assist to help find the right AI Agents to map — requires well-defined Description/Instructions.

**Define trigger page** — Add Trigger: Select trigger (Created or updated), Trigger name, Table (Incident). Once Table is set: **Conditions** (when to trigger, e.g. Category=Password Reset), **Run as** (whose permissions the AI Agent uses — existing table or custom script), **Objective Template** (the goal, e.g. "Help me resolve ${number}").

**Select display page** — configures whether the workflow shows in Now Assist Panel (NAP), defaults off. Toggle Display on, add role `now_assist_panel_user` in User roles field, Save and test.

## Exercise 2: Exploring AI Agent

Open the **Next Best Action Agent** from the Connect AI agents section.

Fields: **Name**, **Description**, **AI agent role** (capabilities/responsibilities), **Instructions** (task-oriented guidelines with conditions/steps/constraints).

**Add tools and information** — tool types: Catalog item, Conversational topic, Flow action, Now Assist skill, Record operation, Script, Search retrieval, Subflow, Web search. **All tool inputs/outputs can only be String.**

Activate via **Define availability** > Status toggle on.

## Exercise 3: Test the Agentic Workflow and AI Agent

AI Agent Studio > Testing. Test scenario: What to test = Agentic Workflow ("Generate resolution plans"), Task = "Help me resolve Incident INC0009005". Click Start Test — monitor progress in Output pane; decision logs on the right (expandable, downloadable). Verify in Now Assist panel that steps are appropriate. Review the incident's work notes activity to see the agent's thought process.

## Exercise 4: Duplicate an Agentic Workflow

Verify Global application scope (Duplicate copies into the session's current scope). AI Agent Studio > Create and manage > Agentic Workflows > "Generate resolution plans" > Duplicate > confirm.

Rename to `"<PREFIX> - Generate resolution plans"`. Update **Description** and add a 5th **Instructions** step:
```
5. Create change record with the generated resolution plan
- Create a change request with the resolution plan generated by the
  "Next action recommendation AI Agent (Copy)" AI Agent, using the
  "Create Change record with Plan" AI Agent.
```

Add a new trigger: Created, name "Incident created by admin", Table Incident, Conditions "Created | is | admin", Run as "Caller [incident]", Objective template "Help me resolve ${number}", check Show Notifications. Enable Display, add role `now_assist_panel_user`. Save and test.

## Exercise 5: Duplicate and Modify an AI Agent

Same application scope as the duplicated workflow. Open "Next action recommendation AI agent" > triple-dot menu > Duplicate → "Nex action recommendation AI Agent (Copy)".

Add a new instructions step:
```
5. Output a message with a script with the Incident number.
6. Finish.
```

Open the **Get similar Incidents** Flow actions tool: set Display output = Yes, Output transformation strategy = Concise.

> **Important (Yokohama Patch 1 gotcha)**: modifying a tool in a copied AI Agent **also modifies the tool in the original agent**. Manually duplicate the tool first if you don't want this side effect.

Add a Script tool: Name "Message Output", Description "Run a script that outputs a message that a plan has been approved for the given Incident number." Input: `inc_number` / "Incident number". Script:
```javascript
(function(inputs) {
  gs.info("Plan approved for " + inputs.inc_number);
})(inputs);
```
Execution mode: **Autonomous** (no permission ask). Display Output: **No** (nothing communicated to user).

## Exercise 6: Create an AI Agent

New AI Agent: Name "Create Change record with Plan", Description "This agent can create change records.", AI agent role "You are an expert in creating change records.", Instructions "Create a change record with the generated plan from the 'Nex action recommendation AI Agent (Copy)'. After record is successfully created, you are finished."

Add Tool > Record operation: Name "Create Change Request record", Description "Create a change request record with the resolution plan." Inputs: `change_title` ("Summary of resolution plan"), `res_plan` ("Resolution plan created by ..."). Table: Change Request. Operation: Create record. Field values: Short description = `{{change_title}}`, Description = `{{res_plan}}`. Execution mode: **Supervised** (asks user permission before creating). Display output: Yes. Output transformation strategy: Concise.

Add this agent + the modified "Next action recommendation AI Agent (Copy)" to the duplicated workflow, remove the original "Next action recommendation AI Agent", ensure the "Incident created by admin" trigger is Active. Test with an incident number.

Expected test flow: record details displayed → similar incidents listed → resolution plan generated, asks for approval → script runs (check System Logs for the incident number) → change request created (approval requested, testing panel shows agent switching over).

## Exercise 7: Deploying to the Now Assist Panel

Create a new Incident (caller = admin, matching the trigger condition). Navigate to Workspaces > Service Operations Workspace — Now Assist panel shows a notification. Click to open, review the agent run. When asked to proceed with creating a change record, respond "Yes proceed." Once created, verify in the Workspace's change list.

Manual invocation is also possible by typing into the Now Assist Panel, similar to the trigger's objective template. AI Agent Studio > Analytics shows usage analytics.

## Exercise 8 (Optional): Troubleshooting

Error "There are no agents available at the moment. Please try again later." — check:
- AI Search is enabled
- Agentic Workflow and AI Agent(s) are active and connected
- Triggers are active
- AI Agent's **Proficiency** (add as a column in the AI Agents list; generated by the LLM, cannot be modified) — must be detailed and match the intended goal/objective template

## Notable comment thread

- Q: does adding a trigger on the AI Agent (in addition to the Agentic Workflow) cause conflicts? Author didn't directly answer inline (question posted 2026-01-06, unresolved as of fetch).
- Q: how does the agent pick tools when instructions are vague — matching words, AI search? (unresolved as of fetch)
- Q: are OOB tool scripts "black boxes"? (unresolved as of fetch)
- @Apaul: "add to virtual agent" only appears for AI agent, not workflow — author points to `sn_aia.enable_va_conversation` system property (same answer as in the companion Travel Approval article).

23 Helpfuls · 49,854 Views

## Why this might matter to this vault

This is the most complete step-by-step build tutorial fetched in this batch — directly usable as a template for building [[partner-case-summary-agent]] in AI Agent Studio (exercise 5/6 pattern: duplicate-and-modify vs. create-new AI Agent, Record operation tool config with `{{input}}` field-value syntax, Supervised vs Autonomous execution mode). The Yokohama Patch 1 "duplicating an agent doesn't duplicate its tools" gotcha is a real trap worth flagging if anyone reuses this pattern.
