---
title: "How to Schedule a regular Restart of a MID Server, to clear recurring Stuck Threads, Memory leaks, Buffers or Handles"
aliases:
  - KB0692080
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692080
kb_number: KB0692080
last_modified: 2025-01-03
---

## How to Schedule a regular Restart of a MID Server, to clear recurring Stuck Threads, Memory leaks, Buffers or Handles

  

### Issue

It is possible that jobs running in MID Servers get stuck, and then block one of the worker threads, eventually leading to a MID Server with no threads left available to run anything. This can happen due to poor design of custom JavascriptProbe jobs, or there have been some product defects that also leave stuck threads behind after the job has finished.

Memory and Handle leaks can also be caused by known problems, eventually making the MID Server unusable, or appear Down even though the service is still running.

A MID Sever restart clears stuck threads, and leaked memory and handles. Until your causes of stuck threads are fixed, one possible workaround is to have a scheduled script run periodically to tell the MID Server(s) to restart themselves.

### Resolution

1.  Open a list of all MID Servers: In the navigation **MID Server -> Servers**. (ecc\_agent table)
2.  Filter the list down to only the MID Servers(s) you need to be restarting. e.g. **Name Contains 'Disco'.**
3.  Add an extra condition for **Status IS Up**, so that we only restart MID Servers that are running.
4.  Right click the blue filter line and '**Copy query**'. This will give you the _Encoded Query String_ for this list filter that we will use in the script. **e.g. "nameLIKEdisco^status=Up"**  
      
    ![](sys_attachment.do?sys_id=df79a022db42b450e515c223059619fe)  
      
    
5.  Open a new Scheduled Script record (sysauto\_script): **System Definition -> Scheduled Jobs**, click **New**, click **Automatically run a script of your choosing**.
6.  Fill in ****Name: (custom) Restart MID Servers to clear stuck threads****
7.  Fill in the schedule fields. e.g. **Run: Weekly, Day: Sunday, Time: 07:00:00.** Pick a time when no jobs are likely to be running in your MID Servers.
8.  Paste the following script into the **Run this script** field:  
      
    
    // scheduled script to regularly restart MID Servers to clear out stuck threads (KB0692080)
    var midGr \= new GlideRecord('ecc\_agent');
    midGr.addEncodedQuery('**<paste query string here>**'); // This query string limits which MID Servers are restarted.
    midGr.query();
    while(midGr.next()) {
    	var agent\_name \= midGr.name.replace(/'/g, "\\\\'");
    	var midmanage \= new MIDServerManage();
    	midmanage.restartService(agent\_name); // This line writes the restart ecc\_queue output to the mid server.
    	gs.info('(custom) Restart MID Servers to clear stuck threads job: Restarting MID Server: ' + agent\_name);
    }
    
9.  Paste your query string copied earlier into the addEncodedQuery function highlighted above. The line will then look like e.g.  
      
    
    midGr.addEncodedQuery('**nameLIKEdisco^status=Up'**); // This query string limits which MID Servers are restarted.
    
      
    
10.  **Submit**. The script will now run on the next scheduled time.
11.  To test this script, or run it on demand, use the **Execute Now** button. 

### Related Links

[KB0832784 / PRB1414364 After upgrading to Orlando Patch 5, SNMP Discovery causes a File Handler leak, leaving MID Servers unstable or Down](https://support.servicenow.com/kb_view.do?sysparm_article=KB0832784 "KB0832784 / PRB1414364 After upgrading to Orlando Patch 5, SNMP Discovery causes a File Handler leak, leaving MID Servers unstable or Down")
