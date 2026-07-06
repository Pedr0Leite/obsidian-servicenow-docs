---
title: "String index out of range exception with an inbound JSON call"
aliases:
  - KB0725882
tags:
  - servicenow
  - support-kb
  - json-api
  - dictionary
  - task-table
  - custom-fields
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725882
kb_number: KB0725882
last_modified: 2024-04-07
---

## String index out of range exception with an inbound JSON call

  

### Issue

# Symptoms

* * *

When performing the below inbound call on JSON API from browser on the incident table, we see an error with the exception -

"**{"reason":null,"error":"String index out of range: -10"}"** and the incident records were not retrieved in the browser results

 **Inbound API Call:**

https://<instance name> .service-now.com/incident.do?JSONv2&sysparm\_action=getRecords&sysparm\_query=active=true&displayvalue=true

**Exception in the browser with the above Inbound call:**

![](/sys_attachment.do?sys_id=665be86adb42b450e515c22305961988)

# Release

* * *

Issue reported on Kingston Patch 12 but the exception is irrelevant of the product version. It can trigger on any version if the table field types were not configured correctly

# Cause

* * *

-   There exists a custom field named "xxxxx" on the task table which is of type counter for which the expected values should be date/time values.
-   It is observed that the values for this field on the task table ranges between 0 and 17 which are of type Integer. The platform code is expecting this to be a date/time value and does a substring starting at position 11.
-   Since the current integer values which you've got for this field were less than 11 characters( Not the Date/Time Values), you see an "String index out of range" exception when tried to query the incident table using JSON API 

# Resolution

* * *

The solution is to change the type of above mentioned  "xxxxx" custom field on task table from "counter" to "integer string" and then run the JSON call. This should retrieve the incident records in the browser results successfully.

## Related

- [[c_TableAPI]] - REST Table API reference (JSONv2 predecessor of the Table API)

