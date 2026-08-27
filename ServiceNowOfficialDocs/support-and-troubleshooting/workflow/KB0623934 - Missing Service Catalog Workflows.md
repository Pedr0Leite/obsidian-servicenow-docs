---
title: "Missing Service Catalog Workflows "
aliases:
  - KB0623934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623934
kb_number: KB0623934
last_modified: 2024-09-21
---

## Issue

# Symptoms

* * *

Missing Service Catalog Workflows

# Release

* * *

In all versions.

# Cause 

* * *

 The affected instance had a change request to clean demo data.  As mentioned in HI for Service Catalog, **Remove Demo Data**:

Please note - Our demo data removal deletes the default CMS Pages (ESS etc.) as well as default Service Catalog Items.

# Resolution

* * *

Restore the default Service Catalog workflows:

1.  Go to Plugins.
2.  Search for Workflow Authoring Tools.
3.  Within the UI Action, click on 'Load Demo Data only'.
4.  Confirm and wait for the additional XML content to get uploaded in the instance.
