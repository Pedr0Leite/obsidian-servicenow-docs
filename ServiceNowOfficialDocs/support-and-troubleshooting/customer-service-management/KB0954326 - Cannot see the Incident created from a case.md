---
title: "Cannot see the Incident created from a case"
aliases:
  - KB0954326
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954326
kb_number: KB0954326
last_modified: 2024-01-27
---

## Cannot see the Incident created from a case

  

### Issue

After creating an Incident from the Case, the Incident is not visible.

Steps to Reproduce:

-   Create a case through the service portal
-   The agent enters the cases and goes to the additional action menu on the top of the case form and selects create an incident
-   An error appears saying no record found (Screenshot attached)

### Cause

The OOB business rule 'Incident query' has been customized:  
nav\_to.do?uri=sys\_script.do?sys\_id=2bc2f9b1c0a801640199f9eb0067326e  

### Resolution

Reverting the above OOB Business Rule to OOB will fix the issue.
