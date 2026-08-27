---
title: "How to find if a given User is part of a AD group ?"
aliases:
  - KB0785335
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785335
kb_number: KB0785335
last_modified: 2024-09-21
---

## Issue

Please review the use case below

1.  Add the user to the AD group when the user is not in the group, succeeds with no result returned.  
    2\. Add user to a group when the user is in the group it will return with a message as 'Object already exists'.  
    3\. Remove the user from the group where the user is already in the group succeeds with no result returned.  
    4\. Remove a user that does not exist in the group it will error with "The server is unwilling to process the request. (Exception from HRESULT: 0x80072035)"

In this scenario, you should validate the user before you add/ Remove.

## Resolution

Now, In order to eliminate the above error - Please do perform a check  
  
  
Using the Query AD activity, you can use the following to look up the user that is a member of a group.  
It seems like the memberOf query needs to be very specific to the implementation of AD which is why it was hard to see a useful result out of the query.  
  
**Query AD \[Orchestration Activity\]  
**

[/nav\_to.do?uri=wf\_element\_activity.do?sys\_id=84a60d307f010200b547b8038dfa9102](https://\<INSTANCE-NAME\>.service-now.com/nav_to.do?uri=wf_element_activity.do?sys_id=84a60d307f010200b547b8038dfa9102)  
  
Inputs :

**DomainController: <IP ADDRERSS>**  
**SearchFilter: (&(samaccountname=<NAME OF THE USER>)(memberOf=CN=<AD\_GROUP\_NAME>,OU=<>,OU=<>,DC=<>,DC=<>,DC=<>))**  
  
If you use this you should get an empty result if the user is NOT in the group. And you will get a full user record when the user is found to be a member of the group.  
You should be able to set up conditions in a workflow to handle these cases and avoid the error you receive from the Add and/or Remove user activities.

**Note:**  Please provide the correct path to the Group. An example is below. OU and DC represent the path to the Group in the AD.

(memberOf=CN=ServiceNow\_Admin\_Userrs,OU=nowGroup,OU=admins,OU=Global,DC=corp,DC=now,DC=org))
