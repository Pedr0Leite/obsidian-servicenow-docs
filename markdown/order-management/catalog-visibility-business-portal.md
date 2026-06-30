---
title: Configuring product catalog visibility on the Business Portal
description: Only authorized customers can view the product catalog on the Business Portal by default. After setting up your product catalog and pricing, use the CustomerPortalCatalogAccessUtil script include to extend catalog visibility to additional users.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/catalog-visibility-business-portal.html
release: australia
topic_type: concept
last_updated: "2026-03-17"
reading_time_minutes: 1
breadcrumb: [Business Portal, Configure, Sales Customer Relationship Management]
---

# Configuring product catalog visibility on the Business Portal

Only authorized customers can view the product catalog on the Business Portal by default. After setting up your product catalog and pricing, use the CustomerPortalCatalogAccessUtil script include to extend catalog visibility to additional users.

When customers [[order-management-access-the-business-portal|access the Business Portal]], the product catalog is visible by default to users who have the sn\_customerservice.customer role and are registered in the ServiceNow CRM software. This default visibility is controlled by the CustomerPortalCatalogAccessUtil script.

To grant product catalog visibility to other users, use the CustomerPortalCatalogAccessUtil script to extend access to those users. Navigate to **All** &gt; **Activity Subscriptions** &gt; **Administration** &gt; **Script Includes**. In the **Name** column, search for CustomerPortalCatalogAccessUtil.

You must also set up your product catalog and configure pricing to help ensure that the correct products and prices are available to customers on the portal. For more information, see [[som-managing-product-catalogs|Configuring product offerings and catalogs]] and [[som-managing-product-pricing|Configuring product pricing]].

**Related topics**  


[[som-self-service-business-portal|Customer self-service for Sales Customer Relationship Management]]

[[order-mgt-business-portal|Customer self-service using the Business Portal]]

## Related

- [[som-managing-product-catalogs|Configuring product offerings and catalogs]]
- [[som-managing-product-pricing|Configuring product pricing]]
- [[som-self-service-business-portal|Customer self-service for Sales Customer Relationship Management]]
- [[order-mgt-business-portal|Customer self-service using the Business Portal]]
- [[order-management-access-the-business-portal|Access the Business Portal]]
