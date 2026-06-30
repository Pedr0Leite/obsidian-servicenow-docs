---
title: Using Workplace Space Mapping
description: With Workplace Space Mapping, your organization can integrate with third-party applications such as Mappedin, customize imported maps, and manage the required data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/employee-service-management/wsm-using-workplace-space-mapping.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Workplace Space Mapping, Workplace Service Delivery, Employee Service Management]
---

# Using Workplace Space Mapping

With Workplace Space Mapping, your organization can integrate with third-party applications such as Mappedin, customize imported maps, and manage the required data.

## View interactive location directories

You can view your imported map in interactive location directories.

## Type mappings

When you integrate with a indoor map provider - [[Indoor-mapping|Indoor Mapping]] or Mappedin, you must first associate the map types to the map types used by [[workplace-service-delivery-suite-landing-page|Workplace Service Delivery]]. This association ensures that your spaces are imported to the correct table with the correct type \(Workplace and Desk\).

-   Indoor Mapping provides inbuilt indoor maps for indoor navigation and wayfinding. Synchronize Indoor Mapping place types with Workplace Indoor Mapping places and spaces. [[configure-ind-mapping|Configure Indoor Mapping]] place and place type in the Map studio and then import the map objects and place types in Workplace Indoor Mapping. After the map data and map objects are synchronized, use [[workplace-services-portal-hr|Workplace Service Portal]] for managing reservations within workplace, [[case-management-workspace|case management]], and [[move-mgmt|move management]]. For more information, see [Synchronize Indoor Mapping with Workplace Service Delivery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/indoor-mapping/synchronize-ind-mapping-wsd.md).
-   Mappedin is a third party map provider and provides indoor maps and wayfinding for workplace users. For more information on how type mappings are converted from Mappedin to Workplace Space Mapping, see [[wsm-mappedin-type-table|Convert Mappedin data to Workplace Space Mapping data]].
-   For more information on maintaining type mappings for Mappedin, see [[wsm-mappedin-type-mappings|Maintain type mappings]].

## Import flow

The weekly \(Saturday\) **Auto-Import Buildings** iHub Flow keeps your map up to date by querying the API of your integrated applications. Any changes to one building in the application's software should be reflected in Workplace Space Mapping.

For example, if you integrate with Mappedin and the Auto-import Buildings iHub Flow runs successfully:

-   The Auto-Import Buildings iHub Flow queries for all buildings associated with Mappedin.
-   The Auto-Import Buildings iHub Flow works with the Mappedin export API to look for any changes to a building made by Mappedin. If there are changes, the building is updated.

## External IDs

Use external IDs to resolve spaces that don't match locations between Workplace Service Delivery Mappedin after importing a building or for existing buildings. For more information, see [[wsm-mappedin-ext-ids|Use external IDs to match spaces between Workplace Service Delivery for Mappedin]].

## Configuring map properties

Configure map properties to customize the way your map renders in the Workplace Service Portal location directory. For more information, see [[wsm-configure-map-properties|Customize the map properties]]. For more information about space update and allocation using interactive floor maps, see Map-based Administration [Edit a building's spaces using a map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-central/edit-space-details-for-buildings.md).

-   **[Use external IDs to match spaces between Workplace Service Delivery for Mappedin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/wsm-mappedin-ext-ids.md)**  
After importing a new Mappedin building or after importing an existing Mappedin building, if the locations don't match in Mappedin and Workplace Service Delivery, then use external IDs to resolve space location issues.

**Parent Topic:**[[wsm-mappedin-admin|Workplace Space Mapping]]

## Related

- [[wsm-mappedin-type-table|Convert Mappedin data to Workplace Space Mapping data]]
- [[wsm-mappedin-type-mappings|Maintain type mappings]]
- [[wsm-mappedin-ext-ids|Use external IDs to match spaces between Workplace Service Delivery for Mappedin]]
- [[wsm-configure-map-properties|Customize the map properties]]
- [[wsm-mappedin-admin|Workplace Space Mapping]]
- [[Indoor-mapping|Indoor Mapping]]
- [[workplace-service-delivery-suite-landing-page|Workplace Service Delivery]]
- [[configure-ind-mapping|Configure Indoor Mapping]]
- [[workplace-services-portal-hr|Workplace Service Portal]]
- [[case-management-workspace|Case management]]
- [[move-mgmt|Move Management]]
