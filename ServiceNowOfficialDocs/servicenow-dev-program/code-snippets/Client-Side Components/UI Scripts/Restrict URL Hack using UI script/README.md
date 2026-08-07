---
title: "Restrict URL Hack using UI script"
aliases:
  - Restrict URL Hack using UI script
tags:
  - servicenow-dev-program
  - code-snippet
  - restrict-url-hack-using-ui-script
  - ui-scripts
---

1.Go to System UI >UI Scripts >Create a new UI script and Check the Global field.
2.Below is an example 

Lets say the Original URL opened is:

https://devXXXXX.service-now.com/sys_security_acl.do?sys_id=-1&sys_is_list=true&sys_target=sys_security_acl&sysparm_checked_items=&sysparm_fixed_query=&sysparm_group_sort=&sysparm_list_css=&sysparm_query=name%3dincident%5eoperation%3dread

and we need to monitor "sysparm_fixed_query" parameter in the URL.


![image](https://user-images.githubusercontent.com/42912180/195846361-d51f40ba-cdc0-40e1-8057-b19a0906a9a8.png)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Custom Change Schedule/README|Custom Change Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Disable Copy Paste For Portal/README|Disable Copy Paste For Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Display number of created records/README|Display number of created records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Make OOB Attachment Mandatory/README|Make OOB Attachment Mandatory]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Observe MRVS Events/README|Observe MRVS Events]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/PersistentAnnouncementBanner/README|PersistentAnnouncementBanner]]
