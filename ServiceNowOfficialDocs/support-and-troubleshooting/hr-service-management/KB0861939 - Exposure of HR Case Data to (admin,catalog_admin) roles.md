---
title: "Exposure of HR Case Data to (admin,catalog_admin) roles"
aliases:
  - KB0861939
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861939
kb_number: KB0861939
last_modified: 2025-09-03
---

## Exposure of HR Case Data to (admin,catalog\_admin) roles

  

### Issue

The way the record producer "Click Here to Raise a Case for HR" works exposes as a big risk of HR cases information being made available to users who have admin or catalog admin role. It becomes accessible in question\_answer table and the column Value shows the case description for all the records that have Question= Description you will see all the details of HR case. Way the role (permissions) work Out of the Box in Servicenow, users with admin or catalog\_admin role have read access to the question\_answer table, which needs to be reviewed. What is ServiceNow's advice on how to close off this exposure to HR case data?

### Release

Orlando Patch 3 Hot Fix 2

### Cause

The OOB property glide.enforce\_security\_scope.sn\_hr\_core is missing on the instance.

### Resolution

Issue is reproducible on the instance where the outside scope ACLs are also triggered and able to access the Scoped records. When compared to OOB with affected instance , there is a property that is missing on the instance . Property name is glide.enforce\_security\_scope.sn\_hr\_core. After adding this OOB property on instance , catalog\_admin are not able to see the question\_answer table data. Attached the OOB property for xml.
