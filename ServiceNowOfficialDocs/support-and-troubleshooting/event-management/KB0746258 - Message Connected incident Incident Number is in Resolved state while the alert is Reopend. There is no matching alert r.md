---
title: "Message: Connected incident <Incident Number> is in Resolved state while the alert is Reopend. There is no matching alert rule to reopen the incident. Disconnecting the incident from the alert"
aliases:
  - KB0746258
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746258
kb_number: KB0746258
last_modified: 2024-04-07
---

## Message: Connected incident is in Resolved state while the alert is Reopend. There is no matching alert rule to reopen the incident. Disconnecting the incident from the alert

  

### Issue

# Symptoms

When an alert is reopened with the associated incident should Create New Incident, Reopen Incident, or Does nothing depending on the event management property "_evt\_mgmt.alert\_reopens\_incident_".  
  

```
Link to the property: https://<instance-name>.service-now.com/nav_to.do?uri=sys_properties.do?sys_id=0b018b12eb2211004d7763fba206fe34
```

  
Sometimes the message below is thrown on the alert form when the above property is set to "_Reopen Incident_".  
  

```
Connected incident <Incident Number> is in Resolved state while the alert is Reopened. There is no matching alert rule to reopen the incident. Disconnecting the incident from the alert
```

# Release

All releases

# Environment

Event Management plugin is installed

# Cause

One reason would be not defining the alert rule correctly.  
For example, we might add `State is Open` in the Alert filter condition as below.

![](sys_attachment.do?sys_id=669a24a6db42b450e515c223059619d9)![](sys_attachment.do?sys_id=2a9a24a6db42b450e515c223059619de)

# Resolution

When an alert is reopened, the state of the alert would be '**Reopen**' not '**Open**' and hence the alert would not match to Alert rules/Alert Management rules and hence the message is thrown and the incident is not opened.  
  
Hence modify the alert accordingly by adding another condition to include **`State is Reopen`** or **`dont not include the state field`**in the rule.
