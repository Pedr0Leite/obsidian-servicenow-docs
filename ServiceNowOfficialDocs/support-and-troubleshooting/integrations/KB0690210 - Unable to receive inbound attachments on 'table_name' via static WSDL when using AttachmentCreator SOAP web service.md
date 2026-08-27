---
title: "Unable to receive inbound attachments on 'table_name' via static WSDL when using AttachmentCreator SOAP web service"
aliases:
  - KB0690210
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690210
kb_number: KB0690210
last_modified: 2024-01-28
---

## Unable to receive inbound attachments on 'table\_name' via static WSDL when using AttachmentCreator SOAP web service

  

### Issue

# Symptoms

* * *

In the response body we can see that the attachment is not created in ServiceNow and in payload we see the message:

"Could not find a record in table <table\_name> with sys\_id <sysID>". 

The sys\_id is the one of the record to be updated.

# Release

* * *

Jakarta, Kingston.

# Cause

* * *

The issue is due to the system property **glide.soapprocessor.large\_field\_patch\_max** having a default value of 512 KByte. This is an expected fixed value rather than a cut-off limit, therefore any attachment file with smaller size than this will not be created.

# Resolution

* * *

If you are using SOAP to perform the insert, the payload file size limitation is overridden by the value set in the system property **glide.soapprocessor.large\_field\_patch\_max**. 

When sending a file with a smaller size via the AttachmentCreator, the value should be set accordingly in the system property.

However, the AttachmentCreator SOAP web service is not recommended. Instead, use the [REST Attachment API](https://docs.servicenow.com/csh?topicname=c_AttachmentAPI.html&version=latest#c_AttachmentAPI "REST Attachment API") to manage attachments with web services.

# Additional Information

* * *

Related documentation page: [AttachmentCreator SOAP web service](https://docs.servicenow.com/csh?topicname=r_AttachmentCreatorSOAPWebService.html&version=latest "AttachmentCreator SOAP web service")

[Limitations of the SOAP Attachment Creator webservice with Domain MSP](https://hi.service-now.com/kb_view.do?sysparm_article=KB0690724 "Limitations of the SOAP Attachment Creator webservice with Domain MSP")
