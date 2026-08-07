---
title: "GlideAjax is working inconstantly"
aliases:
  - KB0687687
tags:
  - servicenow
  - support-kb
  - glideajax
  - client-scripts
  - script-includes
  - async
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687687
kb_number: KB0687687
last_modified: 2024-01-28
---

## GlideAjax is working inconstantly

  

### Issue

# Symptoms

* * *

When you have a client script making an asynchronous GlideAjax using "getXML" and if you use "getAnswer()" function the client script can be prone to inconsistent behavior 

# Release

* * *

ALL

# Cause

* * *

getAnswer() API is supposed to be used only for Synchronous GlideAJAX 

# Resolution

* * *

When you are using _getXML("function call")_ use 

_var answer = response.responseXML.documentElement.getAttribute("answer");_ instead of 

_var answer = <synchronous object>.getAnswer();_

Inside the function definition 

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=c\_GlideAjaxAPI.html&version=latest](https://docs.servicenow.com/csh?topicname=c_GlideAjaxAPI.html&version=latest)

## Related

- [[KB0749222 - Scripted fields not filling in for non-admin Users for the scoped applications]]
- [[KB0790917 - Glide Ajax returns 'null' value when trying to get value from Script include in Portal]] — another GlideAjax response-handling pitfall
- [[KB0752241 - Client scripts or UI Policies throws error ReferenceError HelloWorld is not defined when tring to call a Script Include]] — related script include call syntax issue
- [[KB0686723 - The Field MessageNotification will be cleared if we use Client Script to set value for the field on a form]] — related client script sequencing pitfall
- [[c_GlideAjaxAPI]] — official GlideAjax API reference

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749222 - Scripted fields not filling in for non-admin Users for the scoped applications|Scripted fields not filling in for non-admin Users for the scoped applications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749991 - [Service Portal] Injection argument not found (newValue) error|[Service Portal]: Injection argument not found (newValue) error]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
