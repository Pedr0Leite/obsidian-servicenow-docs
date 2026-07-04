---
title: "Configuring Issue ID with a Jira ID disables the Additional Fields option in Flow Designer "
aliases:
  - KB0818292
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818292
kb_number: KB0818292
last_modified: 2025-06-27
---

## Configuring Issue ID with a Jira ID disables the Additional Fields option in Flow Designer

  

### Issue

Learn how to configure an Update Issue action in Jira when using a Jira ID results in the unavailability of the Additional Fields option. This does not occur in a Create Issue action. 

![](sys_attachment.do?sys_id=c096eb079792a6d024a7739c1253af37)

### Release

Beginning with London release

### Resolution

When configuring an Update Issue Action, the Additional Field depends on the Issue ID field. 

Use a valid Jira Issue ID in the **Issue ID** field to ensure that the Additional Fields option is available.

If you are using a data pill to populate the Issue ID, refer to [this knowledge article](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818189). 

![](sys_attachment.do?sys_id=3f86eb079792a6d024a7739c1253af34)
