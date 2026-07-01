---
title: Setting up Workplace Space Mapping
description: Configure and synchronize Indoor Mapping and Mappedin map data and objects with Workplace Service Delivery.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/set-up-workplace-service-mapping.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure, Workplace Space Mapping, Workplace Service Delivery, Employee Service Management]
tags:
  - employee-service-management
  - type-concept
---

# Setting up Workplace Space Mapping

Configure and synchronize [[Indoor-mapping|Indoor Mapping]] and Mappedin map data and objects with [[workplace-service-delivery-suite-landing-page|Workplace Service Delivery]].

## Activating Workplace Space Mapping

Activation of the [[wsm-mappedin-admin|Workplace Space Mapping]] plugin depends on what family release you are currently using.

For Workplace Service Delivery to work with Workplace Indoor Mapping and Mappedin install both Indoor Mapping and Workplace Indoor Mapping plugins from store. For Mappedin install the Mappedin plugin \(sn\_wsd\_mappedin\) from store.

## Configure Indoor Mapping with Workplace Service Delivery

Synchronize the Indoor Mapping map data and map objects to work with Workplace Service Delivery, see [[wsd-integration-indoor-mapping|Configure Workplace Indoor Mapping]].

## Configure Mappedin with Workplace Service Delivery

To use Mappedin as your third-party map application, complete the configuration requirements.

<table id="table_xwx_ffn_trb"><thead><tr><th>

Requirement

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Obtain Mappedin credentials and export credentials

</td><td>

ServiceNow uses credentials provided by MappedIn to import space data \(buildings, floors, and spaces\).

 Export credentials are required by the ServiceNow AI Platform to render a Mappedin map and to successfully periodically reimport updated floor plans.

 -   The Client ID credential is the equivalent of a user name in [[workplace-safety-mgmt-hr|Workplace Core]]
-   The Client Secret is the equivalent a password in Workplace Core

</td></tr><tr><td>

Install and activate the Mappedin integration

</td><td>

Install and activate the Mappedin integration in order to use Workplace Space Mapping to manage imported data and customize the map. For more information, see [[wsm-mappedin-activate|Install the Mappedin integration]]

</td></tr><tr><td>

Enter credentials in Workplace Space Mapping

</td><td>

You must enter your Mappedin credentials in Workplace Space Mapping. For more [[wsm-mappedin-credentials|Maintain Workplace Service Delivery Mappedin credentials]]

</td></tr><tr><td>

Configure a connection in Workplace Space Mapping

</td><td>

The base system provides a pre-configured connection to Mappedin.

</td></tr></tbody>
</table>-   **[Maintain Workplace Service Delivery Mappedin credentials](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/wsm-mappedin-credentials.md)**  
To configure and work with Mappedin ensure that you have a valid login credential. Work with the Mappedin to obtain these credentials.
-   **[[wsm-configure-map-properties|Customize the map properties]]**  
Customize how your map renders in the [[workplace-services-portal-hr|Workplace Service Portal]] by configuring Workplace Space Mapping properties.

**Parent Topic:**[[wsm-config_space_mapping|Configuring Workplace Space Mapping]]

**Related topics**  


[Configure Workplace Indoor Mapping]()

[Configure Mappedin]()

## Related

- [[wsd-integration-indoor-mapping|Configure Workplace Indoor Mapping]]
- [[wsm-mappedin-activate|Install the Mappedin integration]]
- [[wsm-mappedin-credentials|Maintain Workplace Service Delivery Mappedin credentials]]
- [[wsm-configure-map-properties|Customize the map properties]]
- [[wsm-config_space_mapping|Configuring Workplace Space Mapping]]
- [[Indoor-mapping|Indoor Mapping]]
- [[workplace-service-delivery-suite-landing-page|Workplace Service Delivery]]
- [[wsm-mappedin-admin|Workplace Space Mapping]]
- [[workplace-safety-mgmt-hr|Workplace Core]]
- [[workplace-services-portal-hr|Workplace Service Portal]]
