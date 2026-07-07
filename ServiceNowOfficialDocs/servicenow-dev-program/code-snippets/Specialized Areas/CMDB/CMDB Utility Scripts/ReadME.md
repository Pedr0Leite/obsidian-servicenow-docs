---
title: "CMDB Utility Scripts"
aliases:
  - CMDB Utility Scripts
tags:
  - servicenow-dev-program
  - code-snippet
  - cmdb-utility-scripts
  - cmdb
---

This script is used in ServiceNow to automatically fill in the missing manufacturer information for Configuration Items (CIs) in the CMDB (Configuration Management Database).

1. Predefined Mapping:
The script starts with a list of known model names and their corresponding manufacturer names.For example, a model called ThinkPad T14 is made by Lenovo, and MacBook Pro 16 is made by Apple
2. Look Up Manufacturer:
    * It defines a function that looks up the manufacturer’s record in the core_company table (based on the name) and gets its unique ID (sys_id).
3.  Find CIs Missing a Manufacturer:
    * The script goes through all CIs in the cmdb_ci table where the manufacturer field is empty.
4.  Update Missing Manufacturer:
    * For each of those CIs:
        * It checks the model name.
        * If the model is in the predefined mapping:
            * It looks up the correct manufacturer in the core_company table.
            * It updates the CI record by setting the manufacturer field with the correct sys_id.
            * It also logs that the update was successful.
        * If the manufacturer is not found in the system, it logs a warning.
5.  Final Log:
    * After going through all matching CIs, it logs how many records were successfully updated.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Utility Scripts/softwareCreationREADME|softwareCreationREADME]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB CI Deduplication Task Generator/README|CMDB CI Deduplication Task Generator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Dynamic Status Update Function/README|CMDB Dynamic Status Update Function]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Get CI Relationships/README|CMDB Get CI Relationships]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Health Check/README|CMDB Health Check]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB record count/README|CMDB record count]]
