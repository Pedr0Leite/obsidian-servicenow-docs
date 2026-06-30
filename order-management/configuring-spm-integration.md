---
title: Configuring the Strategic Portfolio Management integration
description: Configure the Strategic Portfolio Management integration so that order delivery tasks in Order Management can be tracked as planned project tasks in SPM.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-spm-integration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Order Management integration with Strategic Portfolio Management, Integrate, Sales Customer Relationship Management]
---

# Configuring the Strategic Portfolio Management integration

Configure the Strategic Portfolio Management integration so that order delivery tasks in [[explore-order-management|Order Management]] can be tracked as planned project tasks in SPM.

As an admin, follow these tasks to set up the SPM integration.

<table id="table_n2l_dcy_qxb"><thead><tr><th>

Configuration step

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Activate PPM Standard \(Project Portfolio Management\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/t_ActivateProjectPortfolioSuiteWithFinancials.md)

</td><td>

Install the PPM Standard \(com.snc.financial\_planning\_pmo\) plugin. If you're tracking customer projects, you must also activate the Customer Project Management \(com.snc.csm\_ppm\) plugin. For information on setting up Customer Project Management, see [Integrate with Customer Project Management using Guided Setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/csm-ppm-configuration.md).

**Note:** If you installed the Order Management application before activating the PPM Standard or Customer Project Management plugins, you must repair the Order Management \(com.sn\_ind\_tmt\_orm\) plugin to get the plugin-dependent updates and demo data for the SPM integration.

</td></tr><tr><td>

[[creating-project-templates-orders|Create project templates and project template tasks]]

</td><td>

Use the Project Portfolio Management application to create the project templates for order lines and project template tasks for domain orders and order tasks.

</td></tr><tr><td>

[[configure-project-table-mapping|Configure field mapping between orders and projects]]

</td><td>

Configure the CSM table maps to associate [[fields|fields]] in order lines, domain orders, and order tasks to projects and programs in SPM.

</td></tr><tr><td>

[[setting-up-project-oversight|Set up project oversight conditions and decision rules]]

</td><td>

Configure the conditions and decision [[rules_101|rules]] for determining the order lines, domain orders, and order tasks that qualify for project management and order tasks that qualify for project management oversight. You also specify the project templates to be used to create those projects.

</td></tr><tr><td>

[[control-auto-closure-proj-tasks|Control the automatic closure of project tasks]]

</td><td>

Manage the automatic closure of project tasks when related child tasks are completed or cancelled.

</td></tr></tbody>
</table>

## Related

- [[creating-project-templates-orders|Creating project templates and project template tasks]]
- [[configure-project-table-mapping|Configure field mappings]]
- [[setting-up-project-oversight|Setting up project oversight conditions and decision rules]]
- [[control-auto-closure-proj-tasks|Control automatic closure of project tasks]]
- [[explore-order-management|Order management]]
- [[fields|Fields]]
- [[rules_101|Rules]]
