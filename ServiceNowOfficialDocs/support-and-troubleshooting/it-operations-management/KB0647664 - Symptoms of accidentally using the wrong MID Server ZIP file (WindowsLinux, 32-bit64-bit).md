---
title: "Symptoms of accidentally using the wrong MID Server ZIP file (Windows/Linux, 32-bit/64-bit)"
aliases:
  - KB0647664
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647664
kb_number: KB0647664
last_modified: 2026-04-23
---

## Symptoms of accidentally using the wrong MID Server ZIP file (Windows/Linux, 32-bit/64-bit)

  

### Issue

Although for a few years now only 64bit installer files are available, in the past there were both 32bit and 64bit for atime, and before that only 32bit even though 64bit operating systems had been common for years.

Symptoms of accidentally using the wrong MID Server ZIP file (Windows/Linux, 32-bit/64-bit). 

Occasionally, the wrong one of the four available MID Server installer ZIP files is accidentally downloaded. It is also possible to configure the wrapper-override.conf file to use an extenal JRE rather than the bundled one, and that could accedently be the wrong architecture.

This article describes the common symptoms and causes seen by Customer Support over the years due to installing the inappropriate build.

You installed a Linux version on Windows and the service will not start  

* * *

If you download the Linux installer and try to install it on Windows, it will appear to install and a Windows service will be created but will fail to start.

C:\\MID\_SERVERS\\j\_linux\\agent>start.bat  
C:\\MID\_SERVERS\\j\_linux\\agent>bin\\mid.bat start  
wrapper  | ServiceNow MID Server service installed.  
wrapper  | Starting the ServiceNow MID Server service...  
wrapper  | **The ServiceNow MID Server service was launched, but failed to start.**  
wrapper  | Please check the log file more information: C:\\MID\_SERVERS\\j\_linux\\agent\\logs\\wrapper.log.ROLLNUM

The wrapper log will show:

2017/10/30 18:08:56 | ServiceNow MID Server service installed.  
2017/10/30 18:08:56 | Starting the ServiceNow MID Server service...  
2017/10/30 18:08:56 | --> Wrapper Started as Service  
2017/10/30 18:08:56 | Java Service Wrapper Standard Edition 64-bit 3.5.17  
2017/10/30 18:08:56 |   Copyright (C) 1999-2012 Tanuki Software, Ltd. All Rights Reserved.  
2017/10/30 18:08:56 |     [http://wrapper.tanukisoftware.com](http://wrapper.tanukisoftware.com)  
2017/10/30 18:08:56 |   Licensed to ServiceNow, Inc. for MID  
2017/10/30 18:08:56 |   
2017/10/30 18:08:56 | **The value of wrapper.java.command does not appear to be a java binary**.  
2017/10/30 18:08:56 | The use of scripts is not supported. Trying to continue, but some features may not work correctly..  
2017/10/30 18:08:56 | Launching a JVM...  
2017/10/30 18:08:56 | Unable to execute Java command.  The system cannot find the file specified. (0x2)  
2017/10/30 18:08:56 |     "jre\\bin\\java" -Djava.util.logging.config.file=properties/glide.properties -Dsun.net.maxDatagramS.....etc.  
2017/10/30 18:08:57 |   
2017/10/30 18:08:57 | --------------------------------------------------------------------  
2017/10/30 18:08:57 | Advice:  
2017/10/30 18:08:57 | **Usually when the Wrapper fails to start the JVM process, it is**  
2017/10/30 18:08:57 | **because of a problem with the value of the configured Java command**.  
2017/10/30 18:08:57 | Currently:  
2017/10/30 18:08:57 | wrapper.java.command=jre\\bin\\java  
2017/10/30 18:08:57 | Please make sure that the PATH or any other referenced environment  
2017/10/30 18:08:57 | variables are correctly defined for the current environment.  
2017/10/30 18:08:57 | --------------------------------------------------------------------  
2017/10/30 18:08:57 |   
2017/10/30 18:08:57 | Critical error: wait for JVM process failed  
2017/10/30 18:08:58 | The ServiceNow MID Server service was launched, but failed to start.  
2017/10/30 18:08:58 | Please check the log file more information: C:\\MID\_SERVERS\\j\_linux\\agent\\logs\\wrapper.log.ROLLNUM

The problem is that although our Java application is basically the same for both Linux and Windows, the Java runtime JVM binaries are included only for Windows or Linux in the ZIP file.

You can evaluate the file type by checking the \\agent\\jre\\bin directory. A file of type File with no extension (for example, "java") indicates that the file is a Linux JVM.

**Solution**: Reinstall using the Windows ZIP file. The expected java.exe and other Windows files will be available.

You set wrapper.java.maxmemory to higher than 1024, and the service will not start  

* * *

Windows x64 operating systems are backwards compatible with 32-bit Windows programs, so you can install either 32-bit or 64-bit versions on an x64 Windows computer. A MID Server defaults to 1G Java heap size, so that isn't a problem unless you want to assign the MID Server more RAM than that.

32-bit Windows applications cannot use more than 2G RAM, which is a limitation of the processor/operating system. In reality it is a bit less, so anything approximately 1600-1800 MB being reported as available would also be an indicator.

You can increase the RAM available to the MID Server with this parameter in the /agent/conf/wrapper-override.conf file.

################################################################################  
\# System resources  
################################################################################  
\# Memory, CPU, etc. Remember to refer to < conf/wrapper.conf > for defaults.  
#  
\# OPTIONAL: Maximum Java Heap Size (in MB)  
**wrapper.java.maxmemory=4096**

Using a setting of **4096** for the 32-bit Windows version will result in the Windows service failing to start with this error:

2017/10/30 18:39:12 | Java Service Wrapper Standard Edition 64-bit 3.5.17  
2017/10/30 18:39:12 |   Copyright (C) 1999-2012 Tanuki Software, Ltd. All Rights Reserved.  
2017/10/30 18:39:12 |     [http://wrapper.tanukisoftware.com](http://wrapper.tanukisoftware.com)  
2017/10/30 18:39:12 |   Licensed to ServiceNow, Inc. for MID  
2017/10/30 18:39:12 |   
2017/10/30 18:39:12 | Launching a JVM...  
2017/10/30 18:39:13 | Error: Could not create the Java Virtual Machine.  
2017/10/30 18:39:13 | Error: A fatal exception has occurred. Program will exit.  
2017/10/30 18:39:13 | **Invalid maximum heap size: -Xmx4096m**  
2017/10/30 18:39:13 | **The specified size exceeds the maximum representable size.**  
2017/10/30 18:39:13 | JVM exited while loading the application.

With a setting of **2048**, it will fail with this error:

2017/10/30 18:43:59 | Java Service Wrapper Standard Edition 64-bit 3.5.17  
2017/10/30 18:43:59 |   Copyright (C) 1999-2012 Tanuki Software, Ltd. All Rights Reserved.  
2017/10/30 18:43:59 |     [http://wrapper.tanukisoftware.com](http://wrapper.tanukisoftware.com)  
2017/10/30 18:43:59 |   Licensed to ServiceNow, Inc. for MID  
2017/10/30 18:43:59 |   
2017/10/30 18:43:59 | Launching a JVM...  
2017/10/30 18:44:00 | Error occurred during initialization of VM  
2017/10/30 18:44:00 | **Could not reserve enough space for 2097152KB object heap**  
2017/10/30 18:44:00 | JVM exited while loading the application.

If you must use the 32-bit version, a setting of around **1600** is as high as you can expect to work.

The "Java Service Wrapper Standard Edition 64-bit" name is misleading because the wrapper will always be installed to match the computer (in this case x64) even if the MID Server application is 32 bit. These logs were for a 32-bit ZIP file install on a 64-bit Windows machine.

To find out which installation you have, within your MID Server installation folder, open the \\agent\\conf\\wrapper-jvm.conf file in a text editor:

-   "set.SNC\_JVM\_ARCH=**x86-32**" means the **32 bit** version.
-   "set.SNC\_JVM\_ARCH=**x86-64**" means the **64 bit** version.

**Solution**: Reinstall the MID Server using the 64-bit version instead.

You installed using a ZIP file newer than the instance version, and the MID Server malfunctions  

* * *

Always try to download the correct matching version from the instance on the day you install a new MID Server (for example, Jakarta Patch 6) because using a future version compared to the instance will cause the MID Server to attempt to "upgrade" to an older version. This kind of downgrade is not supported or tested, and often leads to a corrupt installation.

A MID Server will not auto-upgrade until after the instance is upgraded because web services in the instance need to be upgraded first before the MID Server on the same version can operate properly. This is why MID Servers already on later instances get into problems when they make updates to the instance via the old APIs, or are taking configurations from an instance with old versions of the APIs.

This situation can also happen if you clone an older version instance over a newer version one that already has a MID Server connected to it. To avoid this issue, retire the MID Servers from the previous incarnation of the instance before the clone and then install new ones for the new incarnation.

There are various symptoms for this issue, such as the message "Validation and Re-Key not working".

You can see whether this has happened recently in the agent log, and other side effects.

10/30/17 19:15:00 (404) StartupSequencer Current packages:  
10/30/17 19:15:00 (404) StartupSequencer   **Installed**: \[mid-core.**jakarta-05-03-2017\_\_patch4**\-09-21-2017\_10-04-2017\_1643.universal.universal.zip, mid-jre.jakarta-05-03-2017\_\_patch4-09-21-2017\_10-04-2017\_1643.windows.x86-64.zip\]  
10/30/17 19:15:00 (404) StartupSequencer   **Assigned**: \[mid-core.**helsinki-03-16-2016\_\_patch12a**\-08-25-2017\_09-12-2017\_1404.universal.universal.zip, mid-upgrade.helsinki-03-16-2016\_\_patch12a-08-25-2017\_09-12-2017\_1404.universal.universal.zip\]  
10/30/17 19:15:00 (404) StartupSequencer   Missing: \[mid-core.helsinki-03-16-2016\_\_patch12a-08-25-2017\_09-12-2017\_1404.universal.universal.zip, mid-upgrade.helsinki-03-16-2016\_\_patch12a-08-25-2017\_09-12-2017\_1404.universal.universal.zip\]  
...  
10/30/17 19:15:06 (224) StartupSequencer WARNING \*\*\* WARNING \*\*\* Can't read because table ACL is missing or **table is invalid: ecc\_agent\_router**  
...  
10/30/17 19:15:08 (080) AutoUpgrade.3600 **Setting mid status to Upgrading**

In this example, the Jakarta MID Server first expects to use a table called ecc\_agent\_router, which doesn't exist in the Helsinki version, then will set the MID Server record in the Helsinki instance to the Upgrading state, which isn't a valid value in Helsinki. Other code in a Jakarta MID Server will also go wrong when it tries to update or communicate with the pre-Jakarta instance. Things like this are what leads the MID Server installation to become corrupted.

**Solution**: Reinstall the MID Server.

You installed the 64-bit version on a 32-bit server, and the service will not start  

* * *

This installation also doesn't work, and will give errors in the Wrapper log when starting the service.

To confirm which version was installed, within your MID Server installation folder, open the \\agent\\conf\\wrapper-jvm.conf file in a text editor and if you see "set.SNC\_JVM\_ARCH=**x86-64**", it is the 64-bit version.

**Solution**: Reinstall the MID Server using the 32-bit installer.

### Release

Any. 

### Resolution

See the Issue sections for the various solutions.
