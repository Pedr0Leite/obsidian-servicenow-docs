---
title: "Error: Your update version entry can not be reverted because it is not the latest base system entry"
aliases:
  - KB0727665
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727665
kb_number: KB0727665
last_modified: 2025-10-16
---

## Error: Your update version entry can not be reverted because it is not the latest base system entry

  

### Issue

After activating "Software Asset Management Professional or any other related plugins" we would have to revert the SAM related record to OOTB for the application to work as expected without issues.  
  
While trying to revert some of the files by clicking the UI action "Revert to Base System" UI action on the skipped file in the sys\_upgrade\_history\_log table we see the error:

"**Your update version entry can not be reverted because it is not the latest base system entry"**

### Release

Any

### Cause

When we revert a record, the code will look at the most previous version that is available. If we look at the record, source shows up empty which is most likely the problem. In order for something to be reverted back properly it needs to have a proper source. For this reason using the revert to base system will not work for some records since the last previous record has no update source.

### Resolution

1) Go to '**sys\_update\_version'** table

2) Search for the filename of the record we would have to revert

3) Choose the history version you wish to revert to.

3) Open the history version and click on the UI action '**Revert to this version'**.
