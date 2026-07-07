---
title: "Hide attachment icon"
aliases:
  - Hide attachment icon
tags:
  - servicenow-dev-program
  - code-snippet
  - hide-attachment-icon
  - catalog-client-script
---

# Hide Attachment Icon on Catalog Items

## Use Case / Requirement
Hide the attachment icon on a specific catalog item when the end user should not submit supporting documents. This can reduce confusion and prevent oversized uploads.

## Solution
Use an onLoad catalog client script to target the attachment button rendered on the Service Portal form and hide it with jQuery. The snippet works for both classic and Service Portal experiences.

## Implementation
1. Create a new catalog client script with Type set to onLoad.
2. Copy the contents of Hide Attachment icon.js into the script field.
3. Adjust the selector if your catalog item uses a custom portal or markup.

## Notes
- Requires jQuery, which is available on standard Service Portal forms.
- The DOM can change between releases; retest after theme or layout updates.
- Remove the script if the catalog item later requires attachments.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
