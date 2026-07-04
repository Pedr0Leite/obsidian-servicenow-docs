---
title: "Recommendation on initiating approval requests on HR Case watchlist users dynamically"
aliases:
  - KB0864282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864282
kb_number: KB0864282
last_modified: 2025-09-03
---

## Recommendation on initiating approval requests on HR Case watchlist users dynamically

  

### Issue

 On a custom requirement in HR Case with the below scenario,

1\. HR Agent while working on a HR Case would need to trigger approvals for that case.

2\. However the list of approvers is dynamic and should be picked up from the Watchlist of the HR Case.

Using Service Activity to see if this requirement can be achieved it using HR Service Configuration but with that, it is firing approvals on the creation of HR Case but not midway based on trigger conditions or a UI action.

### Resolution

There is no OOB behaviour to achieve this custom requirement.  
  
This can be achieved by configuringing a flow designer
