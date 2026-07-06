---
title: "Multiple Identity Provider and Certificate records are created or records are empty after cloning "
aliases:
  - KB0813009
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813009
kb_number: KB0813009
last_modified: 2023-11-21
---

## Multiple Identity Provider and Certificate records are created or records are empty after cloning

  

### Issue

Multiple Identity Provider and Certificate records are created or records are empty after cloning.

### Cause

This is because Preserve Data and Exclude tables are not setup properly before cloning on the source instance.

### Resolution

You have to set up both Exclude and Preserve before cloning because of the following reasons: 

-   Exclude Table will create an empty table on the target instance.
-   Preserve will preserve the data on the target instance depending on the conditions.

### Related Links

Example : 

On the source instance, there are 2 Certificates ( 'sys\_certificate' table)

On the target instance, there will be 3 Certificates ('sys\_certificate' table)

  

If just Exclude Table is set, the table on the target instance will be empty after clone.

If just just Preserve data is configured, the table on the target instance will have 5 Certificate records in the 'sys\_certificate' table after clone.

If both Exclude Table and Preserve Data, the target instance will have 3 Certificates and Source will have 2 Certificates in the 'sys\_certificate' table after clone.

  

The above is true for Identity Provider Records also.
