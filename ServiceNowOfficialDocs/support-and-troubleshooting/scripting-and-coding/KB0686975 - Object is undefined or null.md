---
title: "Object is undefined or null "
aliases:
  - KB0686975
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686975
kb_number: KB0686975
last_modified: 2024-04-25
---

## Object is undefined or null

  

### Issue

Pop up /Message saying that the object is undefined.

### Cause

In javascript, the object was set to **null** as the method returned **null**.

### Resolution

Include an _if_ statement to check if the object **is not null** and then use the object properties, for example:

var priority = gr. getreference("incident\_prioirty")  
if (prioirity)  
{  
  // do something with the priority   
}
