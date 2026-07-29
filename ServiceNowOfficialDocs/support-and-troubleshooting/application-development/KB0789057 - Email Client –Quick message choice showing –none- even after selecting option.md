---
title: "Email Client –Quick message choice showing –none- even after selecting option"
aliases:
  - KB0789057
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789057
kb_number: KB0789057
last_modified: 2024-04-08
---

## Email Client –Quick message choice showing –none- even after selecting option

  

### Issue

Recent upgrades to New York patch 3 and we have seen defect that in Email client Quick message choice showing –none- even after selecting the option.

### Release

New York

### Cause

Prior to New York, when a Quick Message was applied to an email draft, it replaced the in-progress content of the draft. This was problematic for reply emails.  
Quick Messages are now additive and will be inserted at the cursor  
All in-progress content can be replaced by selecting the email body and then selecting the Quick Message

### Resolution

To revert to the previous behavior (replace) by setting the value of glide.email\_client.quick\_message.insert from True to False.
