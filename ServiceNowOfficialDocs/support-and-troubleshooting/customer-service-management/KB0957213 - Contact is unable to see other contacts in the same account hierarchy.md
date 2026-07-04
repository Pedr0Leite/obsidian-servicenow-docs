---
title: "Contact is unable to see other contacts in the same account hierarchy"
aliases:
  - KB0957213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957213
kb_number: KB0957213
last_modified: 2024-02-15
---

## Issue

A contact is unable to view all of the contacts in their own account/sub-accounts.

## Resolution

One way to resolve this is discussed in the following outline. The implementation is a customization:

1\. Create a new constant file to hold the configurations for their role similar to CSQueryBRUtilOOBConstants.  

2\. Go to the custom constant file's ROLE\_PERMISSIONS\_POOL section. For the customer\_contact table under their role add this line: 

"{'access\_context': \[CSQueryBRUtilOOBConstants.MY\_ACCOUNT, CSQueryBRUtilOOBConstants.ACCTS\_FROM\_CONTACT\_RELATIONSHIP, CSQueryBRUtilOOBConstants.SUB\_ACCTS\]}"

3\. Create a new extension instance, CSQueryExtensionPoint, to hold the logic returning this new constant file to CSQueryBRUtil. 

## Additional Information

See also:

[https://community.servicenow.com/community?id=community\_question&sys\_id=79832945dbfe909011762183ca9619e0](https://community.servicenow.com/community?id=community_question&sys_id=79832945dbfe909011762183ca9619e0)

[https://docs.servicenow.com/bundle/orlando-customer-service-management/page/product/customer-service-management/concept/creating-custom-csm-user-roles.html](https://docs.servicenow.com/bundle/orlando-customer-service-management/page/product/customer-service-management/concept/creating-custom-csm-user-roles.html)

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0685767](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685767)
