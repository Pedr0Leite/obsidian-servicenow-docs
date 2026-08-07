---
title: "Removing the snc_external and snc_internal roles roles from system added by the CSM Plugin"
aliases:
  - KB0814842
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814842
kb_number: KB0814842
last_modified: 2025-09-15
---

## Removing the snc\_external and snc\_internal roles roles from system added by the CSM Plugin

  

### Issue

When the **CSM Plugin** is activated it enables the **Explicit Roles** plugin (com.glide.explicit\_roles) which adds the snc\_external and snc\_internal roles.

Additionally, as per our Service Manager, we want to know if the roles “snc\_internal” and “snc\_external” lead to additional license cost for us or not.

### Resolution

It's not possible to remove these roles once the plugin is activated. Many other functionalities, such as Consumer portals, widgets, pages, etc. use these roles. Along with that, there are many Script Includes, Business Rules, various other processes, and functionalities that are activated as well.

All of these make use of these explicit roles to define who sees what and who accesses what. That's why this explicit role plugin is one of the bases of the entire CSM ecosystem Architecture. Removing these roles will disturb the foundation and CSM will not render its functionalities at 100%.

If you are enabling CSM that means you have customers and who have people who are serving those customers. Servicenow platform offers these two roles snc\_internal / snc\_external so that you can differentiate between these:

-   Customer - snc\_external
-   Person serving customer = agent - snc\_internal

There is no additional license cost involved for these two roles, but CSM does require a license.
