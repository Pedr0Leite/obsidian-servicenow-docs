---
title: "Service Mapping Error: \"Process detection failed: Check that the process is running on the host\"
aliases:
  - KB0727847
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727847
kb_number: KB0727847
last_modified: 2026-06-10
---

## Issue

During ServiceMapping the instance logs the error:

"Process detection failed: Check that the process is running on the host, verify the CI has a running processes \[sic\] on this port, and check the process strategy for the pattern's section is correct."

## Resolution

1.  For the failed node on the Service Map, look at the discovery pattern log.
2.  In the Process detection section that run initially see the commands that are being attempted.
3.  Insure that the commands there are returning the expected result and not failing.

### Example

On a Linux Host, the process detection on the discovery pattern log:

\===========================================

Executing SSH command: ps -eo user,pid,ppid,comm,args | grep -i '\[PID\_USED\]' | grep -v grep  
  
Executing SSH command: command -v sudo  
  
Command result: /usr/bin/sudo  
  
Command result:  
12332 12827 sleep sleep 1  
12827 1 sitter.bash /bin/bash /usr/\[SOME\_PATH\]  
  
Executing SSH command as superuser: ls -l /proc/\[PID\]/exe  
  
Host \[IP\_ADDRESS\] requested password while running command with sudo (or other privileged command), but no password is available when using SSH key. Configure sudo not to prompt for password  
  
Sending CTRL-C to abort command  
  
Failed to find process on port. Invalid SSH credentials for host 10.215.106.53. Host required password, but no password was available. Verify that proper credentials are defined.

\===========================================

We can see above that command "ls -l /proc/\[PID\]/exe" fails. 

That credential needs to have permission to run this command against the host linux server. Once the command is allow-listed, this should work properly. 

**Note:** Even though you allow-list this command, on the next run the next command for process detection may fail with the same issue. At that time, you will need to allow-list that next command as well. 

## Additional Information

[PRB1547409 Pattern Debugger fails with error 'Test failed: Failed to execute task, PatternDebuggerTask, with failure message: null'](https://support.servicenow.com/kb_view.do?sysparm_article=KB1123732 "Pattern Debugger fails with error 'Test failed: Failed to execute task, PatternDebuggerTask, with failure message: null'")

[Debugging  customized pattern will throw "Process detection failed" Error](https://support.servicenow.com/kb_view.do?sysparm_article=KB0760308 "Debugging  customized pattern will throw \"Process detection failed\" Error")
