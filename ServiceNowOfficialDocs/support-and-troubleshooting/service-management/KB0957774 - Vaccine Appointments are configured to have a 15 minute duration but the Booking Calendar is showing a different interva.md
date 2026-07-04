---
title: "Vaccine Appointments are configured to have a 15 minute duration but the Booking Calendar is showing a different interval"
aliases:
  - KB0957774
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957774
kb_number: KB0957774
last_modified: 2024-02-24
---

## Vaccine Appointments are configured to have a 15 minute duration but the Booking Calendar is showing a different interval

  

### Issue

You have set your **Vaccine Appointment Configurations** so that the **Vaccine Appointments** have a **Duration** of **15 minutes**.

However, when using the **Booking Calendar** (In **Reschedule Appointment**) you are seeing there is a **30 minute interval** (or other) on the calendar.

### Cause

This is because the **"sn\_vaccine\_sm.enable\_vam\_appointment\_config" System Property** is not **enabled** on your instance.

Therefore it is not using the advanced appointment configurations which have been set up.

  

#### Prerequisite:

-   You must have **Version 4.0.5** or **later** of **Vaccine Administration Management** in order to enable this functionality.

### Resolution

Please **enable** the **"sn\_vaccine\_sm.enable\_vam\_appointment\_config"** **System Property** to use this functionality.

Once it is **enabled**, be sure that you **avoid disabling it** since this could cause some data inconsistencies in regards to appointment times.

  

#### Steps To Resolution:

1.  Navigate to **Vaccine Administration Management > Administration > Properties**
2.  Set the **"Enables location specific Appointment configuration for Vaccine Administration Management." Property** to **true**
3.  Click **Save**
