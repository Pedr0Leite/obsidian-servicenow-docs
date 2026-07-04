---
title: "ILMT integration is not getting computer information only server version"
aliases:
  - KB0815822
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815822
kb_number: KB0815822
last_modified: 2024-04-08
---

## Issue

ILMT integration is not getting computer information only server version.

Error is found in the logs:

"2020-02-24 08:53:31 (278) worker.4 worker.4 txid=4daf45671b07 WARNING \*\*\* WARNING \*\*\* ILMTImportWorker: No active connections found."

The scheduled import below is running as "System Administrator" which is OOB.  
Due to this missing admin capabilities, necessary backend GlideRecord queries are unable to fetch the connection table details.  
  
Scheduled Job: SAM - IBM Data Import  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=8b1be03453d003002658ddeeff7b12c4  
  
User: System Administrator  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_user.do?sys\_id=6816f79cc0a8016401c5a33be04be441

  
The "No active connections found" message is coming from the below script include.  
  
Script Include : ILMTImportWorker  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=2a5828f053d003002658ddeeff7b12c4

## Resolution

1\. Add the "admin" role to the "System Administrator" user.  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_user.do?sys\_id=6816f79cc0a8016401c5a33be04be441  
  
2\. Once the role is added, try to execute the "SAM - IBM Data Import' job again.
