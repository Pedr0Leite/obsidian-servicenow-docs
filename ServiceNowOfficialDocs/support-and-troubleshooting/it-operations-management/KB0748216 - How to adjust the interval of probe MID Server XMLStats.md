---
title: "How to adjust the interval of probe \"MID Server XMLStats\"
aliases:
  - KB0748216
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748216
kb_number: KB0748216
last_modified: 2024-04-07
---

## How to adjust the interval of probe "MID Server XMLStats"

  

### Issue

# Description

After MID server is configured on an instance, an ECC queue record with Topic "queue.stats" and Name "MID Server XMLStats" is received on the instance every 10 minutes.

This ECC queue record provides useful MID Server statistics include memory and CPU usage data.

Since there are only 6 ECCs generated per hour for each MID server, this feature won't have much impact on the Instance / MID server.

However if you would like to modify the interval that this ECC message is received, please follow steps below.

# Procedure

To apply on all MID servers:

1\. Navigate to MID Server > Properties

2\. Add a new property with name: mid.metrics.interval

Set the value, which is in seconds. For example, if you want to set interval to be 20 minutes, the value should be 1200.

Default value is 600.

3\. Restart the MID servers

To apply on a particular MID server:

1\. Navigate to MID Server > Servers > open the MID server record > under Configuration Parameters, create a New parameter: debug, with empty value (this is just a dummy parameter which we will change in step 2.)

2\. On the MID server record, under Configuration Parameters, highlight the parameter we just created,

(don't click on the hyper link), click on the empty space so you can rename it.

Rename it as mid.metrics.interval, then set value to the interval you need (in seconds).

For example, if you would like to change it to 15 minutes, set the value to 750.

(The default value is 600, which is 10 minutes)

3\. Restart the MID server

# Applicable Versions

All
