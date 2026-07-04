---
title: "Accessing a Public table through SOAP fails"
aliases:
  - KB0597588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597588
kb_number: KB0597588
last_modified: 2024-01-28
---

## Accessing a Public table through SOAP fails

  

### Issue

Error when retrieving Public table data using SOAP

Problem

* * *

Unable to retrieve a record from a table using SOAP web service.

Symptoms

* * *

Public table is queried (the sys\_public table has an entry for this table and the value is true) and the following error is returned to the SOAP client application: 

com.glide.processors.soap.SOAPProcessingException: insufficient rights to read <table\_name> <sys\_id></faultstring>  
<detail>com.glide.processors.soap.SOAPProcessingException: insufficient rights to read <table\_name> <sys\_id>  
at com.glide.processors.soap.command.Get.process(Get.java:54)  
at com.glide.processors.soap.SOAPProcessorThread.doCommand(SOAPProcessorThread.java:305)  
at com.glide.processors.soap.SOAPProcessorThread.doCommand(SOAPProcessorThread.java:294)  
at com.glide.processors.soap.SOAPProcessorThread.processStandardWebService(SOAPProcessorThread.java:226)  
at com.glide.processors.soap.SOAPProcessorThread.processBody(SOAPProcessorThread.java:204)  
at com.glide.processors.soap.SOAPProcessorThread.processRequest(SOAPProcessorThread.java:171)  
at com.glide.processors.soap.SOAPProcessorThread.run0(SOAPProcessorThread.java:129)  
at com.glide.util.ParentedThread.run(ParentedThread.java:51)

Cause

* * *

When the SOAP processor receives a request to access a public page, it is processed as the "guest" user. The guest user is unable to process the SOAP request, even though it is a public page. 

Resolution

* * *

To workaround the issue, use a database view that is not public to:

-   enable the correct user to [authenticate](https://docs.servicenow.com/ "authenticate")
-   correctly evaluate against all applicable ACLs

Workaround steps:

1.  [Create a database view](https://docs.servicenow.com/csh?topicname=t_CreateADatabaseView.html&version=latest "Create a database view") against [the table](https://docs.servicenow.com/csh?topicname=t_AddATableToTheDatabaseView.html&version=latest "the table") in question that is public (do not make the view public).
2.  [Add read/create/write ACLs](https://docs.servicenow.com/csh?topicname=t_CreateAnACLRule.html&version=latest "Add read/create/write ACLs") to the database view.
3.  Consume the [WSDL](https://docs.servicenow.com/csh?topicname=c_SOAPWebService.html&version=latest "WSDL") of the database view.
4.  Run the SOAP requests against the view.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: Do not add the database view to the sys_public page. This view must not be public, or the same error occurs.</td></tr></tbody></table>
