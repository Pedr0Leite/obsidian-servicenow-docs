---
title: "Specific User can make a Workplace Reservation"
aliases:
  - KB1205512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1205512
kb_number: KB1205512
last_modified: 2025-10-13
---

## Specific User can make a Workplace Reservation

  

### Issue

A specific user can not make a reservation on WSD reservation portal.

The following error message is seen when submitting the reservation: "A reservation could not be created at the moment, please try again. Unable to make a reservation."

### Cause

The root cause of this issue is the length of the user name.

It seems that in the business rule (Available for validation), it is getting the userName by calling current.sys\_updated\_by.

The table's (sn\_wsd\_core\_reservation) "sys\_updated\_by" field can only take a string of a max length of 40 characters. In the case of an affected user, the username is more than the max length of the "sys\_updated\_by" field. This causes it to return only the partial username of this user.

This username is later used in the business rule to find the userId by checking against this partial username and returning null. Due to this, the business rule gets aborted and this user won't be able to book a reservation.

### Resolution

Update the business rule "Available for validation" to get the username from gs.getUserName() instead of current.sys\_updated\_by (line 5)

Business rule > Available for validation

https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=cccc5ee50f0220107f2bd2d92f767ec8
