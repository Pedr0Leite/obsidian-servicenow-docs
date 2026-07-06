---
title: "Troubleshooting \"Run After\" discovery"
aliases:
  - KB0689001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0689001
kb_number: KB0689001
last_modified: 2024-04-07
---

## Troubleshooting "Run After" discovery

  

### Issue

# Overview

* * *

A discovery schedule can be configured to run after the completion of another schedule, for example, so that only a limited set of discovery schedules run at a time. The following figure shows three scheduled discoveries followed by discoveries that are set to "Run After" each respective discovery.

![](sys_attachment.do?sys_id=430c642edb42b450e515c2230596197a)

"Run After" enables you to sequentially stagger the schedule. Use this option to run this schedule after the discovery designated in the Run after field finishes. Check the **Even if canceled** checkbox to designate that this discovery should run even if the Run After discovery is canceled before it finishes.  
  
Note the following:

-   This option is not valid when the Discovery is started via DiscoverNow, or when using the Discover CI feature.
-   You cannot designate an inactive Discovery schedule.
-   You cannot create a loop by designating the Run After discovery to be the same discovery.
-   This discovery does not run if the Run After discovery does not finish unless the **Even if canceled** option is selected and the discovery is canceled.

# Troubleshooting Overview

* * *

The following flowchart displays the flow from one schedule discovery to the discovery that runs after it.

![](sys_attachment.do?sys_id=570c642edb42b450e515c2230596197f)

Important business rules, script includes, and script actions involved in triggering the next discovery are:

-   Business rule: Discovery - Complete
-   Script Action: Discovery Run Next
-   Script Includes: Discovery, DiscoveryPhaser

# Troubleshooting steps

* * *

1.  Confirm that the discovery\_status.description is "Scheduled". "Discover Now" and "Discovery CI" will not trigger the next discoveries.
    
2.  Check that the discovery.complete or discovery.canceled event was created in the sysevent table.
    
3.  Check that the listed business rules, script includes, and script actions are not customized but match the out of the box versions.
    

# Additional Information

* * *

See the [Create a discovery schedule](https://docs.servicenow.com/csh?topicname=t_CreateADiscoverySchedule.html&version=latest) product documentation topic
