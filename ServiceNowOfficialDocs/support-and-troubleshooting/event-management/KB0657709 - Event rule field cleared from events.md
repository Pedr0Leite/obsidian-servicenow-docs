---
title: "Event rule field cleared from events"
aliases:
  - KB0657709
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657709
kb_number: KB0657709
last_modified: 2024-04-07
---

## Event rule field cleared from events

  

### Issue

# Issue

* * *

If an event rule that was applied for processing events is made inactive or deleted, it iscleared out from all the events that were processed with that rule. A listener field on the dictionary clears the event rule if it is deleted or made inactive, which results in clearing out the 'rule applied' field on all the events that were previously processed with rule.

The dictionary entry that clears out the field on the em\_event is:

https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_dictionary.do?sys\_id=e7b8c10e13c312009f507e776144b03f%26sysparm\_view=advanced.

# Solution

* * *

If you still want to retrieve the event rules applied for the events that have been processed even when the rules are made inactive, set the reference cascade rule to "-- None --" in the Choice list. For more information, see the product documentation topic [Configure cascade delete rules](https://docs.servicenow.com/csh?topicname=t_CascadeDeleteRules.html&version=latest).
