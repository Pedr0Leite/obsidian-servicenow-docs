---
title: "CI Identifiers do not allow adding reference identifier fields as a criterion attribute(s)."
aliases:
  - KB0696924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696924
kb_number: KB0696924
last_modified: 2024-04-07
---

## CI Identifiers do not allow adding reference identifier fields as a criterion attribute(s).

  

### Issue

# Symptoms

* * *

CI Identifiers do not allow adding reference identifier fields as a criterion attribute(s). 

# Release

* * *

ALL releases.

# Cause

* * *

This is expected OOB behavior as it is not possible to add reference fields as a criterion attribute for CI Identification. This is because reference fields store the sys\_id that point to a record in another table, and thus is considered a weak criterion attribute (in terms of uniqueness) for the current table. Therefore, using a reference field as a criterion attribute is not exactly the most unique way to distinctly identify a CI. 

# Resolution

* * *

Use the attributes and fields that are not of reference field type as reference fields have sys\_IDs that actually point to a record in another different table, and hence it is considered a weak criterion attribute.
