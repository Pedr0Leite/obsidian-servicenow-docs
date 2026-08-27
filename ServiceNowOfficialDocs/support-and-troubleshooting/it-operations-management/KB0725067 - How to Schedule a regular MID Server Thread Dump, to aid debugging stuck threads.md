---
title: "How to Schedule a regular MID Server Thread Dump, to aid debugging stuck threads"
aliases:
  - KB0725067
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725067
kb_number: KB0725067
last_modified: 2024-04-07
---

## How to Schedule a regular MID Server Thread Dump, to aid debugging stuck threads

  

### Issue

# Description

* * *

It is possible that threads running in MID Servers get stuck, and then block other MID Server threads such as Probes or Patterns. To aid debugging, you can schedule a regular thread dump (jstack) of the MID Server application, to help understand what is blocked or waiting for what. 

# Procedure

* * *

1.  Open a list of all MID Servers: In the navigation **MID Server -> Servers**. (ecc\_agent table)
2.  Filter the list down to only the MID Servers(s) you want Thread Dumps for. e.g. **Name Contains 'Disco'.**
3.  Add an extra condition for **Status IS Up**, so that we only send new thread dump jobs to MID Servers that are running. (we need to avoid a backlog building up)
4.  Right click the blue filter line and '**Copy query**'. This will give you the _Encoded Query String_ for this list filter that we will use in the script. **e.g. "nameLIKEdisco^status=Up"**
5.  Open a new Scheduled Script record (sysauto\_script): **System Definition -> Scheduled Jobs**, click **New**, click **Automatically run a script of your choosing**.
6.  Fill in **Name: (custom) MID Servers Thread Dump**
7.  Fill in the schedule fields. e.g. **Run: Periodically, Minutes: 10.** Pick a time when no jobs are likely to be running in your MID Servers.
8.  Paste the following script into the **Run this script** field:

// scheduled script to regularly do a MID Servers Thread Dump (KB0725067)  
var midGr = new GlideRecord('ecc\_agent');  
midGr.addEncodedQuery('**<query string goes here>**'); // You may want additional conditions to limit which MID Servers are involved.  
midGr.query();  
while(midGr.next()) {  
 var agent\_name = midGr.name.replace(/'/g, "\\\\'");  
 var midmanage = new MIDServerManage();  
 midmanage.threaddump(agent\_name); // This line writes the thread dump ecc\_queue output to the mid server.  
 gs.info('(custom) Running MID Server Thread Dump for MID Server: ' + agent\_name);  
}

1.  Paste your query string copied earlier into the addEncodedQuery function highlighted above.
2.  Submit. The script will now run on the next scheduled time.
3.  To test this script, or run it on demand, use the **Execute Now** button.
4.  You can then Grab Logs for a MID Server to see the thread dumps in the wrapper.log file.

Note: This will spam the MID Servers wrapper logs, which may have consequences for disk space, so be sure to deactivate this job once you have finished your debugging.
