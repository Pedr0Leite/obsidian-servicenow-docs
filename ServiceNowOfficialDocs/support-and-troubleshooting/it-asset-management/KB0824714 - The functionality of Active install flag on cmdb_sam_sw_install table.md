---
title: "The functionality of Active install flag on cmdb_sam_sw_install table"
aliases:
  - KB0824714
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824714
kb_number: KB0824714
last_modified: 2026-04-23
---

## The functionality of Active install flag on cmdb\_sam\_sw\_install table

  

### Issue

The documentation does not discuss the functionality of the Active Install flag which can be found in the cmdb\_sam\_sw\_install table. We will present below a few questions that other customers had regarding this feature.

### Release

All

### Resolution

1\. What is the significance of this flag?  
\- This flag is related to a de-duplicate process within SAM. Here's how de-duplication works:  
Initially, when Discovery runs on a CI, it will find pieces of software installed on this CI and create records in cmdb\_sam\_sw\_install table. If there're multiple Discovery sources run and they all find the same piece of software, there might be duplicate install records, where de-duplication needs to kick in to handle this. When deduplication finds duplicated installs from different Discovery source, it will leave one active = true and mark the rest active = false.  
(This active flag has nothing to do with user utilization. )  
  
2\. When it will be false?  
\- It means it's a duplicate and processed by de-duplication. It has nothing to do with the user/ assigned\_to field.  
  
3\. In case of false what will be the effect on reconciliation?  
\- Recon will not take it into consideration.  
  
4\. Does this flag false represent software is retired or deleted?  
\- It has nothing to do with retirement. This active field is defaulted to be true as long as the software is physically installed on a CI. Only the de-duplication process can flip it to false.  
For deletion, it's Discovery's job to find it and remove it from our install table.  
  
5\. How service-now realize software has been deleted on the machine (we are importing SW scan into software installation table)?  
\- As explained in question #4, the record will be removed after Discovery run if it's deleted. So the install record will be there as long as it's still on that CI regardless of user utilization. The active field only reflects duplicates.  
  
6\. Will there be any scenario in which we have to manually delete or mark active false in software installation table record?  
\- There should be no such scenario. This field is set as Read-Only in order to not allow this to happen.
