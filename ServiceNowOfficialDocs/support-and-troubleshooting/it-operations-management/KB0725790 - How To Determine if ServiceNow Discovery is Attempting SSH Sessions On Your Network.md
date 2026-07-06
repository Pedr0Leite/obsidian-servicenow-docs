---
title: "How To Determine if ServiceNow Discovery is Attempting SSH Sessions On Your Network "
aliases:
  - KB0725790
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725790
kb_number: KB0725790
last_modified: 2024-04-07
---

## How To Determine if ServiceNow Discovery is Attempting SSH Sessions On Your Network

  

### Issue

# Description

* * *

ServiceNow can use SSH as part of the discovery process. From time to time customer's network security teams notice failed SSH login attempts as part of their daily network monitoring job. In some cases too many failed SSH login attempts can create network outages. The network team might reach out to the ServiceNow Admin with the belief that ServiceNow is attempting too many logins. The network team may provide a list of IPs that are attempting SSH logins. The ServiceNow Admin would then create a ServiceNow incident/case in which they believe the ServiceNow MID Servers configured for Discovery are creating this issue and request a root/possible cause analysis (RCA/RCA). The following is a procedure to check if your MID Servers are the culprit of SSH login attempts.

# Procedure

* * *

**Go to the list of your MID Servers** [https://YOUR\_INSTANCE.service-now.com/ecc\_agent\_list.do](https://YOUR_INSTANCE.service-now.com/ecc_agent_list.do "https://YOUR_INSTANCE.service-now.com/ecc_agent_list.do")

**Click the cog wheel (gear icon in blue) and move IP Address from the "Available" left pane to the "Selected" right pane and click OK.**

![](sys_attachment.do?sys_id=655968eedb02b450e515c223059619d4)

![](sys_attachment.do?sys_id=e55968eedb02b450e515c223059619d9)

**Right click IP Address and select "Group by IP address"**

![](sys_attachment.do?sys_id=295968eedb02b450e515c223059619de)

**At this point you should see a list like this with all your MID Server's IP addresses.**

![](sys_attachment.do?sys_id=695968eedb02b450e515c223059619e3)

**You can use these IP addresses to cross reference the network security team's list of IPs attempting too many SSH logins.**
