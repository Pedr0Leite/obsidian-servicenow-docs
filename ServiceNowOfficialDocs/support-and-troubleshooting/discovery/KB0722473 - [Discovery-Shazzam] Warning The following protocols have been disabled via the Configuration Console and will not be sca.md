---
title: "[Discovery-Shazzam] Warning \"The following protocols have been disabled via the Configuration Console and will not be scanned by Shazzam: XXXXX\"
aliases:
  - KB0722473
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722473
kb_number: KB0722473
last_modified: 2024-04-07
---

## \[Discovery-Shazzam\] Warning "The following protocols have been disabled via the Configuration Console and will not be scanned by Shazzam: XXXXX"

  

### Issue

# Symptoms

* * *

We may encounter some warning messages as below in the discovery log within Discovery Status.

""

The following protocols have been disabled via the Configuration Console and will not be scanned by Shazzam: XXXXX

""

XXXXX - wbem, SSH, WMI, etc..

# Release

* * *

All Releases...

# Cause

* * *

When we initiate the discovery schedule, it will check for the protocols that are deactivated within the Protocol Categories. If it finds any protocol category is deactivated then it will throw Warning message as above.

# Resolution

* * *

 Method #1: (Using the Configuration Console)

-   Open Application Navigator >> Discovery Definition >> Configuration Console
-   Under the Devices section, enable the related device protocol.

![](/sys_attachment.do?sys_id=646d20e2db82b450e515c22305961941)

Reference: [Discovery Configuration Console](https://docs.servicenow.com/csh?topicname=c_DiscoveryConfigurationConsole.html&version=latest?cshalt=yes "Discovery Configuration Console")

Method #2: (Using the table entries)

-   Check the Protocol Categories table list and see if any protocol is deactivated.
-   Table: discovery\_category\_protocol
-   If you would like to enable that category, activate them else if you don't want them to be discovered, you can ignore the messages.

![](/sys_attachment.do?sys_id=a46d20e2db82b450e515c22305961946)
