---
title: "How to reference the current user in a User Criteria script using the user_id variable"
aliases:
  - KB0780775
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780775
kb_number: KB0780775
last_modified: 2026-05-26
---

## How to reference the current user in a User Criteria script using the user\_id variable

  

### Issue

When writing a scripted User Criteria record, sessions APIs such as gs.getUser(), gs.getUserID(), or gs.getUserName() return unexpected results or cause conflicts when the criteria is tested in diagnostic and preview tools. The script evaluates against the logged-in administrator instead of the user being checked.

### Release

All releases

### Cause

Session-based APIs return the user tied to the current session, not the user the User Criteria engine is evaluating. Diagnostic tools (for example, the "Try it" / preview functions that test a criterion against a selected user) pass the target user through a predefined script variable rather than through the session, so any logic that relies on session APIs ignores that input and produces incorrect results.

### Resolution

Use the predefined **user\_id** variable available inside every User Criteria script. It contains the sys\_id of the user currently being evaluated, whether the evaluation is happening at runtime or inside a diagnostic tool. Return the result of the evaluation through the predefined **answer** variable.

Example — grant access only to users whose manager matches a specific sys\_id:

(function() {  
  
// Simulate what the User Criteria engine injects at runtime  
  
var user\_id = '62826bf03710200044e0bfc8bcbe5df1';  
  
var answer;  
  
  
//62826bf03710200044e0bfc8bcbe5df1 abel  
  
//0a826bf03710200044e0bfc8bcbe5d7a Make Adela Abel's Manager  
  
var userGR = new GlideRecord('sys\_user');  
  
if (userGR.get(user\_id)) {  
  
answer = (userGR.getValue('manager') == '0a826bf03710200044e0bfc8bcbe5d7a');  
  
} else {  
  
answer = false;  
  
}  
  
gs.info('User: ' + (userGR.isValidRecord() ? userGR.getValue('user\_name') : '\[not found\]'));  
  
gs.info('Manager sys\_id on user: ' + userGR.getValue('manager'));  
  
gs.info('answer = ' + answer);  
  
})();  
  
  

Result:

![Example result shows Adela to be Abel's manager](/sys_attachment.do?sys_id=3ea8bf5697090710dfd73dae2153af49 "Example result shows Adela to be Abel's manager")

### Related Links

[Create a User Criteria](https://docs.servicenow.com/csh?topicname=t_CreateAUserCriteriaRecord.html&version=latest "Create a User Criteria")
