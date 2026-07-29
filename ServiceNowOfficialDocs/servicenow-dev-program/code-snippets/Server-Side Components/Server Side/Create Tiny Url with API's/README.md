---
title: "Create Tiny Url with API's"
aliases:
  - Create Tiny Url with API's
tags:
  - servicenow-dev-program
  - code-snippet
  - create-tiny-url-with-apis
  - server-side
---

we can turn any servicenow url to tiny url with the code attached.

it just need a user authentication details, any user who dont even have any roles also fine, the user just need to able to login to instance.

example:
We can turn this url :
https://devxxxx.service-now.com/incident_list.do?sysparm_query=caller_id%3D681ccaf9c0a8016400b98a06818d57c7%5Epriority%3D1%5Estate%3D2%5Esys_updated_by%3Dadmin%5Eshort_description%3DManager%20can%27t%20access%20SAP%20Controlling%20application&sysparm_first_row=1&sysparm_view=


To this:
https://devxxxx.service-now.com/incident_list.do?sysparm_tiny=cb4c40e12fd61d10c083d0ccf699b62a

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Dynamic Catalog Task Creation/README|Dynamic Catalog Task Creation]]
