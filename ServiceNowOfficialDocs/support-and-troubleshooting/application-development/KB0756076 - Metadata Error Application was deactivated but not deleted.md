---
title: "Metadata Error: Application was deactivated but not deleted"
aliases:
  - KB0756076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756076
kb_number: KB0756076
last_modified: 2026-02-17
---

## Issue

Uninstall of application will fail with the error, "Deleted XXX metadata records, could not delete X. The application was deactivated but not deleted".

Check the sys\_metadata table and filter by the application name, this will show all the metadata records that still need to be deleted.

Also when filtering the application in sys\_db\_object or sys\_dictionary you will see the table details for the application.

## Resolution

When you have identified the name of record that is causing the error complete the following:

1.  Go to the sys\_metadata table and search for the record.
2.  Manually delete the record.
3.  Go back to the application and click Uninstall.

The application should now completely delete from your instance.
