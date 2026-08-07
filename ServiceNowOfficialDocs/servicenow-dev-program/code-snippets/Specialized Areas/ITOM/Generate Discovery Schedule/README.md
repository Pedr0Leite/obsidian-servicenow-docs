---
title: "Generate Discovery Schedule"
aliases:
  - Generate Discovery Schedule
tags:
  - servicenow-dev-program
  - code-snippet
  - generate-discovery-schedule
  - itom
---

This script will help in generating a discovery schedule with the list of IP addresses mentioned in the ip_list variable and then starting the discovery.

It has some properties present in it like:
    -> discover.<region>.cluster => SYS ID of the regional cluster made
    -> discover.mid_user => JSON object of mid_user accounts based on region similar to midCluster.
        Ex:
            {
                "europe":"<sys_id_of_mid_user_of_the_europe_cluster>",
                "las_vegas":"<sys_id_of_mid_user_of_the_las_vegas_cluster>",
            }, etc.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Bulk Location Update/README|Bulk Location Update]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/Pre README|ServiceNow Discovery Pre Sensor Script: IP Router Association]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Discovery/README|Discovery]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/ITOM/Track Discovery Status/readme|Track Discovery Status]]
