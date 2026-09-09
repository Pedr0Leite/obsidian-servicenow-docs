---
title: "How to change the default ServiceNow sender email"
aliases:
  - KB0818299
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818299
kb_number: KB0818299
last_modified: 2025-11-25
---

## How to change the default ServiceNow sender email

  

### Issue

All emails sent from an instance use the default ServiceNow sender email address.  
This use case is applicable when you do not want recipients to see the default ServiceNow email address.

### Release

All

### Cause

Out of the box, ServiceNow instances are provisioned with default SMTP and POP3 email accounts.

### Resolution

There are 2 options:

1.  Edit the SMTP sender name   
    Edit the **From** field in the **ServiceNow SMTP** Email Account.  
    For example; [helpdesk@mydomain.com](mailto:helpdesk@mydomain.com)  
    Bear in mind that this will only change the label shown for the recipient in the email client. The ServiceNow SMTP email address will still be shown.  
      
      
    ![Provisioned with both SMTP and POP3](sys_attachment.do?sys_id=2165557f87ddfa5057288519dabb351f "Provisioned with both SMTP and POP3")  
      
    ![Edit SMTP sender name](/sys_attachment.do?sys_id=d965557f87ddfa5057288519dabb3518 "Edit SMTP sender name")  
      
      
    
2.  Add a new SMTP Account.  
      
    The 2nd option consists in using your own SMTP server because all emails sent from your server will only show your own domain, and will no longer show the default ServiceNow domain  
    Please refer to the documentation link below:  
      
      
    [Enable using your own SMTP server.](https://docs.servicenow.com/csh?topicname=t_ConfAltEmailUsgOwnSMTP.html&version=latest "Enable using your own SMTP server.")  
      
    

### Related Links

[Enable using your own SMTP server.](https://docs.servicenow.com/csh?topicname=t_ConfAltEmailUsgOwnSMTP.html&version=latest "Enable using your own SMTP server.")
