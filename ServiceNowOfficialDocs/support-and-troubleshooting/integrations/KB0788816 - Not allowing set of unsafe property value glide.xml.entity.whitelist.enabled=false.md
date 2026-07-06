---
title: "Not allowing set of unsafe property value: glide.xml.entity.whitelist.enabled=false"
aliases:
  - KB0788816
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788816
kb_number: KB0788816
last_modified: 2024-04-20
---

## Issue

System does not allow setting glide.xml.entity.whitelist.enabled to false

## Resolution

This property is not supposed to be reverted back to 'false' under any circumstances. It's a major security risk to have it set to 'false'.  
Moreover, latest releases treat this property as always on, even if does not exist in the instance.  
  
If some external entities need to be whitelisted, there's a special property for it: "glide.xml.entity.whitelist"
