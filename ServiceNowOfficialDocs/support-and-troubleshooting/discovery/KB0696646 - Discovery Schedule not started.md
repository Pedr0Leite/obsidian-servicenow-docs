---
title: "Discovery Schedule not started"
aliases:
  - KB0696646
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696646
kb_number: KB0696646
last_modified: 2025-09-09
---

## Discovery Schedule not started

  

### Issue

A discovery job (discovery\_schedule) has a set time to start as configured in the discovery schedule record, as well as how often to run the job. This article highlights a few things to check if the discovery is not started as expected.

### Troubleshooting Discovery Schedule Start

The discovery\_schedule table extends the sysauto\_script table which extends the sysauto table.

![](sys_attachment.do?sys_id=36d75f20dbfe0d50e515c223059619cb)

Like other scheduled jobs, there are a couple of items required to properly trigger a discovery:

1.  A sys\_trigger record that details when the job will run again
2.  A script that runs when the job is triggered

Troubleshooting:

1.  Open the sys\_trigger table and confirm that a sys\_trigger record with the same name as the discovery schedule exists.  
    -   If no matching sys\_trigger record is found, de-activate and activate the discovery\_schedule to create a sys\_trigger.
2.  Open the discovery\_schedule record and confirm the discovery\_schedule.script field is properly populated, compare to a discovery schedule which starts successfully.  
    -   If the script is missing, copy the script from the original discovery\_schedule record. This issue is only seen when the discovery is imported.
3.  Check if there are IP Ranges which could cause issues such as and update the Ranges accordingly:  
    -   Remove IP Ranges for /31 or /32 subnets. These are not valid ranges for discovery.
    -   IP Ranges for subnets which are too large (/16, /15, /13) may need to be split into smaller IP Ranges.
4.  Check the syslog table for any errors at the time the discovery was supposed to start.
5.  Compare the discovery\_schedule record xml from a discovery schedule which begins successfully to one that does not.

### Related Links

The following articles provide information regarding other topics in discovery schedules:

-   [How to investigate a canceled Discovery "because max run time window has been exceeded"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0676340 "How to investigate a cancelled Discovery \"because max run time window has been exceeded\"")
-   [Discovery Cancellation Process Overview](https://support.servicenow.com/kb_view.do?sysparm_article=KB0695928 "Discovery Cancellation Process Overview")
