---
title: "Autopopulate user information fields"
aliases:
  - Autopopulate user information fields
tags:
  - servicenow-dev-program
  - code-snippet
  - autopopulate-user-information-fields
  - catalog-client-script
---

## Overview
This onchange catalog client script and script inlcude work together autopopulate the user fields that might show up on a catalog item. In the 
global scope you will have to create the client callable script include to be able to use the Ajax call that is in the on change client script.
In this example we use the OOB Requested For field that already auto populates the user that is logged in then we go to the server to get that 
users information. The fields that are brough back are the ones that are in the code but you can modify to bring back more or less fields if needed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
