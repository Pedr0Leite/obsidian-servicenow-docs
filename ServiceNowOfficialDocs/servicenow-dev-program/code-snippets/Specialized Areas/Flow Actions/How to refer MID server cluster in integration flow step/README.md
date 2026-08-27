---
title: "How to refer MID server cluster in integration flow step"
aliases:
  - How to refer MID server cluster in integration flow step
tags:
  - servicenow-dev-program
  - code-snippet
  - how-to-refer-mid-server-cluster-in-integration-flow-step
  - flow-actions
---

During integration set up using flow designer integration action step (JDBC, Powershell,REST, SOAP etc..) wheh you select connection type as "Define Connection inline", you have an option to use MID Cluster when MID selection is "Specific MID server"
![image](https://github.com/gowdah/code-snippets/assets/42912180/dcb8c69b-72a3-493b-8db2-72b92daefce0)
MID cluster step expects "MID Server cluster sys_id (not the MID cluster server name or individual MID servers) to to use availble MID server in the cluster.
MID Server Cluster.js file logic return expected result

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
