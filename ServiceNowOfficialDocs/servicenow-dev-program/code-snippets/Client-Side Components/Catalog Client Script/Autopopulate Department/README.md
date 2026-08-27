---
title: "Autopopulate Department"
aliases:
  - Autopopulate Department
tags:
  - servicenow-dev-program
  - code-snippet
  - autopopulate-department
  - catalog-client-script
---

# Autopopulate Department Catalog Client Script

Use this onChange catalog client script to populate a **department** variable in a catalog item based on a modifiable **requested_for**. Both variables must be reference type pointing to their respective tables.

## Use case

The GlideUser API (g_user) does not provide a way to retrieve a user's department in a client-side script. Here is a small snippet using `g_form.getReference()` to retrieve the user from the **requested_for** variable and populate the **department** variable in a catalog item while allowing the submitter to still change the department if the data is incorrect.

Attach this client script to a variable set for easy reuse. It can be augmented with a number of other fields from the user record such as email, phone number, manager, etc. Just be mindful of field types and whether the desired field will return a sys_id or display text.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate user information fields/README|Autopopulate user information fields]]
