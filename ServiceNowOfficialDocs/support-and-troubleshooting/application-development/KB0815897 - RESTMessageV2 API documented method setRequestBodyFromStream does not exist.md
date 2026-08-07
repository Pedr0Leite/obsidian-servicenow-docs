---
title: "RESTMessageV2 API documented method setRequestBodyFromStream does not exist"
aliases:
  - KB0815897
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815897
kb_number: KB0815897
last_modified: 2024-04-08
---

## Issue

According to the ServiceNow API documentation (here: ), [setRequestBodyFromStream(Object stream)](https://developer.servicenow.com/app.do#!/api_doc?v=newyork&id=r_RMV2-setRequestBodyFromStream_O "setRequestBodyFromStream(Object stream)") should be a method "setRequestBodyFromStream", however using that method in a Scripted REST API results in an error:  
{  
"error": {  
"message": "Cannot find function setRequestBodyFromStream in object \[object RESTMessageV2\].",  
"detail": "TypeError: Cannot find function setRequestBodyFromStream in object \[object RESTMessageV2\]. (sys\_ws\_operation.aaca4efbdbaed3406bc9aa484b96190d.operation\_script; line 11)"  
},  
"status": "failure"  
}

## Resolution

  
An alternative would be using   
  
Scoped GlideSysAttachment - writeContentStream(GlideRecord record, String fileName, String contentType, String content)  
Inserts an attachment for the specified record.  
  
Parameters  
Name Type Description  
record GlideRecord The record to which the attachment is to be attached.  
fileName String The attachment's file name.  
contentType String The attachment's content type.  
content String The attachment content.  
  
  
[GlideSysAttachment - Scoped](https://docs.servicenow.com/csh?topicname=c_GlideSysAttachmentScopedAPI.html&version=latestPI.html "GlideSysAttachment - Scoped")
