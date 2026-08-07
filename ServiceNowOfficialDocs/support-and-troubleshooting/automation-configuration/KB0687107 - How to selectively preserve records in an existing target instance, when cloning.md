---
title: "How to selectively preserve records in an existing target instance, when cloning"
aliases:
  - KB0687107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687107
kb_number: KB0687107
last_modified: 2025-01-07
---

## How to selectively preserve records in an existing target instance, when cloning

  

### Issue

  
  

# Description

* * *

This is a procedure for selectively preserving records in a target instance, when cloning instances.

# Procedure

* * *

To preserve data on a table in the target instance, set up a data preserver for that table.

To exclude that same table from coming over in the clone (from the source instance), set up the exclusion for it.

To preserve a single record or small number of records, export to XML and reimport after cloning.

You can also set up post-clone cleanup scripts to perform more specific clone-related tasks.

# Applicable Versions

* * *

All

# Additional Information

* * *

 The clone process first brings over all data, minus the excluded data. The preserved data is then applied on top of this cloned database.
