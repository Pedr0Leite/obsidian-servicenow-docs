---
title: "Health Scan Prevent Insert Update in Before BRs"
aliases:
  - Health Scan Prevent Insert Update in Before BRs
tags:
  - servicenow-dev-program
  - code-snippet
  - health-scan-prevent-insert-update-in-before-brs
  - client-scripts
---

**Client script Deatils**
1. Table: sys_script
2. Type: onSubmit
3. UI Type: Desktop

**Benefits**
1. This client script will prevent admin users to do insert/update operation in  onBefore business rules.
2. It will help to avoid HealthScan findings thus increasing healthscan score.
3. Will prevent recursive calls.

Link to ServiceNow Business Rules best Practise : https://developer.servicenow.com/dev.do#!/guide/orlando/now-platform/tpb-guide/business_rules_technical_best_practices

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
