---
title: "get field values for multiple records from a table"
aliases:
  - get field values for multiple records from a table
tags:
  - servicenow-dev-program
  - code-snippet
  - get-field-values-for-multiple-records-from-a-table
  - script-includes
---

## Script contains scalable method to get display value of particular field from a table for any number of records filtered by a encoded query

> Method: \_getFieldDisplayValues(tableName, query, fieldName)

-   @param {String} tableName: Table name
-   @param {String} query: query to filter the records
-   @param {String} fieldName: Field name for which display value is required

-   @returns {String OR boolean}: comma separated field display values of filtered records
    **OR** false if no record/no display value if found on filtered records

### Example Methods

> getUserEmailAddressesBySysIDs(sysIDs)

-   @param {String} sysIDs: Comma separated list of sysIDs (can also be single sysID)
-   @returns {String}: comma separated email addresses of user profiles sys_id passed in as comma separated values.

> getUserNamesBySysIDs(sysIDs)

-   @param {String} sysIDs: Comma separated list of sysIDs (can also be single sysID)
-   @returns {String}: comma separated names of user profiles sys_id passed in as comma separated values.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
