---
title: "Highlight Mandatory fields on form"
aliases:
  - Highlight Mandatory fields on form
tags:
  - servicenow-dev-program
  - code-snippet
  - highlight-mandatory-fields-on-form
  - browser-bookmarklets
---

## Highlight Mandatory Fields

**Description**
- This bookmarklet visually highlights all mandatory fields on a ServiceNow form by adding a glowing border or background around them.
- It helps developers, admins, or QA testers quickly see which fields are marked as mandatory.
- It also helps partial visually paired people to find the mandatory fields instead of looking for small * icon for field.
- This works as a toggle. One click highlights the mandatory fields and clicking again removes the highlight.

**Example :**

- When activated on a form (e.g. Incident, Request Item):
- Mandatory fields like Short description, Caller, etc get a soft glowing yellow border.
- Click again → glow is removed.

**How it works:**  
- Detects `g_form` context.
- Adds a temporary CSS class (`.mandatory-glow`) to all mandatory fields.
- Click again to remove the highlights.

**Sample screenshot**
<img width="1882" height="674" alt="image" src="https://github.com/user-attachments/assets/1320c9c3-976d-4bf0-92d5-e051825dbe6c" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create new update set/README|Create new update set]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create story task/README|Create story task]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Impersonation/README|Impersonation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Open copied record/README|Open copied record]]
