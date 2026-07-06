---
title: "How to see which Threads were running in a MID Server at a recent point in time"
aliases:
  - KB0693277
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693277
kb_number: KB0693277
last_modified: 2025-11-14
---

## How to see which Threads were running in a MID Server at a recent point in time

  

### Issue

The MID Server form has a related list of Threads currently running in the MID Server. If you had a performance problem a few days ago and have since restarted the MID Server, this will not be any use for knowing what the MID Server was doing at the time.

The data for that list is sent by the MID Servers every 10 minutes, and those ecc\_queue records remain in the table for 4-5 days, so the data may still be there.

  

#   

### Resolution

1.  Open the ECC Queue: **MID Server - ECC Queue**
2.  **Set the list filter** for the records you are interested in:  
    -   **Agent** IS **mid.server.<_MID Server you are interested in_\>**
    -   **Name** IS **MID Server XMLStats**
3.  Find the record created shortly before the time you are interested in, and open it
4.  Open the **XML of the Payload**. 
5.  Scroll down and you will see a **<threads>** section, something like this:

 ![](sys_attachment.do?sys_id=fcba6ca6db42b450e515c22305961910)

  

Normal jobs, including Discovery probes, will run in the "Worker-Standard" thread pool. There will be one entry for each of the number of threads you have set in the MID Server parameter.   
"Worker-Standard:Idle" means the thread is free and not running anything.

You may see things running e.g. "Worker-Standard:JDBCProbe", where _JDBCProbe_ is the probe type, and will match the value of the 'Topic' field of the ECC Queue output record for that job.
