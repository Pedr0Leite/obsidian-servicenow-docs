---
title: "CacheHelper"
aliases:
  - CacheHelper
tags:
  - servicenow-dev-program
  - code-snippet
  - cachehelper
  - script-includes
---

# BenchmarkRunner
Just a wrapper around GlideCacheManager with methods to enable validation of Cache key and data and ability to use the GlideCacheManager easily.

## Example server-side call (background script)
```javascript
var cacheName = "rahman_test";
var cacheKey = "1";

var helper = new CacheHelper(false);

// Either get the data from cache or add it
var data = helper.getOrAddToCache(cacheName, cacheKey, function(){
    gs.log("This will be called if the data is not in the cache. The second time will not be called.");

    // This will be called if the data is not in cache!!!
    var data = {
        name: "rahman",
    }

    return data;
})

gs.log(JSON.stringify(data));

//helper.removeFromCache(cacheName)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
