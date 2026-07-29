---
title: "Model Category on Asset Does Not Update When CI Class Changes"
aliases:
  - KB3007054
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3007054
kb_number: KB3007054
last_modified: 2026-05-08
---

## Model Category on Asset Does Not Update When CI Class Changes

  

### Issue

When the class of a configuration item changes (for example, from IP Switch to IP Router), the model category field on the linked hardware asset (`alm_hardware`) record does not update automatically. Users may expect the model category to reflect the new CI class after the change.

### Release

Not release specific

### Resolution

This is expected behavior. The following explains how the system handles model category updates and why the asset record is not affected.

The "Update model category" business rule runs on the `cmdb_ci` table. This business rule updates the `cmdb_model.cmdb_model_category` list to make sure that the model record includes the appropriate category for the CI's class. However, the rule does not update the linked hardware asset (`alm_hardware`) record.

When a CI's class changes, the asset's model category remains as it was set during asset creation or when the model was last changed. There is no default logic to synchronize model category changes from the CI to the asset. This behavior is by design to preserve asset history and data integrity.

**Normalization**

Model normalization operates at the model level (`cmdb_model`) and is based on manufacturer, product name, and version metadata.

The model category and CI class are not part of the normalization criteria.

Any mismatch between the CI class and the asset model category does not affect model normalization.
