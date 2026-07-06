---
title: "Correct usage of the \"Table Transform\" pattern operator."
aliases:
  - KB0727901
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727901
kb_number: KB0727901
last_modified: 2023-07-18
---

## Correct usage of the "Table Transform" pattern operator.

  

### Issue

# Description

* * *

1.  In many patterns, the "Table Transform" step is used to move data from one table to another or add more data to the existing table.
2.  When customers use the "Table Transform" operator, they may be under the impression that existing data in the target table will be retained if the source table is different.
3.  In reality, if the source table and target table on the operator are different, the data in target table is completely overridden by data in source table. 

# Usage

* * *

1.  Table transform operator should be used when the data should be moved out of a temp table to another temp table/CI table.
2.  Further, to populate more CI fields, the source and target table field values can be the same and additional fields can be added under "Target Field/Value" section

# Applicable Versions

* * *

All

#
