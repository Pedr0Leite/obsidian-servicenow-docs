---
title: "Pattern log shows missing pattern when running horizontal discovery."
aliases:
  - KB0727189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727189
kb_number: KB0727189
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

When running Discovery you are getting error "...Discovery status is FAILURE, Discovery using patterns could not be executed due to missing pattern <some pattern name>. Synchronize the pattern with the Mid Servers and try again". After syncing the pattern to the MID Servers you still get the same error.

* * *

# Cause

* * *

This may be due to pattern being set to inactive.  Please note that even a published pattern may be set to inactive.

![](sys_attachment.do?sys_id=731968aedb02b450e515c22305961985)

# Resolution

* * *

Tick the active box and update the pattern.

# Additional Information

* * *

This should trigger creation of ECC output queue record for each MID Server with Topic "SystemCommand", Name "sa\_pattern" and Source "FileChange".  You should also ECC input queue created shortly by the active MIDs with the same Topic,Name and Source.
