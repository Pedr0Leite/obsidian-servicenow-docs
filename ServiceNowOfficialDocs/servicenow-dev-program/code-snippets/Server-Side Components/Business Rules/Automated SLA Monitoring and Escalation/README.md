---
title: "Automated SLA Monitoring and Escalation"
aliases:
  - Automated SLA Monitoring and Escalation
tags:
  - servicenow-dev-program
  - code-snippet
  - automated-sla-monitoring-and-escalation
  - business-rules
---

**Create a New Business Rule:**

    1. Navigate to System Definition > Business Rules in your ServiceNow instance.
    
    2. Click on New to create a new business rule.

**Configure the Business Rule:**

    1. Name: Set a descriptive name (e.g., "SLA Breach Check").
    
    2. Table: Set to Incident.
    
    3. When: Select Before.
    
    4. Insert: Check this box.
    
    5. Update: Check this box.
    
    6. Condition: You can set it to check if the state is "In Progress" and if the SLA is about to breach.
    
    Use the following condition script:
    
    '''current.state == 'In Progress' && current.sla_due <= gs.minutesAgo(30);'''

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
