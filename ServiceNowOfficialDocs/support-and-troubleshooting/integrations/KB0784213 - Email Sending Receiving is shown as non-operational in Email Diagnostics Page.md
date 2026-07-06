---
title: "Email Sending / Receiving is shown as non-operational in Email Diagnostics Page"
aliases:
  - KB0784213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784213
kb_number: KB0784213
last_modified: 2025-09-10
---

## Email Sending / Receiving is shown as non-operational in Email Diagnostics Page

  

### Issue

Email Sending / Receiving is non-operational in ServiceNow Instance Email Diagnostic Page

![](sys_attachment.do?sys_id=b61ae417837f221ccdbbc430feaad33e)

### Release

Any

### Cause

When accessing the "Email Diagnostics" page, the instance will run the function "isReceivingOperational()" within the script "EmailDiagnosticsV2" to determine if everything is working as expected. In order to determine whether the "Email Receiving" is operational, it needs to meet the following conditions:

-   Email Receiving is enabled (System Properties > Email Properties > Email sending enabled)
-   Email Reader processing time is <= 10000ms (this can be modified by system property "glide.email\_diag.threshold.email\_reader.runtime")
-   Email Reader's last run must be within the last 10 minutes (can be modified by system property "glide.email\_diag.threshold.email\_reader.last\_run")

### Resolution

As you can see the "Processing Time" exceeds the OOB setting of 10000ms hence the Diagnostic page advertise Email Sending / Receiving is non-operational but in actual there is no issue with the SMTP and POP3 account. The Processing Time may also be marked red when there are too many email items to send or to download from the mail server.

Nevertheless check the following:

-   Do a test connection for the SMTP and POP3 account
-   If the email is taking time to process and you do not want to see this alert you can increase the value of the system property "glide.email\_diag.threshold.email\_reader.runtime" accordingly.
-   Check the logs and find out the email which is taking time and analyse further.
-   Check the amount of Pop/Imap accounts in the instance, it might be advisable to  create Email Account Groups and multiple email readers according to this Documentation: 
    
    [Multiple email readers](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/notification/concept/email-account-groups.html) This way each Email Reader job has less accounts to retrieve email from thus a bigger chance remaining under the 10 seconds.
    

### Related Links

[Email Diagnostic Page](https://docs.servicenow.com/csh?topicname=r_MailDiagnostics.html&version=latest "Email Diagnostic Page")

[Verify that the Email Reader is running](https://support.servicenow.com/kb_view.do?sysparm_article=KB0523573#POPrunning "Verify that the Email Reader is running")
