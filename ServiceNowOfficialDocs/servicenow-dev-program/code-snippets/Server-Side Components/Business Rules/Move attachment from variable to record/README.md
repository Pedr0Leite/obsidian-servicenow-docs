---
title: "Move attachment from variable to record"
aliases:
  - Move attachment from variable to record
tags:
  - servicenow-dev-program
  - code-snippet
  - move-attachment-from-variable-to-record
  - business-rules
---

**Scenario**:

In some catalog items, we might want to make attachments mandatory based on certain conditions.
To achieve this, we typically use an Attachment variable on the catalog item.

When a user submits the catalog item, any attachments uploaded through this variable are stored in the sys_attachment
table with the table name set to the variable’s source — usually ZZ_YYsc_cat_item_producer.
However, in certain cases, we might want these attachments to be associated directly with the RITM (sc_req_item) record instead of staying linked
to the variable.

**Solution**:

We can create an After Insert Business Rule on the sc_req_item table that automatically reassigns such attachments to the corresponding RITM.

This rule will run only for RITMs created from specific catalog items, as defined in the filter condition of BR, and retrieve the attachment record from the sys_attachment table using the attachment variable value. It will then update the table_name to 'sc_req_item'.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
