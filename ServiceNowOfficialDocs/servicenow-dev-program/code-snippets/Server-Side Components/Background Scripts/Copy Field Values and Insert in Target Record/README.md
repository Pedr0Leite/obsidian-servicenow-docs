---
title: "Copy Field Values and Insert in Target Record"
aliases:
  - Copy Field Values and Insert in Target Record
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-field-values-and-insert-in-target-record
  - background-scripts
---

Script Usage :

This function takes the parameters such as source table, source record sys_id, target table, fields that needs to be copied to target table.

As a validation check, the fields from source table should be similar to target else abort inserting the record.


Same Code to invoke the function: 
copyFieldsValidated(
    'dmn_demand',
    '8c10306edbc00810f777526adc961976',
    'pm_project',
    ['name', 'short_description']   //will throw error since name field not common in both tables
);


copyFieldsValidated(
    'dmn_demand',
    '8c10306edbc00810f777526adc961976',
    'pm_project',
    ['short_description']   //Insert the record since short_description is common in both tables
);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
