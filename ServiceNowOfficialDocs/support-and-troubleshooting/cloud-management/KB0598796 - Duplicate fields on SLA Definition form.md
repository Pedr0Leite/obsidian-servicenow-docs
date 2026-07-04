---
title: "Duplicate fields on SLA Definition form"
aliases:
  - KB0598796
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598796
kb_number: KB0598796
last_modified: 2024-04-07
---

## Duplicate fields on SLA Definition form

  

### Issue

Duplicate fields on SLA Definition form 

Overview

* * *

If you modified the SLA Definition form and then upgraded to Geneva or a later release, duplicate fields may appear and cause issues.

Problem

* * *

Starting in Geneva, the SLA Definition form layout was changed to have multiple sections.  

Previous Fuji SLA Definition Layout

![](sys_attachment.do?sys_id=261be82adb42b450e515c2230596190c)  

New Geneva SLA Definition Layout

![](sys_attachment.do?sys_id=7a1be82adb42b450e515c22305961944)

If you modified the form in an earlier release to add base fields (such as Reset condition or Condition type), add custom fields, or rearrange the layout, an upgrade to Geneva or a later release adds the new sections, but may not touch the existing form layout. This results in the same field appearing on the form more than once and is known to cause erratic behaviors.

Solution

* * *

1.  Navigate to **Configuration > Form Layout**.
2.  Remove any duplicates from the form.
3.  Correct the fields in the SLA Definition section of the form to reflect the base system configuration.  
    The base system fields in the Geneva form section are:  
      
    ![](sys_attachment.do?sys_id=721be82adb42b450e515c22305961962)
