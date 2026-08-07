---
title: JDBCProbe
description: A JDBC probe runs on the MID Server to query an external database via JDBC and returns results to ServiceNow.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/t\_JDBCProbe.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Supported integration interfaces, Integration options, Integration with third-party applications and data sources, Integrations, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# JDBCProbe

A JDBC probe runs on the MID Server to query an external database via JDBC and returns [[hs-results|results]] to ServiceNow.

## Before you begin

Role required: admin

## About this task

Probes interact with the MID Server through the ECC Queue. The JDBC probe response returns as an XML payload in an input ECC Queue record. By default, each response payload contains up to 200 rows. To change this limit, set the **jdbcprobe\_result\_set\_rows** probe parameter to the desired number.

Contact Customer Service and Support to activate the **Integration - JDBC** \(com.snc.integration.jdbc\) plugin.

## Procedure

1.  Navigate to **System Definition &gt; Plugins**.

2.  Right-click the plugin name on the list and select **Activate/Upgrade**.

    If the plugin depends on other plugins, these plugins and their activation status are listed.

3.  Select the **Load demo data** check box.

    Some plugins include demo data—sample records that are designed to illustrate plugin features for common use cases. Loading demo data is a good policy when first activating the plugin on a development or test instance. You can load demo data after the plugin is activated by repeating this process and selecting the check box.

4.  Select **Activate**.


-   **[[c_DirectJDBCProbe|Direct JDBC Probe]]**  
A direct JDBC probe specifies all the parameters necessary in the outbound ECC Queue XML payload.
-   **[[c_JDBCProbesViaDataSource|JDBC Probes via Data Source]]**  
JDBC probes are executed via a JDBC data source when an import is running against the data source.
-   **[[c_SelectJDBCProbeShortCut|Select \* JDBC Probe short cut]]**  
Alternatively, you may specify a **table\_name** parameter instead of a work element and the following query could be executed.
-   **[[r_DirectJDBCProbeParameters|Parameters]]**  
The following parameters are available in a direct JDBC probe.
-   **[[c_UsingTheWorkElement|Using the Work Element]]**  
The work element encodes SQL statements to be executed by the probe.

**Parent Topic:**[[r_SupportedIntegrationInterfaces|Supported integration interfaces]]

## Related

- [[c_DirectJDBCProbe|Direct JDBC Probe]]
- [[c_JDBCProbesViaDataSource|JDBC Probes via Data Source]]
- [[c_SelectJDBCProbeShortCut|Select \* JDBC Probe short cut]]
- [[r_DirectJDBCProbeParameters|Parameters]]
- [[c_UsingTheWorkElement|Using the Work Element]]
- [[r_SupportedIntegrationInterfaces|Supported integration interfaces]]
- [[hs-results|Results]]
