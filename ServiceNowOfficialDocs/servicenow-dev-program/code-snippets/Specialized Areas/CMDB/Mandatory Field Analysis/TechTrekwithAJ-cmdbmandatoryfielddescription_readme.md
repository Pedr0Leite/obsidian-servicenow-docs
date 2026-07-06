---
title: "TechTrekwithAJ-cmdbmandatoryfielddescription_readme"
aliases:
  - TechTrekwithAJ-cmdbmandatoryfielddescription_readme
tags:
  - servicenow-dev-program
  - code-snippet
  - mandatory-field-analysis
  - cmdb
---

 CMDB Table Definition:
        cmdbTableName specifies the CMDB class you want to analyze (e.g., cmdb_ci_computer).
        Modify this to the desired table name.
Mandatory Fields Array:
        mandatoryFields is an array that holds the names of the fields you want to check for mandatory values. Customize this list as per your requirements.
GlideRecord Query:
        A GlideRecord object is created to query the specified CMDB table.
Iteration and Check:
        The script iterates through all records in the CMDB table and checks each mandatory field to see if it is populated.
        If a mandatory field is missing, it adds the field name to the missingFields array.
Logging:
        If any mandatory fields are missing for a record, it logs the record's sys_id and name, along with the missing fields.
        It also counts and logs the total number of records with missing mandatory fields at the end.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/Mandatory Field Analysis/README|Mandatory Field Analysis]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB CI Deduplication Task Generator/README|CMDB CI Deduplication Task Generator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Dynamic Status Update Function/README|CMDB Dynamic Status Update Function]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Get CI Relationships/README|CMDB Get CI Relationships]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Health Check/README|CMDB Health Check]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Utility Scripts/ReadME|CMDB Utility Scripts]]
