---
title: "A Post-Clone script to Deactivate and Cancel Discovery Schedules"
aliases:
  - KB0789119
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789119
kb_number: KB0789119
last_modified: 2026-05-07
---

## A Post-Clone script to Deactivate and Cancel Discovery Schedules

  

### Summary

Discovery Schedules will be copied as part of a clone. They will then run on the same schedule on the clone target instance, and may cause performance problems for the instance, MID Servers of the target instance, or the devices and servers that are being Discovered due to the unwanted additional probes running against those IPs. Customers generally don't need or want the CMDB updated so regularly or at all on sub-production instances.

This KB provides a way of automatically turning off Discovery jobs on any sub-prod instances immediately after a clone.

### Release

Any.

### Instructions

This solution leverages the Post-Clone Cleanup Script platform feature. [More details of what that is are in the docs.](https://www.servicenow.com/docs/r/platform-administration/post-clone-cleanup-scripts.html "More details on what that is are in the docs.")

1.  Navigate to: **System Clone -> Clone Definition -> Cleanup Scripts**
2.  Click **New**
3.  **Name: De-activate And Stop Discovery Schedules**  
    **Script**: (see below)
4.  **Submit**

/\*
Custom post-clone cleanup script based on Service-Now KB0789119
David Piper, 12/12/2019

This will deactivate any scheduled discoveries on the clone target after the clone, and stop any that are already started.
\*/
deactivateAndStopDiscoverySchedules();

function deactivateAndStopDiscoverySchedules() {
	// De-activate Discovery Schedules
	var schedules = new GlideRecord('discovery\_schedule');
	schedules.addEncodedQuery("active=true^disco\_run\_typeINdaily,weekly,monthly,periodically,weekdays,weekends,month\_last\_day,calendar\_quarter\_end");
	schedules.query();
	while (schedules.next()) {
		schedules.active = false;
		schedules.update();
	}
	
	// Stop any running schedules
	var statuses = new GlideRecord('discovery\_status');
	statuses.addEncodedQuery('stateINStarting,Active');
	statuses.query();
	while (statuses.next()) {
		var dac =  new SncDiscoveryCancel();
		dac.cancelAll(statuses.sys\_id);
	}
}

Alternatively, an update set is attached containing this script.

![](sys_attachment.do?sys_id=98ecf70c47744f5877748d01426d439d)
