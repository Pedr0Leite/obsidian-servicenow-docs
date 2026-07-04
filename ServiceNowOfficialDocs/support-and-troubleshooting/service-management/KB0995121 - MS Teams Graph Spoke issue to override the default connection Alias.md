---
title: "MS Teams Graph Spoke issue to override the default connection Alias"
aliases:
  - KB0995121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995121
kb_number: KB0995121
last_modified: 2024-08-01
---

## Issue

Expected Current Behaviour: In Microsoft Graph, ‘Look up Teams by User ID’ action used delegated permissions and this action only works for the user(signed-in user) which has token.

To use it for all any User ID, we need to use Application permissions.

Use Case Requirement:When user wants to override the default connection alias shipped with the action and  
user wants to use grant type different than the one used by default connection alias.

Then they need to create a child connection alias with the required grant type using  default connection alias as parent.

Once child alias is created, if users can call the action from script and they can override parent alias with child alias at run time.

## Resolution

Code snippet for reference

try {  
var inputs = {"user\_id":"xyz@azuredomaint.com"};  
var result = sn\_fd.FlowAPI.getRunner()  
.action('sn\_msteams\_ahv2.list\_teams')  
.withConnectionAliasOverride('<Parent Alias SysID>', '<Child Alias SysID>')  
.inForeground()  
.withInputs(inputs)  
.run();  
gs.info(result.getOutputs());  
} catch (ex) {  
var message = ex.getMessage();  
gs.error(message);  
}

[Connection Alias Override reference](https://developer.servicenow.com/dev.do#!/reference/api/quebec/server/sn_fd-namespace/ScriptableFlowRunnerScopedAPI%23FR-wConnectionAliasOverride_S_S?navFilter=alias "Connection Alias Override reference")
