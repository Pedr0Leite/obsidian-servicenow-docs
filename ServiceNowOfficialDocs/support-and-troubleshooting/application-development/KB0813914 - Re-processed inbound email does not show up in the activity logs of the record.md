---
title: "Re-processed inbound email does not show up in the activity logs of the record"
aliases:
  - KB0813914
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813914
kb_number: KB0813914
last_modified: 2024-04-08
---

## Re-processed inbound email does not show up in the activity logs of the record

  

### Issue

Re-processed inbound email does not show up in the activity logs of the record

![](sys_attachment.do?sys_id=6ba36cc5dbc8f0d016d2a345ca96198a)

### Release

This is applicable to all versions of the product

### Cause

If the emails to be reprocessed are more than a day old, you will experience this behavior. Its a hard coded threshold in our base code, on the query that limits the emails that it looks for to a day old at the latest. Emails older than that won't get pulled in for performance reasons.

### Resolution

To re-process emails older than a day, please change the value on the 'Created On' field using this script-

var gr = new GlideRecord('sys\_email');  
gr.addQuery('<query of the emails to be reprocessed>');  
  
gr.query();  
  
if(gr.next())  
{  
gs.print(gr.subject);  
gr.setDisplayValue('sys\_created\_on', gs.nowDateTime());  
gr.update();  
}

Once the date has been updated, you can then reprocess the emails and this will ensure an entry on the activity formatter.
