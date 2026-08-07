---
title: "Users with the sn_customerservice roles are not able to see company cases"
aliases:
  - KB0718506
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718506
kb_number: KB0718506
last_modified: 2026-06-03
---

## Users with the sn\_customerservice roles are not able to see company cases

  

### Issue

 

Users with the sn\_customerservice.customer role can submit a case (sn\_customerservice\_case) through the portal, but after submission they cannot view the case and receive a "Record not found" error.

Users with the sn\_customerservice.customer\_admin role cannot view all cases associated with their company.

### Release

  N/A

### Cause

The Contact field on the sn\_customerservice\_case record is empty and is not populated with the user who submitted the case.

The Company field on the customer\_contact or sys\_user record is not populated.

Access is restricted by the out-of-box business rule "Case query for customer", which is working as designed.

### Resolution

This behavior is expected when the Contact field on the sn\_customerservice\_case record is not populated with the user who submitted the case.

The "Case query for customer" business rule applies the following access rules:

### 1\. Users with the sn\_customerservice.customer role

Can view:

-   All cases where contact = logged-in user

Query:

```
contact=<logged-in user ID>
```

### 2\. Users with the sn\_customerservice.partner role

Can view:

-   All cases where contact = logged-in user
-   All cases where partner\_contact = logged-in user

Query:

```
(contact=<logged-in user ID>) OR (partner_contact=<logged-in user ID>)
```

### 3\. Users with the sn\_customerservice.partner\_admin role

Can view:

-   All cases where contact = logged-in user
-   All cases where partner = my company
-   All cases from my company hierarchy
-   All cases for accounts from contact relationships

Query:

```
(contact=<logged-in user ID>)
OR (partner=<my account>)
OR (account.account_path=<my account path>)
OR (account IN <all accounts from my contact relationship>)
```

### 4\. Users with the sn\_customerservice.customer\_admin role

Can view:

-   All cases where contact = logged-in user
-   All cases from my company hierarchy
-   All cases for accounts from contact relationships

Query:

```
(contact=<logged-in user ID>)
OR (account.account_path=<my account path>)
OR (account IN <all accounts from my contact relationship>)
```

### Related Links

[Customer Service Management Roles and FAQs](https://hi.service-now.com/kb_view.do?sys_kb_id=0330bab5db4cafc0a39a0b55ca961912 "Customer Service Management Roles and FAQs")
