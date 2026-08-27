---
title: "Domain picker on Software Asset Workspace shows \"Error: Could not load domain configurations.\"
aliases:
  - KB1307823
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1307823
kb_number: KB1307823
last_modified: 2026-04-17
---

## Domain picker on Software Asset Workspace shows "Error: Could not load domain configurations."

  

### Issue

Domain picker on Software Asset Workspace shows "**Error: Could not load domain configurations**.", where "domain configurations" is the label of the "domain" table.

The user will be able to list at least their own domain in a normal list view, showing record level APIs are not the issue:  
https://<instance>.service-now.com/domain\_list.do

![](/sys_attachment.do?sys_id=dcc6acfd931043945736b25d6cba10a9)

The Browser debug's Javascript console will also show a 403 status error for this rest request, which is to the REST Table API, for the domain table.

The instance appnode localhost log will show the error "RESTAPIProcessor : User Not Authorized" and "response\_status:403":

1534434 /api/now/table/domain  
Page: api/now/table/domain  
Query Count: 2  
Complete: false  
Debug: false  
12:10:59.160 TIME = 0:00:00.000 PATH = processor/RESTAPIProcessor/execute CONTEXT = RESTAPIProcessor App: Global RC = true RULE =  
12:10:59.160 #1534434 \[REST API\] RESTAPIProcessor : User Not Authorized  
12:10:59.161 \*\*\* End #1534434 /api/now/table/domain, user: <sam admin user>, impersonated by: <admin user>, total time: 0:00:00.000, processing time: 0:00:00.000, CPU time: 0:00:00.000, SQL time: 0:00:00.001 (count: 2), ACL time: 0:00:00.001, source: 10.59.21.134, type: rest , method:null, api\_name:null, resource:null, version:null, user\_id:xxxx, response\_status:403 

### Release

Domain Separation environments

### Cause

The instance has probably been hardened by activating the REST Endpoint ACL for the Table API. This is an out-of-box ACL, but is inactive by default.

https://<instance>.service-now.com/sys\_security\_acl.do?sys\_id=9ef8bc918733320025fbd1a936cb0bdd  
Name:  
Role required: snc\_platform\_rest\_api\_access

If this is active, and the user does not have the snc\_platform\_rest\_api\_access role, the Software Asset Workspace can't get the list of domains due to that ACL blocking it.

### Resolution

You could add the required snc\_platform\_rest\_api\_access role to the sam\_admin role, or sam\_user role, so that any users with those roles also inherit the snc\_platform\_rest\_api\_access role.

[Docs: Software Asset Management roles](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/sam-installed-components.html)

[Docs: Add a role to an existing role](https://www.servicenow.com/docs/r/platform-administration/user-administration/t_AddARoleToAnExistingRole.html)

Note: Giving these users that role will allow them access to any table via the Table API, not just the Domain table. Record/field level ACLs would also still apply for the data in those tables, in the same wasy as when a user opens lists/forms when logged into the instance.

If the pair of API Access Policies for Table API have been activated, those could also affect this.
