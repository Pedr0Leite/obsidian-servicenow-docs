---
title: "Checking which records will be captured within an Update Set"
aliases:
  - KB0535262
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535262
kb_number: KB0535262
last_modified: 2025-03-03
---

## Checking which records will be captured within an Update Set

  

### Issue

For an update to be captured within **sys\_update\_xml** and thus be captured with an Update Set, the corresponding table must have the _update\_synch=true_ attribute.

### Resolution

To locate which tables have this attribute in a fresh instance:

1.  Navigate to the **sys\_dictionary** table.
2.  Personalize the list to include the **Attributes** column.
3.  Filter on Attributes is _update\_synch=true_. 

This will reveal approximately 300 tables, depending on the platform version, which have the _update\_synch=true_ attribute. If the table is not listed for the update , then the update will not be properly recorded within _sys\_update\_xml_ or subsequently within the intended Update Set. 

**Note**: ServiceNow does not recommended to add the _update\_synch=true_ attribute to any table that does not have it Out-of-box (OOB). Doing so can cause false updates to inundate the **sys\_update\_xml** table and in time will result in the inability to install plugins, commit Update Sets, and will cause unintended performance degradation issues.
