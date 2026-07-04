---
title: "Unable to Create New Program under Vaccine Administration Program"
aliases:
  - KB0963782
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963782
kb_number: KB0963782
last_modified: 2024-05-08
---

## Unable to Create New Program under Vaccine Administration Program

  

### Issue

You are finding that the **New Program** you created is not allowing **Users** to book appointments from the **VAM Portal**.

### Cause

This is the **expected System Behaviour** in this scenario.

Currently the **Vaccine Administration Management Product** will only support **1 Active Program** and therefore it will not be working if there is more than **1 Active Program**.

  

The current functionality is based around the **Default Program** which is set in the **Vaccine Properties** and the Portal will only be allowing bookings for the **Program** which is defined in this property.

You can see the related **"vaccine.management.default\_program" System Property** in your instance to validate this.

### Resolution

Since this functionality is not currently part of the **Vaccine Administration Management Product** then you will need to perform one of the following:

1.  Revert to using just **1 Active Program**
2.  Apply **customisations** to **Out Of Box Code** so that it will support **Multiple Programs**
