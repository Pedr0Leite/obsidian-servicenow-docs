---
title: "Discovery - Evaluating the no sensors defined message"
aliases:
  - KB0547844
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547844
kb_number: KB0547844
last_modified: 2025-07-10
---

## Discovery - Evaluating the no sensors defined message

  

### Issue

Every active probe looks for a corresponding sensor to process the data that is collected by the probe. The **No Sensors Defined** message indicates that the corresponding sensor for the probe is missing or inactive. 

### Finding the no sensors defined error message

To find the cause of this error, identify the short message field of the error record. This field shows the name of the probe for which the sensor is missing.

To identify the short message field of the error record:

1.  Navigate to **Discovery > Discovery Log**.
2.  Filter on the **Level name** of **Error**. You can also view the Error Gauge on the Discovery dashboard.
3.  Note the **Short Message** field of the error record. This field shows the name of the sensor.

In the example below, the sensor error occurred when the Shazzam probe checked for the existence of the Shazzam sensor. 

![](/SensorNotDefinedStackTrace.pngx)

### Fixing the no sensors defined error message

To fix the No Sensors Defined error:

1.  Navigate to **Discovery Definition > Probes**.
2.  Search for the name of the probe. In this example, search for the name **Shazzam**.
3.  Click the link in the **Name** field to go to the Shazzam probe page.
4.  View the **Sensors that react to this probe** related list.
5.  If a sensor exists in this related list, check that the sensor is active. If this column contains **false**, double-click the value and choose **true** from the drop-down menu to make the sensor active.
6.  If a sensor does not exist in this related list, you can add a sensor. Click the **Edit** button.
7.  The **Edit Members** page displays.

![](/SensorEditMembers%20%281%29.pngx) 

8.  Search for the appropriate sensor from the **Collection** bucket.
9.  Select the sensor, and click **Add** to add the sensor to the **Sensors that react to this probe List** bucket.
10.  Click **Save**.
11.  Verify that the sensor now appears and is active on the **Sensors that react to this probe** related list.

If you can not find a sensor that matches the probe in the **Collection** bucket, you must create a new sensor.

### Release

All

### Resolution

.
