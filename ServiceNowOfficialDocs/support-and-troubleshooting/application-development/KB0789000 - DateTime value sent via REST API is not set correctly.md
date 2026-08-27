---
title: "DateTime value sent via REST API is not set correctly"
aliases:
  - KB0789000
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789000
kb_number: KB0789000
last_modified: 2024-01-25
---

## DateTime value sent via REST API is not set correctly

  

### Issue

When you update or insert a DateTime field using REST API, the value that is saved might be different from what was sent.

You can see the DateTime value gets saved in the UTC timezone.

### Cause

sysparm\_input\_display\_value is not set to true for the REST API request

### Resolution

REST API stores the date-time in the UTC time zone unless you specify sysparm\_input\_display\_value to true.

If you specify sysparm\_input\_display\_value to true, then the date-time is stored exactly what you sent in the request.

If not, the date-time sent via REST API is converted to the UTC time based on the User's timezone(User initiating the REST call)

If the User's time zone is not set then the system time is taken for reference to convert to UTC.

### Related Links

Please refer - [What is the equivalent of "sysparm\_input\_display\_value" for Change management API](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1588873) for implementing this solution in Change management API
