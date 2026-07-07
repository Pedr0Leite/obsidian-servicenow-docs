---
title: "Create Admin Users"
aliases:
  - Create Admin Users
tags:
  - servicenow-dev-program
  - code-snippet
  - create-admin-users
  - server-side
---

# Purpose
After first login to a freshly provisioned ServiceNow instance it is recommended creating personalized admin accounts. The following script will do the job for you. Just pass the most important properties to the method and a new user is being created with some preconfigured values such as roles and preferences.
# Usage
```javascript
var strUserSysID = createAdminUser(
  'john.doe',
  'John',
  'Doe',
  'john.doe@example.com'
);

if (strUserSysID != null) {
    //user has been created successfully
}
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Dynamic Catalog Task Creation/README|Dynamic Catalog Task Creation]]
