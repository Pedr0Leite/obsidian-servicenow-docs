---
title: "Alert management rule not loading the Alert filter section."
aliases:
  - KB0748938
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748938
kb_number: KB0748938
last_modified: 2024-04-07
---

## Alert management rule not loading the Alert filter section.

  

### Issue

# Symptoms

Alert management rule not loading the Alert filter section.

![](sys_attachment.do?sys_id=e0fa202adb42b450e515c22305961938)

# Release

London and above

# Cause

This is because the condition in the alert filters is having a string value more than 2083 character.

# Resolution

Use Regex or dynamic expressions to match the values.
