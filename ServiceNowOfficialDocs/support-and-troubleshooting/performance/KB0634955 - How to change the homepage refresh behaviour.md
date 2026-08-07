---
title: "How to change the homepage refresh behaviour"
aliases:
  - KB0634955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634955
kb_number: KB0634955
last_modified: 2025-07-15
---

## How to change the homepage refresh behaviour

  

### Issue

ServiceNow uses a very open homepage configuration model that allows most users unlimited access to create and change their homepages to suit their personal needs.

One of these options allows users to select an auto-refresh rate for their homepage by default. This list contains options for auto-refreshing every 5 minutes, 15 minutes, 30 minutes, or 1 hour.  
  

![Homepage Refresh Interval](sys_attachment.do?sys_id=0dd9ab3397bd26505ad8f6e11153af17 "Homepage Refresh Interval")

### Release

All releases

### Resolution

### How to change the listed refresh rates

The default list can be overwritten by adding a new property with a comma-separated list of options. These values are in seconds. In the example below, the 5-minute option (300) will be removed.

1.  Navigate to the module: **System Properties > All Properties**
2.  Create a new property with the following settings:  
    -   Name: glide.home.refresh\_intervals
    -   Description: A comma-separated list of refresh intervals is available on homepages.
    -   Type: String
    -   Value: 900,1800,3600
3.  When removing an interval, consider changing all users who are using this interval to a new value.  
    1.  Navigate to the module **User Administration > User Preferences**
    2.  Filter > Name is "home\_refresh" and the value is 300 or off.
    3.  Use the "Update All" list control option to set the value to one of the new intervals.

**NOTE**: Adding a value less than 5 minutes (300 seconds) will lead to performance issues as homepage transactions make up between 30-50% of most instances' user traffic.

### Related Links

For more information, see the product documentation to [refresh the](https://docs.servicenow.com/search?q=refresh+the+homepage "refresh the homepage") [homepage](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/administer/advanced-work-assignment/concept/awa-admin-console-home.html).
