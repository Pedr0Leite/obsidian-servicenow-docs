---
title: "How to increase the default timeout duration for ATF tests"
aliases:
  - KB0695425
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695425
kb_number: KB0695425
last_modified: 2026-01-09
---

## How to increase the default timeout duration for ATF tests

  

### Issue

ATF tests will fail if the maximum timeout duration is exceeded. For such failures you will see a message similar to the following:  
  
"The test timed out because the max execution time (600 seconds) was reached while executing step 2 - 4"  
  
The default value of 600 seconds can be increased by increasing the value of the sn\_atf.batch.timeout system property.

### Release

All supported versions.

### Resolution

Follow the procedure below:

* * *

1.  Type sys\_properties.LIST in Application Navigator and press enter
2.  Click the New button to create a new property
3.  Set the values as follows:  
    -   Name: `sn_atf.batch.timeout`
    -   Type: integer
    -   Value: Some value greater than 600
4.  Save the record
