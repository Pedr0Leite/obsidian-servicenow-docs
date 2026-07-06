---
title: "Outbound REST Call through MID server  fails with error:   javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake_failure"
aliases:
  - KB0755198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755198
kb_number: KB0755198
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

While calling a secured REST service through a MID server running on a Linux host, the call fails and the MID server log file shows an error like this:

Worker-Expedited:MIDWorker-c045e7acdb523b80ff419809db961907 Worker starting: RESTProbe source: [https://ws.mycompany.com/api/request](https://clockworks-dev-jnt6.oit.duke.edu/provision/REQ0239844.json)  
Worker-Expedited:MIDWorker-c045e7acdb523b80ff419809db961907 WARNING \*\*\* WARNING \*\*\* javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake\_failure.

You have properly loaded the required SSL certificates in the MID server cacerts store.

# Release

* * *

Madrid Patch3, hotfix1. However it may happen in any supported release.

# Cause

* * *

This issue may happen if the Java Runtime Environment (JRE) installed in the MID server is a 32 bit word-length,  while the host operating system is a 64 bit type.

# Resolution

* * *

To check if your JRE java binary is a 32 bit or 64 bit, do the following:

For a Linux x86-64 host:

1.  In the MID server, go to the bin directory under the JRE folder located under agent folder:  ../agent/jre/bin
2.  Run the command: file java
3.  Check if the command returns something like this:
    
    java: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.9, BuildID\[sha1\]=49410ff7b4a9cea9622810efa3098b618f666337, not stripped
    
    4\. If the java binary does not return type ELF 64-bit, then you have the incorrect JRE.  

If the test shows that the installed java binary is not a 64 bit word-length binary, then:

1.  Download the correct 64 bit MID server file from your instance.
2.  Make a backup copy of your existent MID server ../agent/config.xml file and ../agent/jre/lib/security/cacerts file.
3.  Stop the MID server.
4.  Install the 64 bit MID server.
5.  Replace back the ../agent/config.xml file and ../agent/jre/lib/security/cacerts file.
6.  Restart the MID server.

## Download the MID Server files

[https://docs.servicenow.com/csh?topicname=t\_DownloadMIDServerFiles.html&version=latest](https://docs.servicenow.com/csh?topicname=t_DownloadMIDServerFiles.html&version=latest)

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: If you have custom properties added to the wrapper config files, take a backup before replace the MID server,&nbsp; and then restore them.</td></tr></tbody></table>
