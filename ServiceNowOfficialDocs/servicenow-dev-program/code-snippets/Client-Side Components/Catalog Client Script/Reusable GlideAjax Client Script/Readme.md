---
title: "Reusable GlideAjax Client Script"
aliases:
  - Reusable GlideAjax Client Script
tags:
  - servicenow-dev-program
  - code-snippet
  - reusable-glideajax-client-script
  - catalog-client-script
---

This solution provides a generic and reusable GlideAjax-based client-server interaction in ServiceNow that allows querying any table by passing:

Table name
Key field and value
Desired fields to retrieve

It dynamically returns field values from the server and populates them on the form, making it ideal for use cases like CMDB enrichment, entitlement lookups, or dynamic form population.

1. Client Script (onChange)
Triggers on field change.
Sends parameters to the Script Include via GlideAjax.
Receives JSON response and sets target field value.

Parameters:
sysparm_table_name: Table to query (e.g., sys_user)
sysparm_key_field: Field to match (e.g., sys_id)
sysparm_key_value: Value to match
sysparm_fields: Comma-separated list of fields to retrieve

2. Script Include: DynamicTableQueryUtil
   
Processes incoming parameters.
Queries the specified table and retrieves requested fields.
Supports both standard fields and catalog item variables.
Returns a JSON object with field values and display values.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
