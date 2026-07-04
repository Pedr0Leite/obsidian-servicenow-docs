---
title: "Searches do not return all expected results after cloning"
aliases:
  - KB0552002
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552002
kb_number: KB0552002
last_modified: 2026-05-07
---

## Searches do not return all expected results after cloning

  

### Issue

 

After cloning, search functionality does not return all expected results.

### Symptoms

After a clone completes, the following search areas may not return all expected results:  
• Global Search bar in the top-right of the user interface  
• "For text" search widget in any list view  
• Knowledge Base search bar  
• Service Catalog search bar

### Release

All supported ServiceNow releases. Applies to non-production instances that have received a clone from another instance

### Cause

After a clone completes, clone cleanup scripts run automatically. One of the standard cleanup operations is to re-index text search. Text indexes are excluded from clones to significantly reduce clone times and the amount of data transferred between instances. During re-indexing, searches may not return all expected results

### Resolution

After re-indexing completes, searches are expected to return results as normal. To verify that re-indexing is complete or to monitor its progress, navigate to System Definition > Text Indexes and review the index status.  
  
For additional guidance, see:  
• KB0694751 — How to verify that text indexing is complete  
• KB0687779 — How to make text indexing faster  
  
If searches are still not returning expected results after re-indexing completes, contact ServiceNow Support.
