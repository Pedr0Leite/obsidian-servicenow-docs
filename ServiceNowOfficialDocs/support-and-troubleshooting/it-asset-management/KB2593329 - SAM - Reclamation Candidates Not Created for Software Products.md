---
title: "SAM - Reclamation Candidates Not Created for Software Products"
aliases:
  - KB2593329
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2593329
kb_number: KB2593329
last_modified: 2025-11-19
---

## SAM - Reclamation Candidates Not Created for Software Products

  

### Issue

I executed the scheduled job "SAM - Identifying New Reclamation Candidates" to generate removal candidates for Figma. The job ran successfully, but no candidates were created under Figma. I would like to understand why the expected reclamation entries were not generated and whether any configuration changes are needed.

### Release

NA

### Cause

Ran and executed the Scheduled Job :   
SamIdentifyingNewReclamationCandidates  
  
  
Checking code to see how many records qualify for the creation of Reclamation candidates   
\====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====  
  
getM2mRuleProductRecords: function() {  
var m2m = new GlideRecord(M2M\_RULE\_PRODUCT\_TABLE);  
m2m.addNotNullQuery('reclamation\_rule');  
m2m.addNotNullQuery('software\_product');  
m2m.addQuery('reclamation\_rule.create\_reclamation\_candidate', true);  
m2m.addNullQuery('parent');  
m2m.query();  
return m2m;  
},  
\====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====  
  
This only returns Software Products record with no parent .  
  
  
These products should now create Reclamation candidates:   
Checking the Script include:  
  
\====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====  
generateReclamationCandidatesForM2mRuleProductRecord: function(m2m) {  
if (GlidePluginManager.isActive('sn\_sam\_saas') && m2m.reclamation\_rule.applies\_to.toString() === 'Subscription Software') { return; }  
  
if (GlidePluginManager.isActive('com.sn\_samp\_eng\_app') && m2m.reclamation\_rule.applies\_to.toString() === 'Engineering App License') {  
this.generateEngAppReclamationCandidates(m2m);  
} else {  
this.generateOnPremReclamationCandidates(m2m);  
}  
},  
\====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====\*====

  
Checked the conditon:

parent for a Software Product is NULL and the Reclamation Rule is 'Subscription Software

### Resolution

  
If the parent for a Software Product is NULL and the Reclamation Rule is 'Subscription Software,' the reclamation/removal candidate won't be created for such a Product.   
  
Create a Subscription profile for that software product, and let the automated process do the rest of the work.   
It should auto-create the user subscriptions and reclamation rule.
