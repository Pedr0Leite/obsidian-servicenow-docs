---
title: "Duplicate CI's getting created when existing CI's Data Source is set to Duplicate."
aliases:
  - KB0695124
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695124
kb_number: KB0695124
last_modified: 2025-04-07
---

## Duplicate CI's getting created when existing CI's Data Source is set to Duplicate.

  

### Issue

# Symptoms

* * *

When existing CI's Data Source (discovery\_source) is set to 'Duplicate', running a Discovery on the same CI would result in creation of duplicates.

# Release

* * *

Up to Madrid. New York does not use re-use the Discovery Source field for marking CIs as Duplicate any more.

# Cause

* * *

Identification Rules do not match Name, Serial Number and other even if the CI exists in CMDB when CI Data Source is set to 'Duplicate'. Those CIs are ignored, so that the CI not marked as duplicate can still continue to be updated.

However if CIs were manually de-duplicated by deleting the older of the duplicate records, only one CI will remain, and that is one of the newer CIs that had been set as Duplicate. From the point of view of the Identification engine, which ignores this record, no CI exists, so it creates one.

# Resolution

* * *

In order to avoid any duplicates getting created, the CI's "Data Source" must be set to anything other than Duplicate and CI's "Duplicate of" must be set to null or none. By doing this the Identification Rule works: It sees this CI when it tries to match name, serial number and updates that CI.

As part of resolving de-duplication tasks (which will have been created at the same time the CI was marked duplicate), one should also clear the discovery source value of Duplicate or revert it to the previous value, because this is not automatically done even when using the de-duplication tasks.
