---
title: "Is it possible to delete a Knowledge Base created accidentally?"
aliases:
  - KB0688279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688279
kb_number: KB0688279
last_modified: 2025-05-13
---

## Is it possible to delete a Knowledge Base created accidentally?

  

### Issue

# Symptoms

* * *

Inability to delete a Knowledge Base, can't intuitively remove a Knowledge Base

# Release

* * *

Jakarta Patch 8a

# Cause

* * *

It is recommended that Knowledge Bases be made active = false rather than they be deleted (see "Resolution" for further details).

# Resolution

* * *

At ServiceNow, it is recommended that users make Knowledge Bases which are no longer needed active = false rather than deleting them. This is reflected in the platform.   
  
This is by design to safeguard against the accidental deletion of Knowledge Articles, as many companies have thousands of articles stored within any given Knowledge Base, and having them deleted would have a large (negative) impact on their business.  
  
Recommend to the customer that they simply making the Knowledge Base active = false. The default filter for Knowledge Bases is active = true, so the deactivated Knowledge Base will not show up in that list.
