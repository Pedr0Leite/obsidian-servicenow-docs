---
title: "Business service - Cannot create new business service as the 'new' button/action is missing"
aliases:
  - KB0721235
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721235
kb_number: KB0721235
last_modified: 2024-04-07
---

## Business service - Cannot create new business service as the 'new' button/action is missing

  

### Issue

While in a domain separated instance, if we navigate to 'Business Service' under 'Service Mapping', there is no option to create a 'new' business service.

### Release

Any release which supports Service Mapping

### Resolution

\*This is expected behavior.

In a domain separated environment, the creation of business service is permitted while in a LEAF DOMAIN. So, a user will not see a 'NEW' button while in the GLOBAL domain or any non-leaf domains.

 The product has been designed in a way that while the instance is domain separated, the business services are expected to be independent to each of the domains, serving the specific purpose of the domain, using the domain-specific MID servers and the CIs.

### Related Links

UI action that controls the visibility of 'NEW' option:

https://<Instance\_Name>.service-now.com/sys\_ui\_action.do?sys\_id=e4a0b812c31031001c13587981d3ae0e&sysparm\_view=&sysparm\_record\_target=&sysparm\_record\_row=1&sysparm\_record\_list=sys\_idCONTAINSe4a0b812c3103%5EORDERBYorder&sysparm\_record\_rows=1

If the function "isBusinessServiceCreationPermitted()", if returned true, only then the 'new' button is shown.
