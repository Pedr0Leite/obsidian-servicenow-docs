---
title: "The get_lat_long business rule is not populating latitude and longitude"
aliases:
  - KB0522699
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522699
kb_number: KB0522699
last_modified: 2025-10-02
---

## The get\_lat\_long business rule is not populating latitude and longitude

  

### Issue

The get\_lat\_long business rule, which queries Google Maps, does not populate the latitude and longitude fields for a new location in the Location \[cmn\_location\] table. This business rule is included in the base system and is used to obtain the latitude and longitude of an address for a location record.

### Release

Any

### Resolution

Due to a change in relevant terms of service, a new framework is in place that allows users to take advantage of the global longitude and latitude functionality by obtaining the appropriate license key from Google or other geocoding services such as Yahoo, Bing!, US Govt. For information regarding the change in TOS from Google Maps API, please refer to [Set up Google Maps API](https://docs.servicenow.com/csh?topicname=set-up-google-maps-api.html&version=latest "Set up Google Maps API") in the ServiceNow product documentation.

Alternatively, other geocoding services can be used to take advantage of the auto-population of longitude and latitude. There is no specific recommendation as to which service to use; however, the framework of using HTTPAdaptor will remain basically the same.
