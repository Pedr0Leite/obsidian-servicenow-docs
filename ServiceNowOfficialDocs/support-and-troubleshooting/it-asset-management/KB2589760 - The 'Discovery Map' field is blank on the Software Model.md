---
title: "The 'Discovery Map' field is blank on the Software Model"
aliases:
  - KB2589760
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2589760
kb_number: KB2589760
last_modified: 2026-05-18
---

## The 'Discovery Map' field is blank on the Software Model

  

### Issue

When reconciliation runs, software models are getting created and are being attached to Discovery models but DMAP is not getting attached to all software models. 

### Symptoms

The 'Discovery Map' field is blank on the Software Model

### Release

All releases

### Resolution

The SAM Content Library content does not hold every possible combination for Product/Publisher/Edition/Version to be associated with Software Models automatically   
  
While Discovery Maps are used to add pre-defined Product/Publisher/Edition/Version, suite associations, lifecycles and other additional information to link to a Software Model, and are recommended to use if they are available - especially for Software Suites, they are not a requirement for calculating compliance, which is defined by the Software Model's associated entitlements   
  
If you wish to have new Discovery Maps added to the Content Library, then refer to the process of submitting a Content Request:  
[Create Content Request](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790305)

  

### Related Links

[Create Content Request](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790305)
