---
title: "How to update the display name for outgoing emails"
aliases:
  - KB0815999
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815999
kb_number: KB0815999
last_modified: 2025-10-28
---

## How to update the display name for outgoing emails

  

### Issue

To change your display name on outgoing emails, you update the glide.email.username system property, but you may find that the display name does not change. You need to update the display name in two places. This article explains the steps to update the email display name in ServiceNow. 

### Release

All supported releases

### Cause

Even though the glide.email.username system property was updated, the **Email user label** field in **System Mailboxes** > **Email Accounts** still contains the previous display name value.

### Resolution

To update the display name for outgoing emails, you must change the value in two places:

1.  In **System Property** > glide.email.username  
      
    ![Step 1 In system properties update glide.email.username](https://support.servicenow.com/sys_attachment.do?sys_id=f5bcf7ee47bcb694c4e1a325126d4355)  
      
    
2.  In **System Mailboxes** > **Email Accounts** > **Email user label** field  
      
    ![Step 2 Update Email User Level field](https://support.servicenow.com/sys_attachment.do?sys_id=b5bc37ee47bcb694c4e1a325126d439a)  
      
    

### Related Links

For more information about email properties, see [Email properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest).
