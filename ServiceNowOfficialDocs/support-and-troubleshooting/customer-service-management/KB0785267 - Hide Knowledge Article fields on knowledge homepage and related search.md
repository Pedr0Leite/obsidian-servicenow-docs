---
title: "Hide Knowledge Article fields on knowledge homepage and related search"
aliases:
  - KB0785267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785267
kb_number: KB0785267
last_modified: 2023-09-28
---

## Hide Knowledge Article fields on knowledge homepage and related search

  

### Issue

Need to restrict few users to see the content inside a custom field on the knowledge homepage. Even though the are ACL's to restrict the users to read the content but they are not working in the knowledge homepage.

### Resolution

To enforce the ACLs on the knowledge homepage, enable the property 'glide.knowman.search.apply\_acls' to true.
