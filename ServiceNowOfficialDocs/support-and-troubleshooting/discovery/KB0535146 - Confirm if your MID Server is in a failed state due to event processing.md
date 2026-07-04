---
title: "Confirm if your MID Server is in a failed state due to event processing"
aliases:
  - KB0535146
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535146
kb_number: KB0535146
last_modified: 2024-04-30
---

## Confirm if your MID Server is in a failed state due to event processing

  

### Issue

Confirm if your MID Server is in a failed state due to event processing

  
  

# Resolution

* * *

Whether it is a MID Server that is being deployed for the first time or one that has been active for a while, there may be an occasion when the MID Server record on the instance reports that the MID Server is **Down**. This article describes how to confirm that your MID Server is actually down by checking event processing.

To confirm:

1) Check that your MID Servers are showing as down in the instance.

2) Review the diagnostics page to determine if the event queue is stuck. 

![](/sys_attachment.do?sys_id=6a6efc22db0ab450e515c2230596193c)

3) If it is similar to the below screenshot with numerous events pending, then it is probably the event processing that is holding up the heartbeat probes from processing.

![](/sys_attachment.do?sys_id=e26efc22db0ab450e515c22305961946)

4) Go to the Scheduled Jobs table.

![](/sys_attachment.do?sys_id=6a6efc22db0ab450e515c2230596196a) 

5) Check the events process job and check the **State**. If it is in an error state, change it back to ready. This should allow the event process job to continue working.

![](/sys_attachment.do?sys_id=766efc22db0ab450e515c2230596197f)

6) Check the ECC queue.

![](/sys_attachment.do?sys_id=fe6efc22db0ab450e515c2230596199a)

7) Check to see if the HeartbeatProbes are getting processed or not for your respective MID Server. 

![](/sys_attachment.do?sys_id=366efc22db0ab450e515c223059619a3)

For more information, please review [MID Server Down: A Guide on How to Restore a MID Server](/kb_view.do?sysparm_article=KB0535040&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=547176f519db1dc0957b47117a9df4f26896e65737412b900be6e811583a64ac049ddee0&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0535040&sysparm_topic= "MID Server Down: A Guide on How to Restore a MID Server") and [MID Server Heartbeat](https://docs.servicenow.com/csh?topicname=r_MIDServerHeartbeat.html&version=latest "MID Server Heartbeat").
