---
title: "SAMP Software subscription data does not automatically map to the corresponding Software Models"
aliases:
  - KB0778471
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778471
kb_number: KB0778471
last_modified: 2024-04-08
---

## SAMP Software subscription data does not automatically map to the corresponding Software Models

  

### Issue

"SAM - Import User Subscriptions" job would import the Software subscriptions for Office 365 or Adobe.

Link to the job: https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=0a9fc2e087600300697c6ccfb7cb0bbf

In some cases the subscription data is loaded but they are not associated to the corresponding Software model records.

Subscription data would be loaded into this table: samp\_sw\_subscription

### Release

Software Asset Management Professional for Adobe/Software Asset Management Professional for Microsoft plugins are installed.

### Cause

The job "SAM - Import User Subscriptions" did not complete successfully and might have some issues while looking yup the content.

The job status can be checked in the 'samp\_job\_log' table.

When running the scheduled job through the background script below errors are observed:

Job was run like below:  
  

```
new SamImportUserSubscriptions().process();
```

  
Errors observed:  
  

```
CanonicalName: Discovered Name: 'Adobe Systems' Canonical is: 'Adobe Systems'CanonicalName: Discovered Name: Adobe Systems core_company is: 445182cfdb80ff406adb54904b961961Background message, type:error, message: Publisher and Product manufacturer do not matchOperation against file 'cmdb_software_product_model' was aborted by Business Rule 'Product should match publisher^1fd013d2dbf733448812644a4b9619c9'. Business Rule Stack:Product should match publisher
```

  
The reason why "Product should match publisher" business rule was failing is because there are two core\_company records for Adobe Systems.

### Resolution

Combine the two company records into one and running the job again fixed the issue.
