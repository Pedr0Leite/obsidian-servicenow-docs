---
title: Customer-created maps
description: Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-management-for-the-enterprise/r\_Manually-builtMaps.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
tags:
  - service-management-for-the-enterprise
  - type-reference
---

# Customer-created maps

Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.

-   **[[c_SpaceRollupCalculations|Space roll up calculations]]**  
The [[FacilitiesLandingPage|Facilities Service Management]] application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups apply to spaces that are designated as 'occupiable'. The occupancy values from that space are rolled up to the level above them.
-   **[[t_AddOrEditACampus|Add or edit a campus]]**  
A campus represents the top level in the organization space, and contains buildings and map sets. Details include its location, manager, gross area, and usable area. Occupancy and utilization metrics are calculated using these details.
-   **[[t_AddOrEditABuilding|Add or edit a building]]**  
Buildings are assigned to campuses with a unique name, and contain floors or levels, a location, and utilization thresholds.
-   **[[t_AddOrEditAFloorOrLevel|Add or edit a floor or level]]**  
A floor is a level in a structure that contains spaces. It can be a floor of a building, the basement, levels in a parking lot, or outdoor areas.
-   **[[t_AddOrEditASpace|Add or edit a space]]**  
Spaces are assigned to floors or levels, and can be cubicles, conference rooms, restrooms, gymnasiums, elevators, parking spaces, and so on. Spaces are assigned users and assets, and have the most data defined.
-   **[[t_AddOrEditAZone|Add or edit a zone]]**  
Zones are a logical collection of spaces that can be shared across campuses, floors, or buildings. Examples of zones are: Chiller 4 Zone, Guest Wi-Fi Zone, AC 1 Zone, Power Circuit 3 Zone, and so on.
-   **[[t_DeleteACampus|Delete a campus]]**  
Delete all buildings assigned to a campus, before deleting the campus itself.
-   **[[t_DeleteABuilding|Delete a building]]**  
Before deleting a building, delete any floors or levels defined for it.
-   **[[t_DeleteAFloorOrLevel|Delete a floor or level]]**  
Before you can delete a floor, you must first delete any spaces defined for it.
-   **[[t_DeleteASpace|Delete a space]]**  
Spaces can be deleted from any floor or from another space as long as the space you want to remove does not have other spaces associated with it. For example, if you want to delete a space that contains several offices, those spaces must be deleted before the parent space can be deleted.
-   **[[t_DeleteAZone|Delete a zone]]**  
When deleting a zone, any associated assets or spaces is also deleted.

**Parent Topic:**[[r_SpaceManagement|Space management]]

## Related

- [[c_SpaceRollupCalculations|Space roll up calculations]]
- [[t_AddOrEditACampus|Add or edit a campus]]
- [[t_AddOrEditABuilding|Add or edit a building]]
- [[t_AddOrEditAFloorOrLevel|Add or edit a floor or level]]
- [[t_AddOrEditASpace|Add or edit a space]]
- [[t_AddOrEditAZone|t_AddOrEditAZone]]
- [[t_DeleteACampus|Delete a campus]]
- [[t_DeleteABuilding|Delete a building]]
- [[t_DeleteAFloorOrLevel|Delete a floor or level]]
- [[t_DeleteASpace|Delete a space]]
- [[t_DeleteAZone|Delete a zone]]
- [[r_SpaceManagement|Space management]]
- [[FacilitiesLandingPage|Facilities Service Management]]
