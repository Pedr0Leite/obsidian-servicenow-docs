---
title: "Duplicate Asset Records are Created via Manual Asset Entry"
aliases:
  - KB2628934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2628934
kb_number: KB2628934
last_modified: 2026-06-18
---

## Duplicate Asset Records are Created via Manual Asset Entry

  

### Issue

Duplicate Asset Records are Created via Manual Asset Entry

### Symptoms

Duplicate records are being created in the alm\_hardware table.

Both records are inserted with the exact same time stamp.

### Release

Xanadu P9

### Cause

The associated Record Producer script contained statements to both initialize and insert a new record, causing 2 new records to be created simultaniously.

var asset=newGlideRecord('alm\_hardware');

asset.initialize();

followed by

asset.insert();

### Resolution

Remove one or the other statements.
