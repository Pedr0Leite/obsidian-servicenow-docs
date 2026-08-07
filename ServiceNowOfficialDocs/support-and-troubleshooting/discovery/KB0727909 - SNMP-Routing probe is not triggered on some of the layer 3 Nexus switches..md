---
title: "SNMP-Routing probe is not triggered on some of the layer 3 Nexus switches."
aliases:
  - KB0727909
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727909
kb_number: KB0727909
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

On an IP router or a layer 3 Switch, SNMP-Routing probe is triggered to gather information about the routing tables on the devices.  
  
Link for the Routing Probe:  
**https://<instance-name>.service-now.com/nav\_to.do?uri=discovery\_probes\_snmp.do?sys\_id=a2bada940a0a0b6100d5e020a828fdeb**  
  
For some devices SNMP-Routing probe is not triggered and some of the data is not updated on the CMDB.

# Environment

* * *

Discovery probes are used.

# Cause

* * *

OOTB Standard Network Switch and Standard Network Router has SNMP-Routing probe under the Triggers probes.

 ![](sys_attachment.do?sys_id=ed3f3826db0ab450e515c22305961950)

This probe is not getting triggered if the below condition is not:  
  
**values.get('routing') == 'true' && values.get('block\_router\_exploration') == 'false'**

The 'routing' would be true if "ipForwarding oid" is equal to 1 AND "ipForwDatagrams" is greater than 0.

For of the Nexus 7K switches ipForwarding is set to '2' because of which SNMP-Routing probe is not triggered even though the device has layer 3 capabilities. This is a bug documented by cisco in 'CSCve67179'.

Link: [https://quickview.cloudapps.cisco.com/quickview/bug/CSCve67179](https://quickview.cloudapps.cisco.com/quickview/bug/CSCve67179)

# Resolution

* * *

Open the SNMP-Routing classifier record -> **https://<instance-name>.service-now.com/nav\_to.do?uri=discovery\_classifier\_probe.do?sys\_id=1524018237120100dcd48c00dfbe5d36** and remove the condition script as below.

 ![](sys_attachment.do?sys_id=293f3826db0ab450e515c22305961956)
