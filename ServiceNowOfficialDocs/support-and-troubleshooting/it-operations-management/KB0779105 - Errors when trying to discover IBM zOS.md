---
title: "Errors when trying to discover IBM zOS"
aliases:
  - KB0779105
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779105
kb_number: KB0779105
last_modified: 2024-04-08
---

## Errors when trying to discover IBM zOS

  

### Issue

When trying to discover our IBM systems (IBM zOS) customer is getting some errors during the horizontal pattern phase of discovery. 

### Cause

1) From the IBM zOS pattern, it seems to fail at this step:

\- **set version and os type**  
2019-09-05 13:12:47: Executing SSH command: echo "/\*rexx \*/ \\n Say 'Operating system level:' MVSVAR('SYSOPSYS')\\n" > /tmp/ver.rx;chmod 755 /tmp/ver.rx; /tmp/ver.rx ;rm -f /tmp/ver.rx  
2019-09-05 13:12:47: Executing SSH command: command -v sudo  
2019-09-05 13:13:06: Command result:  
2019-09-05 13:13:06: Command failed with status 1  
2019-09-05 13:13:06: Command result:  
/tmp/ver.rx: FSUM7725 history: EDC5000I No error occurred.  
Operating system level: z/OS 02.02.00 HBB77A0  
2019-09-05 13:13:06: setAttribute(ci,\[{osType=EDC5000I, osVersion=No}, {osType=z/OS, osVersion=02.02.00}\])  
2019-09-05 13:13:06: setAttribute(osType,EDC5000I)  
2019-09-05 13:13:06: setAttribute(osVersion,No)  
2019-09-05 13:13:06: Execution time: 18752 ms  
2019-09-05 13:12:47: Executing SSH command: echo "/\*rexx \*/ \\n Say 'Operating system level:' MVSVAR('SYSOPSYS')\\n" > /tmp/ver.rx;chmod 755 /tmp/ver.rx; /tmp/ver.rx ;rm -f /tmp/ver.rx  
2019-09-05 13:12:47: Executing SSH command: command -v sudo  
2019-09-05 13:13:06: Command result:  
2019-09-05 13:13:06: Command failed with status 1

 - This seems to be a permission issue. In our docs for z/OS Discovery it states "The user must have permission to write to /tmp, have read access to all user processes, and be able to run REXX scripts."  
Please refer to the following documentation.   
\- [https://docs.servicenow.com/csh?topicname=zOS-discovery.html&version=latest](https://docs.servicenow.com/csh?topicname=zOS-discovery.html&version=latest)

2) Also, noticed the following error from the UNIX - Classify input payload:  
**vmware: snc\_func\_1 5: FSUM7351 not found**

-   This error **FSUM7351** means the java cannot be found. 

### Resolution

1) Give the correct permissions for the user mentioned in the docs.

[https://docs.servicenow.com/csh?topicname=zOS-discovery.html&version=latest](https://docs.servicenow.com/csh?topicname=zOS-discovery.html&version=latest)

2) There happens to be a known bug **vmware: snc\_func\_1 5: FSUM7351 not found**, mentioned from IBM:

[https://www.ibm.com/support/pages/fsum7351-not-found-returned-when-running-dfhbuildsns](https://www.ibm.com/support/pages/fsum7351-not-found-returned-when-running-dfhbuildsns)

Add the directory for the Java™ Development Kit (JDK) that contains the file "java" to your PATH environment variable in OMVS prior to running DFHBuildSNS.   
  
"java" is the executable command that is used to run DFHBuildSNS.   
  
You can set the PATH from within OMVS with an "export PATH=" statement (replace the path with the correct path and version of Java that you are running):  
  
**export PATH=/usr/lpp/java/J6.0/bin/:/bin/:/usr/sbin/:.  
  
**This example contains the JDK directory /usr/lpp/java/J6.0/bin/ and directories /bin/ and /usr/sbin/. You can also add the export command to your profile.   
  
You can enter **ENV** from within OMVS to display the current values of your environment variables, including the value of PATH.
