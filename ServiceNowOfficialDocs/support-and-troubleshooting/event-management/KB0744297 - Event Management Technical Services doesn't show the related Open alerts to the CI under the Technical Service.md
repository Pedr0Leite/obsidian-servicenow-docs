---
title: "Event Management Technical Services doesn't show the related Open alerts to the CI under the Technical Service"
aliases:
  - KB0744297
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744297
kb_number: KB0744297
last_modified: 2025-01-02
---

## Event Management Technical Services doesn't show the related Open alerts to the CI under the Technical Service

  

### Issue

When there is an Open alerts related to a CI under a Technical Services, the alert/s are not shown in the Alerts panel of the Technical Service when selected.

The Impact Calculation job is running fine.

### Cause

There's no impact graph (em\_impact\_graph.LIST) built for any of the Technical Services, therefore the impact will not be calculated.  
The "Out-Of-The-Box" impact rules (em\_impact\_rule.LIST) are missing. 

On this case, it was found out that the Impact Rules were deleted on the instance.

### Resolution

To resolve this issue, Import the  Out-Of-The-Box" impact rules (em\_impact\_rule) to the affected instance.

1\. Login to an "Out-Of-The-Box" instance.

2\. Navigate to the impact rules (em\_impact\_rule.LIST).

3\. There are 8 "Out-Of-The-Box" rules, go to the header, right-click, Export > XML

4\. Check the XML contains the 8 "Out-Of-The-Box" rules

5\. Login to the affected instance, go to any list or em\_impact\_rule.LIST.

6\. Right click the header, Import XML

7\. Verify that the list contains the 8 impact rules.

8. Update the Technical Service "Operational status" from "Operational" to "Non-Operational". Click Save.

9. Update the Technical Service "Operational status" from "Non-Operational" to "Operational". Click Save.

10\. Check the Technical Service again, it should have the related alerts listed.

Note:

Steps 8 & 9, are necessary to be able to built the impact tree. This should be done on each of the Technical Service.
