---
title: "Call JavaScript Probe"
aliases:
  - Call JavaScript Probe
tags:
  - servicenow-dev-program
  - code-snippet
  - call-javascript-probe
  - business-rules
---

With this script you can call MID Server Script Include via JAVASCRIPT probe. As soon as you run this script it will insert the entry in
ecc_queue table and output record will be created against that. In that output record you will see the parameters sent to "SFTP"
Then once the file is successfully copied or moved to SFTP and input record in ecc_queue will be inserted and gives the output whether the file
transfer was successful or any errors.

You can call this script from any Server side scritping

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
