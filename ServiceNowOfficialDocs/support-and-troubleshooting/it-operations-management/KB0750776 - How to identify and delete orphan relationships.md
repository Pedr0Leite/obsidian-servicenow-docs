---
title: "How to identify and delete orphan relationships"
aliases:
  - KB0750776
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750776
kb_number: KB0750776
last_modified: 2025-12-08
---

## How to identify and delete orphan relationships

  

### Issue

How to count and delete orphan relationships (cmdb\_rel\_ci)?

### Release

All releases.

### Resolution

Here is the script can be used to find the orphan relationship counts:

```
// Find orphan rel count
var ga = new GlideAggregate('cmdb_rel_ci');
ga.addEncodedQuery('parent.sys_class_path=NULL^ORchild.sys_class_path=NULL');
ga.addAggregate('COUNT');
ga.query();
ga.next();
gs.log(ga.getAggregate('COUNT'));
```

To delete orphan relationship

```
//delete orphans
var gr = new GlideRecord('cmdb_rel_ci');
gr.addEncodedQuery('parent.sys_class_path=NULL^ORchild.sys_class_path=NULL');
//gr.deleteMultiple(); //uncheck when required.
```
