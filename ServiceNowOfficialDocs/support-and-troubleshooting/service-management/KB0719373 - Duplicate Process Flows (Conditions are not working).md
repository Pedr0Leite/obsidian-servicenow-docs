---
title: "Duplicate Process Flows (Conditions are not working)"
aliases:
  - KB0719373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719373
kb_number: KB0719373
last_modified: 2024-04-07
---

## Duplicate Process Flows (Conditions are not working)

  

### Issue

# Symptoms

* * *

-   Duplicate Flow formatters are seen in all Change Requests. The user was expecting only certain Flow formatters to show under the prescribed conditions added in the condition builder.

# Release

* * *

-   Kingston Patch 4 Hot Fix 1
-   Kingston Patch 7
-   Kingston Patch 9

# Cause

* * *

The purpose of the condition builder was misunderstood by the user (further explanation below).

# Resolution

* * *

The user mistakenly believed that the condition builder on the Flow formatter determined whether or not to display the particular Flow formatter. This is not the case.  
  
Rather, the purpose of the condition builder is "to set the conditions under which the formatter is highlighted as current" ( ref: [Process flow formatter](https://docs.servicenow.com/csh?topicname=r_ProcessFlowFormatter.html&version=latest "Process flow formatter") ).  
  
The same behavior (seeing duplicate Flow formatters) is reproducible Out of Box (OOB) by creating a new Flow formatter with the same "name" and "label" field values as an already existing Flow formatter.  
  
As there is no OOB functionality which determines (based on conditions) if a certain Flow formatter is displayed or not, it was recommended to the user to kindly reach out to their internal development team to accomplish this customization. Additionally, the user can be referred to Professional Services (note: there is a fee with this service).
