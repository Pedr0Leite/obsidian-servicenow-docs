---
title: "REST Table API Version Differences"
aliases:
  - KB0551763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551763
kb_number: KB0551763
last_modified: 2024-04-07
---

## REST Table API Version Differences

  

### Issue

REST Table API Version Differences

# What Table API versions are available?

* * *

Versions v1 and v2 of the Table API are available. Version v2 is available starting with the Geneva release.

# How are v1 and v2 different?

* * *

-   In version v1, if a GET query to retrieve multiple records matches no records, the response is the error _**No Record Found**_ with status code 404.
-   In version v2, if a GET query to retrieve multiple records matches no records, the response is an empty array with status code 200.

Other Table API HTTP methods such as POST or DELETE behave the same in v1 and v2.

# Table API v1 example

* * *

**Query:** 

[https://<instance>.service-now.com/api/now/v1/table/incident?sysparm\_query=short\_descriptionLIKEdescription\_random](https://\<instance\>.service-now.com/api/now/v1/table/incident?sysparm_query=short_descriptionLIKEdescription_random)

**Response:**

Status Code: 404 Not Found

Response body:

{

  "error": {

    "message": "No Record found",

    "detail": "Records matching query not found. Check query parameter or offset parameter"

  },

  "status": "failure"

}

# Table API v2 example

* * *

**Query:** 

[https://<instance>.service-now.com/api/now/v2/table/incident?sysparm\_query=short\_descriptionLIKEdescription\_random](https://\<instance\>.service-now.com/api/now/v1/table/incident?sysparm_query=short_descriptionLIKEdescription_random)

**Response:**

Status Code: 200 OK

Response body:

{

  "result": \[\]

}
