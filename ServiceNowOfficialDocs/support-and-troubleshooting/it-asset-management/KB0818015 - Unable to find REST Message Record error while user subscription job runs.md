---
title: "Unable to find REST Message Record error while user subscription job runs"
aliases:
  - KB0818015
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818015
kb_number: KB0818015
last_modified: 2024-05-21
---

## Issue

When the scheduled job to gather adobe integrations run to capture subscription data from adobe profile we see the following error in the system log:

REST Msg Outbound - RESTMessageClient : Error constructing REST Message/Method: \*\*\*\* - lobal/Default GET: com.glide.generators.InvalidGlideRecordException: Unable to find REST Message Record with Name:\*\*\*\*\*\* - lobal: com.glide.rest.outbound.RESTMessageDAO.getRestMessageRecord(RESTMessageDAO.java:86)  
com.glide.rest.outbound.RESTMessageDAO.<init>(RESTMessageDAO.java:71)  
com.glide.rest.outbound.RESTMessageDAO.newInstance(RESTMessageDAO.java:67)  
com.glide.rest.outbound.RESTMessageConfig.initNew(RESTMessageConfig.java:67)  
com.glide.rest.outbound.RESTMessageClient.<init>(RESTMessageClient.java:57)  
com.glide.rest.outbound.scriptable.ScriptableRESTMessageClient.<init>(ScriptableRESTMessageClient.java:56)  
com.glide.rest.outbound.scriptable.ScriptableRESTMessageClient.jsConstructor(ScriptableRESTMessageClient.java:40)  
sun.reflect.GeneratedMethodAccessor2933.invoke(Unknown Source)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)

## Resolution

Create the rest message in a global scope or while creating the integration profile for adobe ensure you are in the global scope.
