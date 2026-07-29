---
title: "Get KB Article Permalink"
aliases:
  - Get KB Article Permalink
tags:
  - servicenow-dev-program
  - code-snippet
  - get-kb-article-permalink
  - flow-actions
---

# Get KB Article Permalink
Flow Action which will take KB Article Number as input and returns the latest version of Permalink. This URL will stay constant always even if the KB Article is updated with new version.

**Input** : KB Article Number (Type : String)

**Script Step** : Generates the Permalink URL for KB Article (see the script.js file in this folder)

**Output** : Permalink (Type : URL)

**Usage** : This can be used in multiple scenarios where the KB Article Link/URL is required. It can either be in notifications, scripts, Integrations, etc. Since this Permalink is always fixed and works even if the KB Article is updated to new version, there is no maintainance required.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Add signature and update fields to a fillable PDF document/README|Add signature and update fields to a fillable PDF document]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
