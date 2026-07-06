---
title: "How to send Outbound REST request with multipart/form-data"
aliases:
  - KB0745010
tags:
  - servicenow
  - support-kb
  - rest-api
  - integration-hub
  - flow-designer
  - mid-server
  - attachments
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745010
kb_number: KB0745010
last_modified: 2024-09-05
---

## How to send Outbound REST request with multipart/form-data

  

### Issue

This article describes the procedure to send an outbound REST request of type 'multipart/form-data'.

### Prerequisite

Multipart/form-data requests are supported only via a REST action step in the IntegrationHub which comes as part of the [ServiceNow IntegrationHub](https://docs.servicenow.com/csh?version=latest&topicname=integrationhub.html "ServiceNow IntegrationHub") plugin. 

### Procedure

Once the required plugin is activated, follow the below steps to create the flow.

1.  Navigate to "Flow Designer" in the filter navigator. 
2.  Click on "Designer"
3.  Create a new flow by clicking on "New" and selecting "New Flow"
4.  Enter the **Name**, **Application**, **Description**, **Run as user** and **Submit**. 
5.  Set the trigger conditions as per your requirement. 
6.  **Save**

The following steps explain how to create the Action.

1.  In the flow designer UI, click on the "+" icon. 
2.  Click on "New Action". 
3.  Enter the required configuration parameters and click on "Submit".
4.  Create a new step here by clicking on the '+' icon under "Action Outline".
5.  In the list of action step options, select "REST" under "Integrations".
6.  Configure the connection details by defining connection inline or by using a connection alias. 
7.  Under Request details, specify the HTTP Method as POST. 
8.  **DO NOT** set the **Content-Type** header. The request will break if you set this. The Content-type is automatically set by the REST Step. 
9.  Under Request Content, select the Request type as "Multipart".
10.  Specify the content of a multiple-part request.
     -   For each request part, specify its name, content type, and value. The name can be any valid string and the type can be any valid type. The value must match the content type.
     -   When Part type File is used the value MUST be the sys\_id of the file in the instance. See [documentation](https://docs.servicenow.com/bundle/washingtondc-build-workflows/page/administer/flow-designer/reference/rest-request-action-designer.html) for more details.
11.  For type, specify the MIME type of the content. For example, application/json, text/plain, etc.
12.  For attachments, set the type and value as given below:  
     1.  Type: attachment
     2.  Value: The Sys ID of the Attachment record containing the content. You can look up this record in a prior step or define it as an input variable.

This completes the setup required for sending outbound REST requests with type multipart/form-data.

-   A sample of how this would look if you sent 2 text fields and one file field are as follows:  
    ![](/sys_attachment.do?sys_id=1b13d05847689a90c4e1a325126d43cb "Capture.PNG")  
    -   It's relevant to note since the REST step is sending an HTTP POST in this example the type is going to be application/json since its a JSON array, but the content-type will be file will be what you set it as. In this sample its application/pdf.

 **Note:** When you send the requests through a MID Server, you will need to ensure that the user configured for the MID server has read access to the attachment table. Otherwise, both the outbound HTTP log and the ECC queue input will indicate that the particular attachment could not be found.

## Related

- [[KB0726269 - Outbound Rest Message that uses a MID Server with the endpoint behind a proxy fails with error java.net.SocketTimeoutExc]] - other outbound REST/MID Server troubleshooting
- [[KB0747638 - Attachment limit for Inbound Integration with base64 encoding]] - related attachment-handling limits
- [[c_AttachmentAPI]] - Attachment API reference

