---
title: "How to use an extension point to modify a read protected script include (WalkUpQueue) for the Walk Up plugin"
aliases:
  - KB0720744
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720744
kb_number: KB0720744
last_modified: 2024-01-28
---

## Issue

# Description

* * *

This article shows how to create an extension point to allow the modification of the WalkUpQueue script include without impacting the OOB code as the WalkUpQueue has readonly policy protection set. Extension Points is a new feature in London which makes it easier to integrate customisations without actually altering the base code for an application, minimising potential upgrade conflicts.

# Procedure

* * *

1.  First open a 2nd tab, with the OOTB WalkUpQueue script include record.  
    2\. Next, in a separate tab, in the navigation filter, enter sys\_extension\_point.list  
    3\. Find record with the API Name \`sn\_wlkup.WalkUpQueue\` in the list, and click into it  
    4\. In the Related Links section below the form, click on "Create Implementation". once this has been created, a new script include will have been made, where the customer can make their own modifications.  
    5\. Copy the original script from the OOTB \`WalkUpQueue\` script that you opened in the other tab, into this new script include, then start making your modifications on this new script include.

# Applicable Versions

* * *

London onwards

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=extension-points.html&version=latest](https://docs.servicenow.com/csh?topicname=extension-points.html&version=latest)
