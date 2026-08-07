---
title: "No Restriction on Email Recipient List(to,cc,bcc) in $mailto script"
aliases:
  - KB0816015
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816015
kb_number: KB0816015
last_modified: 2024-04-08
---

## No Restriction on Email Recipient List(to,cc,bcc) in $mailto script

  

### Issue

This KB explains the scenario when the email links contain a larger number of recipients populated using $mailto in the email script:

-   Customers use $mailto in the email template script in order to populate the email links which are normally used for email approvals.
-   In this case, when the customer clicked on the email link in the received email, $mailto will be read by email client applications like outlook and prepares to send the email as per the recipient list mentioned in the script.
-   In some cases, if the recipient list is too large then the email client application not able to open the email and throw some error.
-   From ServiceNow end when the customer uses a $mailto script we pull all the recipient's list from the database and add them in the email (.msg file) with a href link which will be opened by email client applications. In this scenario, there is no any such limitation at ServiceNow end on the number of recipients.
-   Observed that there are some restrictions at email client applications due to which some email client applications are unable to open the email if the recipient list is too large.

  

-   Please find the example below where I opened the $mailto script which contains a large recipient list.  
    -   Step 1: Click on the link in the received email.

  

![Received email contains $mailto](sys_attachment.do?sys_id=cf2f6cc5db88b4d0471f9c41ba9619de "Received email contains $mailto")

  

-   -   Step 2: Link is getting opened via Gmail email client. Can see the 413 error.

  

![Your client issued a request that was too large](sys_attachment.do?sys_id=cb2f6cc5db88b4d0471f9c41ba9619e1 "Your client issued a request that was too large")

### Release

All Releases

### Cause

-   Customers can see this issue when the recipient list is too large in the email links which are generated using $mailto.
