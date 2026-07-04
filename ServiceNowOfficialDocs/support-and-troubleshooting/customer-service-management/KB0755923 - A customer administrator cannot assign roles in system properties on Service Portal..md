---
title: "A customer administrator cannot assign roles in system properties on Service Portal."
aliases:
  - KB0755923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755923
kb_number: KB0755923
last_modified: 2025-08-17
---

## A customer administrator cannot assign roles in system properties on Service Portal.

  

### Issue

A customer administrator (sn\_customerservice.customer\_admin role) cannot assign roles listed in the system properties (sn\_customerservice.contact\_role\_assignment) on Service Portal.

Steps to reproduce:

1.  Go to **Customer Service** > **Administration** \> **Properties** (sn\_customerservice.contact\_role\_assignment system property)
2.  The list of roles in **External roles that can be assigned to contacts via Customer portal** should be available to edit on CSM.
3.  Impersonate a user who has the customer admin (sn\_customerservice.customer\_admin) role.
4.  Go to **/csm**
5.  Go to **Support** \> **Contacts**
6.  Select any contact to edit.
7.  Select **Edit Role**.

Following these steps, only sn\_customerservice.customer and sn\_customerservice.customer\_admin are available. The admin cannot see the Partner administrator role (sn\_customerservice.partner\_admin) or the Partner role (sn\_customerservice.partner).

### Release

Any version

### Cause

The roles availability depends on the configuration of the account that the contact belongs to.

If the account is configured only as a customer then partner roles would not be available in **Edit Role**.

### Resolution

To check if the account is a customer or Partner, follow these steps:

1.  Go to **Customer service** > **Contact**
2.  Open the contact (user) to check the account this contact belongs to.
3.  Go to **Customer** \> **Account**
4.  Open the account to see which checkbox is selected: Customer or Partner
