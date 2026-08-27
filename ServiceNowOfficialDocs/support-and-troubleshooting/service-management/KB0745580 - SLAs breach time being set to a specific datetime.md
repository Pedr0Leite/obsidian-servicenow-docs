---
title: "SLAs breach time being set to a specific date/time"
aliases:
  - KB0745580
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745580
kb_number: KB0745580
last_modified: 2024-04-07
---

## SLAs breach time being set to a specific date/time

  

### Issue

All Task SLAs for some SLA definitions are having their breach time set to a specific date and time.  

### Release

ALL

### Cause

The schedule associated to those SLA Definitions has a specific date set on the "**Repeat Until**" field for the main daily entry. For that reason, no additional schedule items are added to the schedule after that date and the SLA breach time is being set to the latest business time on repeat until date set.

### Resolution

According to our [documentation](https://docs.servicenow.com/csh?topicname=r_ScheduleEntryFields.html&version=latest "documentation"), the "**Repeat Until**" field is defined as:

Select a repetition end date. If you leave this field blank, the schedule repeats indefinitely. 

To set a new date or remove the repeat until definition:

-   Open the schedule definition related to the affected SLAs;
-   On the related list "_Schedule Entries_", open the entry containing the main repetition (daily, Weekly on Weekdays, etc);
-   Update or clear the "**Repeat Until**" field;
