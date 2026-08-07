---
title: "Incident Priority Set on Insert Only"
aliases:
  - Incident Priority Set on Insert Only
tags:
  - servicenow-dev-program
  - code-snippet
  - incident-priority-set-on-insert-only
  - transform-map-scripts
---

# Incident priority set on insert only

## What this solves
Recurring imports often overwrite priority even after the service desk has triaged the ticket. This onBefore script sets priority only when a row is inserted. Updates pass through without touching priority.

## Where to use
Attach to your Incident Transform Map as an onBefore script.

## How it works
- Checks the Transform Map action variable for insert vs update
- On insert, computes priority from impact and urgency
- On update, does nothing to priority

## References
- Transform Map scripts  
  https://www.servicenow.com/docs/bundle/zurich-integrate-applications/page/administer/import-sets/task/t_AddOnBeforeScriptToTransformMap.html
- Incident fields and priority logic  
  https://www.servicenow.com/docs/bundle/zurich-it-service-management/page/product/incident-management/concept/incident-fields.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Check if the Import file is valid/README|Check if the Import file is valid]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Choice Field Validator/README|Choice Field Validator]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Conditional Coalesce/README|Conditional Coalesce]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Email Formatter/README|Email Formatter]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Global Variable in Transform Map/README|Global Variable in Transform Map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Verify headers of a CSV attached file/README|Verify headers of a CSV attached file]]
