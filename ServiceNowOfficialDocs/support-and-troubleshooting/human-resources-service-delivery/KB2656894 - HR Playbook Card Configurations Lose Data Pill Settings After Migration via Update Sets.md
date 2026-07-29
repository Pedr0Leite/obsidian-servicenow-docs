---
title: "HR Playbook Card Configurations Lose Data Pill Settings After Migration via Update Sets"
aliases:
  - KB2656894
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656894
kb_number: KB2656894
last_modified: 2025-12-17
---

## HR Playbook Card Configurations Lose Data Pill Settings After Migration via Update Sets

  

### Issue

HR Playbook card configurations (`sn_hr_le_playbook_card_config`) lose their data pill settings when moved between instances using update sets. After deployment, cards display placeholders (e.g., `{{ }}`) instead of actual data.

### Release

Any

### Cause

Data pill mappings are stored in `sys_element_mapping` records, which are not automatically included in update sets unless explicitly added.

### Resolution

-   When creating update sets for HR Playbook card configurations, explicitly add `sys_element_mapping` records that store data pill mappings.
-   Validate that these records are included before migrating to the target instance.
-   After migration, confirm that cards display actual data instead of placeholders.
