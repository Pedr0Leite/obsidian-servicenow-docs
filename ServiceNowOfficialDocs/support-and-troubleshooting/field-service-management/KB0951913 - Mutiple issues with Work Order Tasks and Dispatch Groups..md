---
title: "Mutiple issues with Work Order Tasks and Dispatch Groups."
aliases:
  - KB0951913
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951913
kb_number: KB0951913
last_modified: 2024-10-09
---

## Issue

Unable to assign Work Order Tasks due to the following error message: The dispatch group is required in order to be assigned

## Resolution

Populate the dispatch\_group on the work order task. If this field is not required, you can change the configuration for this option by navigating to the sm\_config table and settting the  Dispatch Queue to false on the field service record.
