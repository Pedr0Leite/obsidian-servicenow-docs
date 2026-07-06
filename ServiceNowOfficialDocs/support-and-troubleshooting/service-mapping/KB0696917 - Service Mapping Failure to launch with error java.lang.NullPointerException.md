---
title: "Service Mapping Failure to launch with error:  \"java.lang.NullPointerException\""
aliases:
  - KB0696917
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696917
kb_number: KB0696917
last_modified: 2024-04-07
---

## Service Mapping Failure to launch with error: "java.lang.NullPointerException"

  

### Issue

# Symptoms

* * *

Service mapping view map Just throws a nullpointer exception after entering the entry point

"java.lang.NullPointerException"

# Release

* * *

All releases

# Cause

* * *

Out of the box, Service mapping depends on the following relationship types, if any of these relationships types are modified or removed we will be throwing a nullpointer exception

Not all of them are mandatory for service mapping to succeed. But some are critical. list of mandatory relation typed that should not be modified or removed

Runs On::Runs  
Hosted on::Hosts  
Applicative Flow To::Applicative Flow From  
Implement End Point To::Implement End Point From  
Use End Point To::Use End Point From  
Cluster of::Cluster  
Contains::Contained by  
Members::Member of  
Depends on::Used by

We also query for these relationship types based on the sys\_id as part of the script include "MetadataRulesProvider", If you modify or recreate the relationship types, make sure you update the sys\_id of the rel\_type in the script include.

\*\*\*\*\*\*Code\*\*\*\*\*\*

var HOSTED\_ON = "14cdeec3138bda001c5b38b2f244b068";//original was "5f985e0ec0a8010e00a9714f2a172815";  
var CONTAINS = "d0756272245578001a9d3579d366084a";//original was "55c95bf6c0a8010e0118ec7056ebc54d";

# Resolution

* * *

\-If any of the above rel\_types are missing, re-import or re-create these relationship types.

\-If the rel\_type has a different sys\_id than what we are querying for in "MetadataRulesProvider", please update it with proper sys\_id.

* * *
