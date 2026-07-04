---
title: "After updating a record, some date/time fields are set to 1969-12-31"
aliases:
  - KB0549867
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549867
kb_number: KB0549867
last_modified: 2025-06-02
---

## After updating a record, some date/time fields are set to 1969-12-31

  

### Issue

After updating a record, one or more date/time fields display the value `1969-12-31`, which may seem unexpected or incorrect.

### Symptoms

-   A date/time field (e.g., `time_worked`, `start_date`, `end_date`) displays `1969-12-31` or a similar time-stamped value.
-   The behavior often occurs when setting a date/time field to empty (null) through a script or update.
-   In certain time zones, the displayed value includes a time offset (e.g., `1969-12-31 19:00:00`).

### Release

All Supported Releases

All modules using date/time fields

### Cause

This behavior stems from how date/time fields are stored and interpreted internally in ServiceNow:

Date/time fields are stored as the number of milliseconds since `1970-01-01 00:00:00 GMT`, also known as the Unix epoch.

If a field is null and not explicitly cleared or properly initialized, the system may interpret it as zero milliseconds.

Zero milliseconds = `1970-01-01 00:00:00 GMT`.

> Time zone adjustment:  
> If your user profile is in a negative GMT offset (e.g., Eastern Time), the system adjusts the displayed value by subtracting the time zone offset, resulting in a display of `1969-12-31`.

-   Client Script Behavior  
    A client script sets a date/time field to empty on mobile/tablet, and it displays as `1969-12-31 19:00:00`.
-   Null Date Initialization  
    A GlideRecord update leaves a date field null, and the system renders it as the Unix epoch in the user’s timezone.

### Resolution

To prevent this behavior:

-   Always explicitly handle date/time fields when updating records:
    -   Use `field.setDisplayValue('')` for clearing via GlideForm.
    -   Use `field = null` or `field = ''` appropriately on the server side depending on context.
-   Avoid leaving date/time fields unintentionally null if you expect them to be unset without showing the epoch date.
-   Consider adding validations or default values where necessary to prevent zero-millisecond interpretations.

### Related Links

-   [Client Script: Setting a Date/Time field to empty returns 1969-12-31 19:00:00](https://support.servicenow.com/kb_view.do?sysparm_article=KB0681663 "A Client Script used to set a Date/Time field to empty in Tablet Mode may return the unexpected value 1969-12-31 19:00:00")
-   [Rendering issues when time\_worked is set to less than epoch date](https://support.servicenow.com/kb_view.do?sysparm_article=KB0681662 "Updating time_worked field to a value less than 1969-12-31 00:00:00 yields strange results when that field is rendered on a form")
