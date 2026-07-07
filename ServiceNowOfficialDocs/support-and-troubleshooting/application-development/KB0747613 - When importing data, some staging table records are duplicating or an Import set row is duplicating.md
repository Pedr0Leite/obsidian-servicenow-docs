---
title: "When importing data, some staging table records are duplicating or an Import set row is duplicating"
aliases:
  - KB0747613
  - When importing data, some staging table records are duplicating or an Import set row is duplicating
tags:
  - servicenow
  - support-kb
  - import-sets
  - transform-maps
  - staging-table
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747613
kb_number: KB0747613
last_modified: 2024-04-07
---

## When importing data, some staging table records are duplicating or an Import set row is duplicating

  

### Issue

# Symptoms

* * *

You recognise this problem because:

-   Running of transform map is duplicating the records in staging table.
-   There are multiple transform map is using for same Import set.
-   There is no traces in node logs about this staging table

# Cause

* * *

This is the expected behavior if you are using multiple transform maps for the same Import set in a singe run.

One import set row is created per transform map. This behavior can cause a large number of temporary records to be generated.

# Resolution

* * *

Clean the staging table. If you need to clean the staging table increase the clean up frequency.  

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: For large imports, increase the clean up frequency of the staging tables</td></tr></tbody></table>

## Related

- [[KB0749267 - When import sets from two different data sources are using same staging table, only latest one is used during transform]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749267 - When import sets from two different data sources are using same staging table, only latest one is used during transform|When import sets from two different data sources are using same staging table, only  latest one is used during transform]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/ModelManufacture.README|ModelManufacture.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/README|Import sets overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/TriggerDataSource.README|TriggerDataSource.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/debug/README|debug]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0758037 - Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by security_admin Role|Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by \"security_admin\" Role]]
