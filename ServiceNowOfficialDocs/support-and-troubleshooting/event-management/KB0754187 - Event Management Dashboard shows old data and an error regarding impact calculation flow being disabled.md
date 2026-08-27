---
title: "Event Management Dashboard shows old data and an error regarding impact calculation flow being disabled"
aliases:
  - KB0754187
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754187
kb_number: KB0754187
last_modified: 2024-04-07
---

## Event Management Dashboard shows old data and an error regarding impact calculation flow being disabled

  

### Issue

# Symptoms

![](/sys_attachment.do?sys_id=0bece422db82b450e515c22305961901)

# Cause

It is likely that the impact caculation enable hash is disabled. You should also check that the impact calculator trigger job is also enabled.

# Resolution

**To enable the impact\_calculator\_enable hash:**  
1\. In the navigator, type "sa\_hash.list"  
2\. Press enter  
3\. In the list, filter name by \*impact  
4\. locate the impact\_calculation\_enable record and make sure that the Hash is set to true

![](/sys_attachment.do?sys_id=cbece422db82b450e515c22305961906)

**To enable the impact calculator trigger job:**  
1\. In the navigator, go to System Definition > Scheduled Jobs  
2\. Filter the name by \*Impact Calculator Trigger  
3\. Locate the "Event Management - Impact Calculator Trigger" job and make sure that active is True

![](/sys_attachment.do?sys_id=13ece422db82b450e515c2230596190e)
