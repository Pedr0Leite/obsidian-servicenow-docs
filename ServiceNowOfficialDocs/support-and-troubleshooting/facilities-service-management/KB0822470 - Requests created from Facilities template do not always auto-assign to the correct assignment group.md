---
title: "Requests created from Facilities template do not always auto-assign to the correct assignment group"
aliases:
  - KB0822470
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822470
kb_number: KB0822470
last_modified: 2024-04-08
---

## Requests created from Facilities template do not always auto-assign to the correct assignment group

  

### Issue

There are assignment rules in place to auto assign assignment groups when the facilities request is created but the 'assignment group' is not populating properly.

### Release

Madrid

### Cause

The 'SM Template Definition' defined for the template that is overriding the assignment group value

### Resolution

The 'SM Template Definition' was overriding the 'Assignment Group' value from the assignment rules for the records created from the custom template.  
  
After deleting the template definition, the issue is resolved.  
  
Since there are 'assignment rules' in place to populate the 'Assignment Group' field, the 'Template Definition' record can be removed.
