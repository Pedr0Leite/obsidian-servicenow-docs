---
title: "Normalization Issue - Duplicate entries of normalized records for same vendor on core_company table"
aliases:
  - KB0855759
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855759
kb_number: KB0855759
last_modified: 2024-04-08
---

## Normalization Issue - Duplicate entries of normalized records for same vendor on core\_company table

  

### Issue

After completing guided setup for Normalization Data Service, we noticed core\_company table had duplicate entries of normalized records for same vendor.

### Release

Any

### Cause

Normalization Data Services (NDS) does not normalize the core\_company table. So it won't reduce core\_company records where there may be duplicate names. It creates a one to many relationship between the normalized company name (cds\_client\_name) table that matches the name in core\_company table record to Normalized mapping (cds\_client\_mapping) record. Then it updates the reference qualifier on select cmdb and asset related fields that reference core\_company table to display the record where the name matches the value in the normalized company (cds\_client\_name) table.

### Resolution

A user can manually add many records to core\_company table with same or similar name. So if "Normalized data service client" plugin is enabled and follow Normalized Data service guided setup. Then Normalized data service put the correct core\_company value with column "Normalized = true". So the record with column value "Normalized = true" should be picked.

  
Conclusion - Multiple records can be present in the core\_company table with same/similar name. If the record has "Normalized = true", then this is the only record shown when picking up the company value from the asset table. Meaning, it will only let you to select the core\_company record which is normalised.
