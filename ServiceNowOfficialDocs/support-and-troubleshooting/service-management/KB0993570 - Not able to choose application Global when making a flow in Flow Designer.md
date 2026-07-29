---
title: "Not able to choose application Global when making a flow in Flow Designer"
aliases:
  - KB0993570
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993570
kb_number: KB0993570
last_modified: 2025-04-28
---

## Not able to choose application Global when making a flow in Flow Designer

  

### Issue

Not able to choose application Global when making a flow in Flow Designer.

### Cause

The user who was trying to create flow has the delegated\_developer role.

A user with a delegated\_developer role cannot have access to the global application in any way without giving them the admin role.

As the documentation for Delegated Developer indicates, it is intended to allow non-admins application-specific access to certain modules within the platform. It is not intended that such a developer create content in the global scope in Flow Designer.

A user with the delegated\_developer role is given Application-specific permissions for access to features such as 'Service Portal', 'Flow Designer', etc. In fact, if you look at such a users 'sys\_user\_has\_role' records you will see a corresponding role named <company\_name>\_dd\_<scope\_name>\_flowdesigner. Such a user should only be creating content within application scopes for which the user has been granted delegated developer flow designer feature access.
