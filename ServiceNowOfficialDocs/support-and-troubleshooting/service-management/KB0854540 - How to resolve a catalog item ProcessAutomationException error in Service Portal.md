---
title: "How to resolve a catalog item ProcessAutomationException error in Service Portal"
aliases:
  - KB0854540
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854540
kb_number: KB0854540
last_modified: 2026-02-23
---

## How to resolve a catalog item ProcessAutomationException error in Service Portal

  

### Issue

Resolve a ProcessAutomationException error that occurs when a user opens a catalog item with an associated Flow Designer flow in Service Portal.

When the user tries to open the catalog item, the following error appears:

"com.snc.process\_flow.exception.ProcessAutomationException: Plan does not exist with id of"

Additional error details may include:

-   Script source code logged to console
-   Failing widget: SC Catalog Item

### Release

All supported releases

### Cause

The default business rule Delegated Dev Filter Flows restricts access to Flow Designer based on the user's assigned roles. When this restriction is active, the user cannot open catalog items that have an associated Flow Designer flow.

To review this business rule, go to the following URL on your instance:

https://<instance\_name>/sys\_script.do?sys\_id=03b2ec1567200300c4098c7942415ada

### Resolution

The Delegated Dev Filter Flows business rule checks the User \[sys\_user\] record for roles with the prefix "sn\_dd." If these roles are present, the business rule restricts access to Flow Designer, which also prevents the user from opening associated catalog items.

To resolve this issue:

1.  Go to **User Administration** > **Users** and open the affected user's record.
2.  Review the Roles related list for any roles with the prefix "sn\_dd."
3.  If roles with this prefix are present, evaluate whether they can be removed based on your business requirements.
4.  Remove the unnecessary sn\_dd roles to restore access to the catalog item.

**Note**: Roles with the "sn\_dd" prefix are related to delegated development and deployment. Verify that removing these roles does not affect other functionality the user requires.

### Related Links

[Instance-specific deployment user roles](https://docs.servicenow.com/csh?topicname=delegated_deployment_user_roles.html&version=latest#delegated-developer-and-deployment-user-roles "Instance-specific deployment user roles")
