---
title: "Flow Designer did not send out e-mails as expected"
aliases:
  - KB0818879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818879
kb_number: KB0818879
last_modified: 2024-12-10
---

## Flow Designer did not send out e-mails as expected

  

### Issue

The user has a Flow that should send out e-mails to users based on their time card information. Recently, this did not work and e-mails were not sent out.

### Resolution

It was found that some changes had been made to the Flow and erroneous data pills were being utilized (there was a data pill referencing a step which no longer existed in the Flow).

It was noted that the action being performed relied on the information stored within the data pill. As a result of the data pill being broken, the functionality which was using it also broke.  
  
Resolving the erroneous data pill fixed the issue.
