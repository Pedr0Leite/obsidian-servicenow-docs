---
title: "Service Mapping Troubleshoot 101: Business Service with Service Model (Why my business service map is not showing up on the page?)"
aliases:
  - KB0683761
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0683761
kb_number: KB0683761
last_modified: 2024-04-07
---

## Service Mapping Troubleshoot 101: Business Service with Service Model (Why my business service map is not showing up on the page?)

  

### Issue

# Background

* * *

1) The business service map for the Service Mapping, has a "Service Model" data structure at the backend. 

  
2) When we ask to do the "View Map", the system will have to produce the "Service Model" in a JSON format, and the page will render the data. 

3) With Kingston release, there is a "Related Link" on the business service, name "Recompute Business Service" which will do a recompute of the service model.

4) There are three additional links on the "Related Links" of each of the "Discovered Service" (cmdb\_ci\_service\_discovered)  
which are only showing up for "maint" at the moment.   
They are:   
a) "Show Service Model JSON"   
b) "Sync with Service Model"   
c) "Remove from Service Model" 

Note:  
The three links are defined on the "UI Actions" of the instance. If you will like to have access to those links, you can open the respective records, change the condition to only show for specific users and do an "Insert and Stay" to create a separate record. Please use these links with care, a misuse of these features may result in performance issues on your instance.

# Checks

* * *

If the "Discovery Service" (cmdb\_ci\_service\_discovered) is not showing up, we want to check to see if the "Service Model" JSON is returning the correct information.

To do this, click on the "Show Service Model JSON" link and see if a proper JSON object shows up.  
If you get just a "null" word, check to see if there are proper "Entry Point" for the "business service".

  
If there are proper "Entry Point" for the "business service", you can try the following Quick Fixes.

# Quick Fix 1

* * *

If the "Show Service Model JSON" returns with just a "null" word, you can try to click on the "Recompute Business Service" once.

What this does, is that it will do a "Recomputation" for the "Service Model" for the "business service".

After you a while, try the "Show Service Model JSON" and see if it returns a proper JSON.

If it still returns the same result, you could try the background script as listed on the "Service Model Troubleshooting" at the bottom of this KB.

# Quick Fix 2

* * *

Try the "Recompute Business Service" first.

If the "Show Service Model JSON" still returns with just a "null" word, you can try to click on the "Sync with Service Model" once.

What this does, is that it will do a "Recomputation" for the "Service Model" for the "business service".

\*\* USE WITH CAUTION \*\*  
This "Sync with Service Model" removes and then adds the business service to the Service Model, along with its Entry Points and Boundary Endpoints. As a result, all business service history resets.

After you a while, try the "Show Service Model JSON" and see if it returns a proper JSON.

# Quick Fix 3

* * *

Try the "Recompute Business Service" and "Sync Service Model JSON" first.

Occasionally, we may need to do the whole "Service Model" again.  
Warning: By doing this step, the whole history of the business service, will be gone forever. 

The steps are:  
1) Click on the "Remove from Service Model"  
2) Click on the "Sync with Service Model"

To check, click on the "Show Service Model JSON" again to see if it returns a proper JSON.

# Service Model Troubleshooting

* * *

If trying the above Quick Fix, the "Show Service Model JSON" still returns a single word "null", it may suggest that the system had some trouble trying to do the "recomputation" for the "Service Model".

To do this, we have to run the following script using the "Background Scripts" on the instance.  
  

// Begin Script   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.coordinator","info,warn,error,\*");   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.template", "info,warn,error,\*");   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.matching", "info,warn,error,\*");   
gs.setProperty('glide.transaction.max\_logs', 200\*10000);   
  
var gr = new GlideRecord('cmdb\_ci\_service\_discovered');   
gr.get('<replace\_with\_business\_service\_sys\_id'); // <<<<<<<======= replace argument with service sys\_id   
var layerId= gr.layer;   
var layerGr= new GlideRecord('svc\_layer');   
layerGr.get(layerId);   
var env= sn\_svcmod.ServiceContainerFactory.loadEnvironment(layerGr.environment);   
  
var allLayers= env.layers();   
for (var i= 0 ; i< allLayers.length; i++) {   
var layer = allLayers\[i\];   
layer.markRecomputationNeeded();   
}   
  
SNC.ServiceMappingFactory.recomputeLayer(layerGr);   
  
gs.setProperty('glide.transaction.max\_logs', 200\*1000);   
gs.setProperty("glide.cmdb.logger.source.service\_mapping", "info,warn,error");   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.coordinator", "info,warn,error");   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.template", "info,warn,error");   
gs.setProperty("glide.cmdb.logger.source.service\_mapping.matching", "info,warn,error");   
// End Script
