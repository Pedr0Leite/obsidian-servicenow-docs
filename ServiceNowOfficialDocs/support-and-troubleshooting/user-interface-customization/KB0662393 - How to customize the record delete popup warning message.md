---
title: "How to customize the record delete popup warning message"
aliases:
  - KB0662393
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0662393
kb_number: KB0662393
last_modified: 2024-01-28
---

## How to customize the record delete popup warning message

  

### Issue

How to customize the record delete popup warning message

  

# Overview

* * *

If you run into the situation where you need to delete task records, and want to customize the popup warning message generated from any delete UI Action, this article will be helpful. Below is a sample screenshot of the warning message shown while deleting records from an incident list.

  

![Delete warning message](sys_attachment.do?sys_id=7b49e4eedb02b450e515c2230596197c "Delete warning message")

#   

# Additional information

* * *

The delete confirmation and warning message come from the following out of the box UI Page in the instance:

'delete\_confirm\_list'

  

You can customize the code in this UI Page navigating to:

/nav\_to.do?uri=sys\_ui\_page.do?sys\_id=35ea35b1c33310000f343b251eba8f7c

  

Please note that when you make changes to any out of the box object, this will be considered as a customized component on your instance, hence skipped during a future upgrade. It is recommended to trace and note down these customizations, to make sure to not overlook any unwanted skipped updates, or to confirm the customizations validity in the upgraded version.

  

Please refer to the following documentation on how to handle customizations during an upgrade:

[Best practices for creating, testing, and moving customizations](https://docs.servicenow.com/ "Best practices for creating, testing, and moving customizations")

[Overwrite customizations during an upgrade](https://docs.servicenow.com/csh?topicname=t_OverwriteCustomizsDuringUpgrades.html&version=latest "Overwrite customizations during an upgrade")
