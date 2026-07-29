---
title: "Users can't select a timeslot for their Vaccine Appointments"
aliases:
  - KB0956924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0956924
kb_number: KB0956924
last_modified: 2024-02-16
---

## Users can't select a timeslot for their Vaccine Appointments

  

### Issue

Seeing that **no calendar** is shown to the User when trying to book a **Vaccine Appointment**.

  

**Prerequisite:**

-   The **'sn\_vaccine\_sm.enable\_appointment\_slot\_choice'** **System Property** must be set to **true**

  

### Cause

-   Either the **System Property** to **enable this functionality** is **not active** on the instance.
-   Or, the **Portal Widget / Page** has been **customised** and missed an upgrade which has prevented the new **Time Slot Booking Functionality** from being created on the system.

### Resolution

1.  Please check the **'sn\_vaccine\_sm.enable\_appointment\_slot\_choice' System Property** and ensure that this is set to **true**.
2.  If it **is set to true**, then you should check your **Vaccine Booking Details \[sp\_widget\]** and **Vaccine Booking \[sp\_page\]** to ensure that they are **not missing upgrades**.
3.  These should be **reverted** to **Out Of Box** and have any customisations **re-applied** as needed.
