---
title: "Discovery Cancellation Process Overview"
aliases:
  - KB0695928
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695928
kb_number: KB0695928
last_modified: 2025-09-09
---

## Discovery Cancellation Process Overview

  

### Issue

A discovery schedule can be configured to have a "max run time". The discovery will be automatically cancelled if this max run time is reached.

### Discovery Cancellation Process Overview

A couple of important script includes are called when a discovery is created:

-   Discovery
-   StartDiscovery

StartDiscovery creates a scheduled job(sys\_trigger record) to cancel the discovery. The following is an example scheduled job created to cancel a discovery:

![](sys_attachment.do?sys_id=983fb426db0ab450e515c2230596195f)

The scripts will also log to "System Logs" that the discovery will be cancelled and at what time:

![](sys_attachment.do?sys_id=9c3fb426db0ab450e515c22305961964)

### Troubleshooting

If the discovery is not cancelled as expected, the following can be done for troubleshooting.

1.  Check that script includes Discovery and StartDiscovery are OOB.
2.  Check that the cancellation scheduled jobs are being created as expected, a test discovery can be run to confirm this.
3.  Search the "System Logs > System Log > All" for "Cancelling Discovery <discovery\_status\_number>" (replace with the actual discovery number).  
    -   If the "Cancelling Discovery ..." message is found, then the mechanism to cancel the discovery was successful.
4.  Check that there were no performance issues at the time the discovery should have been cancelled and that the workers were not behind (unlikely to happen).

### Related Links

Related to this topic:

-   [How to troubleshoot a cancelled Discovery in case of max run time window has been exceeded](https://support.servicenow.com/kb_view.do?sysparm_article=KB0676340 "How to troubleshoot a cancelled Discovery in case of max run time window has been exceeded")
