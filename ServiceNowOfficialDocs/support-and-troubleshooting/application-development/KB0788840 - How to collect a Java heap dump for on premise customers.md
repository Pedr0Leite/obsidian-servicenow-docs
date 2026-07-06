---
title: "How to collect a Java heap dump for on premise customers"
aliases:
  - KB0788840
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788840
kb_number: KB0788840
last_modified: 2023-09-08
---

## Issue

In order to collect a heap-dump please follow these steps:

1\. **ssh** to the affected node  
  
2\. identify the Java PID and save it:  
**ps -ef | grep -v grep | grep java | grep <node\_name>**

3\. run jmap using the Java PID:  
**jmap -F -dump:live,format=b,file=<path\_to\_file/heap\_dump>.bin <PID>**

**Other method if above not working**

$ /glide/java/bin/jhsdb jmap --pid <java process ID> --dumpfile <dump file name> --binaryheap  
  
If this doesn't work, try either of the following:  
  
\- Use jcmd  
$ /glide/java/bin/jcmd <java process ID> GC.heap\_dump -all <dump file name>  
  
\- Use gcore to create a process dump, and then use jhsdb jmap to dump heap  
$ gcore <java process ID>  
$ /glide/java/bin/jhsdb jmap --core <generated core file> --binaryheap --dumpfile <dump file name> --exe /glide/java/bin/java
