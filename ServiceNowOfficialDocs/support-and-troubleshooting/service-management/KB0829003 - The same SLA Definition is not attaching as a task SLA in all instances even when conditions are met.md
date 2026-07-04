---
title: "The same SLA Definition is not attaching as a task SLA in all instances even when conditions are met"
aliases:
  - KB0829003
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829003
kb_number: KB0829003
last_modified: 2025-09-03
---

## The same SLA Definition is not attaching as a task SLA in all instances even when conditions are met

  

### Issue

The user was experiencing an issue where SLA Definition "Apple" was attaching just fine in their Dev and Test instances, but the same SLA Definition was not attaching (even when the Start conditions were matching) in their UAT instance. They wanted to know why this was.

### Resolution

Every so often when a SLA Definition is moved from one instance to another, an issue can occur where the definition does not completely insert into the back-end.   
  
Unfortunately, the only symptom of this behavior is that the user will take note that even when the Start conditions are met, the SLA Definition does not attach as a task SLA - **_ever_**. If the SLA Definition does attach, even intermittently, the user can be sure that this is not the incomplete insert issue.  
  
A good test to see that the user is facing this specific behavior is to do an insert and stay on the affected SLA Definition(s), making some prefix to the name of the SLA to distinguish it from the defunct original. If upon creating a test record the insert-and-stay version of the SLA Definition attaches as a task SLA, the user can be sure that they are facing this incomplete insert issue.  
  
To resolve the behavior, then, the user should navigate to the affected SLA Definition(s), export them to XML, and re-import them. A simple second test record will prove that the behavior has been resolved if the original SLA Definition and the insert-and-stay version of the SLA Definition both attach. The insert-and-stay version of the SLA Definition can then be removed.
