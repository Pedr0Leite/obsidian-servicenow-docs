---
title: "CMS Service Catalog missing header"
aliases:
  - KB0551789
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551789
kb_number: KB0551789
last_modified: 2024-04-07
---

## CMS Service Catalog missing header

  

### Issue

CMS Service Catalog missing header  

Problem

* * *

Service Catalog within CMS is not displaying the header search bar, breadcrumbs, and results-per-page choice list.  

Symptoms

* * *

This screenshot show the issue:

![](/sys_attachment.do?sys_id=06ce7ca2db0ab450e515c22305961926)    
  

Cause

* * *

The **Simple catalog display** option on the Site record controls this behavior. The option simplifies catalog pages in the site by hiding the search bar, breadcrumbs, and the results per page choice list. Selecting this option also prevents you from adding attachments from record producers to your CMS site.  
  
![](/sys_attachment.do?sys_id=4ece7ca2db0ab450e515c2230596192f)

Resolution

* * *

1.  Navigate to **Content Management > Sites**.
2.  Select the site record experieincing the issue.
3.  Ensure that the 'Simple catalog display' option is not selected if you want to see the header (search bar, breadcrumbs, and results per page choice list) within the CMS Catalog

For more information, see [Creating a New Site](https://docs.servicenow.com/csh?topicname=t_CreateANewSite.html&version=latest "Creating a New Site") in the product documentaiton.
