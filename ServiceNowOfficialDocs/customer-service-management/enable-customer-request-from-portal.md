---
title: Enable external customers to create requests
description: Enable your external customers to create and track requests from the Customer and Consumer Service Portals.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/enable-customer-request-from-portal.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Setting up CSM integration with IT Service Management, Integrate with IT Service Management, Integrate, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Enable external customers to create requests

Enable your external customers to create and track requests from the Customer and Consumer Service Portals.

## Before you begin

Role required: admin

## About this task

Each submitted request generates a case, with the request record associated to that case. Customer service agents can also create requests on behalf of contacts and consumers.

**Note:** This feature requires activation of the Customer Service with Request Management plugin \(com.sn\_cs\_sm\_request\).

## Procedure

-   Configure the [[r_CustomerServiceCaseForm|Case form]] to display the **Initiated as request** field.

    When a request is created from the portal, the system creates a case for the request and sets this field to true.

    **Note:** The **Initiated as request** field is read-only for all users.


**Related topics**  


[[agent-create-request-for-customer|Create a request on behalf of a customer or consumer]]

[[customer-request-from-portal|Request an item or service from the Customer Service Portal]]

## Related

- [[agent-create-request-for-customer|Create a request on behalf of a customer or consumer]]
- [[customer-request-from-portal|Request an item or service from the Customer Service Portal]]
- [[r_CustomerServiceCaseForm|Case form]]
