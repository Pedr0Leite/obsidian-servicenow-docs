---
title: "Create Request UI action is not associating request to the parent record"
aliases:
  - KB0723005
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723005
kb_number: KB0723005
last_modified: 2023-12-04
---

## Create Request UI action is not associating request to the parent record

  

### Issue

# Symptoms

* * *

Created Request is not associated to the parent record ( incident or interactions, etc)

# Release

* * *

London

# Cause

* * *

The most probable causes of the issue are listed below.

1.  The script include "CatalogTransactionCheckout" has been customized
2.  The property "Use the sc\_layout driven cart macros (default true)" (glide.sc.use\_cart\_layouts) is set to false
3.  The "Use Cart Layout" field for the individual catalog item is unchecked (set to false)

# Resolution

* * *

In London, when the Request is created from an incident (using the UI action Create Request), the incident sys\_id is in the URL's parameter "sysparm\_parent\_sys\_id" and when the request is created, it will be associated to the incident using the url parameter.

The customized script include "**CatalogTransactionCheckout**", skipped the London upgrade version and therefore the code that associates the Request to Incident using the URL is also skipped and the issue is seen.

To resolve the issue, revert the script include to London OOB version and then add the customizations on top of it.

      If all the script includes, UI macros and UI pages related to the item ordering process is out of the box, then please check if the property "**Use the sc\_layout driven cart macros (default true)**" (glide.sc.use\_cart\_layouts) is set to true.

Also, make sure that the individual catalog item has the "Use Cart Layout" checkbox checked.

**TO ENABLE CART LAYOUT:**  
1\. Go to the catalog item table and select the item  
2\. Click on context menu in the header and select configure -> Form Layout  
3\. Add "Use cart layout" from available to the selected section  
4\. Check the checkbox for the "Use cart layout"

 Cart Layout is required for the association to work properly. Please refer to this documentation for more details,

[https://docs.servicenow.com/csh?topicname=create-request-from-other-flow.html&version=latest](https://docs.servicenow.com/csh?topicname=create-request-from-other-flow.html&version=latest)
