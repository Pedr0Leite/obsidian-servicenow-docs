---
title: "Why addQuery() method in Business Rule constructs incorrect query?"
aliases:
  - KB0692550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692550
kb_number: KB0692550
last_modified: 2024-01-28
---

## Why addQuery() method in Business Rule constructs incorrect query?

  

### Issue

# Symptoms

* * *

"Before query Business Rule" on a "task" record suppose to filter the data based on the AddQuery() method and parameters supplied in "script" section of the business rule. 

However, the AddQuery() method was constructing an incorrect query and hence expected results were not returned while viewing the task record / list.

Below screenshot shows this incorrect query constructed by the before query business rule,

![](sys_attachment.do?sys_id=386e3c22db0ab450e515c223059619d6)

Another symptoms is, at times, the query also can be reversed, for example, when you expect query to have "LIKE", it might have "NOT LIKE" operator.

# Release

* * *

Any supported release.

# Cause

* * *

In the script section of before query business rule, an additional space was suffixed with the operator on the addQuery() method as shown in the below screenshot.

![](sys_attachment.do?sys_id=3c6e3c22db0ab450e515c223059619db)

# Resolution

* * *

Remove any space prefixed/suffixed from the operators in  addQuery() method.

# Additional Information

* * *

[Business rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business rules")

[GlideRecord query](https://docs.servicenow.com/csh?topicname=c_UsingGlideRecordToQueryTables.html&version=latest "GlideRecord query")

[Available operators](https://docs.servicenow.com/csh?topicname=c_UsingGlideRecordToQueryTables.html&version=latest "Available operators")
