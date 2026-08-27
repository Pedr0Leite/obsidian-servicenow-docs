---
title: "Reports using the kb-use table to report on article views are not reporting correctly"
aliases:
  - KB0720738
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720738
kb_number: KB0720738
last_modified: 2024-04-07
---

## Reports using the kb-use table to report on article views are not reporting correctly

  

### Issue

Reports using the kb-use table to report on article views are not reporting correctly

### Release

ALL

### Cause

KnowledgeHelp Script include was modified

### Resolution

KnowledgeHelp Script include was customized and that did not count the no.of views on the article.

Reverting this to OOB, resolved the issue.
