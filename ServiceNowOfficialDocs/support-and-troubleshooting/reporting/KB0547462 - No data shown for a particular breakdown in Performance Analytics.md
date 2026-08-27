---
title: "No data shown for a particular breakdown in Performance Analytics"
aliases:
  - KB0547462
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547462
kb_number: KB0547462
last_modified: 2026-04-07
---

## No data shown for a particular breakdown in Performance Analytics

  

### Issue

 

# There is no data shown on the scorecard / dashboard for a particular breakdown in Performance Analytics even though there is data in the system.

### Release

Any Release

### Cause

### Resolution

**1\. Check if the indicator which is using the breakdown is included in a job**

1.  Please review KB0547461: No data shown for a particular indicator in Performance Analytics.

**2\. Check the number of breakdown elements to be included in a data collection**

1.  Check the properties at Performance Analytics > System > Properties.

**3\. Check if the breakdown is excluded in the Breakdown matrix exclusions list:**

1.  Navigate to Performance Analytics > Indicators > Automated Indicators.
2.  Open the indicator that does not show any scores.
3.  Scroll down to the bottom of the indicator form.
4.  Click the Breakdown matrix exclusions tab.
5.  Check if the breakdown is in the exclusions list.
6.  Remove the breakdown from the exclusions list.
7.  Click Update.

**4\. Update the PA property to a larger number than the number of elements shown on previewing the breakdown source.**  
[com.snc.pa.dc.max\_breakdown\_elements\_limit  
  
](https://empvinnilondon.service-now.com/sys_properties.do?sys_id=38d0e311d7121100ef2281537e610385&sysparm_record_target=sys_properties&sysparm_record_row=4&sysparm_record_rows=5&sysparm_record_list=nameCONTAINSbreakdown_element%5EORDERBYname)**5\. Look for empty (no name) elements in the breakdown source table.**

1.  Navigate to breakdown source and click on Preview.
2.  Sort by the name to see if there are any elements that are blank.
3.  Update the element to have a name or delete it from the list.

Re-run the data collection job.
