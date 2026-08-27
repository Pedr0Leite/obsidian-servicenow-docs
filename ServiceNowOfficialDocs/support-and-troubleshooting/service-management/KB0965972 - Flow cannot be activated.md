---
title: "Flow cannot be activated"
aliases:
  - KB0965972
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965972
kb_number: KB0965972
last_modified: 2025-01-09
---

## Flow cannot be activated

  

### Issue

When you press the "activate" button, you get the message "Flow activated successfully". However, the flow remains in the "Draft" or "Modified" state and the "activate" button is still available.  
  
No error appears during this process and at times we see the following in the system logs:  
  

Flow Designer: Failed to invoke public com.glide.flow.model.ComponentInstance() with no args
com.google.gson.internal.ConstructorConstructor$3.construct(ConstructorConstructor.java:113)
com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.read(ReflectiveTypeAdapterFactory.java:212)
com.google.gson.internal.bind.TypeAdapterRuntimeTypeWrapper.read(TypeAdapterRuntimeTypeWrapper.java:41)
com.google.gson.internal.bind.CollectionTypeAdapterFactory$Adapter.read(CollectionTypeAdapterFactory.java:82)
com.google.gson.internal.bind.CollectionTypeAdapterFactory$Adapter.read(CollectionTypeAdapterFactory.java:61)
com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$1.read(ReflectiveTypeAdapterFactory.java:131)

### Cause

Issue is cause of due to a corrupt data pill which had a missing reference which caused the Flow to not get activated.

### Resolution

On adding the missing reference, the flow will be successfully activated.
