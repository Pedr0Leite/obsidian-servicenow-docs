---
title: "How to fix notifications that send despite advanced condition script returning false"
aliases:
  - KB0787284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787284
kb_number: KB0787284
last_modified: 2025-10-29
---

## How to fix notifications that send despite advanced condition script returning false

  

### Issue

Notifications in non-global application scopes may incorrectly send emails if their advanced condition scripts use the answer variable, despite conditions that should prevent the notification from firing. 

### Release

All supported releases

### Cause

The global answer variable is unavailable to scripts in non-global application scopes, causing the following error in the system logs: 

org.mozilla.javascript.EcmaError: Assignment to undefined "answer" in strict mode 

### Resolution

This issue can be resolved by one of two methods:

-   Use the answer variable
-   Create a function that returns a true or false value

For notifications in non-global application scopes, modify your advanced condition script to use the function method:

(function() {
  var groupMember = gs.getUser();
  return !groupMember.isMemberOf('XYZ');
})();

### Related Links

[Advanced conditions for email notifications](https://docs.servicenow.com/csh?topicname=c_OptSpecifyingAdvancedCond.html&version=latest "Advanced conditions for email notifications")
