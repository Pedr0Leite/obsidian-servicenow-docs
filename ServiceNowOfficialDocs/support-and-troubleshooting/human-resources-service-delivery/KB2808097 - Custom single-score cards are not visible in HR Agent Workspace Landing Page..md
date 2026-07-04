---
title: "Custom single-score cards are not visible in HR Agent Workspace Landing Page."
aliases:
  - KB2808097
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2808097
kb_number: KB2808097
last_modified: 2026-03-02
---

## Custom single-score cards are not visible in HR Agent Workspace Landing Page.

  

### Issue

**Problem**  
1\. The VP Cases and HRBP Cases cards on the HR Agent Workspace landing page are not displaying data as expected, showing 'No more HRBP cases' despite a count of 3. The HRBP Cases are also not visible in each other’s related carousels, unlike the OOB 'All Cases' card.  
2\. The label on the VP Cases card redirects to the list view of HR cases   
  

### Release

NA

### Cause

**Root Cause**  
1\. The card configuration used to fetch HR cases for display in the VIP HR cases carousel differed from the configuration used for the single-score visualization, resulting in inconsistent HR case counts.  
2\. The output of the databroker was not bound to the repeater in the HRBP carousel, causing the cards to remain hidden.  
  

### Resolution

**Steps to Resolve**  
1\. Align and update the conditions in both configurations (card configuration for the VIP HR cases carousel and single-score visualization) to ensure they are identical, as differing conditions cause mismatched HR case counts.  
2\. Bind the output of the databroker to the repeater in the HRBP carousel to ensure the cards are visible.  
3\. Modify the configurations as needed per requirement after implementing the above steps.
