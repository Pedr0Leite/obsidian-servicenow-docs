---
title: "[DOCUSIGN] Software Model did not get created."
aliases:
  - KB0955549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955549
kb_number: KB0955549
last_modified: 2024-02-05
---

## \[DOCUSIGN\] Software Model did not get created.

  

### Issue

**Steps to Reproduce:**  
1\. Go to "All User Subscriptions" under "Saas License".  
2\. Filter data for Docusign Integration Profile.  
3\. The Software Model didn't get updated.

Software Subscription: Name = DOCUSIGN, Software Model = empty.  
https://_**<instance\_name>**_.service-now.com/samp\_sw\_subscription\_list.do?sysparm\_query=display\_name%3DDOCUSIGN&sysparm\_view=

### Release

Paris

### Cause

There are 2 "core\_company" records where 1 is normalized (true) and 1 is not (false).

"core\_company" starts with "DocuSign"  
https://_**<instance\_name>**_.service-now.com/core\_company\_list.do?sysparm\_query=nameSTARTSWITHDocusign&sysparm\_view=

The Publisher record, "manufacturer" field points to the "core\_company" record where "normalized" is false.

https://_**<instance\_name>**_.service-now.com/nav\_to.do?uri=samp\_sw\_publisher.do?sys\_id=_**<sys\_id>**_

### Resolution

Make sure that the "manufacturer" value is set to the "core\_company" record that is "normalized" = true.  

https://_**<instance\_name>**_.service-now.com/nav\_to.do?uri=samp\_sw\_publisher.do?sys\_id=_**<sys\_id>**_
