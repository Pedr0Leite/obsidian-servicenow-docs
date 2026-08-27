---
title: "Check if the Import file is valid"
aliases:
  - Check if the Import file is valid
tags:
  - servicenow-dev-program
  - code-snippet
  - check-if-the-import-file-is-valid
  - transform-map-scripts
---

**Example use Case:**

Vendor data is periodically imported into ServiceNow via a scheduled data load (import set) sourced from an external application. These files contain only valid vendor records. After the import, any existing vendor records in ServiceNow that are not present in the latest file should be marked as inactive.

**Risk:**

If the incoming file is empty due to an issue in the source application, all existing vendor records in ServiceNow could be incorrectly marked as inactive, resulting in data loss or disruption.

**Solution:**

To prevent this, implement an "onStart" transform script that checks whether the import set contains any data before proceeding with the transformation. If it is found to be empty, the script should:

1. Abort the transformation process.
2. Automatically raise a ticket to the responsible team for investigation.(Optional)


   
This ensures that the existing vendor data in ServiceNow remains unchanged until the issue is resolved.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Choice Field Validator/README|Choice Field Validator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Conditional Coalesce/README|Conditional Coalesce]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Email Formatter/README|Email Formatter]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Global Variable in Transform Map/README|Global Variable in Transform Map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Incident Priority Set on Insert Only/README|Incident Priority Set on Insert Only]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Verify headers of a CSV attached file/README|Verify headers of a CSV attached file]]
