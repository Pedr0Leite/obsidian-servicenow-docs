---
title: Configuring Lead-to-Cash Process Management
description: Plan and configure your implementation of Lead-to-Cash Process Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-lead-cash-process-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [sales cockpit]
breadcrumb: [Order operations apps, Configure, Sales Customer Relationship Management]
---

# Configuring Lead-to-Cash Process Management

Plan and configure your implementation of Lead-to-Cash Process Management.

## Configuration overview

1.  Review the dependencies for installing and using Lead-to-Cash Process Management.
    -   For sales process managers to be able to create and monitor sales process records through the CSM Configurable WorkspaceCustomer Service Management \(CSM\) must be installed.
    -   To be able to monitor opportunities, quotes, or orders in the sales process, you must have [[opportunity-management|Opportunity Management]], [[quote-management|Quote Management]], [[explore-order-management|Order Management]] installed.
    -   Business Object Core \(sn\_bo\_core\) is automatically installed as a dependency when you install the Lead-to-Cash Process Management application \(app-l2c-cockpit\).
2.  [[install-lead-cash-process-management|Install Lead-to-Cash Process Management]]

    You can install the Lead-to-Cash Process Management application \(app-l2c-cockpit\) if you have the admin role. The application installs related ServiceNow® Store applications and plugins if they aren’t already installed. Install Lead-to-Cash Process Management on each of your environments.

3.  [[assign-roles-lead-cash-process-management|Assign roles to Lead-to-Cash Process Management users]]

    Assign roles to your users so that they can access features, capabilities, and data in the Lead-to-Cash Process Management application.

4.  [[create-business-object-group-define-entity-relationship|Set up business objects for sales process records]]

    Create business object group and business object types. Define relationships between the business object types, and add them as members under the business object group. This enables the sales process managers to create sales process records using these entities.

5.  [[customizing-sales-process-dashboard|Customizing the sales process dashboard]]

    Define the number of levels and tile content on the node map, and determine how tasks are consolidated on the Tasks tab, to enhance clarity and control so sales process managers can focus on relevant data and navigate through complex sales processes effectively.

6.  [[modifying-table-cleanup-policy-l2c-process-management|Modifying data retention and table cleanup policy for Lead-to-Cash Process Management]]

    Access and [[Modify|modify]] the default data retention and table cleanup policy to modify it to suit your needs.

7.  [[enabling-email-l2c-process-management|Setting conditions for enabling email access in Lead-to-Cash Process Management]]

    Sales process managers can [[lead-management-use-emails-tab|compose emails]] directly from the dashboard for sales entity records that are monitored in a sales process record.


**Related topics**  


[[explore-lead-cash-process-management|Lead-to-Cash Process Management]]

[[using-lead-cash-process-management|Using Lead-to-Cash Process Management]]

## Related

- [[install-lead-cash-process-management|Install Lead-to-Cash Process Management]]
- [[assign-roles-lead-cash-process-management|Assign roles to Lead-to-Cash Process Management users]]
- [[create-business-object-group-define-entity-relationship|Set up business objects for sales process records]]
- [[customizing-sales-process-dashboard|Customizing the sales process dashboard]]
- [[modifying-table-cleanup-policy-l2c-process-management|Modifying data retention and table cleanup policy for Lead-to-Cash Process Management]]
- [[enabling-email-l2c-process-management|Setting conditions for enabling email access in Lead-to-Cash Process Management]]
- [[explore-lead-cash-process-management|Lead-to-Cash Process Management]]
- [[using-lead-cash-process-management|Using Lead-to-Cash Process Management]]
- [[opportunity-management|Opportunity Management]]
- [[quote-management|Quote Management]]
- [[explore-order-management|Order management]]
- [[Modify|Modify]]
- [[lead-management-use-emails-tab|Compose emails]]
