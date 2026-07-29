---
title: "Alert Management Rule Subflow fails with No record found for table em_alert with sys id null"
aliases:
  - KB0748976
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748976
kb_number: KB0748976
last_modified: 2024-04-07
---

## Alert Management Rule Subflow fails with No record found for table em\_alert with sys id null

  

### Issue

# Symptoms

Create a custom subflow and use it in the Alert Management Rule. Here the customer is trying to update the alert record fields. 

# Release

All releases where Alert Management Rules apply.

# Cause

Input defined to read values from fields which doen't have "ah\_" prefix in the name.

![](sys_attachment.do?sys_id=70dcaceedb42b450e515c2230596197c)

# Resolution

Make sure to follow Alert management Template when creating your own subflows. If the input is not given with necessary prefixes then you will see the above error mentioned.

# Additional Information

Of course this is one of the reasons. Also, check the Business Rule Update Variables Model Information is OOB and up to date.
