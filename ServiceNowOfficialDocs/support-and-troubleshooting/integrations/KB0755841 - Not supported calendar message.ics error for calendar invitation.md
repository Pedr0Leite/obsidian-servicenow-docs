---
title: "\"Not supported calendar message.ics\" error for calendar invitation"
aliases:
  - KB0755841
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755841
kb_number: KB0755841
last_modified: 2024-11-22
---

## "Not supported calendar message.ics" error for calendar invitation

  

### Issue

The calendar attachment in the email is seen as "not supported calendar message.ics" when received by the recipient for the Cancel Calendar invitation. 

![error](sys_attachment.do?sys_id=0bfbeceadb42b450e515c22305961941 "error")

### Release

-   Instance on Madrid.
-   The Email template used for the notification is created has method other than REQUEST on the VCALENDAR version2, ex.the METHOD: CANCEL.

### Cause

-   -   Meeting invites email content type is always set to METHOD=request, even when METHOD is different inside the calendar data.
    
    **Validation**:
    
    -   In the email logs, the notification which is sent shows content type as method=Request:
    -   The message headers show content type as method=Request:
    
    ![](sys_attachment.do?sys_id=cbfbeceadb42b450e515c22305961946)
    
    -   The message body shows the content type as method=Request:
    
    ![](sys_attachment.do?sys_id=4ffbeceadb42b450e515c2230596194b) 
    

### Resolution

**Resolution:** This is identified as a problem and is being worked on PRB1355204.

**Workaround:**

-   Create a Before business rule on the sys\_email table.

**Conditions**: 

\[Content type\] STARTS WITH 'text/calendar; method='

\[Body Text\] STARTS WITH 'BEGIN:VCALENDAR'

\[Body text\] CONTAINS 'METHOD:CANCEL'

**Actions**:

\[Content type\] TO 'text/calendar; method=CANCEL'

### Related Links

The above states one of the causes behind this issue, There can be multiple reasons behind the cause, Please refer the below article for more info on other reasons:

[https://support.servicenow.com/kb\_view.do?sys\_kb\_id=314c8ad8db87f7844819fb24399619e2](https://support.servicenow.com/kb_view.do?sys_kb_id=314c8ad8db87f7844819fb24399619e2)
