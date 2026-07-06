---
title: "Discovery does not update the Name of the CI even though there is New Name in the payload"
aliases:
  - KB0745368
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745368
kb_number: KB0745368
last_modified: 2024-04-07
---

## Issue

# Symptoms

In a scenario where the name of the CI has been changed on the customers infra, Discovery does not update the name even though the new Name is in the payload.

# Release

Any

# Cause

1) If the new name already exists in the DNS table (cmdb\_ip\_address\_dns\_name) and so is the existing name, then discovery does not update the name. 

2) This is to address the issue where the DNS name Discovery gets back in Shazzam can be in any order if there are more than one names

3) This logic is written in the script include DiscoveryJSONIDSensor. Please see the screenshot for more details on the code involved

![](sys_attachment.do?sys_id=f30aa4e2db42b450e515c223059619b3)

# Resolution

There are 2 options we can recommend to the Customers .

Option 1 : Set the following system property "**glide.discovery.hostname.dns\_nbt\_trusted**" to false

Option 2 : Remove the entries related to the old name from the cmdb\_ip\_address\_dns\_name table.
