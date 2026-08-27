---
title: "HAM CI Asset Swap - Swapped CI inherits the caller's location "
aliases:
  - KB3021675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3021675
kb_number: KB3021675
last_modified: 2026-05-19
---

## HAM CI Asset Swap - Swapped CI inherits the caller's location

  

### Issue

HAM CI Asset Swap - Swapped CI inherits the caller's location not from the location mentioned on the Incident Form.  
  

### Symptoms

After CI swap the new swapped CI takes the location of the caller not the location from the Incident form.  Expectations was that swapped CI should take location from the incident form

### Release

ALL

### Cause

The swapped CI inherited the caller's location instead of the incident's location because the 'Swap Asset' script action did not include the incident's location in the payload when it was not explicitly provided. This was confirmed as expected out-of-box behavior by the development team.  
  

### Resolution

The issue was found to be related to the 'Swap Asset' script action not populating the location field in the payload from the incident form.

Development team suggested following options:

1\. Manual update: If you need to change the location for a specific CI/Asset after swap, you can update it manually from the Asset record page.

2\. Customization (if Incident location is preferred): If you would like the swap flow to use the Incident's Location field for the swapped CI, you can consider adding the following code to the Script Action:  
Script Action Name: Swap Asset  
Event name: sn\_hamp.asset.swap

Add this code between line 3 and line 4 of the script:

// Use Incident's location if not provided in payload  
if (!payload.location && current.isValidField('location') && current.getValue('location')) {  
payload.location = current.getValue('location');  
}
