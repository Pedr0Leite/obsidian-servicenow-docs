---
title: "Validating whether an inbound email action is performed"
aliases:
  - KB0523577
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523577
kb_number: KB0523577
last_modified: 2025-07-31
---

## Validating whether an inbound email action is performed

  

### Issue

**Inbound email actions** enable an administrator to define the actions that ServiceNow takes when receiving email. The email may not display if the **Scheduled Job (sys\_trigger)** picked up the email record and was unable to process the action.

### Release

All

### Resolution

To verify that emails are processed:

1.  1.  Navigate to **System Mailboxes > Received**.
    2.  The **Received** module displays a list of all messages that have been processed.
        
        <table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Received&nbsp;emails may be cleared out every <em>x</em> number of days. For more information, refer to the article on <a title="Table Rotation" href="https://www.servicenow.com/docs/csh?topicname=c_TableRotation.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Table Rotation</a>.</td></tr></tbody></table>
        
          
          
        
         ![Received email frame displaying a processed email within the Created on Today filter](/sys_attachment.do?sys_id=c38ada0e47c36e98c4e1a325126d4326 "Received Email")
        
    3.  If an email is not being processed, click the **Created** link to view the email log files. For more information, refer to the article on [Inbound Email Actions](https://www.servicenow.com/docs/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions").

1.  Scroll to the bottom of the page to view the **Email Log** entries.
    
    ![Sample email log entries that display information on why messages may not have been processed](/sys_attachment.do?sys_id=0b8a9a0e47c36e98c4e1a325126d43ca "Email Log")
    
2.  If no processed record exists, the email action was not executed. The log entries provide detailed information on why an action might have failed.
3.  If assistance is needed, create a case and include the following information:  
    -   Failed email action
    -   Email type, such as _New_ or _Reply_
    -   Relevant scripts
