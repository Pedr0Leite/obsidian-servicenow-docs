---
title: "Instance was not sending or recieving emails"
aliases:
  - KB0811758
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811758
kb_number: KB0811758
last_modified: 2023-11-21
---

## Instance was not sending or recieving emails

  

### Issue

Emails in the email logs  are in 'send-ready' state.

https://<instancename..service-now.com/sys\_email\_list.do?sysparm\_query=sys\_created\_onONToday%40javascript%3Ags.daysAgoStart(0)%40javascript%3Ags.daysAgoEnd(0)

### Cause

The schedule Job "Email Reader" and "SMTP Sender" are not running.

### Resolution

1.  Check the sys\_trigger\_list.do table for : https://<instancename>.service-now.com/sys\_trigger\_list.do?sysparm\_query=nameLIKEEmail%20Reader%5EORnameLIKESMTP
2.  Check if all the Jobs in the above list have the 'Next Action' set to be previous date
3.  Set the record to 'Error' State. Save the record. Change the date to the current date and time( if the date and time is in the past). Save the record.  
    4\. Set the state to 'Ready'
