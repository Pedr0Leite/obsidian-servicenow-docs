---
title: "HPUX pattern for file system cmd \"df -kP\" output can word wrap causing parsing issues"
aliases:
  - KB0693322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693322
kb_number: KB0693322
last_modified: 2024-04-07
---

## HPUX pattern for file system cmd "df -kP" output can word wrap causing parsing issues

  

### Issue

When you run the df -kP command in the HPUX pattern for filesystem the output may word wrap. This word wrap can cause incorrect parsing of the command.

### Cause

The word wrap of the output cause Service Mapping to parse the data incorrectly.![](sys_attachment.do?sys_id=22899a55dbe7570423f4a345ca9619bc)

![](sys_attachment.do?sys_id=44eca022db82b450e515c223059619ea)

  

  

### Resolution

Change the parse command output step from "df -kP" to:

df -kP | sed -e ':a' -e 'N' -e '$!ba' -e 's/\\n\[\[:space:\]\]\[\[:space:\]\]\*/ /g'
