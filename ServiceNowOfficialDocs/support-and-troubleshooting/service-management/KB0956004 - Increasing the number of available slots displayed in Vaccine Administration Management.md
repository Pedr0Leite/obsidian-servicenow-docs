---
title: "Increasing the number of available slots displayed in Vaccine Administration Management"
aliases:
  - KB0956004
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0956004
kb_number: KB0956004
last_modified: 2024-11-07
---

## Increasing the number of available slots displayed in Vaccine Administration Management

  

This article provides updated information on the processes currently documented in the following documentation topic located in docs.servicenow.com: [Configure advanced appointment scheduling for a center.](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/vaccine-management/task/configure-location-level-weekly-schedule-config.html)    

  
**Set future bookable max days to a higher value**

When you create a new Appointment configuration, the default value of **future bookable max days** is 14. This field controls how many future dates will be displayed to the user to book an appointment.

Keeping **future bookable max days** to 14 will prevent users from booking the second appointment if the lead time between both doses is higher than 14 days.

We suggest customers to set **future bookable max days** to a higher value according to their vaccination slot availability. We will increase the default value in the product to a higher value in future releases.
