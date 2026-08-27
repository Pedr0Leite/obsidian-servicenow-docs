---
title: "Issue with Attachments output variables in flow designer actions"
aliases:
  - KB0825333
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0825333
kb_number: KB0825333
last_modified: 2024-04-08
---

## Issue with Attachments output variables in flow designer actions

  

### Issue

User when trying to send multiple attachments as a array of objects, if they try to send two different attachments in output it shows both the attachments are having the same name but different content.

Script to parse the attachment and output the information:

 inputs = {};  
inputs.IncSysId = '84c2e556dbe49050a865bc23e2961923';  
outputs = {};  
execute(inputs, outputs);  
  
function execute(inputs, outputs) {  
  
//Attachments code  
var attachStr;  
var attachments=\[\];  
outputs.attachments=\[\];  
var i=0;  
var attachRec = new GlideRecord('sys\_attachment');  
attachRec.addQuery('table\_sys\_id', inputs.IncSysId);  
attachRec.addQuery('table\_name', 'incident');  
attachRec.query();  
  
while(attachRec.next()) {  
var sa = new GlideSysAttachment();  
var StringUtil = new GlideStringUtil();  
var attachobj={"attachment":{}};  
var fileName=attachRec.file\_name;  
var fileContent=attachRec.content\_type;  
var binData = sa.getBytes(attachRec);   
var encData = StringUtil.base64Encode(binData);  
outputs.attachments.push(attachobj);  
outputs.attachments\[i\].attachment.attachmentFileName = fileName;  
outputs.attachments\[i\].attachment.attachmentFileType = fileContent;  
outputs.attachments\[i\].attachment.attachmentContent= encData;  
  
i++;  
}  
gs.print('0 ' + outputs.attachments\[0\].attachment.attachmentFileName);  
gs.print('1 ' + outputs.attachments\[1\].attachment.attachmentFileName);  
  
// outputs.attachments=attachments;  
outputs.priority=inputs.IncRecord.priority;  
outputs.category=inputs.IncRecord.category;  
outputs.subcategory=inputs.IncRecord.subcategory;  
outputs.contact\_type=inputs.IncRecord.contact\_type;  
outputs.state=inputs.IncRecord.state;  
  
}

### Release

Any Version

### Cause

Issue with the JavaScript Code

### Resolution

Need below changes to the script :

  var fileName=attachRec.file\_name;  
   to:  
  var fileName=attachRec.file\_name.toString();

  var fileContent=attachRec.content\_type;  
   to:  
  var fileContent=attachRec.content\_type.toString();  
  
With out this change the type of both variables are "object" not "string" which is resulting the issue with the output content.
