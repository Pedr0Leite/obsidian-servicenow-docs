---
title: "Unable to customer software product because of related reference with Software Lifecycle Report."
aliases:
  - KB3127713
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3127713
kb_number: KB3127713
last_modified: 2026-06-30
---

## Issue

Deleting "Custom\_software\_product\_name" is not allowed because it is referenced in the record "Related\_product\_name" within the Software Lifecycle Report table.

## Resolution

-   Open sam\_sw\_product\_lifecycle\_report.LIST
-   Apply filter as product sys\_id = your custom software product
-   Copy the encoded query into the background script below:

var gr = new GlideRecord('sam\_sw\_product\_lifecycle\_report');

gr.addEncodedQuery('encoded query'); // Replace query here  
gr.query();  
  
var count = 0;  
while(gr.next()) {  
gr.deleteRecord();  
count++;  
}

gs.log('Deleted ' + count + ' records');

-   Once the report reference is deleted, open the custom software product table and delete the product.
