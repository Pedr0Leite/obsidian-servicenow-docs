---
title: "Some Lifecycle Event Cases are not listed in the \"My Requests\" page"
aliases:
  - KB1916045
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1916045
kb_number: KB1916045
last_modified: 2026-03-17
---

## Issue

Some Lifecycle Event Cases are not listed in the "My Requests" page on Employee Center

## Resolution

  
To display LE Cases associated with a Journey in the "My Requests" page:

1\. Customize the **\_hrCaseParent**() function in Script Include **hr\_caseMyRequestFilterUtil** and comment out those two lines:

else if (GlidePluginManager.isActive('com.sn\_jny') && parentRecord.getValue('jny\_context'))  
addCase = false;

2.If any Restricted Caller Access (RCA) record gets invalidated, move them back to Allowed status:  
https://instance\_name.service-now.com/sys\_restricted\_caller\_access\_list.do?sysparm\_query=sys\_scopeSAMEAStarget\_scope%5Estatus!%3D2%5EORstatus%3DNULL&sysparm\_view=
