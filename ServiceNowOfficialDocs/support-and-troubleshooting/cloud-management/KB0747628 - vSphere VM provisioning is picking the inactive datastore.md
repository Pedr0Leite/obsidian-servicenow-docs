---
title: "vSphere VM provisioning is picking the inactive datastore"
aliases:
  - KB0747628
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747628
kb_number: KB0747628
last_modified: 2023-11-02
---

## vSphere VM provisioning is picking the inactive datastore

  

### Issue

# Description

While performing the Cloud Discovery on Vsphere Datacenter, the available datastores are populated to **"cmdb\_ci\_vcenter\_datastore"** table and marks ACCESSIBLE=TRUE, for some reason if the Datastore is not available at the Vsphere datacenter and next discovery identifies the missing Datacenter and marks the CI to ACCESSIBLE=FALSE.

# Issue

VM provision on Vsphere  Datacenter fails with below stack.

java.lang.RuntimeException: Unable to access the virtual machine configuration: Unable to access file \[USCINFRADS-8\]   
at com.snc.cmp.connector.cloud.compute.provider.impl.vSphereComputeProvider.awaitComplete(vSphereComputeProvider.java:1302)   
at com.snc.cmp.connector.cloud.compute.provider.impl.vSphereComputeProvider.createClone(vSphereComputeProvider.java:1020)   
at com.snc.cmp.connector.cloud.compute.provider.impl.vSphereComputeProvider.createNode(vSphereComputeProvider.java:347)   
at com.snc.cmp.connector.cloud.compute.customizer.impl.vSphereComputeCustomizer.createNode(vSphereComputeCustomizer.java:192)   
at com.snc.cmp.connector.cloud.compute.component.CloudComputeProducer.process(CloudComputeProducer.java:48)   
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
at org.apache.camel.impl.ProducerCache.send(ProducerCache.java:238)   
at org.apache.camel.impl.DefaultProducerTemplate.send(DefaultProducerTemplate.java:128)   
at org.apache.camel.impl.DefaultProducerTemplate.sendBodyAndHeaders(DefaultProducerTemplate.java:253)   
at org.apache.camel.impl.DefaultProducerTemplate.requestBodyAndHeaders(DefaultProducerTemplate.java:313)   
at org.apache.camel.impl.DefaultProducerTemplate$10.call(DefaultProducerTemplate.java:588)   
at java.util.concurrent.FutureTask.run(FutureTask.java:266)   
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)   
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)   
at java.lang.Thread.run(Thread.java:748)  

# Release

-   Kingston P\*, London P\* 

# Cause

-   The Provision operation picks up random Datastore from **"cmdb\_ci\_vcenter\_datastore"** and currently, the vSphere Cloud API(MID - Java api) picks the first datastore and CMP expects that all datastores to be ACCESSIBLE=TRUE. 

# Workaround

-   Select the 'Datastore' and 'ClusterDatastore' by enabling it in the blueprint.

![](/sys_attachment.do?sys_id=72fc2c22db82b450e515c22305961977)

  

-   Manually delete the ACCESSIBLE=FALSE datastores from **"cmdb\_ci\_vcenter\_datastore"** table.

# Fix

-   ServiceNow development team working on **"FTASK43955"** to avail BR/Script include at the provision operation that if the user did not select the Datastore, the provision should only take the Datastores in ACCESSIBLE=TRUE
