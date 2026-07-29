---
title: "Invalid Start Date Message Received when Creating a Change Request in ServiceNow Instance"
aliases:
  - KB0786382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786382
kb_number: KB0786382
last_modified: 2024-04-07
---

## Invalid Start Date Message Received when Creating a Change Request in ServiceNow Instance

  

### Issue

When trying to submit a change request in our ServiceNow instance, an invalid start date error is showing up.

### Resolution

  
\[code\]**Solution:** \[/code\]  
  
The root cause of the issue is with the Client Script which has a invalid way of checking the format of the script.

For Example 

  
In this client script's code:  
  
At line 18:  
\[code\]

  
if (user.next()) {  
		var start\_date = g\_form.getValue('start\_date');  
		var date\_format = user.date\_format;  
		if (date\_format == '')  
			date\_format = 'yyyy-MM-dd';  
		var time\_format = user.time\_format.substr(0, 4);  
		if (time\_format == '')  
\==>			time\_format = 'HH:mm:ss';  
		var time\_date\_format = date\_format + ' ' + time\_format;  
		var start\_date\_value = getDateFromFormat(start\_date,time\_date\_format);

  
\[/code\]  
  
The script is written to check the time as 'HH:mm', but the time is set as 'HH:mm:ss'. Due to this reason the error is showing up.  
  
The validation of the date or time should be in the exact format as the way the system displays.
