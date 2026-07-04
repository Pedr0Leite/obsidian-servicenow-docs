---
title: "Error: 'Unexpected response code from ServiceNow server' seen during the execution of a mass encryption job"
aliases:
  - KB0635051
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635051
kb_number: KB0635051
last_modified: 2024-04-07
---

## Issue

Error: 'Unexpected response code from ServiceNow server' seen during the execution of a mass encryption job

# Symptoms

* * *

When an [encryption job](https://docs.servicenow.com/ "encryption job") is executed, there may be error messages in the logs with the following stack trace:

ERROR Job <Job ID> caught exception during execution  
com.snc.edgeencryption.rest\_client.RestException: Unexpected response code from ServiceNow server: 202  
at com.snc.edgeencryption.rest\_client.RestClient.sendRequest(RestClient.java:409)  
at com.snc.edgeencryption.rest\_client.RestClient.sendRequest(RestClient.java:387)  
at com.snc.edgeencryption.rest\_client.RestClient.streamAttachmentChunk(RestClient.java:167)  
at com.snc.edgeencryption.rest\_client.RestAttachmentChunkIterator.getIter(RestAttachmentChunkIterator.java:21)  
at com.snc.edgeencryption.rest\_client.ALazyRestIterator.ensureIter(ALazyRestIterator.java:51)  
at com.snc.edgeencryption.rest\_client.ALazyRestIterator.hasNext(ALazyRestIterator.java:19)  
at com.snc.edgeencryption.rest\_client.RestAttachmentChunkIterator.hasNext(RestAttachmentChunkIterator.java:5)  
at com.snc.edgeencryption.jobs.mass\_encryption.AMassAttachmentOperationJob.execute(AMassAttachmentOperationJob.java:36)  
at com.snc.edgeencryption.jobs.AJob.run(AJob.java:44)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)  
at java.lang.Thread.run(Thread.java:748)

This may occur at anytime during the job execution.

  

  
  

  

  

  

## Resolution

#   

  

Given a 202 does not indicate the encryption job actually failed, there may be no action that is needed when you come across this error message. Navigate to the Encryption Job Execution Chunk **sys\_encryption\_job\_execution\_chunk** table and change the state to **Ready** for any entries showing **Error**. This queues the job to be processed again and allows only one execution running at any given time.

Alternatively, the mass encryption job can be ran again and may complete without error. Even though the same record count is shown, the server skips rows that have already been encrypted, so the amount of processing required is reduced for each subsequent execution. Once the remaining row count is low enough for the server to process, a 200 status will be issued in the HTTP response and the job is marked complete.
