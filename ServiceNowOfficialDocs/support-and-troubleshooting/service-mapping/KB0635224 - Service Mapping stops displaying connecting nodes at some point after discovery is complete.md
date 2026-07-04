---
title: "Service Mapping stops displaying connecting nodes at some point after discovery is complete"
aliases:
  - KB0635224
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635224
kb_number: KB0635224
last_modified: 2025-06-23
---

## Service Mapping stops displaying connecting nodes at some point after discovery is complete

  

### Issue

If you run a deep, top-down or vertical Service Mapping discovery, the discovered bottom nodes do not display outgoing connections to the next nodes even though the discovery logs tell you that these outgoing connections have been successfully created and no errors were found.

### Resolution

The problem in this scenario is that Service Mapping discovery of the Business Service may have reached the depth of the service model recomputation.

You can increase the service model recomputation depth. To do this:

1.  Add the property named **glide.service\_mapping.computation\_depth** to the sys\_properties table with a value of 30 (the default is 25). 
2.  Run the following script where 939137dd4ff4830056dc70021310c779 is the sys\_id of the business service as an example:

var gr = new GlideRecord('cmdb\_ci\_service\_discovered');  
gr.get('939137dd4ff4830056dc70021310c779'); // the business service sys\_id  
var layerId = gr.layer;  
  
var layerGr = new GlideRecord('svc\_layer');  
layerGr.get(layerId);  
  
var env = sn\_svcmod.ServiceContainerFactory.loadEnvironment(layerGr.environment);  
var allLayers = env.layers();  
for (var i = 0 ; i < allLayers.length ; i++) {  
var layer = allLayers\[i\];  
layer.markRecomputationNeeded();  
}  
  
SNC.ServiceMappingFactory.recomputeLayer(layerGr);

This script syncs the service model for the business service without deleting the history.  
  
If you need to, you can increase glide.service\_mapping.computation\_depth and run the script again.
