<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/in-product-experience-for-agentic-workflows/ta-p/3507831 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via defuddle/WebFetch/CLI with 503 — real browser session succeeded, no login required) -->
<!-- This is the article originally requested that started the whole batch. -->

# In-product experience for Agentic Workflows

samyukthare, ServiceNow Employee — 03-17-2026, edited 06-03-2026

## Overview

Agentic Workflows bring AI driven, multi-step execution directly into the flow of work, embedded inside records and workspaces. Instead of switching to a separate conversational surface, users can trigger, supervise, and review AI workflows exactly where they already work, with clear visibility into what the AI is doing and why.

## What Problem We're Solving

Today, users face several challenges when using AI for complex work:
- **Context switching**: Users must leave their record or workspace to engage AI, breaking focus and slowing work.
- **Low trust in AI outcomes**: Traditional AI experiences act as black boxes, offering limited insight into how decisions are made.
- **Fragmented execution**: Multi-step AI tasks are difficult to monitor, supervise, or course-correct once started.
- **Inconsistent UX across workflows**: Different AI workflows behave differently — increasing cognitive load and reducing adoption.

Agentic Workflows solve these problems by bringing AI execution into the record, standardizing how workflows are triggered, supervised, and reviewed, and making AI activity visible and understandable at every step.

## Business Use Case Examples

The business use cases where this capability would be beneficial are those in which a fulfiller persona (human agent) has one or more Agentic workflows that they frequently use to complete their tasks (cases, incidents, etc.). Instead of leaving the context of the record to trigger the workflow conversationally, they can now trigger it directly within the context of their task.

The processing, status, input (for supervised workflows), and final output (including cited sources) are all surfaced within the record via the Contextual Side Panel, Tab, or Modal (coming soon), depending on how it has been configured.

## Now Assist Panel vs. In-Product Experience

The Now Assist Panel provides fulfillers with capabilities that go beyond merely triggering Agentic workflows. Previously, users lacked an organized method to locate completed or in-progress workflow runs associated with a specific record in the Now Assist Panel. The introduction of the new in-product experience addresses this gap by offering a contextual side panel — view all relevant workflow details (status, run history, outputs) directly within their current workspace.

### Where Users Find In-Product Experience

When the in-product experience UI Action is enabled for an agentic workflow in AI Agent Studio with a specified table name, buttons appear on the record page within workspaces and the UI16 record. Clicking initiates the agentic workflow and adds new cards to a contextual side panel for monitoring progress.

**Record level indicators**: A subtle AI activity indicator appears directly on supported records (UI16 and Workspaces), signaling that agentic workflows are available or running.

**Contextual side panel (AI Activity)**: Clicking the indicator opens a side panel showing all Agentic workflows associated with the record. Each workflow appears as its own card with status and progress. To cancel an active workflow, select the three dots menu and choose the cancel option.

**Notifications**: When a workflow requires user input or approval, a notification alert displays for users to take action.

## Supported Capabilities

- **Trigger Workflows** — launched via UI action buttons on records or workspaces; no need to open the Now Assist Panel or navigate away.
- **Monitor Execution in Real Time** — each workflow card displays current status ("In progress," "Input needed," "Completed," "Failed," "Canceled"); step-by-step processing visible.
- **Supervise and Guide AI** — agentic workflows pause at important moments to request human input (text, Yes/No, choice/multi-select, date selection, approval or approve-all).
- **Embedded Triggers in the Flow of Work** — initiated directly from records/workspaces via UI actions or contextual buttons.
- **Contextual Side Panel for AI Activity** — record-level indicator opens a side panel showing all related agentic workflows as dedicated cards.
- **Real-Time Execution Visibility** — clear status indicators at a glance.
- **Human Supervision and Input** — checkpoints for approval, enabling human-in-the-loop control between autonomous execution steps.
- **Transparency Through Reasoning and Citations** — users can view why the AI took specific actions and what data/sources informed decisions.
- **Output Review Before Action** — AI-generated outputs (plans, summaries, recommendations) reviewed before being applied; approve, reject, or modify; comparisons between previous and proposed values.
- **In-Record Notifications** — notifications directly within the record when a workflow completes or requires attention.

## Setup Requirements

- **License**: Professional or Enterprise+
- **Plugin Version**: ZP7/AP1 — Store app v12.0.11
- **Required Plugins**:
  - Now Assist for Platform (included with Now Assist for ITSM, CSM, and similar apps)
  - `com.glide.ai_record_activity`
- **Roles**: Fulfillers need their standard record-access roles; ensure workflow-specific roles are assigned for any workflow enabled for in-product experience.
- **Workspace Support**: Service Operations and CSM workspaces supported starting March 2026. Additional workspaces coming soon.

Note: This article applies to Zurich-Patch-7, Yokohama-Patch-13, and Australia-Patch-1 with Platform AI Agent & Skills app v12.0.11.

## Outcomes & Business Benefits

**For end users (fulfillers and agents)**: faster task completion with less manual effort; reduced context switching and cognitive load; higher trust in AI through visibility, reasoning, and control.

**For organizations**: more consistent and scalable AI adoption across workflows; standardized UX patterns across BUs and use cases; improved productivity without sacrificing governance or oversight.

**For the platform**: a cohesive, reusable in-product experience for all agentic workflows; clear separation between workflow logic and experience patterns; foundation for future expansion of autonomous and supervised AI execution.

## Target Users & Personas

Any fulfiller or human agent persona accessing a record that has the in-product agentic experience enabled.

## Activation & Config Steps

1. Go to **All → AI Agent Studio** → select the workflow and click on it.
2. Navigate to **'Define security controls'** and add all necessary security roles associated with the selected Agentic workflow.
3. To add a UI button on a record page: navigate to **"Select channels and status,"** add the table and condition, ensure display is set to "on," then click **"Save and Test"** to apply the changes.
4. System property: navigate to `sys_properties.list` and confirm `com.glide.agentic_processes_view.enabled` is set to `true`.
   - If not found, create a new one: application `@servicenow/sn-ai-engagement-experience`, value `true`.
   - Note: `com.glide.agentic_processes_view.enabled` **cannot be set to true by a customer admin** — must follow one of three options in KB2762154 ("UI Action to trigger Agentic Workflows is not visible and enablement property is protected...").
5. If using Service Operations or CSM workspace, no further configuration is required for the contextual side panel — available out of the box once the system property is activated.
   - Customers wishing to enable early (before official support for additional workspaces) may manually configure the contextual side panel via UI Builder — outside the scope of ServiceNow support.

## Conclusion

The in-product experience for Agentic AI represents a significant step forward in how ServiceNow delivers AI-powered work execution. By embedding agentic workflows directly into records and workspaces, this capability eliminates context switching, builds user trust through transparency, and puts humans in control of every step. Available starting March 2026 for Service Operations and CSM workspaces.

8 Helpfuls · 4,957 Views

## Why this might matter to this vault

Directly relevant to [[Proactive Customer Case Communicator]] and [[partner-case-summary-agent]] — this is an *alternative surfacing pattern* (embedded record-level UI actions + contextual side panel) to NAP/VA conversational entry, which the Partner Case Summary Agent architecture already flagged as a secondary/fallback path. The `com.glide.agentic_processes_view.enabled` property gate (admin-restricted, requires KB2762154 workaround) is a concrete config detail worth checking if either agent is ever moved toward this in-record surface instead of pure NAP.
