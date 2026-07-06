---
title: "Cannot clear out field values during update via Easy Import"
aliases:
  - KB0745278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745278
kb_number: KB0745278
last_modified: 2024-04-07
---

## Cannot clear out field values during update via Easy Import

  

### Issue

When you try to clear out values in certain fields while updating records via [Easy import](https://docs.servicenow.com/csh?topicname=c_EasyImport.html&version=latest), you may observe that the values don't change. 

  

### Cause

To be able to clear out values via an import, the "Copy Empty Fields" checkbox in the transform map should be checked. Every time you import via the [Easy import](https://docs.servicenow.com/csh?topicname=c_EasyImport.html&version=latest) option, a new transform map is created with the "Copy Empty Fields" unchecked by default. 

That's the reason, the value in the target record will not change even if you have a blank value in the Excel file. 

#   

### Resolution

Since this is not an option in the Easy Import feature, you need to import using import sets following the documentation below:

[Importing data using import sets](https://docs.servicenow.com/csh?topicname=c_ImportDataUsingImportSets.html&version=latest)
