---
title: "Creating attachments using Web Services"
aliases:
  - KB0546294
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546294
kb_number: KB0546294
last_modified: 2026-06-10
---

## Creating attachments using Web Services

  

### Issue

This article addresses the following two needs:

-   create attachments in ServiceNow through a web service request
-   determine if there are limits on attachment size while sending a large payload as an attachment

### Resolution

Follow the instructions in [Attachment Creator Webservice](https://docs.servicenow.com/csh?topicname=r_AttachmentCreatorSOAPWebService.html&version=latest "Attachment Creator Webservice") in the ServiceNow product documentation.

The article is written for SOAP web services, but the same principle can be used with either REST API or JSONv2. In those cases, send a POST request to the following URLs:

-   REST: https://<instance-name>/api/now/table/ecc\_queue
-   Headers for REST:  
    -   Accept = application/json
    -   Content-Type = application/json
-   JSON v2: https://<instance-name>/ecc\_queue.do?JSONv2?sysparm\_action=insert  
    -   Headers for JSONv2 not required
    -   Use a request body of:
        
        {"agent":"AttachmentCreator","topic":"AttachmentCreator","name":"<FileName>:<Format>","source":"<targetTable>:<SysId>","payload":"<base64encodedStr>"}
        
        Example:
        
        {"agent":"AttachmentCreator","topic":"AttachmentCreator","name":"john1.txt:text/plain","source":"incident:e886867e1b9b2050ac4475561a4bcb34","payload":"SSB3b25kZXIgaWYgc2hlIGtub3ducyB3aGF0IHNoZSdzIGRvaW5nIG5vdy4K"}
        

### Related Links

Business rules and sensors are defined on the ECC Queue to act on records inserted with the AttachmentCreator agent. Sending a request to the ECC Queue as described above through any web service creates the attachment.

Attachment creation is limited by:

-   The size of the payload field  
    -   The payload field can take values up to 16MB so it is usually okay to send a base64 encoded payload with a size up to max 16,777,215 bytes(=15,9MB)
    -   If you are using SOAP to do the insert, the payload file size limitation is overridden by the **glide.soapprocessor.large\_field\_patch\_max** property
-   The max attachment size property  
    -   To check the max attachment file size property, follow the instructions in [Limiting Attachment File Size](https://docs.servicenow.com/csh?topicname=r_AdministeringAttachments.html&version=latest "Limiting Attachment File Size") in the ServiceNow product documentation
-   The size of the request body  
    -   If the body is too big to process within the defined timeout period, the entire transaction can get canceled and cause a timeout response. With the out-of-box HTTP timeout setting, an attachment with a size of 8 MB should still be attached successfully.
