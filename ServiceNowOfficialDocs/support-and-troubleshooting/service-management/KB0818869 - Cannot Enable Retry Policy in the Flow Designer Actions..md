---
title: "Cannot Enable \"Retry Policy\" in the Flow Designer Actions."
aliases:
  - KB0818869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818869
kb_number: KB0818869
last_modified: 2026-04-01
---

## Cannot Enable "Retry Policy" in the Flow Designer Actions.

  

### Issue

In the flow designer actions, go to any out of the box "Actions"

Steps to reproduce:

1) Login to the instance using "admin" user  
2) Go to Flow Designer  
3) Click on the Actions tab  
4) Open out of the box action like "[Add Owner To Group](https://instance.service-now.com/sys_hub_action_type_definition.do?sys_id=40dee7b287220300eead7d5e27cb0b71&sysparm_view=welcome_hub_action_type&sysparm_record_target=sys_hub_action_type_definition&sysparm_record_row=3&sysparm_record_rows=136&sysparm_record_list=system_level%3Dfalse%5EORDERBYname)" action  
5) Click on Rest STEP action.  
6) Try to click on "Enable Retry Policy". It does not get "ticked". See screenshot below:

![](sys_attachment.do?sys_id=cbaf2da84704cf90b7832920326d431c)

### Release

All

### Cause

This is out of the box action which only has "Read Only Action". So, we cannot edit this.

### Resolution

We can create a copy of this action and then edit it. So, on the same action page go to more actions that have vertical 3 dots icon. See below screenshot:

![](sys_attachment.do?sys_id=0baf2da84704cf90b7832920326d4316)
