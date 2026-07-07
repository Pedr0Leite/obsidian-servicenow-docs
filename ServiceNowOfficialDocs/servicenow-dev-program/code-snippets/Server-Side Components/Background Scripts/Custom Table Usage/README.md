---
title: "Custom Table Usage"
aliases:
  - Custom Table Usage
tags:
  - servicenow-dev-program
  - code-snippet
  - custom-table-usage
  - background-scripts
---

# Custom Table Usage Count

This script provides a way of counting where any custom tables (u_) are used in the instance.

**This script is not to be used to determine subscription and license usage.  It is simply to determine how widespread the use of a custom table is in your instance to assist with tidying up unused tables.**

Returns JSON object similar to the following:

```json
[
   {
      "name": "u_cmdb_ci_key_value_staging",
      "label": "Key Value Staging",
      "references": {
         "Dictionary": 0,
         "Variables": 0,
         "Business Rules": 0,
         "Client Scripts": 0,
         "Dictionary Entries": 86,
         "Dictionary Overrides": 0,
         "UI Actions": 0,
         "ACL": 0,
         "UI Policies": 0,
         "Data Policy": 0,
         "Styles": 0,
         "View Rules": 0,
         "Workflows": 0,
         "Flows": 0
      }
   }
]
```

Easily extended by adding more entries in the USAGE_COUNT_CONFIG object.

```javascript
const USAGE_COUNT_CONFIG = [
    { "table": "sys_dictionary", "field": "reference", "title": "Dictionary" },
    { "table": "item_option_new", "field": "reference", "title": "Variables" },
    { "table": "sys_script", "field": "collection", "title": "Business Rules" },
    { "table": "sys_script_client", "field": "table", "title": "Client Scripts" },
    { "table": "sys_dictionary", "field": "name", "title": "Dictionary Entries" },
    { "table": "sys_dictionary_override", "field": "name", "title": "Dictionary Overrides" },
    { "table": "sys_ui_action", "field": "table", "title": "UI Actions" },
    { "table": "sys_security_acl", "field": "name", "title": "ACL", "query": "STARTSWITH" },
    { "table": "sys_ui_policy", "field": "table", "title": "UI Policies", },
    { "table": "sys_data_policy2", "field": "model_table", "title": "Data Policy" },
    { "table": "sys_ui_style", "field": "name", "title": "Styles" },
    { "table": "sysrule_view", "field": "table", "title": "View Rules" },
    { "table": "wf_workflow", "field": "table", "title": "Workflows" },
    { "table": "sys_hub_flow", "field": "sys_id", "title": "Flows", "query": "", "query_field": "sys_id" },
    { "table": "sys_script_include", "field": "script", "title": "Script Include", 'query': 'CONTAINS'}
];
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
