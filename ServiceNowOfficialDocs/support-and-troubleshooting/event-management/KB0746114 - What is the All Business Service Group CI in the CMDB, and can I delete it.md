---
title: "What is the \"All\" Business Service Group CI in the CMDB, and can I delete it?"
aliases:
  - KB0746114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746114
kb_number: KB0746114
last_modified: 2025-08-19
---

## What is the "All" Business Service Group CI in the CMDB, and can I delete it?

  

### Issue

# Description

Service Groups are a type of CI that act as a container for Business Service CIs. The groups are organised as parent and child sub-groups, and sub-sub-groups etc., with the "All" group at the top of the tree, and the only group allowed to not have a parent.

The "All" record that exists out-of-box should not be deleted. This has sys\_id 0e7a06157f10310016181ccebefa91ce, which is hard-coded in various part of the product code related to Service Mapping and Alert Management. Issues with the Alert Dashboard, Impact Calculation and other freatures can be expected if this is deleted.

# Procedure

If you have already deleted this, and no upgrade is planned soon, the [XML of this record is attached](https://support.servicenow.com/sys_attachment.do?sys_id=87be38a2db0ab450e515c223059619c4 "XML of this record is attached"), so you can import it.

When an instance is upgraded or patched, this record will be replaced automatically. This record is not demo data.

/cmdb\_ci\_service\_group.do?sys\_id=0e7a06157f10310016181ccebefa91ce

The ‘Add business service to group ALL’ Busines Rule on cmdb\_ci\_service\_auto will also put this back if it is missing.

# Applicable Versions

Since the Service Model was added in Fuji/Geneva.
