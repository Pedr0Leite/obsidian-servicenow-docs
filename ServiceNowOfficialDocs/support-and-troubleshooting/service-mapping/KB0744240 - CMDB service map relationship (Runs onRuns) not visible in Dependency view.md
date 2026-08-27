---
title: "CMDB service map relationship (Runs on::Runs) not visible in Dependency view"
aliases:
  - KB0744240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744240
kb_number: KB0744240
last_modified: 2024-04-07
---

## Issue

# Symptoms

Runs on::Runs relationship between CIs of class Software \[cmdb\_ci\_spkg\] and Hyper-V Server \[cmdb\_ci\_hyper\_v\_server\] not seen in the Dependency view.

# Release

All releases

# Cause

The relationship defined between the parent CI and child CI, when set to true in the cmdb\_rel\_filter table will not show up in the Dependency View. Relationship Type exclusion list table cmdb\_rel\_filter can be used to exclude the relationships in CI Dependency view.

![cmdb\_rel\_filter table](sys_attachment.do?sys_id=0d8ef462db0ab450e515c223059619ca "cmdb_rel_filter")

# Resolution

1.  Open table cmdb\_rel\_filter
2.  Filter the table with the condition parent table cmdb\_ci\_spkg and child table cmdb\_ci\_hyper\_v\_server with relationship type as Runs on::Runs
3.  Set the field value Active = false
4.  Open either the parent or child CI and click on Dependency View to see the upstream and downstream relationships

The relationships will show in the Dependency view for the CIs.
