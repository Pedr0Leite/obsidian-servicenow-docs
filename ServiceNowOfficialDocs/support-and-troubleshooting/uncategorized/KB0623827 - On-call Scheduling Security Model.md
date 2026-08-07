---
title: "On-call Scheduling Security Model"
aliases:
  - KB0623827
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623827
kb_number: KB0623827
last_modified: 2024-04-07
---

## On-call Scheduling Security Model

  

### Issue

On-call Scheduling Security Model

  
  
Overview

* * *

Have you ever tried delegating the **rota\_manager** for the same user from multiple groups? **sys\_user\_has\_role** only has 1 entry for the first group. 

This works as designed. 

Those designated with the **rota\_manager** role can edit Rotas and the associated rosters for the Rota in situations where they are the manager of the Rota group. 

The **rota\_admin** role needs granted to update Rotas without being a manager of the group.

Here is how the security model for Rotas works: 

-   ADMIN - Access to everything in the system including Rota 
-   **rota\_admin** - Basic CRUD operation for Rota records 
-   **rota\_manager** \+ group manager/ delegate - Ability to CRUD only to that groups' records 

Delegate Roles

* * *

To delegate roles, the manager in this case, must be a **role\_delegator**. This is completed by visiting the following module in the navigator: 

_User Administration > Role Delegation > **Delegate Roles In Group**_ 

![](sys_attachment.do?sys_id=83fc2c22db82b450e515c223059619b0)

To delegate roles as a role\_delegator, visit the following module in the navigator: 

_User Administration > Role Delegation > **Designate Role Delegation**_ 

![](sys_attachment.do?sys_id=c3fc2c22db82b450e515c223059619ba)

The manager can then give a member the **rota\_manager** role, and this generates a **sys\_user\_has\_role** record specifying the role has been granted by the group. 

This user is now able to maintain the rotations for that group only, because it has been granted by that group only. 

To modify the above behavior, investigate the **OnCallSecurityNG** script include, specifically the **rotaMgrAccess** function as this determines whether a groups Rotas should be editable in the calendar.

The helper function uses the platform (**gs.hasRoleInGroup**) to check whether the user has been granted the role by the current group.
