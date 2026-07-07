---
title: "Cloud Management - Cloud  Service Account are unable to discover datacenters error as \"Could not login on vmware instance\"
aliases:
  - KB0694579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694579
kb_number: KB0694579
last_modified: 2025-08-25
---

## Cloud Management - Cloud Service Account are unable to discover datacenters error as "Could not login on vmware instance"

  

### Issue

# Symptoms

* * *

When we are trying to Discover VCenter usign Cloud Service Account, we can see error as "**Could not login on vmware instance**"

When we review cloud API, we can see error stack as 

Route error says -Could not login on vmware instance   
  
Error details are   
java.lang.RuntimeException: Could not login on vmware instance   
at com.snc.cmp.connector.cloud.compute.provider.impl.vSphereComputeProvider.login(vSphereComputeProvider.java:701)   
at com.snc.cmp.connector.cloud.compute.provider.impl.vSphereComputeProvider.listDatacenters(vSphereComputeProvider.java:1860)   
at com.snc.cmp.connector.cloud.compute.customizer.impl.vSphereComputeCustomizer.listDatacenters(vSphereComputeCustomizer.java:399)   
at com.snc.cmp.connector.cloud.compute.component.CloudComputeProducer.process(CloudComputeProducer.java:78)   
at org.apache.camel.util.AsyncProcessorConverterHelper$ProcessorToAsyncProcessorBridge.process(AsyncProcessorConverterHelper.java:61)   
at org.apache.camel.processor.SendProcessor.process(SendProcessor.java:145)   
at org.apache.camel.management.InstrumentationProcessor.process(InstrumentationProcessor.java:77)   
at org.apache.camel.processor.RedeliveryErrorHandler.process(RedeliveryErrorHandler.java:468)   
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)   
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)   
at org.apache.camel.component.direct.DirectProducer.process(DirectProducer.java:62)   
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)   
at org.apache.camel.util.AsyncProcessorHelper.process(AsyncProcessorHelper.java:109)   
at org.apache.camel.processor.UnitOfWorkProducer.process(UnitOfWorkProducer.java:68)   
at org.apache.camel.impl.ProducerCache$2.doInProducer(ProducerCache.java:412)   
at org.apache.camel.impl.ProducerCache$2.doInProducer(ProducerCache.java:380)   
at org.apache.camel.impl.ProducerCache.doInProducer(ProducerCache.java:270)   
at org.apache.camel.impl.ProducerCache.sendExchange(ProducerCache.java:380) 

# Release

* * *

Jakarta and above

Cloud Management Plugin V2.0

# Environment

* * *

Jakarta and above

# Cause

* * *

The Datacenter URL does have the correct format to access.

 If we are not using this then the Service account will not gain access and throws an Error.

# Resolution

* * *

Please update the  Datacenter URL as [https://<IP ADDRESS>/sdk](https://10.120.110.12/sdk) and Run Datacenter Discovery
