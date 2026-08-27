---
title: "RITM Assignment Sync"
aliases:
  - RITM Assignment Sync
tags:
  - servicenow-dev-program
  - code-snippet
  - ritm-assignment-sync
  - business-rules
---

# Script Explanation:
This script is written for a Business Rule in ServiceNow. The purpose of this rule is to assign the same assigned_to value (typically a user) from the request to all related requested items (RITMs)
in the same catalog for a specific catalog item.
This script could be used in scenarios where, once a request is assigned to a particular user (or group), you want all the individual requested items (RITMs) tied to that request to also automatically be assigned to the same user. 
This ensures consistency in assignment across the items in a request.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
