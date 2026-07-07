---
title: "Validate MID servers status inside cluster"
aliases:
  - Validate MID servers status inside cluster
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-mid-servers-status-inside-cluster
  - flow-actions
---

During integration set up with flow designers which involves MID servers  , its better to check if MID server is up and running before we proceed with next steps in the integration.
when we are using MID Server cluster (where more than one MID server as a failover) its recommended to verify if atleast one MID server is up and establish the connect 
MID server status inside cluster.js logic check if atleast one MID server is up if yes process next step in the integration if not abort the integration (we can have process to inform concered team)
example flow action :
where "inputs.midServerCluster.sys_id" is Cluster sys_id as input to the action
![image](https://github.com/gowdah/code-snippets/assets/42912180/82916a5b-213d-440f-94ef-bc3b99465fc6)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
