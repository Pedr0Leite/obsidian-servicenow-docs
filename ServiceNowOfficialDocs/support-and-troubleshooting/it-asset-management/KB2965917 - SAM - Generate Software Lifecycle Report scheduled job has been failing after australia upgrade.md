---
title: "SAM - Generate Software Lifecycle Report scheduled job has been failing after australia upgrade"
aliases:
  - KB2965917
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2965917
kb_number: KB2965917
last_modified: 2026-04-17
---

## SAM - Generate Software Lifecycle Report scheduled job has been failing after australia upgrade

  

### Issue

**Problem**  
The scheduled job 'SAM - Generate Software Lifecycle Report' has been failing silently after an upgrade to the Australia release.

### Symptoms

The job log shows a failure status but provides no error message.

The failure can be observed in the samp\_job\_log table, and the result is that data like 'Current Lifecycle Phase' on the sam\_sw\_product\_lifecycle\_report table is not being populated. To reproduce, open the scheduled job and click 'Execute Now', then monitor the job's progress in the samp\_job\_log table.

![](/sys_attachment.do?sys_id=8a985379475cc798b6d8aa25126d4388 "Screenshot 2026-04-17 at 5.28.09 PM.png")

### Release

Australia 

### Cause

**Root Cause**  
1\. The root cause is a bug in the Software Asset Management (SAM) module, specifically in the getPhaseColumns() method of the SAM lifecycle script include, which returns null when a phase key is not found in its phase column map.

This causes a null dereference in the clearBadPhaseDates() method, leading to job failure. The bug is tracked under PRB2014527 and will be delivered in the next Zurich/Australia compatible patches.  
  

### Resolution

**Steps to Resolve**  
1\. Implement the attached update set to fix the issue. This update set addresses a null dereference in the SampLifecycleReportGenerator script include, preventing the job from failing.

2\. After applying the update set, the job should run successfully.
