---
title: "Attaching attachments to a closed incident"
aliases:
  - KB0696020
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696020
kb_number: KB0696020
last_modified: 2025-01-03
---

## Attaching attachments to a closed incident

  

### Issue

  
  

# Description

* * *

How can you add attachments to closed incidents?

# Procedure

* * *

To achieve this, in the left navigator type "Client Scripts" and choose the option under "System Definition". Once you see the list of client scripts, search for "(BP) Hide Attachment Link when Closed)" this will be marked as active in your instance. Turn this to inactive. Run a cache.do and verify you can attach attachments to closed incidents.

# Applicable Versions

* * *

All Supported Versions
