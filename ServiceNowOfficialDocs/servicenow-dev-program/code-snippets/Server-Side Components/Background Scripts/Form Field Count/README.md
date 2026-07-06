---
title: "Form Field Count"
aliases:
  - Form Field Count
tags:
  - servicenow-dev-program
  - code-snippet
  - form-field-count
  - background-scripts
---

# Form Field Count

A background script that identifies forms with excessive field counts that may impact performance or trigger Health Scan warnings.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. (Optional) Modify `maxFields` variable to set your threshold (default: 30)
4. Click "Run script"

## What It Does

The script:
1. Queries all forms in the instance (`sys_ui_form`)
2. Iterates through each form's sections (`sys_ui_form_section`)
3. Counts fields in each section, excluding container elements (splits, section starts)
4. Reports only forms exceeding the configured threshold
5. Outputs form name and total field count to system logs

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
