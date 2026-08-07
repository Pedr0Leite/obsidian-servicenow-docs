---
title: "Create requestUI action wont associate Request to Incident."
aliases:
  - KB0726510
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726510
kb_number: KB0726510
last_modified: 2025-03-20
---

## Create requestUI action wont associate Request to Incident.

  

### Issue

# Symptoms

* * *

Request number wont be attached to the incident when you submit the catalog item through the create request UI action.

# Release

* * *

All Release.

# Cause

* * *

Catalog Item has a field 'Use Cart Layout' which is false on the item (New Assignment Group). If that is false it goes through a different macro (catalog\_cart\_default).  
Problem exists in catalog\_cart\_default macro.

# Resolution

* * *

-   Go to Catalog Item where you are seeing this issue.
-   Click on configure "Form layout" and add the "Use cart layout" field to the form view.
-   Set 'Use Cart Layout' field value to True.
-   Navigate to the relevant Catalog Item.
-   'Use Cart Layout' field is not on the form by default. Add it.
-   Check (true) the field.

# Additional Information

  
[https://docs.servicenow.com/csh?topicname=create-request-from-other-flow.html&version=latest](https://docs.servicenow.com/csh?topicname=create-request-from-other-flow.html&version=latest)
