---
title: "On Premise - SMTP server is unable to send outbound emails"
aliases:
  - KB0788861
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788861
kb_number: KB0788861
last_modified: 2025-06-12
---

## On Premise - SMTP server is unable to send outbound emails

  

### Issue

The SMTP sender is unable to send emails. Email records get inserted but their state changes from send-ready to ignored.

Troubleshooting steps to verify the issue:

1.  Trigger an default notification so that it creates an email that goes from the state of send-ready to ignored.  
         Email diagnostics show that the custom mail server is working as expected.
2.  Test the connection against the SMTP mail server. which shows successful.
3.  Run  ping and traceroute commands against the mail server to see if there is any packet loss.
4.  Review the logs at the time of the ignored email. It states that the SMTP sender job was completed.
5.  On the SMTP server page, set the port number to 25. Test shows that the connection was successful, however the email is ignored.
6.  Confirm if sending the email works when running a command on the mail server.

### Release

All releases

### Cause

This issue is likely because the following email plugins are not installed:

\-com.glide.email\_client  
\-com.glide.email\_address\_filter  
\-com.glide.email\_attachment

### Resolution

Verify that you have these plugins installed, and if not, install them. If you need to install them, the initial installation should be on a non-production instance.

\-com.glide.email\_client  
\-com.glide.email\_address\_filter  
\-com.glide.email\_attachment
