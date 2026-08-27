---
title: "System Log displays error \"CMS site data missing from table\"
aliases:
  - KB0552183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552183
kb_number: KB0552183
last_modified: 2024-01-28
---

## System Log displays error "CMS site data missing from table"

  

### Issue

System Log displays error: "CMS site data missing from table"

Problem

* * *

The System Log is displaying a reoccurring error similar to:  
  
CMS site data missing from table: \[sc\_catalog\_site\] sc\_catalog: \[e0d08b13c3330100c8b837659bba8fb4\] content\_site: \[faea7ad449922000caa52338b90d7897\]: no thrown error

   
Symptoms

* * *

The following error is seen when the System Administrator naviagates to System Logs > System Log > Errors:  

![](/sys_attachment.do?sys_id=bd2d2c62db82b450e515c223059619bf)

Cause

* * *

This error message is hard-coded, non-editable, and generated from this snippet with the CatalogSite.java code:  
  
// If we get here the object hasn't been cached yet.  
GlideRecord catSiteGr = new GlideRecord(SC\_CATALOG\_SITE);  
catSiteGr.addQuery(SC\_CATALOG, fCatalogId);  
catSiteGr.addQuery(CONTENT\_SITE, fSiteId);  
catSiteGr.query();  
  
/\*  
\* If Customer CMS site hasn't been set up just return a blank string  
\* This may cause some slow down until they set up their CMS site  
\* correctly. We could cache the blank values but would we want to speed  
\* up incorrect config?  
\*/  
if (!catSiteGr.next()) {  
Log.error(String.format("CMS site data missing from table: \[%s\] sc\_catalog: \[%s\] content\_site: \[%s\]",  
new Object\[\]{SC\_CATALOG\_SITE, fCatalogId, fSiteId}));  
return;  
}

The above code cheeks if a CMS Site \[content\_site\] has a corresponding Catalog \[sc\_catalog\]. Starting with Eureka, support for multi-catalogs was introduced. For more information, see [Managing Catalog Sites](https://docs.servicenow.com/csh?topicname=t_ManageCatalogSites.html&version=latest "Managing Catalog Sites").  
  
If you want to use a Catalog \[sc\_catalog\] within a CMS Site \[content\_site\], a Catalog Site \[sc\_catalog\_site\] record must be defined linking the two. The example screenshots shows want is configured in the base system:

  
![](/sys_attachment.do?sys_id=0e2d2c62db82b450e515c223059619f7)  
  

Resolution

* * *

To resolve the error, associate Catalog(s) to the CMS Site with the following steps:  

1.  Navigate to **Content Management > Sites**.
2.  Filter on the sys\_id of the Site \[content\_site\] referenced in the error.
3.  Configure related lists to add the Catalog related list (it is not displayed in the base system by default).
4.  On the related list, click **Edit** to specify the missing Catalog(s).  
    The following is a example of the base system CMS Site's Catalog association:

  
![](/sys_attachment.do?sys_id=c62d6c62db82b450e515c22305961902)
