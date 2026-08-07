---
title: "On-Call users using default system schedules can cause SLA issues"
aliases:
  - KB0861944
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861944
kb_number: KB0861944
last_modified: 2024-04-08
---

## On-Call users using default system schedules can cause SLA issues

  

### Issue

A user reported that some of their task SLAs on incidents were running and accruing business times over the weekend, outside of the schedule provided for the SLA Definitions to run on (8-5 weekdays, excluding holidays).

### Cause

The user was having on-call persons utilize the default system schedule on their sys\_user profile, which the On-Call application references as the user's schedule of availability.

### Resolution

The reason the above On-Call configuration conflicts with SLA functionality is that both the on-call person and the SLA Definition are referencing an Out of Box (OOB), default schedule (and one which is generally referenced system-wide).

The on-call user should _**never**_ be using a default, largely-referenced schedule like the 8-5 weekdays, excluding holidays schedule as if it were a personal on-call schedule.

Here is how the issue arose: when a user is scheduled to be on call, a schedule span is added to their schedule to account for it. Normally, this would not be an issue, as each On-Call user should have their own personal, unique schedule associated with their sys\_user profile. However, in this case, On-Call users were referencing the default schedule 8-5 weekdays, excluding holidays.

As a result, when the user was scheduled to be on-call, a span for coverage was added to the 8-5 weekdays, excluding holidays schedule. Because this is also being used by the SLA Definition in question, unexpected business time accruing over the weekend, as the SLA engine does not know that the newly added span has anything to do with on-call, and considers it as a valid window of business time.

With the added on-call Saturday span, the SLA engine used the window of time to work, thus resulting in unexpected additions to business time on the relevant task SLA. To correct the issue, the user should create personal on-call schedules for each on-call user and associate them to the user's sys\_user profile. All unintentionally added spans should be removed from the default 8-5 weekdays, excluding holidays schedule, and the task SLA should be repaired post-deletion of the on-call span(s).
