---
title: "Get Risk and Controls in Project"
aliases:
  - Get Risk and Controls in Project
tags:
  - servicenow-dev-program
  - code-snippet
  - get-risk-and-controls-in-project
  - background-scripts
---

In ServiceNow Risk Assessment Project, we can assess multiple risks on a single page or UI.
But for each individual risks, we need different Controls to be associated that can mitigate the risk.
So, there is direct relationship between Risk and Control in ServiceNow along with Risk and Risk Assessment Project.
Two m2m tables are - 'sn_risk_m2m_risk_control' and 'sn_risk_advanced_m2m_risk_assessment_project_risk' respectively.

Now organisations need to check how many Controls involved in a Risk Assessment Project for each risk.
To achieve that, we can utilize Risk Assessment Instance Response records where Control Assessment data is stored.
This Control Assessment data is updated whenever we associate Controls with Risks during Risk Assessment and fill out the factors.

In the Background script, if we pass one sys_id of Risk Assessment Project record, that should print Risks and Controls for each risk like this-
<img width="767" height="356" alt="image" src="https://github.com/user-attachments/assets/56e2a719-b767-456d-959d-e84457d31c44" />

Actual Risk Assessment Project on workspace looks like this-

<img width="922" height="412" alt="image" src="https://github.com/user-attachments/assets/c102d444-922b-44ec-9cb4-4a4ae13db4c7" />

<img width="920" height="416" alt="image" src="https://github.com/user-attachments/assets/48f8d6b1-bb25-4d5c-875c-ca49bd6660a8" />

Here, at the left we can select individual risks and inside of Control Assessment for that risk, controls can be added and assessed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
