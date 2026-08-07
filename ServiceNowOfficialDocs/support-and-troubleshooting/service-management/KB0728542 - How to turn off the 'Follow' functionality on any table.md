---
title: "How to turn off the 'Follow' functionality on any table"
aliases:
  - KB0728542
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728542
kb_number: KB0728542
last_modified: 2024-10-17
---

## How to turn off the 'Follow' functionality on any table

  

### Issue

The purpose of this article is to provide instructions on how to turn the 'Follow' functionality off on any table. A user(s) can click on the 'Follow' UI action to subscribe and get notifications on that particular record. 

When the user has subscribed to the record, the UI Action button's caption changes to 'Following'

![](sys_attachment.do?sys_id=442d153a1b7fbc10b00b86edcc4bcbbf)

### Resolution

To turn this function off, this also involves the UI Action button being hidden.

1) Login to your instance as an Admin

2) From your filter navigator go to the list view of the table that you want to turn the feature off, eg: incident.list or sn\_hr\_core\_case.list.

3) Right click on any of the columns and go to Configure ==> Dictionary.

4) Find the record where type is 'collection' and open the record.

5) Click on 'Advanced View' and go to the 'Attributes' field and change the value of the 'live\_feed' attribute from true to false.

6) Save the record.

![](sys_attachment.do?sys_id=c42d153a1b7fbc10b00b86edcc4bcbbc)

### Related Links

When the attribute is set to false, users will no longer see the 'Follow' UI Action button on the record.
