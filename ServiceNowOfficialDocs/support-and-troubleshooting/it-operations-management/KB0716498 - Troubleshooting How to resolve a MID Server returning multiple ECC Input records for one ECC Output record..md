---
title: "Troubleshooting: How to resolve a MID Server returning multiple ECC Input records for one ECC Output record. "
aliases:
  - KB0716498
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716498
kb_number: KB0716498
last_modified: 2024-04-07
---

## Troubleshooting: How to resolve a MID Server returning multiple ECC Input records for one ECC Output record.

  

### Issue

Symptoms

There may be times where you have strange behaviour when running any operation that utilises a MID Server. This can be characterised by double updates to records, Discovery not functioning correctly, or unexplained high CPU utilisation on a MID Server host. 

Possible Cause

This can be caused by multiple java.exe processes running under the context of the 'same' MID Server. 

To identify the issue, you can navigate to the MID Server record on the instance, and run a 'Grab logs'. If you get two sets of agent.log and wrapper.log ECC Inputs come back for one Grab Log, this is definitely the cause. 

_Example Grab log:_ 

![](sys_attachment.do?sys_id=36db24eadb42b450e515c223059619bc)

Remediation

If you see this, open Task manager and check that there are multiple java.exe running. If so:

-   Firstly restart the MID Server host. Sometimes when restarting a MID Server service, the old service fails to shut down properly, leaving a ghost java.exe process. This is easily resolvable by restarting the MID Server host.
-   After restarting, check in the Windows Services panel, and scroll down to "ServiceNow MID Server" xxxxx.
    -   Check if there are multiple MID Server Services running, if so, see which two run from the same folder/file. Then set one to Startup type = disabled, then right click and stop one service.

This should ensure that only one MID Server service is running for one MID Server record. To verify the fix, you can do another Grab log on the MID Server record to ensure that only one set of logs are returned.
