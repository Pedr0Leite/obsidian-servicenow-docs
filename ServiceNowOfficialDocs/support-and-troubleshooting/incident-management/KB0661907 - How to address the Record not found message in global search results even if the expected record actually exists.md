---
title: "How to address the \"Record not found\" message in global search results even if the expected record actually exists"
aliases:
  - KB0661907
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661907
kb_number: KB0661907
last_modified: 2026-06-03
---

## How to address the "Record not found" message in global search results even if the expected record actually exists

  

### Issue

It's possible to run into a scenario where an incident record that exists in the instance can't be retrieved by the Global Search, or opened from the resulting list, but the error message **Record Not found** is displayed. There can be many possible reasons for a record not being retrieved, for example, a _before query_ business rule filtering it, or the recent deletion of the record from the instance.

### Cause

While reviewing the affected incident record and the session's localhost logs, you can observe that it had an invalid \[sys\_id\] value: sys\_id="sysparm\_domain=null&sysparm\_doma". This could have possibly been caused by an edge condition due to events timing. The incident record could have been closed first, but the relevant incident task got closed a few seconds later. In this case, the incident is a parent record, and the incident task is its child record. We can trace this behavior from the instance node transaction logs shown below:

2017-12-06 05:25:44 (010) Default-thread-9 2804B36237F28700DB1712C543990E34 #893115 /incident\_task.do Parameters -------------------------  
sys\_row=0  
sys\_original.incident\_task.state=1  
sys\_display.incident\_task.location=  
sysparm\_redirect\_url=  
activity\_filter\_all=on  
sysparm\_template\_editable=  
sys\_original.incident\_task.company=  
sysparm\_record\_target=task  
incident\_task.sys\_updated\_on=06.12.2017 13:31:37  
sys\_original.incident\_task.location=  
sys\_display.incident\_task.short\_description=Fjerne overvåking av   
sys\_display.original.incident\_task.cmdb\_ci=  
text.value.incident\_task.watch\_list=  
sys\_original.incident\_task.sys\_updated\_by=  
sys\_original.incident\_task.cmdb\_ci=  
sysparm\_collection=  
incident\_task.closed\_by\_label=  
sysparm\_ck=6804b...8301e (length=72)  
sys\_display.incident\_task.cmdb\_ci=  
incident\_task.closed\_by=  
sys\_display.original.incident\_task.company=UDI  
sys\_original.incident\_task.u\_subcategory=  
activity\_filter.priority=on  
sys\_uniqueName=sys\_id  
incident\_task.priority=4  
activity\_filter.assigned\_to=on  
sys\_target=incident\_task  
sys\_display.original.incident\_task.parent=  
sysparm\_action\_template=  
sys\_display.incident\_task.company=UDI  
sys\_display.incident\_task.watch\_list=  
sys\_original.incident\_task.work\_notes=  
sysparm\_collection\_relationship=  
sysparm\_referring\_url=  
sys\_original.incident\_task.number=TASK0020199  
sys\_original.incident\_task.closed\_by=  
sys\_displayValue=TASK0020199  
incident\_task.number=TASK0020199  
incident\_task.correlation\_display=  
incident\_task.closed\_at=  
sysparm\_pop\_onLoad=  
sys\_original.incident\_task.priority=4  
sysparm\_transaction\_scope=  
sys\_original.incident\_task.correlation\_display=  
activity\_filter.state=on  
sys\_original.incident\_task.assigned\_to=  
sys\_display.original.incident\_task.u\_business\_sub\_service=Unknown  
incident\_task.company=  
isFormPage=true  
sys\_original.incident\_task.parent=sysparm\_domain=null&sysparm\_doma  
sys\_display.original.incident\_task.u\_external\_integration=  
sys\_original.incident\_task.watch\_list=  
incident\_task.u\_external\_state=  
sys\_original.incident\_task.assignment\_group=  
incident\_task.work\_notes=  
ni.dependent\_reverse.incident\_task.u\_subcategory=u\_category  
sys\_display.incident\_task.business\_service=Unknown  
incident\_task.u\_subcategory=  
incident\_task.comments=  
sys\_display.original.incident\_task.location=  
sys\_original.incident\_task.business\_service=  
incident\_task.u\_category=alarm  
sys\_original.incident\_task.u\_caller=  
incident\_task.u\_business\_sub\_service=  
incident\_task.parent=sysparm\_domain=null&sysparm\_doma  
sys\_original.incident\_task.short\_description=Fjerne overvåking av   
activity\_filter.cmdb\_ci=on  
sysparm\_goto\_url=  
incident\_task.u\_external\_integration=  
sysparm\_record\_scope=  
sys\_display.incident\_task.u\_business\_sub\_service=Unknown  
sys\_display.incident\_task.assignment\_group=Monitoring Solution  
sysparm\_record\_list=assigned\_to=javascript:gs.user\_id()^active=true^stateNOT  

### Resolution

Please contact SN customer support via a HI incident to correct the invalid sys\_id of the affected task record.
