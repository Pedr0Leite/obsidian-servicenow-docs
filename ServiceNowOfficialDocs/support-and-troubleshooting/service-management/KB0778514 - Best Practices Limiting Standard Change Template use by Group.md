---
title: "Best Practices: Limiting Standard Change Template use by Group"
aliases:
  - KB0778514
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778514
kb_number: KB0778514
last_modified: 2024-04-08
---

## Best Practices: Limiting Standard Change Template use by Group

  

### Issue

Are there any best practices for controlling the visibility of Standard Change templates for groups?

### Resolution

The supported base system (OOB) method to control the visibility of Standard Change Templates for groups is through _User Criteria_.

After creating a few User Criteria on a several demo data Standard Change Templates, these were locked to specific groups and, when impersonating a user within the groups and outside of the groups, only those users within the defined groups were able to see the Change Templates. This is the recommended method.
