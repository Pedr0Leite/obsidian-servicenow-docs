---
title: "Discovery not populating CPU Speed and  Memory fields"
aliases:
  - KB0686817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686817
kb_number: KB0686817
last_modified: 2024-04-07
---

## Discovery not populating CPU Speed and Memory fields

  

### Issue

# Symptoms

* * *

While Discovering HP-UX servers, the probes to capture the data of _**"CPU Speed" and "Total Memory"**_ were not capturing the required details.

# Release

* * *

Jakarta & Kingston 

# Environment

* * *

HP-UX 11 

# Cause

* * *

This is because some of the commands in the HP-UX OS has been depreciated, our probes use the command "'memory\_installed\_in\_machine/D' | adb -k /stand/vmunix /dev/mem | tail -1" to gather the Memory information, and the extensions adb in the command is depreciated, example as below.

root # echo 'memory\_installed\_in\_machine/D' | adb -k /stand/vmunix /dev/mem | tail -1

adb: info: Option -k is deprecated.  
adb: warning: Trouble reading version string from memory file ...  
adb: warning: Object file and memory file may not be matched.  
adb: warning: Could not complete object file specific initializtions ...  
adb: warning: Proceeding anyway; But some commands may fail.  
adb: warning: Unrecognized format character - 'D'.  
memory\_installed\_in\_machine:

Resolution

* * *

Use **"machinfo |grep -i Memory"** command instead of **"memory\_installed\_in\_machine/D' | adb -k /stand/vmunix /dev/mem | tail -1"**

```
Sample Output when executing "machinfo":#machinfoCPU info:Intel(R) Itanium 2 9000 series processor (1.59 GHz, 18 MB)2 cores, 2 logical processors per socket532 MT/s bus, CPU version C2Active processor count:1 socket2 cores (2 per socket)Memory: 8171 MB (7.98 GB)Firmware info:Firmware revision: 01.05FP SWA driver revision: 1.18IPMI is supported on this system.BMC firmware revision: 5.06Platform info:Model: "ia64 hp server rx2660"Machine ID number: ee6ab9e2-2ad6-11dc-a693-2fab98a34215Machine serial number: USE4723KCFOS info:Nodename: itanicRelease: HP-UX B.11.31Version: U (unlimited-user license)Machine: ia64ID Number: 3999971810vmunix _release_version:@(#) $Revision: vmunix: B.11.31_LR FLAVOR=perfLocation of the command# which machinfo/usr/contrib/bin/machinfo
```

# Additional Information

* * *

Existing PRB : **PRB717538**
