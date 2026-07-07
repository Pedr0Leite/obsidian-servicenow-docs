---
title: "Get top 5 CIs with most number of Open Incidents"
aliases:
  - Get top 5 CIs with most number of Open Incidents
tags:
  - servicenow-dev-program
  - code-snippet
  - get-top-5-cis-with-most-number-of-open-incidents
  - glideaggregate
---

Use-case:
**Fetch Top 5 CIs with the most number of Open Incidents along with the count**

Type of Script writted: **Background Script**

**How the code works:**
The code uses the GlideAggregate API to efficiently calculate and retrieve the results -
1. A GlideAggregate query is initiated on the Incident table. The query is restricted to only active Incidents.
2. The query instructs the database to COUNT records grouped by the configuration item(cmdb_ci).
3. Furthermore, the records are instructed to be in descending order of number of incidents related to one CI, also a limit
   of 5 records are applied to be fetched.
4. The query is executed and a loop is iterated over these 5 records to fetch and print
   the CI name and its corresponding incident count.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
