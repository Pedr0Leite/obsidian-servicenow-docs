---
title: "Get thread dump and heap dump for MID Server"
aliases:
  - KB0656229
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656229
kb_number: KB0656229
last_modified: 2026-05-12
---

## Get thread dump and heap dump for MID Server

  

### Issue

On rare occasions when a MID Server cannot or is slow to pick up messages from the instance, you would like to get a thread dump to troubleshoot. This article describes how to do so. Note that you need to have login access to the MID Server.

### Release

All currently supported releases.

### Resolution

# How to get thread dump and heap dump

1.  ServiceNow's OpenJDK bundled with MID Servers include jstack and jmap in the agent\\jre\\bin folder.  
      
    
2.  (If gathering thread dump) Download and unzip PSTools: [https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx "https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx"). You might not have to do this but PsExec is needed to invoke jstack.exe on a process that is run as Local System, this used to be the default but now MID Servers are often running as a non-admin service account when the MID Server is run as a Windows service.  
      
    
3.  Open Task Manager. In 'Processes' tab, sort by Image Name then find 'java.exe' processes. Note the process ID under 'PID' column. If 'PID' column is not shown, goto View > Select Column... and select 'PID' column.
    
    ![](/sys_attachment.do?sys_id=038110b197f8cf5068d477121153aff9)
    
4.  if multiple MID Servers are running, right click each 'java.exe' process then select Properties, to verify correct MID Server process.
    
     ![](/sys_attachment.do?sys_id=07811c7197f8cf5068d477121153af3d)
    
5.  (If gathering thread dump) Open Command Prompt as Administrator change to directory where PSTools is unzipped in step 2. Run the following command if MID Server service account is 'SYSTEM':
    
    psexec -s "<path\_to\_jdk\_install>\\bin\\jstack" -l PID\_HERE >> <path\_for\_generated\_file>\\threadDump.txt
    
    if MID Server service account is a user:
    
    psexec -u <username> "<path\_to\_jdk\_install>\\bin\\jstack" -l PID\_HERE >> <path\_for\_generated\_file>\\threadDump.txt
    
6.  (If gathering heap dump) Run this command:
    
    <path\_to\_jdk\_install>\\bin\\jmap -dump:file=<path\_for\_generated\_file>\\heapDump.bin PID\_HERE
    
7.  Alternately, to dump the heap automatically on out-of-memory exception, modify the wrapper-override.conf file found in the /agent/conf/ directory by adding the following:

        "wrapper.app.additional.501=-XX:+HeapDumpOnOutOfMemoryError" OR "wrapper.java.additional.501=-XX:+HeapDumpOnOutOfMemoryError". 

             **\*\*\*WARNING:** This parameter should only be used for short term with active monitoring. As soon as OOM is reproduced and Heapdump is generated, the parameter must be removed. Leaving this parameter in place for extended period can potentially exhaust disk space.

             There should be no duplicates in either /agent/conf/wrapper.conf or /agent/conf/wrapper-override.conf files.       

             Here is an example:

             ![](sys_attachment.do?sys_id=0f8110b197f8cf5068d477121153affd)

# References

[jmap - Memory Map](http://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html "How to use jmap?") – How to use jmap

[jstack - Stack Trace](http://docs.oracle.com/javase/7/docs/technotes/tools/share/jstack.html "How to use jstack?") – How to use jstack

### Related Links

[KB0717248 How to automatically generate the heap dump from Mid when JVM runs out of memory](https://support.servicenow.com/kb_view.do?sysparm_article=KB0717248 "KB0717248 How to automatically generate the heap dump from Mid when JVM runs out of memory")

[KB0746066 How to analyse a MID Server Heap Dump, for High Memory usage](https://support.servicenow.com/kb_view.do?sysparm_article=KB0746066 "KB0746066 How to analyse a MID Server Heap Dump, for High Memory usage")
