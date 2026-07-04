---
title: "Scoping / HR Roles FAQ"
aliases:
  - KB0691402
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691402
kb_number: KB0691402
last_modified: 2026-04-30
---

## Scoping / HR Roles FAQ

  

### Issue

## Introduction

The purpose of this document is to define best practices and frequent questions about scoping in the context of the HR plugins and scoped roles that are contained with them. We have received quite a few questions about the scoped roles, configuration, and scoping best practices. This document also includes links to other documents where appropriate. 

To start, if you're fairly new to scoping this is a great community article that describes the concept at a high level. Please read this first as it will provide a good background for the context of the rest of this document:

[Understanding Application Scope on the Now Platform](https://community.servicenow.com/community?id=community_article&sys_id=d2dce665dbd0dbc01dcaf3231f9619fe "Understanding Application Scope on the Now Platform")

The latest Plugins for the Human Resources Service Management application are all implemented as separate scoped applications. Each scoped application has a "scoped admin" role that allows admin privileges for components to anyone that has the role. This is a list of plugins and roles: 

## HR Plugins and Scoped Roles Overview

<table style="height: 255px; border-color: #000000;" border="1" width="569"><tbody><tr><td><strong>Plugin Name</strong></td><td><strong>Admin Role</strong></td></tr><tr><td><p>&nbsp;Human Resources Scoped App: Core</p></td><td><p><span style="color: #000000;">&nbsp;sn_hr_core.admin</span></p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Service Portal</p></td><td><p>&nbsp;sn_hr_sp.admin</p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Integrations</p></td><td><p>&nbsp;sn_hr_integration.admin</p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Data Migration</p></td><td><p>&nbsp;sn_hr_migration.admin</p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Lifecycle Events</p></td><td><p>&nbsp;sn_hr_le.admin</p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Employee Document Files</p></td><td><p>&nbsp;sn_hr_ef.admin</p></td></tr><tr><td><p>&nbsp;Human Resources Scoped App:&nbsp;Virtual Agent Conversations</p></td><td><p>&nbsp;sn_hr_va.admin</p></td></tr></tbody></table>

  
Each scoped application/plugin above has its own set of scoped roles that can only be granted by the "scoped admin" or "designated developer."  This is regardless of whether it's granted by assigning the scoped role directly to a user or adding a user to a group that contains the scoped role.   When one of the HR plugins is first installed, this scoped admin role is added as a child to the standard "admin" role. This allows any user with an admin role to grant these scoped roles to users that will be administering the HRSM application. Once a user has been given the admin role as well as a designated developer(below), they can fully administer the scoped application

Please note, for users that aren't concerned with IT having access to the HR data, the standard system admin will be able to completely administer the application by default after the plugins are installed. For added security for the HR scope, most customers will likely want to remove the scoped role from the "admin" role after setting up designated developers. This will allow HR scoped administrators to have full control of the application. 

## Delegated Developer

Once a user has one of the scoped admin roles above, they need to be given the role of Delegated Developer before they can change any of the components in the scope(tables, business rules, the script includes, etc.) Doing this is fairly straightforward and this documentation details it: 

-   [Add Delegated Developer to HR Administrator](https://docs.servicenow.com/csh?topicname=t_HRAdminRoles.html&version=latest "Add Delegated Developer to HR Administrator")

Currently, only the system admin can grant delegated developer roles so this needs to be done before the scoped roles are removed from the admin role. The instructions above apply to adding a delegated developer to any of the scoped admin roles.

## Restricted Caller Access

Another common question comes from users seeing error messages when using the HR Application. These error messages will look like the following one: 

-   "Read operation on table "tablex" from scope "Human Resources: Service Portal" was denied. The application must declare a cross scope access privilege"

These can occur if certain scoped resources (tables, the script includes, etc) are set to deny access to other scopes. To address this a scoped administrator would need to update the Restricted Caller Access record(sys\_restricted\_caller\_access) to allow other scopes to access it. More specific information on how to do this can be found in our official documentation, please see:

-   [Application restricted caller access settings](https://docs.servicenow.com/ "Application restricted caller access settings")
-   [Define cross-scope access to an application resource](https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest "Define cross-scope access to an application resource")
-   [Define access to or from an application scope](https://docs.servicenow.com/csh?topicname=restricted-caller-access-privilege.html&version=latest "Define access to or from an application scope")

A good community blog that talks about how to fix restricted caller access errors:

-   [How to fix the red popup "... must declare a cross scope access privilege" errors](https://community.servicenow.com/community?id=community_blog&sys_id=ce28d5b8db690c5c5129a851ca961999&view_source=searchResult "How to fix the red popup \"... must declare a cross scope access privilege\" errors")

## HR Roles

The main purpose of HR roles is to prevent users outside of the HR organization from accessing HR data.  

Some key points are:

-   Users without an HR scoped role cannot view HR cases or HR profile information.
-   Scoped HR roles can be assigned by a user who has the sn\_hr\_core.admin role or a user who has the assignable by role of the scoped HR role. This is enforced regardless of whether the scoped role is assigned directly to the user or the user is added to a group that contains the scoped role.
-   By default, the system admin role (admin) contains the HR admin role (sn\_hr\_core.admin).  Ensure to configure your system such that only the HR admin role has access to sensitive information. After assigning the HR admin role to the necessary users, remove the HR admin role from the system admin role to prevent the System Administrator from viewing sensitive HR information.  **Note:  Ensure that you have at least two users with the HR Administrator role. If you assign only one person with the role and that person is deactivated, you no longer have a user that can perform the HR admin duties.** See [Remove HR Administrator role from IT System Administrator.](https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/task/t_HRRemoveAdminRole.html "Remove HR Administrator role from IT System Administrator")
-   **Similarly, the above also applies to the sn\_hr\_le.admin role. It should be removed from the system admin role once the role has been added to at least two users.**
-   System admin can impersonate HR admin, but can't perform HR-related stuff.

This documentation talks about how to manage HR Roles and has lots of useful information:

[Manage HR roles](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/human-resources/concept/c_ManageRoles.html "Manage HR roles")

The below doc lists the roles installed with Case and Knowledge Management:

[Roles installed with Case and Knowledge Management](https://docs.servicenow.com/bundle/rome-employee-service-management/page/product/human-resources/reference/components-installed-with-case-and-knowledge-management.html "Roles installed with Case and Knowledge Management")

## FAQ

-   Q: Why can't I grant a scoped role to a user?   
    -   A: All scoped application roles can only be assigned by a user who has the scoped admin role or a user who has the assignable by role of the scoped role.  Also, if the scoped role contains another scoped role, the user also needs to have the assignable by role of this contained scoped role.
-   Q: Will global ACLs be honored by scoped applications? If there is a scoped application querying the user table, will global ACLs on that table work?  
    -   A: Not at this time. Global ACLs need to be copied into a separate ACL in the scoped application. 
-   Q: Can I still call all the APIs and platform script includes that I can in the Global space?   
    -   A: No there is an "inclusion list" of APIs that the platform will allow scoped applications to call. This inclusion list can be found here: [API Reference Server Side Scoped](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=no-namespace "API Reference Server Side Scoped")
-   Q: Why don't I see my scoped roles or my scoped roles taking effect after they are granted to a user.   
    -   A: Users will need to log out and log back in after being granted a role. 
-   Q: Why can't I see some HR services or COE tables on the native Case Creation UI Page (sn\_hr\_core\_case\_creation.do)?  
    -   A: Check the case tables ACLs to see if they are customized
-   Q: Why are some HR profile fields are not editable by the employee?  
    -   A: Some HR profile fields can be configured to be hidden/shown to employees using an HR system property (sn\_hr\_core.hr\_profile\_editable\_fields).  See [Add or modify an HR profile](https://docs.servicenow.com/bundle/paris-hr-service-delivery/page/product/human-resources/task/t_CreateOrModifyAUserProfile.html "Add or modify an HR profile")
-   Q: Why am I not able to add users to a group, which contains scoped application roles (e.g. sn\_hr\_core.basic)?  
    -   A: Scoped application roles can only be assigned by users who have a role specified in the **assignable by** field of the scoped application role.  In the example above, the user needs to have the role sn\_hr\_core.admin which is the assignable by field of the sn\_hr\_core.basic role. See [KB0722958](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722958 "KB0722958") for details.  This is enforced regardless of whether the scoped role is assigned directly to the user or the user is added to a group that contains the scoped role.
    -   Note: Even if the above is satisfied and the user has user\_admin, there's still a situation where the user is not able to add a user to a group containing a role: if the role or any contained roles is missing the assignable by field.  See [KB1113558](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB1113558)
-   Q: Why can't I see certain HR services created in "Human Resources: Service Portal" scope during case creation even though I have the sn\_hr\_core.basic role?  
    -   A: Scoped ACL will only be evaluated for records created in the same scope as the ACL record.  In the example above, there is no ACL that grants read access for HR services created in "Human Resources: Service Portal" scope.  The ACL that grants read access to HR services is in "Human Resources: Core" scope.  The solution is to create the same read ACL in "Human Resources: Service Portal" scope.  See KB [KB0780734.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780734 "KB0780734")
-   Q: Why can't I see sys\_audit records of sn\_hr\_core\_case?  
    -   A: sn\_hr\_core.admin role is required to read audit records

### Release

Updated

### Resolution

Updated
