---
title: "Cancel Incomplete Playbooks on Closure"
aliases:
  - Cancel Incomplete Playbooks on Closure
tags:
  - servicenow-dev-program
  - code-snippet
  - cancel-incomplete-playbooks-on-closure
  - business-rules
---

🛑 Auto-Cancel Playbooks on Incident Deactivation

Script Type: Business Rule (Server-side)
Trigger: before update
Table: incident
Condition: active changes to false

📌 Purpose

Automatically cancel all active Playbooks (sys_pd_context) records associated with an incident when that incident is deactivated (e.g., closed or canceled). 

🧠 Logic

- Finds all active playbooks (not in completed,canceled) where:
- input_table is incident (or any other table)
- input_record matches current incident’s sys_id
- Cancels each playbook using: sn_playbook.PlaybookExperience.cancelPlaybook(playbookGR, 'Canceled due to the incident closure or cancellation.');

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
