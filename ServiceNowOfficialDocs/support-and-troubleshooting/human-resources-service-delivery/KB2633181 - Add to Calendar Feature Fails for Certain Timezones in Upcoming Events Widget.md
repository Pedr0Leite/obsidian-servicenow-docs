---
title: "\"Add to Calendar\" Feature Fails for Certain Timezones in Upcoming Events Widget"
aliases:
  - KB2633181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633181
kb_number: KB2633181
last_modified: 2026-01-01
---

## "Add to Calendar" Feature Fails for Certain Timezones in Upcoming Events Widget

  

### Issue

The Add to Calendar feature in the upcoming events widget does not work for users whose timezone is set using an abbreviation (e.g., IST). The widget throws errors and fails to recognize abbreviated timezones.

### Release

Any Release

### Cause

The widget relies on moment-timezone.js, which supports only IANA timezones in the format `{AREA}/{LOCATION}` (e.g., Asia/Kolkata) and does not accept abbreviated timezones like IST. Using abbreviations causes the script to fail.

### Resolution

**Verify Script Include**

-   Ensure the timezone-related Script Include (e.g., `MomentTimezoneWithData`) is active and updated.

**Update User Timezone**

-   Set the time\_zone field for users to an IANA-compliant value (e.g., Asia/Kolkata) instead of an abbreviation like IST.

**Avoid Customizing OOB Timezone Choices**

-   Do not modify the platform’s default timezone list, as this can cause system-wide issues.

**Optional Display Customization**

-   If you need to show abbreviations (e.g., IST) in the UI:
    -   Use moment-timezone’s `format('z')` function in widget scripts to display abbreviations without breaking functionality.

**Clear Cache and Validate**

-   Clear platform cache.
-   Test the Add to Calendar feature for users with updated timezone values.
-   Confirm events are added successfully.
