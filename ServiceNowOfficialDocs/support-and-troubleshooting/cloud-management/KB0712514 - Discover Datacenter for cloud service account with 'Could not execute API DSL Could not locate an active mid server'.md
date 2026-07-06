---
title: "Discover Datacenter for cloud service account with 'Could not execute API DSL : Could not locate an active mid server'"
aliases:
  - KB0712514
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712514
kb_number: KB0712514
last_modified: 2024-04-07
---

## Discover Datacenter for cloud service account with 'Could not execute API DSL : Could not locate an active mid server'

  

### Issue

# Symptoms

* * *

While setting up Cloud Management v2, one of the first things to do after adding the Service Account is to run Datacenter discovery.  Discover Datacenter can fail due to several reasons.  One of the errors encountered during Datacenter Discovery is:

`"Could not execute API DSL : Could not locate an active mid server - Unable to find any validated MID Server based on status (up), and capability: ({Capability: VMware, value: null},{Capability: Cloud Management, value: null}) com.snc.cmp.cloud.api.modules.orchestrator.exception.CAPIOrchestratorException: Could not execute API DSL : Could not locate an active mid server - Unable to find any validated MID Server based on status (up), and capability: ({Capability: VMware, value: null},{Capability: Cloud Management, value: null})\n\tat`com.snc.cmp.cloud.api.modules.orchestrator.service.impl.CAPIOrchestratorServiceImpl.executeApiDsl(CAPIOrchestratorServiceImpl.java:564)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.CloudAPIInvokerServiceImpl.invokeCloudAPI(CloudAPIInvokerServiceImpl.java:55)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.orchestrate(BlueprintOrchestratorImpl.java:292)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.startOrchestration(BlueprintOrchestratorImpl.java:250)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.restartAfterStepCompletion(BlueprintOrchestratorImpl.java:159)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.completeStep(BlueprintOrchestratorImpl.java:127)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.handleStepCompletion(BlueprintOrchestratorImpl.java:186)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.orchestrate(BlueprintOrchestratorImpl.java:339)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.startOrchestration(BlueprintOrchestratorImpl.java:221)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.orchestrate(BlueprintOrchestratorImpl.java:204)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.CloudOrchestrationServiceImpl.orchestrate(CloudOrchestrationServiceImpl.java:271)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.service.impl.OrderServiceImpl.submitOrder(OrderServiceImpl.java:113)\\n\\tat com.snc.cloud.mgmt.modules.svccatalog.scriptinterface.OrderServiceScript.jsFunction\_submitOrder(OrderServiceScript.java:39)\\n\\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\\n\\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\\n\\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\\n\\tat java.lang.reflect.Method.invoke(Method.java:498)\\n\\tat org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)\\n\\tat 

# Release

* * *

Jakarta and above

# Cause

* * *

The error is mainly encountered if there are no MID server in UP state with the required capabilities (CLOUD, VMWare or ALL)

Another reason this issue may occur is if Domain Separation is enabled on the instance and the needed MID Server, even though set-up correctly, is in a different domain.

# Resolution

* * *

1.  At the time of creation of this article, Domain Separation is not supported for Cloud Management v2.
2.  Please make sure that the intended MID Server has state = UP.  In case MID server is down due to technical issue, please use the available knowledge articles to get it back up and running.
3.  Ensure that the intended MID Server has the needed Capabilities.
