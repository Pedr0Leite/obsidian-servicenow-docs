---
title: "Discovery sensor throws an Error as  \"Discovery Sensor error : Transaction cancelled:maximum execution time exceeded\""
aliases:
  - KB0720635
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720635
kb_number: KB0720635
last_modified: 2026-05-29
---

## Discovery sensor throws an Error as "Discovery Sensor error : Transaction cancelled:maximum execution time exceeded"

  

### Issue

# Symptoms

* * *

Discovery Sensor error : Transaction cancelled:maximum execution time exceeded

![](/sys_attachment.do?sys_id=4c3fb426db0ab450e515c22305961921)

# Cause

* * *

We have an OOB quota rule for discovery sensors. Usually, discovery sensors would timed out when the total processing time reaches as per the quota rule. OOB this is defined as 20 mins. Below are some references

Discovery Sensors Quota Rule : 

**https://<Instancename>service-now.com/nav\_to.do?uri=sysrule\_quota.do?sys\_id=6815f9134733210003d79da33ede27f2**

Documentation :

[https://docs.servicenow.com/csh?topicname=r\_Sensors.html&version=latest  
  
](https://docs.servicenow.com/csh?topicname=r_Sensors.html&version=latest)

# Resolution

* * *

This can be eliminated by modifying the "max\_duration" value of quota rule record to a larger number \[suggest as thrice to the default value \] so that larger payloads would have more time to process.

### Release

ANY

### Resolution

ALL
