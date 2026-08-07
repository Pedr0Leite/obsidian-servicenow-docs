---
title: "Users are not able to see the attachment right away after it's been attached on a service portal or platform page for any HR related records/catalog items"
aliases:
  - KB0752338
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752338
kb_number: KB0752338
last_modified: 2024-04-07
---

## Issue

# Symptoms

When a user attaches any attachment to a service portal or platform page for any HR related records/catalog items he/she is not able to see this attachment right away. It's only visible after the record/form is submitted.

# Release

Madrid

# Cause

The OOB table level read ACL for sys\_attachment has been customized.

The OOB ACL: /sys\_security\_acl.do?sys\_id=859a6a6c536332002b76da86a11c0865

# Resolution

1) Backup the current customized ACL (one with sys\_id of 859a6a6c536332002b76da86a11c0865).

2) Download the XML file that is attached on this KB.

3) Import this XML file to the affected instance.

\*Please note if the XML file is not imported successfully the application scope has to be switched first to "Human Resources: Core"
