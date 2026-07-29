---
title: "On insert business rules do not run on cmdb_rel_ci (CI Relationships) table after discovery"
aliases:
  - KB0694512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694512
kb_number: KB0694512
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Doing discovery to create new relationships does not run the related business rule on the cmdb\_rel\_ci (CI Relationships) table.

# Release

* * *

Beginning with Jakarta.

# Cause

* * *

Beginning with the Jakarta release, the Identification Reconciliation Engine API (IRE API) handles the creation of CI relationships. Therefore, business rules relating to the cmdb\_rel\_ci table are not triggered.

The glide.identification\_engine.insert\_relation\_disable\_workflow system property was introduced in Jakarta to have a configurable way when going through IRE APIs not to trigger business rules on the cmdb\_rel\_ci table only for inserts. This improves End to End (E2E) discovery times because they internally call IRE.

Business rules slow down actual insertion of records by a small amount, which eventually slows down E2E discovery. epecially when discovery is inserting thousands of relations at once. Therefore, for overall performance improvement for discovery, the default setting is not to trigger business rules on cmdb\_rel\_ci on the insert.

If you still want to trigger business rules on this table, create the glide.identification\_engine.insert\_relation\_disable\_workflow system property as described in the Resolution section. Setting this property to false should not adversely effect discovery performance. It will have a minor impact on instance performance. 

# Resolution

* * *

Go to sys\_properties (system properties) and search for the glide.identification\_engine.insert\_relation\_disable\_workflow property.

-   If this system proepty exists, set it to false.
    
-   If this system property does not exist, click **New** and create it with the following values:
    
    -   **Type**: string
    -   **Name**: glide.identification\_engine.insert\_relation\_disable\_workflow
    -   **Value**: false
