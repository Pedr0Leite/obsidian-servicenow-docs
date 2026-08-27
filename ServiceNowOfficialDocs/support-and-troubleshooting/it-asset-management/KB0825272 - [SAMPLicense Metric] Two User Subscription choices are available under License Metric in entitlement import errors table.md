---
title: "[SAMP\License Metric] Two \"User Subscription\" choices are available under \"License Metric\" in entitlement import errors table"
aliases:
  - KB0825272
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0825272
kb_number: KB0825272
last_modified: 2024-04-08
---

## \[SAMP\\License Metric\] Two "User Subscription" choices are available under "License Metric" in entitlement import errors table

  

### Issue

-   On the Entitlement Import Errors table under "License Metric" there are 2 "User Subscription" choices listed in the list.

![](sys_attachment.do?sys_id=306c280ddb00b0905a959c41ba96196e)

### Release

-   Instance with Software Asset Management Professional (com.snc.samp) plugin enabled.

### Cause

-   The dictionary entry of "license\_metric" column on "samp\_entitlement\_import" table misses the metric group filtering i.e. due to the reference qualifier condition which was missing for the "license\_metric" dictionary entry, the value is duplicated.

![](sys_attachment.do?sys_id=b46c280ddb00b0905a959c41ba96196f)

### Resolution

-   To resolve this,

1\. Navigate >> Software Asset >> Licensing >> Entitlement Import Errors.  
2\. Open any record where Error status is "Open".  
3\. Right-click on "License Metric" field and select "Configure Dictionary".  
4\. Click "Advanced view" under "Related Links".  
5\. Select "Advanced" in the "Use reference qualifier" dropdown under "Reference Specification" tab.  
6\. Add "**javascript: 'metric\_groupCONTAINS' + current.metric\_group**" in "Reference qual".  
7\. Click "Update"

-   Post update could see the "license\_metric" filtered with default choices.

![](sys_attachment.do?sys_id=3c6c280ddb00b0905a959c41ba961970)
