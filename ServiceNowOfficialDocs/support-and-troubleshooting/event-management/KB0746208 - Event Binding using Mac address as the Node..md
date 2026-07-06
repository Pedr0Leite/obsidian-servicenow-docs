---
title: "Event Binding using \"Mac address\" as the Node."
aliases:
  - KB0746208
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746208
kb_number: KB0746208
last_modified: 2024-04-07
---

## Issue

# Symptoms

Alerts will not bind to a CI while using Mac address value as a node.

# Release

Any

# Cause

Missing MAC address information from the "cmdb\_ci\_network\_adapter" table.

Instead of looking in the "cmdb\_ci\_hardware" table for the "Mac address" value, the default binding rule will look for that in the "cmdb\_ci\_network\_adapter" table.

# Resolution

Add the "MAC address" information in the "cmdb\_ci\_network\_adapter" table with the corresponding CI information.

# Additional Information

Usually, discovery should populate the "Mac address" information in the "cmdb\_ci\_network\_adapter" table, please make sure you check the discovery payload to see why its not being created.
