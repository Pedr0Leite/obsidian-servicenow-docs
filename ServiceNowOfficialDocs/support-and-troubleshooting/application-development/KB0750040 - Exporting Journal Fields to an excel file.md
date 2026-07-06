---
title: "Exporting Journal Fields to an excel file"
aliases:
  - KB0750040
  - Exporting Journal Fields to an excel file
tags:
  - servicenow
  - support-kb
  - journal-fields
  - export
  - reporting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750040
kb_number: KB0750040
last_modified: 2025-02-20
---

## Exporting Journal Fields to an excel file

  

### Issue

How to Export Work Notes and Additional Comments in an Incident via Export to Excel

### Resolution

Export to Excel works in list view only and it exports only those columns which are added in the list view.

You can add Columns - 1. Work Notes 2. Additional Comments in the list view and export the list of incident to Excel.

Please note that -  Since Additional Comments and Work Notes are diary fields, all the work notes are exported in single cell of the excel file. This also means that Excels imposed limit of number of characters in 1 cell will also apply on the export.

### Related Links

In versions earlier to Istanbul Patch 1, Journal fields (Work notes and Additional Comments) couldn't be exported to reports (csv, excel, pdf). This issue was fixed in Istanbul Patch 1

[https://support.servicenow.com/kb\_view.do?sysparm\_article=KB0598748](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598748)

## Related

- [[KB0694609 - Importing journal field could result in non-matching of comment date and Created By in Additional comments]]
- [[KB0753763 - Updating journal fields fails to trigger Flow Designer]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753001 - Some roles are not visible and cannot be exported from the [sys_user_role] list table|Some roles are not  visible and cannot be exported from the [sys_user_role] list table]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0814892 - Metric definition table is unavailable for fulfiller users|Metric definition table is unavailable for fulfiller users]]
