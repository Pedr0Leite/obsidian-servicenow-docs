---
title: "How to troubleshoot SLA Warning Notifications showing incorrect percentages"
aliases:
  - KB0520314
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0520314
kb_number: KB0520314
last_modified: 2026-06-03
---

## How to troubleshoot SLA Warning Notifications showing incorrect percentages

  

### Issue

When using Service Level Agreement (SLA) calculated values in a **task\_sla** email notification, inaccurate values are sent out in the resulting emails. For example, a SLA Percentage Timer is set up to fire at 75% completion of an SLA. This activity calls another activity that creates a _sla.warning_ event that fires an email notification. The subject line of the SLA notification is set to the dynamic value ${business\_percentage} and the resulting emails show a value other than 75%.

### Cause

The Workflow Percentage Timers and the SLA Calculations are completely independent of each other. Using ${percentage} in a notification will only ever display the most recently calculated value of the task\_sla.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50px; vertical-align: middle; text-align: center;"><img class="documentation" style="border: 0px solid black;" title="Note" src="/Note_25x.pngx" alt="Additional Information" width="25" height="25" align="bottom" border="0"></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: SLAs are calculated on a scheduled basis,&nbsp;and progressively more frequently the closer they are to their planned end time.&nbsp;For more details on how SLAs are calculated, refer to <a title="SLA Automation" href="https://docs.servicenow.com/csh?topicname=c_SLAProcessing.html&amp;version=latest" target="_blank" rel="noopener noreferrer">SLA Automation</a> in the ServiceNow product documentation.</td></tr></tbody></table>

The **Calculate SLAs on Display** (glide.sla.calculate\_on\_display) runs the calculation of SLAs when a task record is viewed to display real-time numbers (percentages, time used, and so on). To perform the calculation, this property imposes an overhead necessary on a case-by-case basis. If the \[glide.sla.calculate\_on\_display\] property is turned on, SLAs are calculated when the case form is viewed. This does not mean that SLAs are updated when a report is run or a case is viewed in a list.

If this property is turned on, the SLA updates when the case form is viewed. For performance reasons, SLAs cannot be calculated on demand. By default, this property is turned off, meaning the business elapsed time and all other calculated fields will only ever represent the values from the last time the SLA was calculated.

### Resolution

To specify elapsed percentage in SLA notifications, it is recommended to use notifications for each percentage level. For example, an email notification for "_75 percent SLA Warning"_ is created and a special event is used to trigger that notification. The event can be called "sla.warning.75".

Another way to accomplish this is by calling the code directly to update the SLA before sending the notification. Using code similar to the Run SLA Calculation UI Action can do this.
