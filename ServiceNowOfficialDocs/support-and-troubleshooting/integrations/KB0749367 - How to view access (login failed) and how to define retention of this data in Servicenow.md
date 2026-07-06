---
title: "How to view access (login failed) and how to define retention of this data in Servicenow"
aliases:
  - KB0749367
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749367
kb_number: KB0749367
last_modified: 2024-04-20
---

## How to view access (login failed) and how to define retention of this data in Servicenow

  

### Issue

A significant number of Servienow administrators are unsure how login data is managed in Servicenow.

They also want to know more about security options for auditing and how long this data is kept in Servicenow instances ?

### Release

All

### Cause

This query related to the access and usage logs retention arises because of company security requirements in a number of companies due to current legal framework

### Resolution

1 - Out of the box login events

There are login events out of the box, those login events are stored in the events table, see screen prints for an example.  
  
The event table has a rotation of 7 days, this means that the longest those events are kept will be 7 days our of the box  
  
Rotation of log tables (Madrid)  
[https://docs.servicenow.com/csh?topicname=security-log-history.html&version=latest](https://docs.servicenow.com/csh?topicname=security-log-history.html&version=latest)  
  

![](sys_attachment.do?sys_id=691b682adb42b450e515c223059619a2)

2 - Optional Event Management plugin

You can change the out of the box functionality or complement it by archiving some events  
  
You need to optionally enable the Event Management plugin  
  
Event Management configuration preferences  
[https://docs.servicenow.com/csh?topicname=r\_EMBestPractice.html&version=latest](https://docs.servicenow.com/csh?topicname=r_EMBestPractice.html&version=latest)  
  

<table class="noteTable" align="left"><tbody><tr><td class="c3">Archive events&nbsp;<br>Avoid changing the default retention time for events.<br>To log events for a longer time, create an archive table and a job that copies new events to it. Do this by scheduling a job to regularly back up events [em_event] to a custom table.<br>Do not extend table rotation by adding more days.</td><td class="c4">&nbsp;</td></tr></tbody></table>

<table class="noteTable" style="height: 13px; width: 573px;" width="601" align="left"><tbody><tr style="height: 13px;"><td class="c3" style="width: 278px; height: 13px;">&nbsp;</td><td class="c4" style="width: 279px; height: 13px;">&nbsp;</td></tr></tbody></table>
