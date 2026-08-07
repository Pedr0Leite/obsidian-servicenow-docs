---
title: "Alert remediation subflow not triggering on alert description updates"
aliases:
  - KB0759348
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759348
kb_number: KB0759348
last_modified: 2025-08-08
---

## Alert remediation subflow not triggering on alert description updates

  

### Issue

The alert remediation subflow associated with an alert management rule fails to trigger when the alert description is updated through subsequent events.

**Steps to reproduce:**

1.  Create an initial alert event that updates the description with several data points.
2.  Verify this initial event triggers the remediation subflow based on the alert management rule.
3.  Confirm the subflow creates an incident with the initial description (containing a "nil" case ID value).
4.  Create a second event associated with this alert that includes a case ID value (for example., "12345665656").
5.  Observe that while this event updates the alert description, it does not trigger the alert remediation subflow.

### Release

Any supported release

### Cause

The automatic executions limit on alert management rule was set to 1. This setting restricts the workflow to run only once while an alert remains open. The counter resets when the alert is closed. 

### Resolution

1.  Open the Alert Management Rule configuration for the affected alert. 
2.  Go to the Actions tab.
3.  Locate the Automatic executions limit field and change the value from one to a higher number, such as 100. 
4.  Save the configuration.

**Note**: You can set this value to any number greater than 1 based on your specific requirements. 

![Alert management rule configuration](sys_attachment.do?sys_id=62ea4cf84753e2d477748d01426d4317)
