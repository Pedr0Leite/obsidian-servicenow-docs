---
title: "Saving System Properties Basic Configuration UI16 changes glide.sys.default.tz to a question mark"
aliases:
  - KB0749107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749107
kb_number: KB0749107
last_modified: 2026-05-11
---

## Saving System Properties Basic Configuration UI16 changes glide.sys.default.tz to a question mark

  

### Issue

After saving the Basic Configuration UI16 system properties form, the glide.sys.default.tz property value changes to a question mark (?), overwriting a previously configured timezone.  
  
Steps to reproduce:  
1\. Navigate to System Properties > Basic Configuration UI16.  
2\. Set glide.sys.default.tz to a timezone not in the available timezones list (for example, Europe/Helsinki).  
3\. Navigate back to System Properties > Basic Configuration UI16.  
4\. Click Save.  
5\. Observe that glide.sys.default.tz is now set to '?'.  
  
![error glide.sys.default.tz = ?](sys_attachment.do?sys_id=a2dbf12947f487107947e551336d4328 "error glide.sys.default.tz = ?")

### Symptoms

\- Admin sets glide.sys.default.tz to a valid timezone such as Europe/Helsinki.  
\- Admin navigates to System Properties > Basic Configuration UI16.  
\- Clicking Save changes the glide.sys.default.tz value to '?'.  
\- The timezone dropdown on the configuration form shows an empty selection before saving.

### Release

Any supported release.

### Cause

The timezone set in glide.sys.default.tz does not exist in the list of available timezones for the instance. When the form loads, the dropdown finds no matching value and shows an empty selection. Clicking Save writes that empty selection as '?' to the property.

### Resolution

  Prerequisites: Admin role required.  
1\. Navigate to System Properties > Basic Configuration UI16.  
2\. Click Configure Available Timezones.  
3\. Add the required timezone (for example, Europe/Helsinki) to the available list.  
4\. Return to System Properties > Basic Configuration UI16.  
5\. Select the newly added timezone from the timezone dropdown.  
6\. Click Save.  
7\. Verify that glide.sys.default.tz now shows the correct timezone value.

![Configure available time zones](sys_attachment.do?sys_id=26dbf12947f487107947e551336d4321 "Configure available time zones")
