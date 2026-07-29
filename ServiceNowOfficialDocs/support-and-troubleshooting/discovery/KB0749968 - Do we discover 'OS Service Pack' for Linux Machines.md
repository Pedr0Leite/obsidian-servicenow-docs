---
title: "Do we  discover 'OS Service Pack' for Linux Machines ?"
aliases:
  - KB0749968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749968
kb_number: KB0749968
last_modified: 2024-04-07
---

## Do we discover 'OS Service Pack' for Linux Machines ?

  

### Issue

# Description

By default (OOB), discovery does not populate the value 'OS Service Pack' for Linux system, you could check out the documentation regarding Linux Discovery Data Collected to confirm the same.  So how do we get that value updated? The things that we know, the term 'OS Service Pack' used for Microsoft system, but for Linux operating system it used 'OS Version' instead.  Therefore, you could get the Linux OS version from Linux server pattern for this instead.

# Procedure

-   In Linux Server pattern, it leverages 'uname -a' command to fetch OS version information, and
-   In step 'Extract distribution version' (image below) we could extract (parsing) the version information and store it in a variable
-   Then the value in os\_version field is then populated with this new value in step 'Update OS Version' on Linux CI

![](sys_attachment.do?sys_id=ccae70a2db0ab450e515c223059619ab)

# Applicable Versions

All releases

# Additional Information

\-Linux Discovery Data Collected:

[https://docs.servicenow.com/csh?topicname=r\_DataCollDiscoLinuxComputers.html&version=latest](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoLinuxComputers.html&version=latest "https://docs.servicenow.com/csh?topicname=r_DataCollDiscoLinuxComputers.html&version=latest")
