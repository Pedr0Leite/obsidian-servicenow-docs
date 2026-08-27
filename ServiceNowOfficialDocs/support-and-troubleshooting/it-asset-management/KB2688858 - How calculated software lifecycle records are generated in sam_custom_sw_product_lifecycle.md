---
title: "How calculated software lifecycle records are generated in sam_custom_sw_product_lifecycle"
aliases:
  - KB2688858
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688858
kb_number: KB2688858
last_modified: 2026-05-15
---

## How calculated software lifecycle records are generated in sam\_custom\_sw\_product\_lifecycle

  

### Issue

Calculated software lifecycle records are automatically created in the `sam_custom_sw_product_lifecycle` table with source = Calculated. This article explains the source of these records.

### Release

All supported releases.

### Resolution

The scheduled job "SAM - Create Calculated Software Lifecycles" is responsible for deleting and recreating records in the `sam_custom_sw_product_lifecycle` table where source = Calculated.

To locate the scheduled job, navigate to System Definition > Scheduled Jobs and search for "SAM - Create Calculated Software Lifecycles".

The job calls the following function in the script include:

`this.calculateLifecycle.insertAndProcessData();`

The `insertAndProcessData` function checks the value of the lifecycle property before processing:

```
insertAndProcessData: function() {
  if (GlideApplicationProperty.getValue(LIFECYCLE_PROPERTY) !== 'true') {
    return;
  }
```

Notes:

-   It is expected behavior for the job to delete and recreate records on each run.
-   To stop the records from being created, set the system property `com.snc.samp.generate.calculated.lifecycles` to false.

To update the property, navigate to System Properties > Search and search for `com.snc.samp.generate.calculated.lifecycles`.
