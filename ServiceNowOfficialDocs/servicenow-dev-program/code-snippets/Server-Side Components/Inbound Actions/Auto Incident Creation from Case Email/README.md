---
title: "Auto Incident Creation from Case Email"
aliases:
  - Auto Incident Creation from Case Email
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-incident-creation-from-case-email
  - inbound-actions
---

**Auto Incident Creation from Case Email** 

**Description** 
This inbound email action automatically creates an incident record when a customer replies to a case email containing keywords like outage, crash, error, or not working. 
The new incident links to the case as a parent and inherits caller and configuration item details. 

**Use Case** 
Ideal for CSM environments integrated with ITSM, where customer issues escalate to incidents automatically. 

**How It Works**
1. The inbound email action scans the subject and body for trigger keywords.
2. If a match is found:
   - A new incident record is created.
   - The incident is linked to the case as a parent.
   - Caller and CI are inherited if available.
   - Work notes of both case and incident records are updated. 

**Inbound Action Configuration**
   - Table: Case[sn_customerservice_case]
   - Action type: Record Action
   - Type: Reply

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Advanced Scripts/README|Advanced Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Reply Email/README|Auto Reply Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Automate creation of incidents through inbound actions/README|Automate creation of incidents through inbound actions]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Duplicate Incident Detection and Creation/README|Duplicate Incident Detection and Creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Email Text as Attachment/README|Email Text as Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Inbound Email Action to Create User and Assign Groups/Readme|Inbound Email Action to Create User and Assign Groups]]
