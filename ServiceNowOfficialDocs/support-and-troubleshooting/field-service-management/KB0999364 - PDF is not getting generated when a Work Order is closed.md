---
title: "PDF is not getting generated when a Work Order is closed"
aliases:
  - KB0999364
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999364
kb_number: KB0999364
last_modified: 2024-10-11
---

## PDF is not getting generated when a Work Order is closed

  

### Issue

After an upgrade, the PDF that is generated and attached when a Work Order is closed and we click on Sign and Confirm is no longer getting generated and attached

### Cause

There are some customization that may be impacting the process.

If you have customized the script include GeneralWOForm to show your own logo and/or different information on the PDF than the one OOB, the script will no upgrade to the latest OOB and this may cause the process to stop working

### Resolution

Revert the script include GeneralWOForm to the latest OOB version.

If needed, apply your custimization on top of the newest code.  
  
Alternatevely you can create a PDF template to generate the PDF:

-   Create the PDF tempolate on table Document templates:  
    /sn\_doc\_template\_list.do?sysparm\_userpref\_module=96c4eab1b73100101cadbc78ee11a927&sysparm\_clear\_stack=true  
      
    
-   Configure the system to use your template on Field service > administration> Configuration> add-ons

![](sys_attachment.do?sys_id=78b70c09dbb73890fd8d2b69139619c3)
