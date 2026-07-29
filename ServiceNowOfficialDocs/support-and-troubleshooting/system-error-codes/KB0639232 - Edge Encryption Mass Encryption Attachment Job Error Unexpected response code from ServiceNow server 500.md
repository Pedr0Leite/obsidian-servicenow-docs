---
title: "Edge Encryption Mass Encryption Attachment Job Error: Unexpected response code from ServiceNow server: 500"
aliases:
  - KB0639232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639232
kb_number: KB0639232
last_modified: 2024-04-07
---

## Edge Encryption Mass Encryption Attachment Job Error: Unexpected response code from ServiceNow server: 500

  

### Issue

Edge Encryption Mass Encryption Attachment Job Error: Unexpected response code from ServiceNow server: 500

  
  

# Problem

* * *

You have started a mass encryption job to encrypt attachments.  For most attachments the job proceeds without error, but at some point you see the following error in the $proxy\_installation\_location/logs/edgeencryption.log:

com.snc.edgeencryption.rest\_client.RestException: Unexpected response code from ServiceNow server: 500  
at com.snc.edgeencryption.rest\_client.RestClient.sendRequest(RestClient.java:410)  
at com.snc.edgeencryption.rest\_client.RestClient.getAttachmentContent(RestClient.java:211)  
at com.snc.edgeencryption.rest\_client.Attachment.getContentIfUnencrypted(Attachment.java:63)  
at com.snc.edgeencryption.jobs.mass\_encryption.MassAttachmentEncryptionJob.processContent(MassAttachmentEncryptionJob.java:38)  
at com.snc.edgeencryption.jobs.mass\_encryption.AMassAttachmentOperationJob.execute(AMassAttachmentOperationJob.java:43)  
at com.snc.edgeencryption.jobs.AJob.run(AJob.java:44)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)

Repeated attempts to run the mass encryption job results in the same error.

  

# Symptoms

* * *

The mass encryption job has errors, see the mentioned errors in the edgeencryption.log file.

  

# Cause

* * *

There are corrupted attachments. The attachments are already corrupted before there is any attempt to do the encryption of the attachments.  Since the attachments are already corrupted there is no possibility to perform the encryption. This is why the same error is seen each time the mass encryption is attempted.

  

# Resolution

* * *

1.  For the attachments that have failed to get encrypted, go to those records with the attachment and try to download the attachments. If the download of the attachments fail or the downloaded attachment file cannot be unzipped or read by the appropriate program for the attachment type, then the attachment is corrupted.
2.  The best action is to simply remove the attachment from the record since in its corrupted state. It really has no value. 
3.  Once all corrupted attachments are removed the mass encryption should execute to the end without any further 500 errors.
