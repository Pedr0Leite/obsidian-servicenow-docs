---
title: "When trying to set \"Requested For\" to user \"Tony Stark\", it is submitting instead under the logged in user, \"Bruce Banner\"."
aliases:
  - KB0783793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783793
kb_number: KB0783793
last_modified: 2024-04-08
---

## When trying to set "Requested For" to user "Tony Stark", it is submitting instead under the logged in user, "Bruce Banner".

  

### Issue

With one-step checkout in Service Portal, when the user is trying to set the Requested for value to "Tony Stark", it is submitting the Request instead under the logged-in user, "Bruce Banner". The user wanted to know why this is happening.

### Resolution

It was found that the behavior the user is experiencing is expected, and is reproducible Out of Box (OOB).

The reason this is happening is that the value of "Bruce Banner" (the logged-in user, the one submitting the request) is always going to be pushed to the sc\_cart with one-step checkout.  
  
To resolve this issue, please enable two-step checkout for Service Portal.  
  
To do this, navigate to sys\_properties table and search for system property "glide.sc.sp.twostep" and set the value to "true".  
  
Then, when the user submits their order, they will be met with a small modal where they confirm who the order should be requested for. In that modal, the user should choose whoever it is they want the Request to be submitted for. With the system property enabled, the sc\_cart will now properly sync with the new requested\_for value, and the Request will be submitted under "Tony Stark" per the user's expectation.
