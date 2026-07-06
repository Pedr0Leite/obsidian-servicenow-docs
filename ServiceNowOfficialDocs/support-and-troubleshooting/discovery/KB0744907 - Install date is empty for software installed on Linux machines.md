---
title: "Install date is empty for software installed on Linux machines"
aliases:
  - KB0744907
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744907
kb_number: KB0744907
last_modified: 2024-04-07
---

## Install date is empty for software installed on Linux machines

  

### Issue

# Overview

In server form field, under "Software Installations", Install Date field is empty.

![](sys_attachment.do?sys_id=b98aac66db42b450e515c223059619d9)

# Details

For Linux machines, the software installed information is being pulled the probe: "Linux - Installed Software". This will not get "Install Date" information.

https://<Instance\_Name>.service-now.com/nav\_to.do?uri=discovery\_probes.do?sys\_id=2c93a59c0a0a0a8b00d5f029ccaf5573

This will only pull Sofware Name, Version and Vendor(Publisher) details.

software.name = this.name;  
software.version = this.version;  
software.vendor = this.maintainer;

However, for Windows machines, the install date field of the software is being fetched from windows registry:

[Windows discovery](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoWindowsComputers.html&version=latest "Windows discovery")

The client might have to raise an enhancement request for the same.
