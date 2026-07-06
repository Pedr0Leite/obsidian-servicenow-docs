---
title: "EMC Isilon Cluster is missing Manufacturer and Model ID after discovery"
aliases:
  - KB0727169
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727169
kb_number: KB0727169
last_modified: 2024-04-07
---

## EMC Isilon Cluster is missing Manufacturer and Model ID after discovery

  

### Issue

# Symptoms

* * *

EMC Isilon Cluster is missing Manufacturer and Model ID after discovery

# Release

* * *

London Patch 4 Hot Fix 2

# Cause

* * *

On step 26 of the **EMC Isilon Pattern** we are setting the Manufacturer and Model ID, which are reference fields, but in some cases discovery may return them as a string value. You will see the Manufacturer and Model ID values returned in the XML payload. 

# Resolution

* * *

An additional Pre Sensor has been created for EMC Isilon devices specifically, which is attached to this KB

\-Import the attached EMC Isilon Pattern XML into the instance.

\-Check the **Network Devices - Pre Sensor** Pattern Pre/Post Script and remove the **EMC Isilon Pattern** from the list of associated patterns

![](/sys_attachment.do?sys_id=a61928aedb02b450e515c22305961900)

\-On the new **EMC Isilon - Pre Sensor** Pattern Pre/Post Script add the **EMC Isilon Pattern**

**![](/sys_attachment.do?sys_id=e61928aedb02b450e515c22305961905)**

\-Navigate to **Discovery** > **MID Servers**  
\-Click **Pattern Sync to Mid**

Additional Information

* * *

[EMC Isilon Discovery](https://docs.servicenow.com/csh?topicname=emc-isilon-discovery.html&version=latest "EMC Isilon Discovery")
