---
title: "How to run a Batch File on a MID Server, using a MID Server Script File and 'Command' Topic ECC Queue output"
aliases:
  - KB0754843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754843
kb_number: KB0754843
last_modified: 2025-02-14
---

## How to run a Batch File on a MID Server, using a MID Server Script File and 'Command' Topic ECC Queue output

  

### Issue

Ideally, IntergrationsHub/Orchestration Powershell/JavascriptProbe activities should be used for running scripts on a MID Server. However, this much simpler technique may be appropriate for very simple requirements.

A Batch File (.bat) can run any commands that could be run from the Windows Command-Line. This pre-dates Powershell and has been around since the early days of DOS. This procedure lets you run a batch file script, defined in the instance, on a MID Server host.

### Release

Any

### Resolution

1.  Define the Batch File  
    -   Open **MID Server -> Script Files**, and click New
    -   Attach the batch file, or enter it in the form directly, using [the normal documented method](https://docs.servicenow.com/search?q=Attach+a+script+file+to+a+MID+Server "the normal documented method").
2.  Wait for the file to be automatically synchronized to the agent\\scripts folder of all MID Servers. This should be almost instant.
3.  Script the insertion of an ecc\_queue Output record, or create one manually from a new ECC Queue record form to test:  
    -   agent ="mid.server._<MID Server's Name>_
    -   topic = Command
    -   name = scripts\\_<Batch File Name>_
    -   queue = output
    -   state = ready
    -   payload = <?xml version="1.0" encoding="UTF-8"?><parameters><parameter name="skip\_sensor" value="true"/></parameters>
4.  Look in the ECC Queue for the Input

![](sys_attachment.do?sys_id=ee9ef868dbd6c990da1999ead3961910)

![](sys_attachment.do?sys_id=aa9ef868dbd6c990da1999ead396190c)

![](sys_attachment.do?sys_id=269ef868dbd6c990da1999ead396190f)
