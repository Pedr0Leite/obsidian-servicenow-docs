---
title: "Resolving the \"MID Server with a duplicate name or sys_id was prevented from connecting\" issue"
aliases:
  - KB0743043
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743043
kb_number: KB0743043
last_modified: 2025-12-09
---

## Resolving the "MID Server with a duplicate name or sys\_id was prevented from connecting" issue

  

### Issue

In the MID Server Issues table \[ecc\_agent\_issue\], you may have a record stating:

A MID Server with a duplicate name or sys\_id was prevented from connecting. Install path: C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent. This issue must be manually resolved.

You may also see this: 

The home directory changed from C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent to C:\\MID\_SERVER\\Prod\_Disco\_MID - Copy\\agent. This issue must be manually resolved.

Other Symptoms may include:

-   **2 inputs returned for each output** in the ECC Queue, including when Grabbing Logs
-   Agent log reports one of  
    -   SEVERE \*\*\* ERROR \*\*\* **Failed to rename ECC enqueued item** from ecc\_queue.<number>.tmp to ecc\_queue.<number>.xml
    -   StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[**An active MID Server with a duplicate name detected.**\] in ensuring agent record on the instance."
    -   **ECCSender.1 SEVERE \*\*\* ERROR \*\*\* Comparison method violates its general contract!**
-   Multiple threads listed when only 1 would be expected e.g. for 2x "ECCSender.1"

### Release

All

### Cause

* * *

**Each MID Server installation _must_ have a unique Name and sys\_id.** In the ECC Queue they are referenced by Name, and in most other places by sys\_id.

It is possible that this rule is broken, when either installations folders are copied, or a second service is created for the same folder:

1.  An existing MID Server install folder is copied to another host server, and started on that server too.
2.  An existing MID Server install folder is copied to another folder on the same host server, and then started.
3.  An existing MID Server install folder has more than 1 Windows Service pointing to it and running for it

![](sys_attachment.do?sys_id=7d7b2bcc4771f290f64de825126d4383)

In all cases the same MID Server Name and Sys ID parameters are used, because identical config.xml files are used.

-   Cases 1 and 2 are usually due to manually copying MID Server installations as a short cut for installing additional MID Servers.  
-   Case 1 has also been seen when a server fail-over arrangement accidentally has both hosts live at the same time. This would be resolved by ensuring one host goes offline when the other goes live.
-   Case 2 requires copying the folder and then modifying the windows service names in the copied wrapper-override.conf in order for a second service to be installed. 
-   Case 3 requires that the windows service names in wrapper-override.conf were modified and then running starts.bat again, or running start.bat before installer.bat. See:  
    [PRB1330396/KB0743123 MID Server start.bat fails to check if a Windows Service already exists for the installation folder before creating another service](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743123)   
    [PRB1380840/KB0792539 MID Server start.bat will create a "snc\_mid" Windows Service without checking that the installer has been run yet, while the config.xml/wrapper-override.conf files still have nonsensible values, leading to duplicate services for the same install folder](https://support.servicenow.com/kb_view.do?sysparm_article=KB0792539 "MID Server start.bat will create a \"snc_mid\" Windows Service without checking that the installer has been run yet, while the config.xml/wrapper-override.conf files still have nonsensible values, leading to duplicate services for the same install folder")

### Resolution

## Table of Contents

-   [The investigation](#mcetoc_1jc190p1dl9)
-   [The Repair Process](#mcetoc_1jc190p1dla)

## The investigation

### An existing MID Server install folder is copied to another host server

The MID Server form will show one of the host servers involved. To figure out what the other is, we can use the XML Stats inputs, that each installation will send to the instance every 10 minutes:

1.  Open **ECC -> Queue** for a list of the ECC Queue \[ecc\_queue\] table
2.  Filter on  
    -   **Topic IS queue.stats**
    -   **Agent IS mid.server.<MID Server name>**
3.  Group by **Source**
4.  You should now see this list grouped by each host-name that has a duplicate MID Server installed.

You now know which host servers need investigating. The following sections will be useful in finding the folder and service on that other host.

### An existing MID Server install folder is copied to another folder on the same host server

If you also had an Issue record for "The home directory changed ..." then that will give a good clue as to what the relevant install folders are. If not:-

1.  Open a **Command Prompt** as a local administrator
2.  Run:  
    
    **wmic service get | findstr /c:"\\conf\\wrapper.conf" /c:"DisplayName"**
    

That would output something along the lines of this (although for clarity I've deleted most columns and re-ordered this a bit): 

DisplayName                              Name                        StartMode  State    PathName                                                                                                                                                                                                            
ServiceNow MID Server\_Prod\_Disco\_MID     snc\_mid\_Prod Disco MID      Auto       **Running C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent**\\bin\\wrapper-windows-x86-64.exe -s C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent\\conf\\wrapper.conf wrapper.console.flush=true wrapper.internal.namedpipe=1065211260                    
ServiceNow MID Server                    **snc\_mid**                     Auto       **Running "C:\\MID\_SERVER\\Prod\_Disco\_MID - Copy\\agent**\\bin\\wrapper-windows-x86-64.exe" -s "C:\\MID\_SERVER\\Prod\_Disco\_MID - Copy\\agent\\conf\\wrapper.conf" wrapper.console.flush\=true wrapper.internal.namedpipe\=0356311188  

Or you could also create an ecc\_queue output record to run a "Command" topic job for the same command, to fetch the same info via the instance.

-   DisplayName - The name listed in the MMC/Control panel Services list
-   Name - The actual service name
-   StartMode - How the service is started. Auto means it would run when the host server is turned on.
-   State - Running/Stopped
-   PathName - Where it is installed

### An existing MID Server install folder has more than 1 Windows Service pointing to it

This case would be similar to the above, but the install folder is identical for 2 services:

DisplayName                                        Name                       StartMode  State    PathName                                                                                                                                                                                                            
ServiceNow MID Server\_Prod\_Disco\_MID MID1       snc\_mid\_Prod Disco MID     Auto       **Running  C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent**\\bin\\wrapper-windows-x86-64.exe -s C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent\\conf\\wrapper.conf wrapper.console.flush=true wrapper.internal.namedpipe=1065211260                    
ServiceNow MID Server\_Prod\_Disco\_MID MID1xxx    **snc\_mid**                    Auto       **Running  C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent**\\bin\\wrapper-windows-x86-64.exe -s C:\\MID\_SERVER\\Prod\_Disco\_MID\\agent\\conf\\wrapper.conf wrapper.console.flush=true wrapper.internal.namedpipe=0258404434                    

In this case you need to now check the \\agent\\conf\\wrapper-override.conf file to check which is the correct service name. e.g.

################################################################################  
\# Windows Service  
################################################################################  
\# The following properties must be unique per MID installed on the same system.  
#  
\# REQUIRED: Name token of the service  
wrapper.name=**snc\_mid\_Prod Disco MID**  
\# REQUIRED: Display name of the service  
wrapper.displayname=**ServiceNow MID Server\_Prod Disco MID**

The other service name is the duplicate.

### An existing MID Server install folder has more than 1 Linux Process running for it

Discovery uses this command on Linux hosts to see what processes are running, and so the same command can be used to check for this:

ps awwxo pid,ppid,command | sed -n '/<defunct>/!p' 

And the output should only include a java process and a wrapper process per MID Server agent folder. This example shows 3 pairs:

12225      1 /var/opt/mid/1d/agent/bin/./wrapper-linux-x86-64 /var/opt/mid/1d/agent/bin/../conf/wrapper.conf wrapper.syslog.ident=mid wrapper.pidfi...
12311  12225 /var/opt/mid/1d/agent/jre/bin/java -Djava.util.logging.config.file=properties/glide.properties -Dsun.net.maxDatagramSockets=65535 -Dco...
28126      1 /var/opt/mid/1d/agent/bin/./wrapper-linux-x86-64 /var/opt/mid/1d/agent/bin/../conf/wrapper.conf wrapper.syslog.ident=mid wrapper.pidfi...
28140  28126 /var/opt/mid/1d/agent/jre/bin/java -Djava.util.logging.config.file=properties/glide.properties -Dsun.net.maxDatagramSockets=65535 -Dco...
33456      1 /var/opt/mid/1d/agent/bin/./wrapper-linux-x86-64 /var/opt/mid/1d/agent/bin/../conf/wrapper.conf wrapper.syslog.ident=mid wrapper.pidfi...
33569  33456 /var/opt/mid/1d/agent/jre/bin/java -Djava.util.logging.config.file=properties/glide.properties -Dsun.net.maxDatagramSockets=65535 -Dco...

## The Repair Process

By now you will have the service names, and the install folders mapped out, and know which one you are keeping, and which needs deleting.

1.  Open a **Command Prompt** as a local administrator
2.  Stop the duplicate service with this command:  
    
    **net stop <name>  
    e.g. net stop "snc\_mid\_Prod\_Disco\_MID MID1xxx"**
    
3.  Delete the Service with this command:  
    
    **sc delete <name>  
    e.g. sc delete "snc\_mid\_Prod\_Disco\_MID MID1xxx"**
    
4.  Where 2 folders exist for the same MID Server, Archive and then Delete the install folder, to prevent similar problems in future. Warning: If someone were to accidentally run start.bat from a backup/copy folder, PRB1330396 means you may be back to square one.
5.  I recommend also Stopping and the Starting the windows service of the MID Server that is being kept, to check it is still functioning correctly, and will pick up any older ecc\_queue outputs.

For Linux servers, a similar thing needs doing.
