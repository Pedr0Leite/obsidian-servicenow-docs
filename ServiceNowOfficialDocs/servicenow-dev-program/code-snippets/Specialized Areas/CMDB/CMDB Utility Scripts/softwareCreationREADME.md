---
title: "softwareCreationREADME"
aliases:
  - softwareCreationREADME
tags:
  - servicenow-dev-program
  - code-snippet
  - cmdb-utility-scripts
  - cmdb
---

This script automates the creation of Software Instance relationships in the CMDB during data import or transformation.
It ensures that each discovered or imported software record is correctly linked to the device on which it is installed, without creating duplicates.



The SoftwareUtils Script Include provides a utility function that checks whether a specific software (cmdb_software_product) is already related to a device (cmdb_ci_computer, cmdb_ci_server, etc.) through a Software Instance (cmdb_software_instance) record.

If the relationship does not exist, it creates a new software instance automatically.

This logic can be used directly within a Transform Map Script (onAfter) during software data import.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Utility Scripts/ReadME|CMDB Utility Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB CI Deduplication Task Generator/README|CMDB CI Deduplication Task Generator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Dynamic Status Update Function/README|CMDB Dynamic Status Update Function]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Get CI Relationships/README|CMDB Get CI Relationships]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB Health Check/README|CMDB Health Check]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/CMDB/CMDB record count/README|CMDB record count]]
