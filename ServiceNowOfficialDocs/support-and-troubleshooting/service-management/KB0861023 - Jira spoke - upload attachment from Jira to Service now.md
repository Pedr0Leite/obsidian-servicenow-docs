---
title: "Jira spoke - upload attachment from Jira to Service now"
aliases:
  - KB0861023
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861023
kb_number: KB0861023
last_modified: 2025-01-02
---

## Jira spoke - upload attachment from Jira to Service now

  

### Summary

You would like to retrieve an attachment that was uploaded to Jira and upload it to ServiceNow.

### Release

undefined

### Instructions

First step is to follow [this](https://hi.service-now.com/kb_view.do?sysparm_article=KB0831019 "this") article and [this](https://docs.servicenow.com/csh?topicname=setup-jira302-webhooks.html&version=latest "this") documentation.

Then you will create the actions and Flow logic that will bring you to this final setup:

![](sys_attachment.do?sys_id=9b093849db40f8d066e0a345ca9619ba)

Note that this is an example that should give you guidance on how to achieve this step. It will be up to you to configure the actions and steps are per your business requirements, and Technical Support does not assist in the implementation per se. 

Note that points like A and B would need to be created before points like 1,2,3,4 but for  avoiding confusion I am presenting here the subflow setup, while  the setup of the actions constituting it will be shown towards the end.

 We will create our example on incident record. You can adapt it to your needs.

These are the steps. 

1\. After configuring  the Bi-directional Jira Integration you should have the below 2 setup in place: 

![](sys_attachment.do?sys_id=1f093849db40f8d066e0a345ca9619cc)

![](sys_attachment.do?sys_id=6b097849db40f8d066e0a345ca961912)

2\. You would then select "Add Flow Logic" and chose "If"

You would then configured as below:

![](sys_attachment.do?sys_id=e3097849db40f8d066e0a345ca961914)

3\. You would then press on the small "+" sign as below:

  

![](sys_attachment.do?sys_id=17093849db40f8d066e0a345ca9619c6)

and configure "Get Attachment Details" action as below:

![](sys_attachment.do?sys_id=df093849db40f8d066e0a345ca9619e2)

Note: The action should be created before this. Please follow step "A" that will be detailed below for creating this action.

4\. Then you would click again on the small "+" sign and configure the "Save attachment from Jira" action as below:

![](sys_attachment.do?sys_id=d3093849db40f8d066e0a345ca9619e6)

Note: The action should be created before this. Please follow step "B" that will be detailed below for creating this action.

  

As mentioned, in order to be able to configure steps 3 and 4 you first need to have the actions created. 

Here is how to configure them:

A: Get Attachment Details Action.

A.1. See input:

![](sys_attachment.do?sys_id=6f097849db40f8d066e0a345ca961915)

A.2. See script step:

![](sys_attachment.do?sys_id=e7097849db40f8d066e0a345ca961917)

  

This is the script:

(function execute(inputs, outputs) {  
var payload = JSON.parse(inputs.payload);  
  outputs.attachment\_name = payload.attachment.filename;  
    outputs.attachment\_url = payload.attachment.content;  
})(inputs, outputs);

  

A.3. See outputs:

![](sys_attachment.do?sys_id=a3093849db40f8d066e0a345ca9619f9)

  

B. Save attachment from Jira action.

B.1. See input:

![](sys_attachment.do?sys_id=63097849db40f8d066e0a345ca961919)

B.2. See script step:

![](sys_attachment.do?sys_id=6b097849db40f8d066e0a345ca961933)

  

This is the script:

(function execute(inputs, outputs) {  
  var result;  
  var url = inputs.conn\_url;  
     var baseUrlPattern = /^https?:\\/\\/\[a-z\\:0-9-.\]+/;  
    var match = baseUrlPattern.exec(url);  
    if (match != null) {  
        result = match\[0\];  
    }  
    if (result.length > 0) {  
        url = url.replace(result, "");  
    }  
  inputs.file\_name = inputs.file\_name.replace(/ /g,"+");  
  if(inputs.file\_name == "" || inputs.file\_name == null)  
    outputs.name = "MyFile";  
  else   
    outputs.name = inputs.file\_name;  
  outputs.resource\_path = url;  
})(inputs, outputs);  
  

  

B.3. This is the REST step:  
  
![](sys_attachment.do?sys_id=e3097849db40f8d066e0a345ca961935)  

Test now by adding an attachment in one of the Jira records.  
With this setup in place you should have a new incident create in ServiceNow,and an attachment should be also attached to the new record.  
  

### Related Links

undefined
