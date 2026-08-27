---
title: "When are SLAs calculated?"
aliases:
  - KB0596023
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596023
kb_number: KB0596023
last_modified: 2026-06-03
---

## When are SLAs calculated?

  

### Issue

To determine when SLAs are calculated, check the status of the following:

-   Scheduled jobs
-   Task updates
-   Task on-display

### Scheduled jobs

The following table lists the six scheduled jobs that calculate Task SLAs based on how close the SLA is to breaching (reaching its Planned end time). The scheduled jobs calculate all active Task SLA records that are not paused and have a Planned end time that falls into the given breach timeframe.

<table class="internalTable" style="border: 1px solid #e0e0e0; border-style: solid; border-color: #000000;" border="1" cellspacing="0" cellpadding="2" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left; width: 225px;"><strong>Scheduled Job</strong></td><td style="vertical-align: middle; text-align: left; width: 955px;"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (already breached)</span></td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;">This job refreshes the timings in task SLA records that have already breached. This is limited to task SLAs where the breach time is within the last 365 days. This job runs once a day.</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (breach after 30 days)</span>&nbsp;</td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;">This job refreshes the timings in task SLA records where the breach time is more than 30 days away. This is limited to task SLA records where the breach time is within the next 365 days. This job runs every 5 days.</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (breach within 30 days)</span></td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;">This job refreshes the timings in task SLA records where the breach time is more than 1 day away and less than 30 days away. This job runs once a day.</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (breach within 1 day)</span>&nbsp;</td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;"><span style="text-align: start;">This job r</span>efreshes the timings in task SLA records where the breach time is more than 1 hour away and less than 24 hours away. This job runs every hour.</span>&nbsp;</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (breach within 1 hour)</span>&nbsp;</td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;"><span style="text-align: start;">This job r</span>efreshes the timings in task SLA records where the breach time is more than 10 minutes away and less than 1 hour away. This job runs every 10 minutes.</span></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left; width: 225px;"><span style="text-align: start;">SLA update (breach within 10 min)</span>&nbsp;</td><td style="vertical-align: middle; text-align: left; width: 955px;"><span style="text-align: start;"><span style="text-align: start;">This job r</span>efreshes the timings in task SLA records where the breach time is in the next 10 minutes. This job runs every minute.</span>&nbsp;</td></tr></tbody></table>

### Task updates

When a task, such as an incident, is updated, the SLA engine processes each of the linked task SLA records. This may include a task SLA that has recently been attached to the task.

If updates to the task result in a stage change on a task SLA, the latest timings are calculated. For example, if the stage changes from **In Progress** to **Paused**, then the latest timings are calculated.

### Task on-display

The system property glide.sla.calculate\_on\_display enables task SLA records to calculate when the task form is displayed for all active Task SLA records that are not paused. This ensures current Task SLA timings are up to date. Note that the time taken to load the form increases if the calculate on display property is enabled.
