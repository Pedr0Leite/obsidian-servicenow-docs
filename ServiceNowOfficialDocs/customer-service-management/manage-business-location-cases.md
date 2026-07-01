---
title: Create and manage cases for a business location
description: As a staff member with the location agent role, create and manage cases for your business locations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/manage-business-location-cases.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Business locations, Configure Service Model Foundation, Data models, Set up your environment, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create and manage cases for a business location

As a staff member with the location agent role, create and [[manage-cases|manage cases]] for your business locations.

## Before you begin

Role required: admin, sn\_customerservice.svc\_location\_agent, and sn\_customerservice.svc\_location\_manager

## About this task

Staff members with the location agent role can do the following:

-   View information for the customers at their location.
-   Create cases for the accounts, contacts, households, and consumers at their location.
-   [[import-create-csm-consumers|Create consumers]].
-   Update cases created at their location.

A case belongs to one business location. When a case is created by a location agent or manager, the **Service Organization** field on the Case form is automatically updated with the business location that the agent or manager belongs to. If the case is reassigned, this field is updated to show the new agent or manager.

If the location agent or manager belongs to multiple locations, the **Service Organization** field may be kept empty. When you fill in this field, make your selection carefully because the service organization controls a location agent's access to cases.

The **Service Organization** can be set manually for a new case or changed for an existing case. Changing the **Service Organization** doesn’t change the assigned agent.

Location agents and managers can create cases for business locations without adding an account, contact, or consumer. The location agent or manager who creates the case is added to the **Opened by** field.

## Procedure

1.  Navigate to **All** &gt; **Customer Service** &gt; **Cases** and select **Create New**.

2.  Select the type of case that you want to create.

3.  On the form, fill in the fields.

    For a description of the field values, see [[r_CustomerServiceCaseForm|Case form]].

4.  Select **Submit**.


**Related topics**  


[[industry-data-model-cases|Service Model Foundation cases]]

[[csm-assign-responsibilities|Assign responsibilities]]

[[configure-data-model-roles|Assign roles]]

[[t_CreateACaseFromCustServApp|Create a customer service case]]

## Related

- [[r_CustomerServiceCaseForm|Case form]]
- [[industry-data-model-cases|Service Model Foundation cases]]
- [[csm-assign-responsibilities|Assign responsibilities]]
- [[configure-data-model-roles|Assign roles]]
- [[t_CreateACaseFromCustServApp|Create a customer service case]]
- [[manage-cases|Manage cases]]
- [[import-create-csm-consumers|Create consumers]]
