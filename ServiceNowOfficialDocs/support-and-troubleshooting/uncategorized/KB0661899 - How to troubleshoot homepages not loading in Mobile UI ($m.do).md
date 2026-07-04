---
title: "How to troubleshoot homepages not loading in Mobile UI ($m.do)"
aliases:
  - KB0661899
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661899
kb_number: KB0661899
last_modified: 2026-04-02
---

## How to troubleshoot homepages not loading in Mobile UI ($m.do)

  

### Issue

## How to troubleshoot homepages not loading in Mobile UI ($m.do)

* * *

The objective of this article is to help troubleshooting home pages on the mobile UI.

## **Procedure**

* * *

-   Access the instance from mobile browser
-   **https://<instance-name>.service-now.com/$m.do#/home**
-   The home page keeps loading indefinitely...
-   Access the instance from the standard desktop UI 
-   **https://<instance-name>.service-now.com**
-   The home page loads properly.

## Problem

* * *

In such a scenario, navigating to **/$m.do** you might observe the following JavaScript error in the bowser console:

  
Uncaught (in promise) TypeError: Cannot read property 'hide\_favorites\_page' of undefined   
at y (js\_includes\_snm.jsx?v=09-05-2017\_1648&lp=Thu\_Dec\_28\_17\_54\_22\_PST\_2017&c=22\_282:10)   
at Object.v \[as getHomepageData\] (js\_includes\_snm.jsx?v=09-05-2017\_1648&lp=Thu\_Dec\_28\_17\_54\_22\_PST\_2017&c=22\_282:10)   
at js\_includes\_snm.jsx?v=09-05-2017\_1648&lp=Thu\_Dec\_28\_17\_54\_22\_PST\_2017&c=22\_282:10   
at <anonymous> 

## Resolution

* * *

The error occurs because records in the \[sys\_ui\_mobile\_home\_page\_module\] associated modules are either not present, or set as inactive in the mobile modules list.

For example: "Share Location", "Favorite KPIs", and "Connect Chat".

![](sys_attachment.do?sys_id=d27aa866db42b450e515c223059619f6)

For the Home page to load properly in the Mobile browser, \[sys\_ui\_mobile\_home\_page\_module\] records should have mobile modules associated with them. These should be active in the Mobile modules as well.

![](sys_attachment.do?sys_id=a67aa866db42b450e515c223059619fb)
