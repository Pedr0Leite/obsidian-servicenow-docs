---
title: "Flow is not activating"
aliases:
  - KB0859953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859953
kb_number: KB0859953
last_modified: 2024-04-08
---

## Flow is not activating

  

### Issue

Flow is not getting activated and testing the flow throw an error:could not retrieve snapshot for test

### Release

Orlando

### Cause

Flow contains "Send Email" action and "Body" field on this action contains incorrect format .

### Resolution

Please remove the incorrect format on the "Body" field on "Send Email" action and activate the flow
