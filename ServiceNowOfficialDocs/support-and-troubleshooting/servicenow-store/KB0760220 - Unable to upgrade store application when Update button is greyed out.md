---
title: "Unable to upgrade store application when Update button is greyed out"
aliases:
  - KB0760220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760220
kb_number: KB0760220
last_modified: 2023-11-21
---

## Issue

When attempting to upgrade a Store app, the 'Update' button is greyed out. The steps below will assist in ensuring functionality.

## Resolution

The glide.sys.domain.delegated\_administration property is set to default value of 'true' when domain separation is enabled and as long as this property is set to true, the code looks for a user in global domain to grant them access to apply update sets, activate plugins and install applications.  
  
1\. Check sys\_properties table for the **glide.sys.domain.delegated\_administration** property and confirm it is set to **True**.

2\. Go to sys\_user table and add the Domain field to the list. Locate the user who is unable to see the Update button active and verify if the user is in global domain. If not, then they will not be able to view the Update button active. 

Make sure to create the admin who needs to have these privileges to be in the global domain to grant them the required privileges to enable them to apply update sets, activate plugins and install applications. 

Note: The glide.sys.domain.delegated\_administration property controls process separation.

## Additional Information

-   [Domain separation setup and administration](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/company-and-domain-separation/concept/c_DomainSeparationSetup.html)
