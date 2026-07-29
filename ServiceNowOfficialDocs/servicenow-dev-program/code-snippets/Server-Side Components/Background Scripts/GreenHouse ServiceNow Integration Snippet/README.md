---
title: "GreenHouse ServiceNow Integration Snippet"
aliases:
  - GreenHouse ServiceNow Integration Snippet
tags:
  - servicenow-dev-program
  - code-snippet
  - greenhouse-servicenow-integration-snippet
  - background-scripts
---

This utility contains sample code to integrate ServiceNow with GreenHouse and pull employee files from GreenHouse in ServiceNow Employee Document Management OOB Table records.

Sample code queries HR profile which a filtered query of active users which has a valid greenhouse ID present in ServiceNow HR profile records.

REST message which calls Greenhouse REST API is using below REST endpoint.
https://developers.greenhouse.io/harvest.html#get-retrieve-candidate

Document Types sys_id can be mapped to relevant document types on your instance.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
