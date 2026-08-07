---
title: "Duplicate entries appear in SQL Server Standard – License Required section after reconciliation"
aliases:
  - KB3035778
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3035778
kb_number: KB3035778
last_modified: 2026-05-25
---

## Duplicate entries appear in SQL Server Standard – License Required section after reconciliation

  

### Issue

During reconciliation, duplicate records appear in the License Required By tab under License usage > Microsoft > SQL Server > Standard. When filtering by Device (Required by) as the CI name, multiple duplicate entries are observed for the same CIs.

### Release

ANY

### Cause

The SQL Server Enterprise software model is missing a downgrade path to the SQL Server Standard software model. Without this configuration, both software models are processed independently during reconciliation, resulting in duplicate license entries for multiple CIs.

### Resolution

-   Navigate to Software Asset Management > Software Models and open the SQL Server Enterprise software model.
-   Select the Downgrade tab and verify whether a downgrade path to SQL Server Standard exists.
-   If the downgrade path is missing, add the downgrade relationship: SQL Server Enterprise → SQL Server Standard.
-   Save the software model configuration.
-   Re-run reconciliation.
-   Navigate to License usage > Microsoft > SQL Server > Standard > License Required By tab and confirm that duplicate entries no longer appear.
