---
title: "Delete Duplicate Mobile records"
aliases:
  - Delete Duplicate Mobile records
tags:
  - servicenow-dev-program
  - code-snippet
  - delete-duplicate-mobile-records
  - fix-scripts
---

Below script is a Fix script used to delete duplicate mobile assets and Cis in your CMDB. In this script we keep recently created assets and its related CI and delete other duplicate assets and related Cis if any.

Note : In this script I have used u_alm_mobile as the table and u_cmdb_ci_mobile, this are my tables but you can use your own table where you have stored your mobile devices.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
