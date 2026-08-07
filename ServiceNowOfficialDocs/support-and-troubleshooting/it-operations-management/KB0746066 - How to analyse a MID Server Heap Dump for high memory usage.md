---
title: "How to analyse a MID Server Heap Dump for high memory usage"
aliases:
  - KB0746066
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746066
kb_number: KB0746066
last_modified: 2026-05-12
---

## How to analyse a MID Server Heap Dump for high memory usage

  

### Issue

There is no way from the MID Server application logs or Thread dumps to see how much memory each thread is currently using. We only monitor the overall memory usage. For per-thread you need a Java Heap Dump for the MID Server application's JVM, and then that needs analysing.

This KB aims to show a way of doing this with the JDK tools, and one simple way to analyse the heap dump using Eclipse and Memory Analyzer, so you can identify the specific Probe(s) that are causing problems.

### Release

Any, as the MID Server application has always been Java based, although each major version of the platform tends to use a different Java version, which may affect which 3rd party tools need using.

### Resolution

You will need 3 bits of 3rd party software:

-   Java JDK, which includes the jtrace tool.  The bundled JRE includes jstack and jmap, but not jtrace.  
    e.g. [Microsoft's build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/download) . Use the same version as the one bundled with the MID Server - See [KB0719830 MID Server Java runtime - Information on Bundled and Compatible versions, Upgrading or Replacing](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719830).
-   Eclipse  
    e.g. Eclipse IDE for Java Developers, see [Download Eclipse](https://www.eclipse.org/downloads/)
-   Memory Analyser plugin for Eclipse  
    e.g. [Memory Analyzer](https://eclipse.dev/mat/) from the Eclipse Marketplace, after installing Eclipse

## Install JDK and get a Heap Dump of your running MID Server

The JDK is required if you are creating a Heap Dump On-Demand. This step is already covered in [KB0656229 Get thread dump and heap dump for MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0656229 "KB0656229 Get thread dump and heap dump for MID Server").

A method of creating a Heap Dump at the moment a MID Server goes out-of-memory, without the JDK, is explained in [KB0717248 How to automatically generate the heap dump from Mid when JVM runs out of memory?](https://support.servicenow.com/kb_view.do?sysparm_article=KB0717248 "KB0717248 How to automatically generate the heap dump from Mid when JVM runs out of memory?")

## Install Eclipse and Memory Analyzer and load the Heap Dump

1.  **Install Eclipse** in the normal way.
2.  A Heap Dump can be very large, up to 1GB by default, or whatever the wraper-override.conf wrapper.java.maxmemory parameter has been increased to. **Eclipse will need more system memory allocated to it** in order to load large heap dumps.  
    Open the eclipse.ini file, which is located in the Eclipse install folder. These changes will increase the Memory available to Eclipse, to e.g. 8GB / 8192m, assuming your computer physically has it to give:  
    Edit these lines:  
    
    \-Xms512m
    -Xmx**8192m**
    
    Add these lines:  
    
    \-XX:PermSize=256m
    -XX:MaxPermSize=512m
    
3.  **Run Eclipse**, and create a Workspace
4.  In the menus select **Help - Eclipse Marketplace**, and then search for **Memory Analyser** and install it.
5.  After Eclipse has restarted, In the menus select **Window - Perspective - Open Perspective - Other, and select Memory Analyser**
6.  In the menus select File - Open Heap Dump, and select your Heap Dump file created earlier. This will take a while to parse.

## Analyse the Heap Dump

Once the heap dump has Parsed. an Overview is shown giving a total memory in use, and a pie chart will be shown which already may allow high memory threads to be identified. This is quite useful in itself.

![](sys_attachment.do?sys_id=46111c399778cf5068d477121153af1f)

1.  Wait for parsing to finish
2.  In the Getting Started popup, select Leak Suspects Report, click Finish. The Leak Suspects Report will start generating in the background, and eventually appear as a new tab.
3.  In the meantime, From the Actions list of the Overview tab, select Dominator Tree. This gives a list of objects and their memory usage, with the worst one at the top.
4.  Expand the high memory objects until you get down to something that is interesting:
    -   It may be a function name that relates to a ServiceNow feature or Probe that gives a clue to what code is running and what it is doing
    -   It will usually be when you find a large array of objects, which in total add up to a lot of memory. These arrays will usually be of discovered data from a target, or lists of IP Ranges, or CMDB CIs.

In this screenshot we find we have a single Azure probe using 1.5GB or RAM, just for that probe, which is a huge over usage of MID Server memory for a Discovery Probe, and almost certainly a existing or new known problem that needs fixing in the product.

![](sys_attachment.do?sys_id=ce11d8399778cf5068d477121153afb5)

The next step may be to open a Support Case in HI, if a search of the Known Error articles in the Knowledge Base do not come up with a cause.

### Related Links

These tools are all 3rd party open source software, with plenty of much more detailed documentation on the web, together with many ways of using it.
