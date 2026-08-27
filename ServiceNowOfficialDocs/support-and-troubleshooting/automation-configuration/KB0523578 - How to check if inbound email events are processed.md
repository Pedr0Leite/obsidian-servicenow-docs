---
title: "How to check if inbound email events are processed"
aliases:
  - KB0523578
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523578
kb_number: KB0523578
last_modified: 2026-03-27
---

## How to check if inbound email events are processed

  

### Issue

Verify that inbound email events are being processed by checking the Events log for email.read events and confirming their status.

### Facts

-   The Events log records all system events that occur within the ServiceNow instance.
-   Every time an email arrives in the instance, an email.read event is created.
-   The scheduled job (sys\_trigger) then selects the email and processes it.

### Release

  All supported releases

### Resolution

To verify that the system event is processed:

1.  Go to **System Logs** > **Events**.
2.  In the **Go to** field, select **Name**.
3.  In the text field, enter **email.read** and select **Search**.
    
    ![Events log toolbar with Go to Name selection and email.read text in the search field](/sys_attachment.do?sys_id=3bfe60c39737765c24a7739c1253af65 "System event log toolbar")
    
4.  A list of all emails that have been processed in the instance appears. Use the **Created** field to search for and select the correct email.read event.
5.  If the email was successful, the **State** field displays **Processed** and the **Processing Duration** field is not empty.
    
    ![Event log details for email.read, including the State field displaying processed and the Processing duration field displaying 327](/sys_attachment.do?sys_id=63fe60c39737765c24a7739c1253af12 "email.read details")
    
6.  If the **State** field is not set to **Processed**, confirm that the scheduled event process job is running.
