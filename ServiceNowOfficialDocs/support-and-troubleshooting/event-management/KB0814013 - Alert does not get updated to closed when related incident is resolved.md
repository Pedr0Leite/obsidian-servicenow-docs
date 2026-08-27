---
title: "Alert does not get updated to closed when related incident is resolved"
aliases:
  - KB0814013
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814013
kb_number: KB0814013
last_modified: 2025-01-03
---

## Alert does not get updated to closed when related incident is resolved

  

### Issue

Alert didn't get close when the related incident which is linked to the alert got closed/resolved if the alert Severity is Information.

### Release

All Versions.

### Resolution

The below script include will be used to check "Alerts" that have closed "Incidents" and it will close the related "Alerts":

EvtMgmtAlertActions.

https://Instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=c9c24f6453b003000238ddeeff7b128a  
  
Here is the code extract: 

```
        var alert = new GlideRecord('em_alert');        // Get alerts with delay, this makes sure all BR on create/update alerts completed before the job is running        alert.addQuery('sys_updated_on', '<=', inProgress);        alert.addQuery('state', '!=', 'Closed');        alert.addQuery('severity', '!=', '5');  //// <<<===== This will exclude Info Alerts.======>>>>        alert.addNotNullQuery('incident');        var gr = alert.addJoinQuery('incident', 'incident', 'sys_id');        gr.addCondition('state', 'IN', '6,7'); // 6 - Resolved or 7 - Closed
```

  
The highlighted line will ignore Alerts with info severity because the expectation is that for Info Alerts, there will no Incidents created.  
  
If the alert Severity is "Info", the alert will be not be captured with the above query and it will not get closed.
