---
title: "Error Message \"Internal Server Error (500)\" on HR Agent Workspace for HR users."
aliases:
  - KB1005870
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1005870
kb_number: KB1005870
last_modified: 2025-09-03
---

## Error Message "Internal Server Error (500)" on HR Agent Workspace for HR users.

  

### Issue

An error message pop-up displayed **"Internal Server Error (500)"** when opening the HR Agent Workspace.  
The error message seems to only show for HR agents who have an HR Case assigned to themselves.

  
![](sys_attachment.do?sys_id=e039eba5db56c910904fa9fb139619a9)

### Cause

The issue can be caused by either Query Business Rule on sn\_hr\_core\_case (or any of the tables extending from it) and/or a Read ACL on **sn\_hr\_core\_case.sys\_updated\_on** preventing the user from being able to access the requested data.

If the user doesn't have access to the records/fields, the **"Internal Server Error (500)"** error would be displayed.

The logic behind the HR Workspace Landing Page calls the "Get Cards" REST Resource in Scripted REST Service "HR Landing Page Cards" (/api/sn\_hr\_ws/landing\_page\_cards)  
[https://instance\_name.service-now.com/sys\_ws\_definition.do?sys\_id=5e3cfb0de7360010809a268b03f6a9e9](https://instance_name.service-now.com/sys_ws_definition.do?sys_id=5e3cfb0de7360010809a268b03f6a9e9)  
  
Scripted REST Resource "Get Cards"  
[https://instance\_name.service-now.com/sys\_ws\_operation.do?sys\_id=8a7c7f0de7360010809a268b03f6a9f0](https://instance_name.service-now.com/sys_ws_operation.do?sys_id=8a7c7f0de7360010809a268b03f6a9f0)  
  
which calls Script Include "hr\_WorkspaceLandingPageCards"  
[https://instance\_name.service-now.com/sys\_script\_include.do?sys\_id=d82140dde7360010809a268b03f6a9e3](https://instance_name.service-now.com/sys_script_include.do?sys_id=d82140dde7360010809a268b03f6a9e3)

This and queries table "Landing Page Card List Configuration" \[sn\_hr\_ws\_landing\_page\_card\_list\_config\]  
[https://instance\_name.service-now.com/sn\_hr\_ws\_landing\_page\_card\_list\_config\_list.do?sysparm\_query=&sysparm\_list\_mode=grid](https://instance_name.service-now.com/sn_hr_ws_landing_page_card_list_config_list.do?sysparm_query=&sysparm_list_mode=grid)

  
If one (or more) of the cases returned by one of the above Card List Config records cannot be read because of a custom Query Business Rule, the error would be displayed.

Even if there are no Query Business Rules involved, this 500 Error can still popup if the user does not have access to one of the fields listed in the \_getCardFromRecord() method in Script Include "hr\_WorkspaceLandingPageCards"

\_getCardFromRecord: function(record) {  
 return {  
  number: record.number.toString(),  
  opened\_at: new GlideDateTime(record.opened\_at.toString()).getNumericValue(),  
  sys\_updated\_on: new GlideDateTime(record.sys\_updated\_on.toString()).getNumericValue(),  
  short\_description: record.short\_description.getDisplayValue(),  
  priority: record.priority.getDisplayValue(),  
  state: record.state.getDisplayValue(),  
  table: record.getValue('sys\_class\_name'),  
  id: record.sys\_id.toString(),  
  tags: this.\_getTags(record)  
 };  
},

  
This script is using the number, opened\_at, sys\_updated\_on, short\_description, priority, state, sys\_class\_name, sys\_id fields on the HR Case table.

One of the most common causes for this issue is the existence of an obsolete OOB Read ACL on **sn\_hr\_core\_case.sys\_updated\_on**. This ACL does not exist anymore in recent releases.

### Resolution

To fix the issue, make sure that the following OOB Read ACLs are **deactivated or deleted**. These ACLs were created back in 2017 and do not exist anymore on instances created recently:

sn\_hr\_core\_case.assigned\_to  
sn\_hr\_core\_case.hr\_service  
sn\_hr\_core\_case.number  
sn\_hr\_core\_case.opened\_by  
sn\_hr\_core\_case.short\_description  
sn\_hr\_core\_case.state  
sn\_hr\_core\_case.subject\_person  
sn\_hr\_core\_case.sys\_updated\_on

![](sys_attachment.do?sys_id=3039afa5db56c910904fa9fb13961920)

[https://instance\_name.service-now.com/sys\_security\_acl\_list.do?sysparm\_query=nameINsn\_hr\_core\_case.assigned\_to%2Csn\_hr\_core\_case.hr\_service%2Csn\_hr\_core\_case.number%2Csn\_hr\_core\_case.opened\_by%2Csn\_hr\_core\_case.short\_description%2Csn\_hr\_core\_case.state%2Csn\_hr\_core\_case.subject\_person%2Csn\_hr\_core\_case.sys\_updated\_on%5Eoperation%3Dread&sysparm\_list\_mode=grid](https://instance_name.service-now.com/sys_security_acl_list.do?sysparm_query=nameINsn_hr_core_case.assigned_to%2Csn_hr_core_case.hr_service%2Csn_hr_core_case.number%2Csn_hr_core_case.opened_by%2Csn_hr_core_case.short_description%2Csn_hr_core_case.state%2Csn_hr_core_case.subject_person%2Csn_hr_core_case.sys_updated_on%5Eoperation%3Dread&sysparm_list_mode=grid)

Note that custom Read ACLs might also be involved and would need to be reviewed and updated accordingly to make sure all the agent workspace/case writer users will have access to the required fields.
