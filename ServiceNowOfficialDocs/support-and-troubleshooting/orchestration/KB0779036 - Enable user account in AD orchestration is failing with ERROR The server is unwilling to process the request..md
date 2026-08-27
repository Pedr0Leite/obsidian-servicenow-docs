---
title: "Enable user account in AD orchestration is failing with *** ERROR *** The server is unwilling to process the request. "
aliases:
  - KB0779036
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779036
kb_number: KB0779036
last_modified: 2024-04-08
---

## Enable user account in AD orchestration is failing with \*\*\* ERROR \*\*\* The server is unwilling to process the request.

  

### Issue

Workflow failed on Enabling AD User Account, We can see the error \*\*\* ERROR \*\*\* The server is unwilling to process the request.

### Cause

This error happens when enabling a user account and usually is raised if the password for the user does not meet domain requirements, as discussed in the link below.

[https://social.technet.microsoft.com/Forums/office/en-US/6fac68a4-6665-4809-a595-68dbbe2dc18f/powershell-enabling-an-account-the-server-is-unwilling-to-process-the-request?forum=ITCG](https://social.technet.microsoft.com/Forums/office/en-US/6fac68a4-6665-4809-a595-68dbbe2dc18f/powershell-enabling-an-account-the-server-is-unwilling-to-process-the-request?forum=ITCG)

### Resolution

1\. We can do a quick test with a different user via the OOB "Enable AD User Account" Activity.

Navigate to -> Orchestration -> Activity Designer Activities -> Enable AD User Account -> Test Input

2\. If the error is triggering only on a specific user, then most likely the issue due to a password requirement is not met. Perhaps password setting activity on prior step has failed.

3\. Manually set the password that met the Domain requirement for the user. Re-run the activity on step 1. IF this pass, it will confirm that prior step setting the Password may have failed.

4\. Troubleshoot further on the Prior Step for setting the password. Check to see if there is a Credential tag for the Activity and that Credential valid and available to the MID Server.

5\. Adding "Tags" and "MID Server" column on the Credential table would help see the issue.
