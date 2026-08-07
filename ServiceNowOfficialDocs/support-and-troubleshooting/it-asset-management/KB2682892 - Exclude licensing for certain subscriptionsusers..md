---
title: "Exclude licensing for certain subscriptions/users."
aliases:
  - KB2682892
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2682892
kb_number: KB2682892
last_modified: 2026-05-21
---

## Exclude licensing for certain subscriptions/users.

  

### Issue

Exclude user subscriptions from "itam\_licensing\_resource\_counts" table from being priced.

### Release

Yokohama

### Resolution

The option is available in Zurich, prior to this we do not have this option.  
  
  
In  Zurich you can use either "identifier-based exclusions for SaaS and SSO applications" or  "Define user-based exclusions for SaaS and SSO applications" based on requirement.

1.Define user-based exclusions for SaaS and SSO applications

A. Navigate to the integration profile.  
  
B.Select an integration profile for which you're defining a user-based exclusion.  
C.Select the Subscription User Exclusion Rule related list.  
D.Select New.On the form, fill in the fields.

E.Subscription User Exclusion Rule form, fill in all the details and save

The user-based exclusion rule is created for the subscription identifier. The specified subscription identifier remains excluded when the scheduled job is executed for license calculations.

2.Define identifier-based exclusions for SaaS and SSO applications

A.Navigate to the integration profile.

B.Select an integration profile for which you're defining an identifier-based exclusion.  
C.Select the Subscription Identifier Exclusion Rule related list.  
D.Select New,On the form, fill in the fields.

The identifier-based exclusion rule is created for the subscription identifier. The specified subscription identifier remains excluded when the scheduled job is executed for license calculations.

### Related Links

Reference:  
https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/subscription-exclusions.html
