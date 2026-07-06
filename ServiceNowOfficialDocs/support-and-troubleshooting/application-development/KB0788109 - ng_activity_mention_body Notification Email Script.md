---
title: "ng_activity_mention_body Notification Email Script"
aliases:
  - KB0788109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788109
kb_number: KB0788109
last_modified: 2025-01-03
---

## ng\_activity\_mention\_body Notification Email Script

  

### Summary

The **ng\_activity\_mention\_body** notification email script is used to send emails to users who have been mentioned in journal fields. This can be used in most use cases however, is not meant to be used for knowledge approvals. Looking at the email script, we can see the following code.

var recordGR = new GlideRecord(current.table);  
if(recordGR.get(current.document)) {  
email.setSubject("You have been mentioned in " + recordGR.getDisplayValue());  
template.print("<p style='color: #424E5B;margin: 0 0 12px;line-height: 26px;margin-bottom: 12px'>You have been mentioned by " + current.user\_from.name + " in <a href='/" + recordGR.getRecordClassName() + ".do?sys\_id=" + recordGR.getUniqueValue() + "'>" + recordGR.getDisplayValue() + "</a></p>");  
}

On line 3, there is a reference to **recordGR.getDisplayValue()** which will set the email subject as the record's display value. This is an issue with knowledge approvals as these records do not have a display value. If we take a closer look at the sysapproval\_approver table and look at the **sysapproval** field, we will notice that this field is a reference field to the task table. The **getDisplayValue()** function in this case would take the display value of the **sysapproval** field however, if a non-task record is up for approval, this field will be empty which will result in no display value being shown.

On line 4, we see that the script is trying to print a link to the record the user has been mentioned in. If the record is a knowledge approval, we see that the link will get created correctly however, there is no actual text for the link since **recordGR.getDisplayValue()** will return NULL so it will end up being blank. We can tell that the link is getting created correctly by navigating to the email record on the platform and parsing the email body. Once there we can see something similar to the below line of code where the link should be

**You have been mentioned by "SOME\_USER" in <a href='/sysapproval\_approver.do?sys\_id=RECORDS\_SYS\_ID\_HERE'/></a>**

### Related Links

A simple customization can be done in order to get knowledge approvals to display properly. We know that we are not able to get the display value of knowledge approvals however, we are able to get the display value of a knowledge article. Although, a sample customization will not be provided here, a simple use case would be to use the **recordGR** variable in the notification email script to get a GlideRecord object of the specific knowledge article. From there, you would simply output the knowledge article's display value instead of the display value of the approval without changing the predefined link since we have determined that the link displays correctly.
