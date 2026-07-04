---
title: "Configure the number of agent assist results to show up in contextual sidebar in HR Agent workspace"
aliases:
  - KB1539913
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1539913
kb_number: KB1539913
last_modified: 2025-09-03
---

## Configure the number of agent assist results to show up in contextual sidebar in HR Agent workspace

  

### Summary

The number of results in response templates is driven by the cxs\_config for a table.

1.   Head to the following URL: <instance\_name>/now/nav/ui/classic/params/target/cxs\_table\_config\_list.do%3Fsysparm\_query%3Dsys\_scope%253Dff837553a1112010db4143775de96b71%26sysparm\_first\_row%3D1%26sysparm\_view%3D
2.   Filter the table and title of your choice. (For example: table: sn\_hr\_core\_case, title: Response templates)
3.   Click on your desired record.
4.   Modify the limit field (search results limit) and results per page field as desired. Refer to the screenshot below: ![](/sys_attachment.do?sys_id=dffe88b793ed3150def533527cba106a "CXS Config.png") 
5.   After clearing your cache, you should be able to see the change in number of results and results per page in your application.
