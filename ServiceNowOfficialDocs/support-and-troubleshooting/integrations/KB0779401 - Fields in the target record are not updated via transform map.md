---
title: "Fields in the target record are not updated via transform map"
aliases:
  - KB0779401
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779401
kb_number: KB0779401
last_modified: 2024-04-26
---

## Fields in the target record are not updated via transform map

  

### Issue

Even though a field map is configured in the transform map and the correct data is imported, the transform map fails to update the field on the target table.

### Cause

This scheduled import has the 'Run as' user as one with no roles. 

### Resolution

For an import to successfully run and transform the data, you should give the role 'import\_admin' to the 'Run as' user configured in the scheduled import.   
This role contains the roles import\_set\_loader, import\_transformer and import\_scheduler roles and without these roles, the import will not work as expected.
