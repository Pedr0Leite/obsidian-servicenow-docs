---
title: "Dependency Views not populating upstream or downstream relationships"
aliases:
  - KB0723085
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723085
kb_number: KB0723085
last_modified: 2025-04-07
---

## Dependency Views not populating upstream or downstream relationships

  

### Issue

# Symptoms

* * *

On the dependency view map, you are not able to see the complete upstream or downstream connections when you have a direct relationship between two servers

# Cause

* * *

If there are very high number of relationships to a server that is directly related to the server on which you are viewing the dependency map, you might not be seeing the connection

# Resolution

* * *

There is a sys\_property "glide.bsm.max\_num\_rels", that has a default value of 100. This property can be increased to view the missing relationships on the dependency view maps
