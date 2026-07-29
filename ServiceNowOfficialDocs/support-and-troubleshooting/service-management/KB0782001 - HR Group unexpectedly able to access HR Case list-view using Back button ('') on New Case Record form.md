---
title: "HR Group unexpectedly able to access HR Case list-view using Back button ('<') on New Case Record form"
aliases:
  - KB0782001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782001
kb_number: KB0782001
last_modified: 2025-09-03
---

## HR Group unexpectedly able to access HR Case list-view using Back button ('<') on New Case Record form

  

### Issue

Members of the user's HR group are able to see the sn\_hr\_core\_case list-view via the '<' (back) button on the form (see attached screenshot) when they should not be able to. The user's expectation is that this HR Group should only be able to create a new case, not see other cases.

### Resolution

The experienced behavior is expected per the user's current configuration, and per Out of Box (OOB) design.

The behavior the user is expecting does not occur naturally OOB for HR. Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementing of customizations like this is not in an engineer's area of expertise.  
  
That being said, Support certainly wants to try to be as helpful as possible - even if all that can be offered is a suggestion to try.

Something akin to the behavior the user is desiring is accomplished in Service Catalog via a Business Rule which restricts viewership based on what page the user is on. The name of the Business Rule is "Hide admin homepage categories".  
  
The user could do something like what is shown below to implement a similar behavior for HR:

Do some query like `GlideTransaction.get().getPageName()` to get the current page, and if the page name has "list" in it, do not allow viewership.  
  
Making a Business Rule containing logic like the above should work to accomplish this custom behavior. However, working out the exact details of implementing, debugging, etc. this custom Business Rule should be owned and maintained by the user.
