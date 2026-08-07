---
title: "Verifying the outbound mail server received the email"
aliases:
  - KB0528658
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528658
kb_number: KB0528658
last_modified: 2025-01-10
---

## Verifying the outbound mail server received the email

  

### Issue

After the instance sends email to the outbound mail server, it moves the email from the Outbox to the Sent mailbox.

If ServiceNow successfully sends email but users are not receiving it, there may be an issue with the outbound mail server.

### Resolution

1.  Navigate to **System Mailboxes > Outbound > Sent**.
2.  Verify that the email notification is in the Sent mailbox with a state of **Processed**.
3.  Select the sent email.
4.  Personalize the form to add the **Message ID** field.
5.  Copy the message ID and send it to the proper outbound mail server administrator.

-   If ServiceNow maintains the SMTP server, open an incident with Technical Support and include the message ID.  
      
    
-   If your instance uses a custom outbound mail server, send the message ID to your outbound mail server's administrator.

### Related Links

[Troubleshooting inbound email messages reaching SN instance with a delay](https://support.servicenow.com/kb_view.do?sysparm_article=KB0866952 "Troubleshooting inbound email messages reaching SN instance with a delay")

[Delay to send and receive emails due to "Server busy. Please try again later"](https://support.servicenow.com/kb_view.do?sysparm_article=KB1383046 "Delay to send and receive emails due to \"Server busy. Please try again later\"")

[Enabling email delivery using SPF records to allow SN mail servers](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535456 "Enabling email delivery using SPF records to allow SN mail servers")
