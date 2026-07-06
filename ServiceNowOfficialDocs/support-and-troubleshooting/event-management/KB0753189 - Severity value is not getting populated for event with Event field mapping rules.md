---
title: "Severity value is not getting populated for event with Event field mapping rules"
aliases:
  - KB0753189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753189
kb_number: KB0753189
last_modified: 2024-04-07
---

## Severity value is not getting populated for event with Event field mapping rules

  

### Issue

# Symptoms

There is an Event Filed Mapping rule to map the Severity field, but the value is not getting mapped to the event's severity field.

# Release

All Versions.

# Details

Event Field Mapping rules will be applied after the events get inserted onto em\_event table. And the mapping rules will be applied to Alerts.

So, if there is a field mapping rule to map the Severity field, it will update the "Alert Severity" field.

# Example

Create Event File Mapping with the below details:

  
**Source:** Trap From Enterprise 111  
**Mapping Type:** Single Filed.  
**From Field:** iso.org.dod.internet.private.enterprises.oracle.oraEM4.oraEMNGObjects.oraEMNGEventTable.oraEMNGEventEntry.oraEMNGEventSeverity.1  
**To Field:** severity.

**Event Field Mapping Pairs:**  
Key: CRITICAL  
Value: 1.

![](sys_attachment.do?sys_id=a92d2c62db82b450e515c2230596196e)

  
Test with the below event through REST API Explorer:  
  

`{     "description": "Test 101010",     "source": "Trap From Enterprise 111",     "node": "1.1.1.1",     "message_key": "2",     "additional_info": "{\"iso.org.dod.internet.private.enterprises.oracle.oraEM4.oraEMNGObjects.oraEMNGEventTable.oraEMNGEventEntry.oraEMNGEventSeverity.1\":\"CRITICAL\"}"   }   `

  
It would create an event with no severity, but the related "Alert" will be created with "severity" = "Critical"

![](sys_attachment.do?sys_id=ad2d2c62db82b450e515c22305961973)  
  
**Event Processing notes:**  
Binding alert CI process flow:  
Node is IP address  
Node was not found, checking by name  
Event CI type is empty  
No CI found for binding (Failed to resolve the event node to CI id)  
Binding Failure Reason: Failed to find the host with name: 1.1.1.1  
**Mapping rule(s) applied: Trap From Enterprise 111 Severity**

**![](sys_attachment.do?sys_id=612d2c62db82b450e515c22305961979)**

Alert created with Severity "Critical"

![](sys_attachment.do?sys_id=252d2c62db82b450e515c2230596197e)

Here is the alert processing notes, showing that the mapping rule is applied.

![](sys_attachment.do?sys_id=e52d2c62db82b450e515c22305961983)
