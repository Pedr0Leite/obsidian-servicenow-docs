---
title: "Exclude IP addresses or IP ranges from a discovery schedule "
aliases:
  - KB0748222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748222
kb_number: KB0748222
last_modified: 2025-07-25
---

## Exclude IP addresses or IP ranges from a discovery schedule

  

### Issue

You can exclude individual IP addresses or ranges of IP addresses from a discovery schedule by following the suggestions in this article. 

### Release

All supported releases

### Resolution

1\. Sign in to the instance, and then go to **Discovery Schedules.** 

2\. Open the schedule that needs to have IP addresses excluded.

\[https://<Instancename>.service-now.com/discovery\_schedule\_list.do\]

3\. Select the **Discovery IP Ranges** tab.

![](sys_attachment.do?sys_id=6f366388470722d4b8a4aa25126d43ab)

4\. Select the preferred range.

\[https://<Instancename>.service-now.com/discovery\_range\_item\_list.do\]

5\. In the **Discovery Range Item Excludes** screen, select the **New** button.

\[https://<Instancename>.service-now.com/discovery\_range\_item\_exclude\_list.do\]

![](sys_attachment.do?sys_id=f3366388470722d4b8a4aa25126d43ae)

6\. Select the **Type** as required.

-   To exclude individual IP addresses, choose **IP Address List**
-   To exclude multiple IP addresses as a group, select **IP Address Range**
-   For an **IP Address Range**, enter the starting IP address and the ending IP address

![](sys_attachment.do?sys_id=37366388470722d4b8a4aa25126d43e2)

7\. Select **Submit** 

The next time discovery is run on the schedule, the IP addresses specified—either as individual addresses or in a range—should be excluded and not scanned.
