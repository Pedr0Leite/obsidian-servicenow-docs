---
title: "SAMP | Software Product Suggestions do not update Software Products for Reclamation Rules with the Suggested Product"
aliases:
  - KB2500366
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2500366
kb_number: KB2500366
last_modified: 2026-05-12
---

## SAMP | Software Product Suggestions do not update Software Products for Reclamation Rules with the Suggested Product

  

### Issue

Software Product Suggestions do not update Software Products for Reclamation Rules with the Suggested Product.

The Inactive Custom Software Products remain mapped to Reclamation Rules.

Expected Behavior:

Accepting a Software Product Suggestion updates all references to the custom software product with references to the suggested software product from the Content Library.

Actual Behavior:

Accepting a Software Product Suggestion does NOT update references to the custom software product with references to the suggested software product from the Content Library on the samp\_m2m\_rule\_product table which maps software products to reclamation rules.

### Symptoms

References to the custom software product on the samp\_m2m\_rule\_product table are not updated when the Software Product Suggestion is accepted.

Reclamation Rules still show the custom software product on their Software Products related list.

Reclamation Rules still show the custom product processes related to custom software products on their Product Process list related list.

### Release

All Releases

### Cause

A background job is executed when a Software Product Suggestion is 'Accepted' that updates all references to the custom software product with references to the suggested software product.

The background job is not updating records on the samp\_m2m\_rule\_product table.

### Resolution

Run the below background script to Update the samp\_m2m\_rule\_product records referencing Custom Software Products with the Suggested Software Product from Accepted Software Product Suggestion records.

If the Reclamation Rule mapped to the Custom Software Product does NOT already have an existing mapping to the Suggested Product, then the script will Update the mapping to the custom software product to reference the Suggested Software Product.

If the Reclamation Rule mapped to the Custom Software Product already has an existing mapping to the Suggested Product, then the script will delete the mapping to the custom software product.

```
updateRRM2MSWPSuggestions();

function updateRRM2MSWPSuggestions(){
	var gr = new GlideRecord('samp_custom_sw_product_suggestion');
	gr.addQuery("status","approved");
	gr.query();
	while(gr.next()){
		var customProduct = gr.getValue('custom_product');
		var suggestedProduct = gr.getValue('suggested_product');
		var suggestedProductName = gr.getDisplayValue('suggested_product');
		gs.print("\n\nCustom SW Product: " + gr.getDisplayValue('custom_product') + " - " + customProduct + "\nSuggested SW Product: " + suggestedProductName  + " - " + suggestedProduct + "\n");
		updateReconRuleM2M(customProduct,suggestedProduct,suggestedProductName);
	}
}

function updateReconRuleM2M(customSWP, suggestedSWP, suggestedSWPName){
	var gr = new GlideRecord("samp_m2m_rule_product");
	gr.addQuery('software_product',customSWP);
	gr.query();
	while(gr.next()){
		var rule = gr.getValue('reclamation_rule');
		var ruleName = gr.getDisplayValue('reclamation_rule');
		var hasSuggested = hasSuggestedRRM2M(rule,suggestedSWP);
		if(hasSuggested){
			gs.print("\n\nReclamation Rule " + ruleName + " has exisiting mapping to Suggested Software Product " + suggestedSWPName + "\nDeleting Reclamation Rule Mapping to Custom SWP: " + gr.getDisplayValue("software_product") + " - " + customSWP);
			gr.deleteRecord();
		}else{
			gs.print("\n\nReclamation Rule " + ruleName + " does NOT have an exisiting mapping to Suggested Software Product " + suggestedSWPName + "\nUpdating Reclamation Rule Mapping to Custom SWP: " + gr.getDisplayValue("software_product") + " with the Suggested SWP: " + suggestedSWPName);
			gr.setValue('software_product',suggestedSWP);
			gr.update();
		}
	}

}

function hasSuggestedRRM2M(rule,suggested){
var gr = new GlideRecord("samp_m2m_rule_product");
gr.addQuery("reclamation_rule", rule);
gr.addQuery("software_product", suggested);
gr.query();
if(gr.next()){
	return true;
}else{
	return false;
}
}
```

### Related Links

[ServiceNow Product Documentation - View custom software product suggestions in workspace](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/task/view-custom-software-product-suggestions-workspace.html)
