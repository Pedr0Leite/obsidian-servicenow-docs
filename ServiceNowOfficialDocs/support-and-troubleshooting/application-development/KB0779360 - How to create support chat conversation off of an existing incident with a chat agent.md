---
title: "How to create support chat conversation off of an existing incident with a chat agent"
aliases:
  - KB0779360
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779360
kb_number: KB0779360
last_modified: 2025-01-03
---

## How to create support chat conversation off of an existing incident with a chat agent

  

### Summary

This article explains how to create connect support chat conversation off of an existing incident with a chat agent.

### Instructions

Create a UI action called "Chat" on the Incident table with the following script

**function chatRedirect() {**  
**var queueID = 'b05cfd27d70122004f1e82285e61038d'; //sys\_id of the chat queue you need to redirect to**  
**location.href = '/$chat\_support.do?queueID='+ queueID +'&fromTable=incident&fromSysID='+ g\_form.getUniqueValue();**  
**}**

Create an after insert business rule on the chat\_queue\_entry table with When to Run condition Selected as ' From Type' is 'Incident' and following script.

**(function executeRule(current, previous /\*null when async\*/) {**

**var inc = current.from\_id.getRefRecord();**

**var groupID = current.getValue('group');**

**var profileID = '';**

**var linkUrl = "/incident.do?sys\_id="+inc.getUniqueValue();**

**var linkName = inc.number+': '+inc.short\_description;**

**var msg = "@L\["+linkUrl+"|"+linkName+"\]";**

**var grProfile = new GlideRecord('live\_profile');**

**grProfile.addQuery('name', 'Cloud Support');**

**grProfile.addQuery('document', current.getUniqueValue());**

**grProfile.query();**

**if (grProfile.next()) {**

**profileID = grProfile.getUniqueValue();**

**}**

**var data = {**

**message: msg,**

**group\_id: groupID,**

**from\_profile: profileID**

**};**

**//add link if we have a valid one**

**if (linkUrl) {**

**data.links = \[**

**{short\_description: linkName, url: linkUrl}**

**\];**

**}**

**var output = JSON.stringify(data, null, 4);**

**gs.log(output);**

**return new LiveFeedMessage().postMessage(data);**

**})(current, previous);**

### Related Links

Click on the Chat UI action and it will redirect you to the connect support page. Enter some text and hit "Send" in the support conversation. You will see a connect support conversation created with a connect card displaying incident details.

![](sys_attachment.do?sys_id=e79e83b8dbc434d0471f9c41ba9619f3)
