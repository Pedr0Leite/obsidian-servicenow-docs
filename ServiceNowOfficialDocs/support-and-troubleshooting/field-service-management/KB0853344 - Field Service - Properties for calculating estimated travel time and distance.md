---
title: "Field Service - Properties for calculating estimated travel time and distance"
aliases:
  - KB0853344
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853344
kb_number: KB0853344
last_modified: 2024-10-09
---

## Issue

Is there a way to disable calculating 'Estimated Travel duration' by either Straight Line or Google API and let it be manual like in Madrid.

## Resolution

Please deactivate the client script ("Set Travel Duration(AssignedTo change)"  
  
The purpose of this client script would auto populate the estimated travel duration when the assigned\_to changes.
