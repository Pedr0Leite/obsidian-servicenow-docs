---
title: " View patterns running on the MID Server"
aliases:
  - KB0687685
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687685
kb_number: KB0687685
last_modified: 2024-04-07
---

## View patterns running on the MID Server

  

### Issue

# Overview

* * *

In the case where the sync to the MID Server did not work, download and compare source code to determine whether the pattern running on the MID Server is the same pattern that you created or modified on the instance.

Patterns are written in Neebula Discovery Language (NDL).

To back up or transfer an NDL file to another instance, use an update set or export the pattern from the Pattern Designer or export an open pattern: right-click in the header and select **Export**.

# Procedure

* * *

1.  Enter sa\_pattern.list in the application search box to open the pattern \[sa\_pattern\] table.
2.  Open the pattern and then click the Grab NDL File from MID Server related link.  
    Note: The link does not appear if you open a pattern from the application menu.
3.  Compare the files to determine how the pattern that ran on the MID Server differs from the pattern created or modified on the instance.
