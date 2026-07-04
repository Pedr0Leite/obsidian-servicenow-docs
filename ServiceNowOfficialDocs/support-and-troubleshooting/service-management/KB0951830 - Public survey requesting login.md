---
title: "Public survey requesting login"
aliases:
  - KB0951830
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951830
kb_number: KB0951830
last_modified: 2025-02-28
---

## Public survey requesting login

  

### Issue

You have created a survey and you want it to be public, answered by persons without having to login.  
However the user gets the login prompt when accessing the link to the survey even though the survey is marked as Public.

### Cause

The sp portal is not public and requires login.

I reviewed the Survey Instances generated, and could see that the instance url defaults to sp page:  
https://xxxxxxx.service-now.com/sp?id=public\_survey&instance\_id=86ecb0c7db2068106177264cd39619a4

In sys\_public pages however, the sp page is not active meaning the portal requires login to access.  
https://xxxxxx.service-now.com/nav\_to.do?uri=sys\_public.do?sys\_id=16cf6901c3313100c8b837659bba8f48

  

### Resolution

  
The behavior is caused by the $sp Public Page \[sys\_public\] being NOT Active.

Activate the $sp Public Page on the affected instance.  
You can do this by navigating to the table 'sys\_public' and setting the below record as Active 'true'  
https://xxxxxx.service-now.com/sp?id=public\_survey&instance\_id=86ecb0c7db2068106177264cd39619a4

  

### Related Links

The $sp Public Page must be Active as per the following docs:  
[https://docs.servicenow.com/bundle/paris-servicenow-platform/page/build/service-portal/concept/c\_SPSSOLoginAndRedirects.html](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/build/service-portal/concept/c_SPSSOLoginAndRedirects.html)  
Require authentication for a Service Portal page  
If you want to require authentication for a Service Portal page, ensure that the Public flag on the page record is not selected. For more information, see Create and edit a page using the Service Portal Designer. If a user navigates to a non-public page, they are redirected to the login page for the requested portal.

Because every page request is routed through the $sp page, this page must be public. The following values in the Public Pages sys\_public table define the page as public:

Page: $sp  
Active: true
