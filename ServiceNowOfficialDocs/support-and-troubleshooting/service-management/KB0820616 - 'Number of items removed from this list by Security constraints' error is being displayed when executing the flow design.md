---
title: "Number of items removed from this list by Security constraints' error is being displayed when executing the flow designer."
aliases:
  - KB0820616
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820616
kb_number: KB0820616
last_modified: 2026-06-04
---

## 'Number of items removed from this list by Security constraints' error is being displayed when executing the flow designer.

  

### Issue

'Number of items removed from this list by Security constraints' error is being displayed when executing the flow designer as the system user.

### Release

N/A

### Cause

The instance has a user named "system" with only one role.

### Resolution

\-- When the flow is set to run as system user, the flow is executed with id as "system".  
\-- In the instance, there is a user whose name and user ID are "system" and has only one role.  
\-- When the flow is executed as system it is considering the above-mentioned user.  
\-- As the user does not have any roles to access the table or records being retrieved, the flow is displaying 'Number of items removed from this list by Security constraints' message.  
  
In order to resolve the issue, you have two different approaches  
\-- Modify the user name and user\_id of user "system" in your instance.  
or  
\-- Change the flow properties to run as "user who initiates sessions".
