---
title: "TableUtils Extension"
aliases:
  - TableUtils Extension
tags:
  - servicenow-dev-program
  - code-snippet
  - tableutils-extension
  - script-includes
---

## Enhanced_TableUtils Script Include extends out of the box TableUtils

It has a getFieldsAndAttributes() method that does not require a GlideRecord. Out of the box getFields() methods from either GlideRecord() or GlideRecordUtil() only work with an existing record and not just with the table name. This one goes to sys_dictionary directly and therefore does not need a valid GlideRecord to work.

**Usage**

```
var fields = new Enhanced_TableUtils('incident').getFieldsAndAttributes();
gs.debug('Field caller_id is of type ' + fields.caller_id.field_type + ' (to table ' + fields.caller_id.reference_table + ')');
```

**Output**

```
*** Script: [DEBUG] Field caller_id is a reference to table sys_user
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
