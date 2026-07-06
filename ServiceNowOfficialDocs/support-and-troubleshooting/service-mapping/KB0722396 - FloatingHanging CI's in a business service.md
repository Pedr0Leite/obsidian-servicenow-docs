---
title: "Floating/Hanging CI's in a business service"
aliases:
  - KB0722396
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722396
kb_number: KB0722396
last_modified: 2024-04-07
---

## Floating/Hanging CI's in a business service

  

### Issue

# Description

* * *

The procedure to identify the problematic endpoints in a business service and remove the Floating/Hanging CI's.

We encounter problems with maps showing 'floating' CIs.

The most common problems are:

1.  CI was not added to the model because we reached the model depth limit
2.  CI was not added to the model since it does not comply with containment/hosting rule (until Jakarta)
3.  Missing relations from the CMDB (root cause not always clear)

# Procedure

* * *

Run as background script to identifying those problems and reports on recommendation action.

  
  
// script to identify Floating/Hanging CI's in a business service.

var gr1 = new GlideRecord('cmdb\_ci\_service\_discovered');

gr1.get(<service\_id>'); //Replace the <service\_id> part 

var layerId = gr1.layer;

var layerGr = new GlideRecord('svc\_layer');

layerGr.get(layerId);

gs.print('env = ' + layerGr.environment);

var allCis = sn\_svcmod.ServiceContainerFactory.queryCIsAssociatedWithEnvironment(layerGr.environment);

gs.print('Ci count: ' + allCis.length);

// First path to build map

var map = {};

for (var i in allCis) {

    var ci = allCis\[i\];

    map\[ci\] = 1;

}

var problem = 0;

for (var i in allCis) {

    var ci = allCis\[i\];

    var epGr = new GlideRecord('cmdb\_ci\_endpoint');

    if (!epGr.get(ci))

        continue;

    // This is an endpoint. Check if it has implemented by relation

    var relGr = new GlideRecord('cmdb\_rel\_ci');

    relGr.addQuery('parent', ci);

    relGr.addQuery('type', '45e94a74532221007c949096a11c0861');

    relGr.query();

    if (!relGr.next()) {

       // No implementing relation. Check if there are outgoing application flow relations. if there are such, and its not cmdb\_ci\_endpoint\_ob\_cluster, something is wrong

       if (relGr.sys\_class\_name == 'cmdb\_ci\_endpoint\_ob\_cluster')

           continue;

       var relGr1 = new GlideRecord('cmdb\_rel\_ci');

       relGr1.addQuery('parent',ci);

       relGr1.addQuery('type', '85d98503ff100200d699ffffffffff8c');

       relGr1.query();

       if (relGr1.next()) {

           gs.print('PROBLEM: Endpoint: ' + ci + ' has outgoing app flows relations, but no outgoing implements relations. Recommended action: 1) try to resume discovery on the endpoint 2) if there is still a problem, delete all outgoing relations from this endpoint');

           problem++;

       }

       continue;

    }

    // Check if the target CI is in the service

    if (!map\[relGr.child\]) {

        // Check if the endpoint is entry point in another service

        var entryPointGr = new GlideRecord('sa\_m2m\_service\_entry\_point');

        entryPointGr.addQuery('cmdb\_ci\_endpoint', ci);

        entryPointGr.query();

        if (!entryPointGr.next()) {

              gs.print('PROBLEM: CI ' + relGr.child + ' implementing endpoint ' + ci + ' is not in the service model. Check (1) if we exceeded the depth limitation (2)consistency of this CI with the identification engine containment and hosting rules');

        problem++;

        }

    } 

}

gs.print("Problem count = " + problem);

**Example of output:**

\*\*\* Script: env = 018c1294139e3640b53afabed144b0fe

\*\*\* Script: Ci count: 3195

\*\*\* Script: PROBLEM: CI c35a67c9135a4304d36c75c36144b03b implementing endpoint 75f8a3c5135a4304d36c75c36144b049 is not in the service model. Check (1) if we exceeded the depth limitation (2)consistency of this CI with the identification engine containment and hosting rules

\*\* Script: PROBLEM: Endpoint: 6444d3174fcc32009d64bc218110c7ae has outgoing app flows relations, but no outgoing implements relations. Recommended action: delete all outgoing relations from this endpoint

\*\*\* Script: Problem count = 159

2) Based on the output, identify the problematic endpoints and remove the applicative flow relations from those endpoints.

3) Once the above step is completed, execute the recompute Business service UI action and return to the discovery on the business service
