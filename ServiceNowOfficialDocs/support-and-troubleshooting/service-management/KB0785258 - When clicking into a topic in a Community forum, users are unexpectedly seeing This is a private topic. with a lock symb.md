---
title: "When clicking into a topic in a Community forum, users are unexpectedly seeing \"This is a private topic.\" with a lock symbol."
aliases:
  - KB0785258
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785258
kb_number: KB0785258
last_modified: 2024-12-27
---

## When clicking into a topic in a Community forum, users are unexpectedly seeing "This is a private topic." with a lock symbol.

  

### Issue

When a community user clicks on a topic that is available for a forum, the page shows it as a private topic and shows a lock symbol. The user wanted to know why this is.

### Resolution

It was found that this unexpected behavior was due to a mis-scoped ACL for "sn\_communities.none". The ACL should have a sys\_scope value of "10809a9edb866200b1f6f78eaf961904", but, in this case, the ACL did not even have the sys\_scope column present in the XML of the record.

As a result, it was not possible to simply have the user import the Out of Box (OOB), correctly scoped ACL, or to change the sys\_scope value via a background script per a Change Request (again, the sys\_scope column was not present). 

The mis-scoped ACL was operating in the "global" scope, so it was necessary to find a solution which would allow the ACL access to the global scope. 

To accomplish this, the Script section of the ACL needed a minor modification. To begin, here is the ACL of concern:

-   https://instance.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=987bd9e6db0e6200b1f6f78eaf96197a

The current version of the Script section of the ACL reads:

answer = execute();

function execute() {  
return new CommunityUser().canReadTopic(current.sys\_id.toString());  
}

And with the small modification which allows the ACL global scope access, it will read:

answer = execute();

function execute() {  
return new sn\_communities.CommunityUser().canReadTopic(current.sys\_id.toString());  
}

By making the above modification and clearing the cache after updating the script section above, the ACL is permitted access to the global scope and the behavior is resolved. The "This is a private topic." message and the lock symbol are cleared away.
