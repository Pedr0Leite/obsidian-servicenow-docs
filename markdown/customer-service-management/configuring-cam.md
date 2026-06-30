---
title: Configuring customer access management
description: Ensure that the customer access management is set up correctly for the user by completing all configuration tasks using the Customer Service Management \(CSM\) application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configuring-cam.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [User management, Set up your environment, Configure, Customer Service Management]
---

# Configuring customer access management

Ensure that the customer access management is set up correctly for the user by completing all configuration tasks using the [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) application.

## Overview of customer access management

Customer Access Management enables you to grant varying levels of access to different contacts and consumers for [[customer-data|customer data]], such as cases, [[sold-product|sold products]], and more. It also enables you to control internal user access based on their relationship with the customer.

As the needs of industry verticals grow, enterprises encounter complex use cases. There are use case scenarios where [[case-management|case management]] can be handled by more than one customer contact. For example, in a B2C scenario, let's assume that a loan applicant wants to add a co-borrower, guarantor, and an attorney to a housing loan application where everyone has the same level of access to respond to the loan application-related case. While in other cases, products purchased by a customer can have multiple departments tracking the product, like the finance team tracking the renewals of the product or the operations team tracking the maintenance of the product.

Customer access management enables enterprises across industry verticals such as hi-tech, telecommunications, financial services, government, and manufacturing to meet these complex use cases.

Customer access management helps customer service agents add multiple related parties and provides them with varying levels of access to a case. While adding related parties to a case, customer service agents can select the relationship type. The relationship type defaults the responsibility that drives the access level for the related parties, such as contacts or consumers on a case.

## Key benefits

Customer access management:

-   Improves the customer experience by enabling related parties to track and collaborate on cases
-   Improves operational efficiency by enabling customers to track cases for products and services
-   Increases automation by automatically granting access to cases based on access to the sold product

## Configuration tasks for customer access management

|Task|Description|
|----|-----------|
|[[csm-cust-access-mgmt-tables|Customer access management tables and plugins]].|Add new tables or modify existing tables to enable customer access management.|
|[[r_rolesinstalledwithcustaccessmgmt|Install roles with customer access management]].|Use different predefined functional and granular roles to establish relationships between users and entities.|
|[[t_CreateAResponsibilityDefinition|Create a responsibility definition]]|Define a role or responsibility that can support your organization and users in the Customer Service Management \(CSM\) application.|
|[[declarative-resposibility-framework|Configure access through the responsibility access configuration]]|Streamline how you create and update your responsibility definitions and access configurations by using the declarative responsibility framework in the Customer Service Management \(CSM\) application.|
|[[adding-related-party-config-to-case|Create related party configurations]].|Link related party entity responsibilities to responsibility definitions by adding related party configurations to a case.|

**Related topics**  


[[csm-data-management|Data management for Customer Service Management]]

[[using-cam|Using customer access management]]

## Related

- [[csm-cust-access-mgmt-tables|Customer access management tables and plugins]]
- [[r_rolesinstalledwithcustaccessmgmt|Roles installed with customer access management]]
- [[t_CreateAResponsibilityDefinition|Create a responsibility definition]]
- [[declarative-resposibility-framework|Configure access through the responsibility access configuration]]
- [[adding-related-party-config-to-case|Create related party configurations]]
- [[csm-data-management|Data management for Customer Service Management]]
- [[using-cam|Using customer access management]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[customer-data|Customer data]]
- [[sold-product|Sold products]]
- [[case-management|Case management]]
