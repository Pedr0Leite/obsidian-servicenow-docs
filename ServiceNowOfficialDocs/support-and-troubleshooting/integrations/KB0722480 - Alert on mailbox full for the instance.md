---
title: "Alert on mailbox full for the instance"
aliases:
  - KB0722480
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722480
kb_number: KB0722480
last_modified: 2026-05-04
---

## Alert on mailbox full for the instance

  

### Issue

The alert will be created when the email property "Email receiving enabled" is unchecked on the instance but there are still emails being sent to the instance email address, filling up your email mailbox (outside the instance).

This problem usually appears when "Email Sending enabled" is checked and it is causing bounced emails back filling up the email mailbox for the instance.

The alert is needed because it needs to be investigated.

### Resolution

Please ensure you perform the following:

1.  Provide permission to delete the email mailbox messages.
2.  To disable outbound emails on the instance, to avoid this problem re-appearing.

Please note the messages deleted from the email mailbox will no longer be available to recover. However, the email mailbox is no longer accepting new emails as it is full. We recommend providing permission to remove all the messages on the email mailbox if they are not used.

Once you provide permission to delete the email mailbox messages, Customer Support will request the removal of the messages from the mailbox.

### Frequent Q&A

Here are a few common questions on this alert.

1.  **Why is the mailbox being filled up?**  
      
    Answer. Usually, the main source for these cases are emails bouncing back from the outbound emails sent by the instance. Please disable email sending on the instance.  
      
    
2.  **Why do we need to disable outbound email?**  
      
    Answer. To avoid emails bouncing back and filling up the mailbox once again.  
      
    
3.  **How to disable outbound emails?**  
      
    Answer. On the email properties form, uncheck "**Email Sending enabled**"  
      
    
4.  **What to do if we need to re-enable the inbound and outbound emails?**  
      
    Answer.  On the email properties form, check "**Email sending enabled**" and "**Email receiving enabled**". The system will be able to receive and send once again. Some delay should be expected if there are messages held on the instance email mailbox.

### Release

All releases

### Resolution

Please ensure you perform the following:

1.  Provide permission to delete the email mailbox messages.
2.  To disable outbound emails on the instance, to avoid this problem re-appearing.

Please note the messages deleted from the email mailbox will no longer be available to recover. However, the email mailbox is no longer accepting new emails as it is full. We recommend providing permission to remove all the messages on the email mailbox if they are not used.

Once you provide permission to delete the email mailbox messages, Customer Support will request the removal of the messages from the mailbox.

### FAQ:

Here are a few common questions on this alert.

1.  **Why is the mailbox being filled up?**  
      
    Answer. Usually, the main source for these cases are emails bouncing back from the outbound emails sent by the instance. Please disable email sending on the instance.  
      
    
2.  **Why do we need to disable outbound email?**  
      
    Answer. To avoid emails bouncing back and filling up the mailbox once again.  
      
    
3.  **How to disable outbound emails?**  
      
    Answer. On the email properties form, uncheck "**Email Sending enabled**"  
      
    
4.  **What to do if we need to re-enable the inbound and outbound emails?**  
      
    Answer.  On the email properties form, check "**Email sending enabled**" and "**Email receiving enabled**". The system will be able to receive and send once again. Some delay should be expected if there are messages held on the instance email mailbox.
