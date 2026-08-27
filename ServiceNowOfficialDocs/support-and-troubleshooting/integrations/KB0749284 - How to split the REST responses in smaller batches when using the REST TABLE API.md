---
title: "How to split the REST responses in smaller batches when using the REST TABLE API"
aliases:
  - KB0749284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749284
kb_number: KB0749284
last_modified: 2024-04-07
---

## How to split the REST responses in smaller batches when using the REST TABLE API

  

### Issue

The table API is an out of the box feature and is ideal when integrating between third-party applications.

### Resolution

If your REST remote application needs to send the query in a single URL, dedicated permissions need to be granted for the query to return results.

The REST Table API can be used as follow:

-   Table API - GET /now/table/{tableName}.  OR
-   Table API - GET /now/table/{tableName}/{sys\_id}

You can also specified the version:

URL format

-   Versioned URL: /api/now/{version}/table/{tableName}
-   Default URL: /api/now/table/{tableName}

The REST Table API has some request parameters that aid the way to split the results.

For example, this Table API REST query returns all the incidents where the priority is low and active is true

Example incident Table API query:

https://xxxxxx.service-now.com/api/now/table/incident?sysparm\_fields=number,caller\_id&sysparm\_query=active=true^priority=4

the **sysparm\_fields** provide a list of the fields that should be returned and the **sysparm\_query** lets you specify the filtered query.

When dealing with Large result sets, use the **sysparm\_offset** with **sysparm\_limit** parameters

So let us say that there are 2500 rows but that is too much in one go, so you only want to return up to 500 rows at a time, to avoid performance issues. You need to return the first batch of 500 and then, the next 500 records and so on up to the point where you return all of the 2500 rows in 5 batches.

  
Here are the 5 batches /queries that will return 5 slices of the result set of the table expected to be around 2500 records large.

https://xxxxx.service-now.com/api/now/table/incident&sysparm\_limit=500&sysparm\_offset=500  
https://xxxxx.service-now.com/api/now/table/incident&sysparm\_limit=500&sysparm\_offset=1000  
https://xxxxx.service-now.com/api/now/table/incident&sysparm\_limit=500&sysparm\_offset=1500  
https://xxxxx.service-now.com/api/now/table/incident&sysparm\_limit=500&sysparm\_offset=2000  
https://xxxxx.service-now.com/api/now/table/incident&sysparm\_limit=500&sysparm\_offset=2500

Be careful that not too many rows are returned, otherwise this will impact the performance of your instance, if you do need to return large results sets, then the **sysparm\_offset** should be used.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Alert" src="/Warning_25x.pngx" alt="Alert icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Warning</strong>: Be careful that this API also lets you delete rows if ACLs permit, ensure that only the relevant access rights are granted.</td></tr></tbody></table>

### Related Links

-   [Table API](<https://docs.servicenow.com/ API> "Table API") \[Orlando docs\]
