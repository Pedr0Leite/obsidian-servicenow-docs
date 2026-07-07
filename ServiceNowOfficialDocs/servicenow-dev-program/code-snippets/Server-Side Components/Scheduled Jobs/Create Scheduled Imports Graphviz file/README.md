---
title: "Create Scheduled Imports Graphviz file"
aliases:
  - Create Scheduled Imports Graphviz file
tags:
  - servicenow-dev-program
  - code-snippet
  - create-scheduled-imports-graphviz-file
  - scheduled-jobs
---

# Graphviz graph of Scheduled Import parent/child relations

Create a Graphviz DOT graph of Scheduled Import with parent/child relations

**Not an actual Scheduled Job but rather to be run as a Background Script or in Xplore.**

Add "grSIS.addEncodedQuery(...)" lines as required to filter on specific Scheduled Imports.

Output is a Graphviz DOT file of all (or filtered) Scheduled Imports parent/child relationships.

The output file can for example be viewed on the following pages:
- https://edotor.net/
- https://dreampuf.github.io/GraphvizOnline/

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
