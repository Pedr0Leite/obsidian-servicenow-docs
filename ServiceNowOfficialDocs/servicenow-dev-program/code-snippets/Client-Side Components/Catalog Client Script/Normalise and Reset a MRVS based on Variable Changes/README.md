---
title: "Normalise and Reset a MRVS based on Variable Changes"
aliases:
  - Normalise and Reset a MRVS based on Variable Changes
tags:
  - servicenow-dev-program
  - code-snippet
  - normalise-and-reset-a-mrvs-based-on-variable-changes
  - catalog-client-script
---

# MRVS - Normalise and Reset Rows on Change

## What this solves
When a controlling variable changes (for example, Environment), existing MRVS rows may no longer be valid. This client script:
- Clears or normalises specific MRVS columns
- Deduplicates rows
- Optionally sorts rows for a cleaner UX
- Works entirely client-side using MRVS JSON

## Where to use
Catalog Item → OnChange client script on your controlling variable.

## How it works
- Reads the MRVS value as JSON via `g_form.getValue('my_mrvs')`
- Applies transforms (clear columns, unique by key, sort)
- Writes back the JSON with `g_form.setValue('my_mrvs', JSON.stringify(rows))`

## Setup
1. Replace `CONTROLLING_VARIABLE` with your variable name.
2. Replace `MY_MRVS` with your MRVS variable name.
3. Adjust `COLUMNS_TO_CLEAR`, `UNIQUE_KEY`, and `SORT_BY` as needed.

## Notes
- To clear the MRVS entirely, set `rows = []` before `setValue`.
- Works with Catalog Client Scripts; no server call required.

## References
- GlideForm API (client): `getValue`, `setValue`, `clearValue`  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideForm/concept/c_GlideFormAPI.html
- Working with MRVS values on the client (community examples)  
  https://www.servicenow.com/community/developer-articles/accessing-multi-row-variable-set-value-outside-the-multi-row/ta-p/2308876

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
