---
title: "Not all the expected To-dos are listed in the 'Open' or 'Completed' tabs on the 'My To-dos' page on Employee Service Center"
aliases:
  - KB0819625
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819625
kb_number: KB0819625
last_modified: 2026-02-26
---

## Not all the expected To-dos are listed in the 'Open' or 'Completed' tabs on the 'My To-dos' page on Employee Service Center

  

### Issue

You might encounter an issue where not all the expected To-dos are listed in the 'Open' tab on the 'My To-dos' page on Employee Service Center.

You might notice a discrepancy in the number of To-dos displayed in the 'To-dos' pill on the ESC header and that of the to-dos actually listed in the 'Open' tab on the 'My To-dos' page.

![](sys_attachment.do?sys_id=46f17079875bbe542d5cbbb5cebb35de)

### Release

All releases.

### Cause

The Widget "HRM Todos Summary" \[hrm-todos-summary\] is used to display the '**My To-Dos**' list on the "hrm\_todos\_page" ESC page:  
[https://instance\_name.service-now.com/nav\_to.do?uri=sp\_widget.do?sys\_id=bdc676957317130030f331d7caf6a74d](https://instance_name.service-now.com/nav_to.do?uri=sp_widget.do?sys_id=bdc676957317130030f331d7caf6a74d)  
  
This widget calls Script Include "todoPageUtils", which contains the logic behind what data is returned:  
[https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=fb5a924473b7130030f331d7caf6a764](https://instance_name.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=fb5a924473b7130030f331d7caf6a764)

This Script Include limits **the total number of to-dos for the sum of all tabs** to `300` by default.

See `line 7`:

```
todoPageUtils.LIMIT_TOTAL_TODOS = 300; // Limit of the total number of to-dos for the sum of all tabs
```

Because of the way the To-Dos are sorted, if the user has more than 300 total To-dos, some of the 'Open' To-dos might not be part of the first 300 records being returned, hence they might not be displayed.

It's worth noting that the 'To-dos' count badge in the portal header does not have this issue because the SQL query behind it is a simple COUNT aggregate, which is less impactful with respect to performance because it does not include any actual to-do data.

### Resolution

A simple solution would be to edit Script Include **todoPageUtils** and set the above limit (`todoPageUtils.LIMIT_TOTAL_TODOS`) to a higher number. However, it is not recommend setting it too high, to avoid any potential performance issue when loading the page.

NOTE that some Restricted Caller Access \[sys\_restricted\_caller\_access\] records might get invalidated after editing the Script Include "todoPageUtils"; if that's the case, make sure to set their status back to 'Allowed'.

\---

A better solution would be to update the **To-do configurations** \[sn\_hr\_sp\_todos\_config\] that represent "closed" tasks to limit the number of completed to-dos being queried:

[https://instance\_name.service-now.com/sn\_hr\_sp\_todos\_config\_list.do?sysparm\_query=&sysparm\_view=](https://instance_name.service-now.com/sn_hr_sp_todos_config_list.do?sysparm_query=&sysparm_view=)
