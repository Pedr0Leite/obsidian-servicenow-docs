---
title: "Reject comments not displayed in email notification for Knowledge article or any table record with approval"
aliases:
  - KB0786276
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786276
kb_number: KB0786276
last_modified: 2024-04-30
---

## Reject comments not displayed in email notification for Knowledge article or any table record with approval

  

### Issue

When a request is submitted for approval and once is approved at first and then it goes to 2nd level approval and when the 2nd level approver rejects the target record the email is triggered but the rejection comments are unavailable to be included in the notification. This works fine when the first level approver rejects the article.

### Resolution

\[**Most Probable Cause:**  
  

  
The filter of the notification script does not seem correct as it is returning many records and using the first one which could be a random record:  
  

  
**Solution**

Check your filter according to your business needs. As This is a customisation, we cannot exactly how it show work but it seems to me that you can add possibly the condition to exclude "No Longer required" approvals:  
  
You can test as a background script to make sure it will work. Additionally, remember that if the notification depends on an event, it has to be triggered not before the rejection.  

var pd = new GlideRecord('sysapproval\_approver');  
pd.addQuery('source\_table', 'kb\_knowledge'); //kb\_knowledge could be replaced by any table  
pd.addQuery('document\_id',"SYS\_ID\_OF\_THE\_REJECTED\_RECORD");  
pd.addQuery('state','rejected');  
pd.orderByDesc('sys\_updated\_on');  
pd.query();  
if(pd.next()) {  
var notes = pd.comments.getJournalEntry(-1);  
var na = notes.split("\\n\\n"); //stores each entry into an array of strings  
for (var i = 0; i < na.length; i++) {  
 gs.print(na\[1\]);  
}  
}

  
  

  
Recommendation:  

  
Always check in sub-production instances to validate if that the filter is correct, test different scenarios before moving into production. You can use background scripts as stated before
