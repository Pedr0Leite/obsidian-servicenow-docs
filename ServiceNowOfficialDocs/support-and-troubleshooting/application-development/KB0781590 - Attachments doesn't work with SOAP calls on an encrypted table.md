---
title: "Attachments doesn't work with SOAP calls on an encrypted table"
aliases:
  - KB0781590
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781590
kb_number: KB0781590
last_modified: 2025-01-22
---

## Attachments doesn't work with SOAP calls on an encrypted table

  

### Issue

The scenario is to have an integration with third party to open incidents along with attachments in the instance using SOAP web service. Instance has a edge encryption proxy with the attachment encryption active on certain tables

The problem occurs when an attachment is sent with the SOAP call to the incident table. The incident is created but the attachment doesn't get loaded to the incident record. If we deactivate the attachment encryption on incident form, attachment is loaded without issues. 

### Release

London 

### Cause

This is working as expected. Attaching documents via SOAP calls on an incident form with attachment encryption enabled on incident table is not SUPPORTED in the platform.

### Resolution

We recommend using REST to attach documents to a table having attachment encryption enabled.

Posting an attachment to an existing form or table having attachment encryption enabled via SOAP results in the following error:  
  
<SOAP-ENV:Envelope xmlns:SOAP-ENV="[http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/)">  
<SOAP-ENV:Header/>  
<SOAP-ENV:Body>  
<SOAP-ENV:Fault>  
<faultcode>SOAP-ENV:Server</faultcode>  
<faultstring>Unable to parse SOAP document</faultstring>  
<detail>Error completing SOAP request</detail>  
</SOAP-ENV:Fault>  
</SOAP-ENV:Body>  
</SOAP-ENV:Envelope>
