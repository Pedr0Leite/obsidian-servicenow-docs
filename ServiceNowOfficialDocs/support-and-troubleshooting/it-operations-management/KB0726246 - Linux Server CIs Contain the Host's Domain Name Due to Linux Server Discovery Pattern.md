---
title: "Linux Server CIs Contain the Host's Domain Name Due to Linux Server Discovery Pattern"
aliases:
  - KB0726246
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726246
kb_number: KB0726246
last_modified: 2024-04-07
---

## Issue

# Description

* * *

The out of box Discovery Pattern "Linux Server" will create cmdb\_linux\_server CI records in the format of hostname.domainname or FQDN.

For example LinuxSRV.domain.com

# Procedure

* * *

You can edit the pattern like below and the pattern will create the Linux Server CI with only the hostname.

1.  **In the Navigation Filter, type Discovery Patterns.**
2.  **Search for Linux Server.**
3.  **Click "discovery" in the Identification Section**
4.  **Click on Step 2.**

  

  

![](sys_attachment.do?sys_id=b81ce42edb42b450e515c22305961970)

  

      **4. Click the plus sign to add a Target.**

  

![](sys_attachment.do?sys_id=7c1ce42edb42b450e515c22305961975)

  

![](sys_attachment.do?sys_id=fc1ce42edb42b450e515c2230596197a)

  

      **5. Add "host\_name" for the Target Field Name and "$formattedHostname" for the value.**

  

![](sys_attachment.do?sys_id=fc1ce42edb42b450e515c22305961998)

     **6. Make sure to click Save and click Publish on the top right hand side of the form.**
