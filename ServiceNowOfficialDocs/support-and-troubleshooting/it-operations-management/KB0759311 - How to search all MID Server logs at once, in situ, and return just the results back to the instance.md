---
title: "How to search all MID Server logs at once, in situ, and return just the results back to the instance"
aliases:
  - KB0759311
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759311
kb_number: KB0759311
last_modified: 2024-04-07
---

## How to search all MID Server logs at once, in situ, and return just the results back to the instance

  

### Issue

MID Server logs are rotated every 10MB, and for the agent logs there are 10 of them. Without downloading them all, you can't know the date cut-offs and so can't know which file you want.

This trick avoids doing that, by getting the MID Server to search all its logs itself for a string you are looking for. e.g.

-   The sys\_id of a specific ECC Queue output record, to find the agent log entries for the thread that ran it
-   An error message, to see if it has occurred before
-   All "LogStatusMonitor" entries, to get e.g. a full record of memory usage

### Resolution

 The basic idea is to use the "Command" probe to run "find" on the logs folder, to return any lines in any file that contain the string.

1.  Open a new blank ECC Queue record form - /ecc\_queue.do
2.  Fill in the fields like so:
    -   Agent = mid.server.<MID Server name>
    -   Topic = Command
    -   Name = **FIND "<search string>" logs\\\*.\***
    -   Queue = Output
    -   State = Ready
    -   Sequence = (clear this value)
3.  Submit
4.  Look in the ECC Queue table for the Input response from that output. The output from the commands will be in the Payload.  
    /ecc\_queue\_list.do?sysparm\_query=topic%3dCommand

For Linux MID Servers, a similar search can be run with grep.

Example:

The following is the output from searching for a specific ecc\_queue output record sys\_id "f3b7c62f1b937b840c50524d6e4bcb5f". In this case it was a Discovery SNMP probe, but the logs from any feature or probe could be searched in the same way, because the thread name will always include the output sys\_id.

![](sys_attachment.do?sys_id=22bb04f8db08b0d0fec4fb24399619ec)
