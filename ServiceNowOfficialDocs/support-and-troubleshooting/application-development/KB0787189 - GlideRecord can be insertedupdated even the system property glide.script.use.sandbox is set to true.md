---
title: "GlideRecord can be inserted/updated even the system property \"glide.script.use.sandbox\" is set to true"
aliases:
  - KB0787189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787189
kb_number: KB0787189
last_modified: 2024-04-08
---

## GlideRecord can be inserted/updated even the system property "glide.script.use.sandbox" is set to true

  

Recrods can be created on the Client Script via "GlideRecord.insert()" even the High Security Settings" Plugin is activated and the system property "glide.script.use.sandbox" is set to true.

Steps to Reproduce:  
1\. Log in as admin.  
2\. Create the following onChange Client Script on the incident table Category field.  
Name: Test Glide  
UI Type: Desktop/All  
Type: onChange  
Field name: Category  
Scirpt:  
function onChange(control, oldValue, newValue, isLoading, isTemplate) {  
if (isLoading || newValue === '') {  
return;  
}

//Type appropriate comment here, and begin script below  
if(newValue == "software"){  
var gr = new GlideRecord("incident");  
gr.short\_description = "test gliderecord.insert client side";  
gr.insert();  
}  
}  
3\. Navigate to "incident.do".  
4\. Select Software for field Category.  
5\. A new incident has been created.

According to the following documentation, "GlideRecord" Data Manipulation methods are not allowed in the Client Script if "glide.script.use.sandbox" is set to true.  
[https://docs.servicenow.com/bundle/london-platform-administration/page/administer/security/reference/r\_ScriptSandboxing.html](https://docs.servicenow.com/bundle/london-platform-administration/page/administer/security/reference/r_ScriptSandboxing.html)

Per TASK CSTASK017723, it should be "GlideRecord" Data Manipulation methods are not allowed in the Client Generated Script.

Document requested DOC76503 has been raised.
