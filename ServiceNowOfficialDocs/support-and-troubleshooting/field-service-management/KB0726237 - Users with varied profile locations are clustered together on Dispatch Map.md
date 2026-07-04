---
title: "Users with varied profile locations are clustered together on Dispatch Map"
aliases:
  - KB0726237
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726237
kb_number: KB0726237
last_modified: 2024-04-07
---

## Users with varied profile locations are clustered together on Dispatch Map

  

### Issue

# Symptoms

* * *

When users have different locations given in their respective profiles they are clustered together at the same location on the Dispatcher's map.

# Release

* * *

Madrid

# Cause

* * *

**\->** Agent (Users) locations get picked up from their latest locations in the geolocation history table (geo\_history) when "Geolocation Tracked" field was checked true in their sys\_user records.   
  

# Resolution

* * *

**\->** Make sure geo\_history table entries for the affected users have no address, no latitude, and no longitude (blanked out these fields) then the users would no longer be clustered and appear to be showing up on the Dispatch Map based on their user profile locations.

**Note:** This solution works for the use-case when we are interested to use the location of users based on their sys\_user record.

# Additional Information

* * *

[Geolocation History](https://docs.servicenow.com/csh?topicname=r_GeolocationHistory.html&version=latest "Geolocation History")

[Location Tracking](https://docs.servicenow.com/csh?topicname=r_LocationTracking.html&version=latest "Location Tracking")
