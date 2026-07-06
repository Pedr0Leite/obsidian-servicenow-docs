---
title: "Bulk Location Update"
aliases:
  - Bulk Location Update
tags:
  - servicenow-dev-program
  - code-snippet
  - bulk-location-update
  - itom
---

This script will get all the CI classes mentioned in the property "nonDiscovery.location.update" in a comma-separated and fetch all the sub-classes of the mentioned classes and update the location data based on subnet information stored in 'cmdb_ci_ip_network_subnet' table and make updates in bulk on location basis.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/Pre README|ServiceNow Discovery Pre Sensor Script: IP Router Association]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/README|Discovery]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Generate Discovery Schedule/README|Generate Discovery Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Track Discovery Status/readme|Track Discovery Status]]
