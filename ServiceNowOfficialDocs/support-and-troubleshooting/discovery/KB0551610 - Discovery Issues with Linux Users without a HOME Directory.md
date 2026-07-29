---
title: "Discovery Issues with Linux Users without a HOME Directory"
aliases:
  - KB0551610
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551610
kb_number: KB0551610
last_modified: 2026-05-19
---

## Discovery Issues with Linux Users without a HOME Directory

  

### Issue

The following issues have been reported when running Discovery against Linux servers:

-   Discovery logs contain "_Cannont chdir to home dir_" warning messages
-   Linux Storage Probe fails

### Release

Any

### Cause

 

We determined that the **user account being used for Discovery on Linux servers did not have a HOME directory** configured, which was a requirement for that customer. 

<table class="noteTable" align="left"><tbody><tr><td><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td><strong>Note</strong>: This behavior was only noticed when using the default <strong>SNC SSH,&nbsp;</strong>not the Legacy SSH.</td></tr></tbody></table>

SSHCommand behavior

* * *

There are two ways to run a SSHCommand using a MID Server:

1.  Run as a command. This is normal behavior.
2.  Run in a script. This method uses SCP to copy the SSHCommand as a script file to the target host and run the script. (Probe failure is endemic of the SCP activity failing.) 

The second behavior is used when the SSHCommand is larger than the value of the MID server configuration parameter:

**mid.ssh.max\_command\_byte\_size** (by default it is = 30000).

The Linux Storage Probe Script is one of the few SSHCommand scripts that is larger than the default size of the MID Server configuration parameter:

**mid.ssh.max\_command\_byte\_size**.

This causes the issue to be flagged with that particular probe.

### Resolution

Our recommendations for this issue are as follows:

1.  Ensure that the Discovery User always has a HOME directory defined.
2.  Increase the value of the **mid.ssh.max\_command\_byte\_size** parameter MID Server configuration parameter so that the use of SCP is negated.

By default in the Fuji Release, the parameter: **mid.ssh.max\_command\_byte\_size** is not available from the drop-down Parameters - and is not available at all in earlier versions of ServiceNow. 

To set the parameter it would be necessary to do the following:

1.  Go to the table: **ecc\_agent\_property**
2.  Create a new property called: **mid.ssh.max\_command\_byte\_size** 
3.  Set the value and save the record.

Please note: Recommendation 1 is the preferred method, as SCP does not work well if a HOME directory has not been configured. The behavior of other Discovery Probes can also be affected if a HOME directory is not defined.
