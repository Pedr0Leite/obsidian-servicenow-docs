---
title: "Adobe Systems Creative Cloud Single App product subscriptions are incomplete"
aliases:
  - KB0955799
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955799
kb_number: KB0955799
last_modified: 2026-05-22
---

## Adobe Systems Creative Cloud Single App product subscriptions are incomplete

  

### Issue

The Adobe SaaS Integration is not adding all user subscriptions when some of these users have two subscriptions that fall under Adobe Systems Creative Cloud Single App, even though the individual Applications are different.

For example:

User 1 has InDesign & Photoshop

User 2 has InDesign & Photoshop

Only 2 user subscriptions are created instead of 4.

### Release

Software Asset Management Professional installed.

### Cause

In Adobe we create a subscription record for a user against the 'Adobe Systems Creative Cloud Single App' product and that the subgroup(Photoshop ,Illustrator etc.) is not taken into account. 'CCSA' is the subscription identifier for 'Adobe Systems Creative Cloud Single App' product.

In SampAdobeAdmin script include there's a method (createSubscriptionRecord) that checks whether a new subscription record has to be created or not. The check is on based on combination of profile, external user id and subscription\_identifier.

Since in this case for the example subscription records are already created with subscription identifier(CCSA) hence new subscription records will not be created. Hence we see only see 2 user subscriptions for Adobe Systems Creative Cloud Single App Software Model.

### Resolution

Import the changed SampAdobeAdmin script include.

Line 222 and 223 are changed like below.

var groupNameComponents = groupName.split(/\\s\*:\\s\*/)\[0\].split(/\\s\*-\\s\*/);  
return groupNameComponents ? 'ADOBESINGLEAPP\_' + groupNameComponents\[1\] : null;
