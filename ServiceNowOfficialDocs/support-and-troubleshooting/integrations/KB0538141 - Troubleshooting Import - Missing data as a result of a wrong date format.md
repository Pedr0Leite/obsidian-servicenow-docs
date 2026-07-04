---
title: "Troubleshooting Import - Missing data as a result of a wrong date format"
aliases:
  - KB0538141
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538141
kb_number: KB0538141
last_modified: 2025-07-28
---

## Troubleshooting Import - Missing data as a result of a wrong date format

  

### Issue

This issue is related to data import and transform. Data is successfully imported into a staging table, but when the data is transformed to a target table, some or all date/time values are missing.

Symptoms:

-   Import says complete, but not all data is present
-   Data discrepancy after import
-   Import set has error

### Release

All

### Cause

When creating the transform map for the new import set, you are adding a field map for a date type field. A field map has a date format attribute you must populate with the format of the date values. The date format is either wrong or was not set, causing the system to use the default date format. In either case, the date format used is different than what the incoming date values are using.

### Resolution

To solve the issue, set the date format on the field map to match the format of the data.

### Related Links

[https://www.servicenow.com/community/developer-forum/issue-with-formatting-date-on-target-field-via-transform-map/td-p/2639023](https://www.servicenow.com/community/developer-forum/issue-with-formatting-date-on-target-field-via-transform-map/td-p/2639023)

[https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/time/reference/r\_UseDateAndTimeFields.html](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/time/reference/r_UseDateAndTimeFields.html)
