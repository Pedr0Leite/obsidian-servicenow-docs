---
title: "When the user who has sn_customerservice.customer_admin role creates a customer contact via Catalog Item: Create Contact, the newly created contact is obtaining snc_internal role"
aliases:
  - KB0722447
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722447
kb_number: KB0722447
last_modified: 2024-10-09
---

## When the user who has sn\_customerservice.customer\_admin role creates a customer contact via Catalog Item: Create Contact, the newly created contact is obtaining snc\_internal role

  

### Issue

# Symptoms

* * *

When the user who has sn\_customerservice.customer\_admin role creates a customer contact via Catalog Item: Create Contact, the newly created contact is obtaining snc\_internal role instead of snc\_external role, which shouldn't happen because the newly created contacts with this snc\_internal role are not able to access the CSM portal.

# Release

* * *

Kingston

# Cause

* * *

When a user with sn\_customerservice. customer\_admin role creates a contact, a query business rule named: "Customer query rule" hides the role: snc\_external.

# Resolution

* * *

1.  Go to sys\_properties.list and find the property named: sn\_customerservice.contact\_role\_assignment
2.  Please append ",snc\_external" to the value of this property
