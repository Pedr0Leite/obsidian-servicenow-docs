---
title: "Blank Content Preview Window in Employee Center After Yokohama Upgrade"
aliases:
  - KB2653675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653675
kb_number: KB2653675
last_modified: 2025-12-17
---

## Blank Content Preview Window in Employee Center After Yokohama Upgrade

  

### Issue

After upgrading to Yokohama, the content preview window in Employee Center displays as blank when viewing any content item. The issue may occur in certain environments (e.g., Production) while others (Dev/Test) remain unaffected.

### Release

Yokohama

### Cause

Known defect tracked under PRB1889589, where the content preview pane height is set to `0px` due to CSS rendering issues.

### Resolution

·  Workaround:  
Add the following CSS to the Page Specific CSS of the affected sp\_page record:

CSS

.sp-page-root {

container-type: normal !important;

}

Show more lines

Apply this change in a sub-production environment first, then in production after validation.

·  Permanent Fix:  
The issue is resolved in Content Publishing June 2025 release as part of PRB1889589.  
Remove the workaround after upgrading to the fixed version.
