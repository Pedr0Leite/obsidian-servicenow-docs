---
title: "Journey Title Icon Broken After Migration Between Instances"
aliases:
  - KB2657373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657373
kb_number: KB2657373
last_modified: 2025-12-14
---

## Journey Title Icon Broken After Migration Between Instances

  

### Issue

After migrating Employee Journey Management records between instances, the Title icon (heading\_title\_icon) in the Journey Configuration table (`sn_jny_journey_config`) appears broken. Although `sys_attachment` and `sys_attachment_doc` records exist, `db_image` records are missing, and image `sys_id` values do not match across instances.

### Release

Any

### Cause

Inconsistent or missing `sys_id` references for images between source and target instances.

Missing `db_image` records and incorrect references in related tables (e.g., `sp_carousel_slide` background attribute).

Updating `sn_jny_journey_config` can delete attachments, requiring manual re-import.

### Resolution

Ensure all required records (`sys_attachment`, `sys_attachment_doc`, `db_image`, and m2m\_sp\_ng\_pro\_sp\_ng\_pro) are present and correctly referenced.

Update image `sys_id` values in:

-   `sn_jny_journey_config`
-   `sp_carousel_slide` background attribute

Re-import missing attachments via XML or update sets.

Validate in sub-production before applying to production.
