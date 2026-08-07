---
title: "Why is UI Action \"Request Extension\", which is only available to non-resource managers present in the Allocation Workbench, which is only available for resource managers?"
aliases:
  - KB0789800
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789800
kb_number: KB0789800
last_modified: 2024-04-07
---

## Why is UI Action "Request Extension", which is only available to non-resource managers present in the Allocation Workbench, which is only available for resource managers?

  

### Issue

The user had some questions/concerns about what the use case is for having a UI Action (e.g. "Request Extension") for the Allocation Workbench which has a condition on it for non-resource\_manager users when the Allocation Workbench is only accessible by users with the resource\_manager role.

### Resolution

The Product Owners explained that the "Request Extension" UI Action is for users with the "resource\_user" role, and that the "Extend Resource Plan" UI Action is for users with the "resource\_manager" role.

Currently, the "Extend Resource Plan" UI Action is not available in both the planning screen (resources tab in workbench) and the Allocation Workbench.

Users with "resource\_user" or "resource\_manager" roles can navigate to the planning screen by clicking the manage button on projects/demands.

The "Request Extension" UI Action can be used by users with the "resource\_user" role in the resources tab in the workbench.

Additionally, it was noted that the Product Owners are planning to provide the "Extend Resource Plan" functionality. It is in their backlog of tasks, as of the publishing of this article.
