---
title: "How to disable the live feed icon for a particular table"
aliases:
  - KB0693858
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693858
kb_number: KB0693858
last_modified: 2025-01-03
---

## How to disable the live feed icon for a particular table

  

### Issue

  
  

# Description

* * *

It may be desirable to keep the live feed icon from showing up for a particular table. This article discusses the procedure needed to allow for this.

# Procedure

* * *

If you want to keep the live feed icon from showing up for a particular table you will need to take the following steps:

1) Go to the dictionary record for the table in question that is the type collection. So for example if you were trying to disable the live feed icon on the incident table you would do the following filter criteria:

Table is incident

and

Type is Collection

This should return a single record.

2) Go into the record

3) Switch to the advanced view

4) Add the following entry to the Attributes field:

live\_feed=false

5) Save the record

That should do it. The live feed icon should no longer appear for that table

# Applicable Versions

* * *

ALL
