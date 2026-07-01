---
title: Community file
description: The community file contains information about the campus, including the number of buildings and the number of floors for each building.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-management-for-the-enterprise/r\_CommunityFile.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Community file

The community file contains information about the campus, including the number of buildings and the number of floors for each building.

The file naming standard is:

-   Must begin with `map`
-   Must contain `-geojson-com-map-`

For example, `map-23641-mv-1-ev-1-geojson-com-map-fv-2.json`

-   **[[r_CampusInfo|Campus information]]**  
Sample code for campus and map set properties.
-   **[[r_BuildingInfo|Building information]]**  
Each drawing in the campus map file represents a building or campus overview. The campus overview is a map that shows the entire campus, and is included for multi-building campuses only.
-   **[[r_LevelInfo|Level information]]**  
Each building \(drawing\) has a list of levels. Each level is a map and represents one floor, though that is not a rule.

**Parent Topic:**[[r_GeoJSONMapFiles|GeoJSON map files]]

## Related

- [[r_CampusInfo|Campus information]]
- [[r_BuildingInfo|Building information]]
- [[r_LevelInfo|Level information]]
- [[r_GeoJSONMapFiles|GeoJSON map files]]
