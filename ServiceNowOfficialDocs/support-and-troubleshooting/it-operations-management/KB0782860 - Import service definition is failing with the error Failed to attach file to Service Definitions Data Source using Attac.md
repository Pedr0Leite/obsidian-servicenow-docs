---
title: "Import service definition is failing with the error \"Failed to attach file to Service Definitions Data Source\" using Attachement API."
aliases:
  - KB0782860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782860
kb_number: KB0782860
last_modified: 2024-04-08
---

## Import service definition is failing with the error "Failed to attach file to Service Definitions Data Source" using Attachement API.

  

### Issue

While trying to import service definition as per our documentation at [https://docs.servicenow.com/csh?topicname=transfer-service-definitions.html&version=latest](https://docs.servicenow.com/csh?topicname=transfer-service-definitions.html&version=latest) it fails with the error "Failed to attach file to Service Definitions Data Source" using Attachement API.

### Cause

There is a System Property that limits the types of files that can be used as an attachment.

System Properties -> Security and under Attachment limits and Behavior section we have a List of file extensions that can be attached to documents via the attachment dialog property.   
https://<instance-name>.service-now.com/system\_properties\_ui.do?sysparm\_title=Security&sysparm\_category=Escaping%20and%20scripting,Attachments,Security%20Manager,Cookies,Client-side%20scripting,Miscellaneous   
  
  

### Resolution

Check if .json files are allowed to be attached on the instance.  
If there are entries and .json file extension is missing please add the .json file extension in here to allow attaching the exported service definitions.
