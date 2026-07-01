---
title: Domain separation and Legal Service Delivery
description: Domain separation is supported for applications in Legal Service Delivery. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/legal-service-delivery/legal-domain-separation.html
release: australia
product: Legal Service Delivery
classification: legal-service-delivery
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Legal Service Delivery, Legal and Contract Operations, Employee Service Management]
tags:
  - employee-service-management
  - lsd
  - legal
  - service-delivery
  - cases
  - type-concept
---

# Domain separation and Legal Service Delivery

Domain separation is supported for applications in [[legal-management-overview|Legal Service Delivery]]. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.

## Support level: Basic



-   Business logic: Ensure that data goes into the proper domain for the application’s service provider use cases.
-   The application supports domain separation at run time. The domain separation includes separation from the user interface, cache keys, reporting, rollups, and aggregations.
-   The owner of the instance must set up the application to function across multiple tenants.

Sample use case: When a service provider \(SP\) uses chat to respond to a tenant-customer’s message, the customer must be able to see the SP's response.

For more information on support levels, see [Application support for domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-separated-apps.md).

## Legal Service Delivery overview

Legal Service Delivery includes the following applications:

-   [[legal-request-management-landing-page|Legal Request Management]]
-   [[legal-matter-management-landing-page|Legal Matter Management]]
-   [Gifts and Entertainment Compliance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-gifts-and-entertainment/lsd-ge-landing-page.md)
-   [[legal-conflict-of-interest-landing-page|Legal Conflict of Interest]]
-   [[legal-digital-forensics-landing-page|Legal Digital Forensics]]
-   [Legal Invention Disclosure](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-invention-disclosure/legal-invention-disclosure-landing.md)
-   [Legal Investigations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-investigations/legal-investigations-landing-page.md)
-   [[legal-simple-contracts-landing-page|Legal Simple Contracts]]
-   [Legal Simple Privacy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-simple-privacy/legal-simple-privacy-landing-page.md)
-   [[legal-stock-preclearance-landing-page|Legal Stock Preclearance]]

All tables installed with the following applications can be domain-separated:

-   Legal Request Management
-   Legal Matter Management
-   [Gifts and Entertainment Compliance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-gifts-and-entertainment/lsd-ge-landing-page.md)
-   Legal Conflict of Interest
-   Legal Digital Forensics
-   [Legal Invention Disclosure](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-invention-disclosure/legal-invention-disclosure-landing.md)
-   [Legal Investigations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-investigations/legal-investigations-landing-page.md)
-   Legal Simple Contracts
-   [Legal Simple Privacy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-simple-privacy/legal-simple-privacy-landing-page.md)
-   Legal Stock Preclearance

## How domain separation works in Legal Service Delivery

-   If an employee submits a legal service request, the request can be assigned to legal department users who are in the same domain as the employee.
-   Lawyers or paralegal staff can work only on those legal requests that have been created within the domain that they belong to.

**Related topics**  


[Domain separation for service providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-sep-landing-page.md)

## Related

- [[legal-management-overview|Legal Service Delivery]]
- [[legal-request-management-landing-page|Legal Request Management]]
- [[legal-matter-management-landing-page|Legal Matter Management]]
- [[legal-conflict-of-interest-landing-page|Legal Conflict of Interest]]
- [[legal-digital-forensics-landing-page|Legal Digital Forensics]]
- [[legal-simple-contracts-landing-page|Legal Simple Contracts]]
- [[legal-stock-preclearance-landing-page|Legal Stock Preclearance]]
