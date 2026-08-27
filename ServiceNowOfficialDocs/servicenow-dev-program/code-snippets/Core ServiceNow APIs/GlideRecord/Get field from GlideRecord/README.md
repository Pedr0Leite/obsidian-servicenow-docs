---
title: "Get field from GlideRecord"
aliases:
  - Get field from GlideRecord
tags:
  - servicenow-dev-program
  - code-snippet
  - get-field-from-gliderecord
  - gliderecord
---

The code snippet provided is a JavaScript function that retrieves and logs the field names from a specified GlideRecord. The function getFields takes a GlideRecord instance as a parameter and returns an array containing the names of all the fields in the specified record.

Functionality
  getFields(gr: GlideRecord): Array
  Purpose:
    - Returns an array of all the fields in the specified GlideRecord.
  Parameters:
    - gr (GlideRecord): A GlideRecord instance positioned to a valid record.
  Returns:
    - An array of strings representing the field names in the specified GlideRecord.
  Note:
    - If there is a field name which is the same as the table name, the getFields() method does not return the value of the field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
