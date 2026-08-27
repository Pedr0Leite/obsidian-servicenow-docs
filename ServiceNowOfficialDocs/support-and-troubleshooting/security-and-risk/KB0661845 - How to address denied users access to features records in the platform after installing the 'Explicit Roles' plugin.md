---
title: "How to address denied users access to features / records in the platform after installing the 'Explicit Roles' plugin"
aliases:
  - KB0661845
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661845
kb_number: KB0661845
last_modified: 2026-06-17
---

## How to address denied users access to features / records in the platform after installing the 'Explicit Roles' plugin

  

### Issue

After installing the 'Explicit Roles' plugin, there are some follow up configurations which have to be made by the admin. If those are not being properly done, non-admin users can loose their permissions for accessing some records and even features in the platform.

**Symptoms**

Non admin Users will not be perform daily tasks, as the following:

-   Accessing records
-   Accessing APIs which are restricted by ACLs
-   Exporting records
-   Basically every task which require which require passing of ACLs

### Cause

-   The Explicit Roles (**`com.glide.explicit_roles`**) plugin provides the **snc\_external** and **snc\_internal** roles
-   The **snc\_internal** role is automatically added to all existing users
-   ACLs which do not require any role will be added with the **snc\_internal** role

If from some reason, the user does not have the **snc\_internal** role, he will not pass the ACL check which is required for performing his current task, and therefore he will not be able to complete it.  
For more information, please read the [Explicit Roles](https://docs.servicenow.com/ "Explicit Roles") documentation.

### Resolution

 In order to solve the issue, the customer will have to grant the users with the snc\_internal / snc\_external roles, based on the ACL which is blocking their access.
