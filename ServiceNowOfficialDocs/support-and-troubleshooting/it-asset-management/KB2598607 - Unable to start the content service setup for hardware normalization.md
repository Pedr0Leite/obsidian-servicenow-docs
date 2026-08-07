---
title: "Unable to start the content service setup for hardware normalization"
aliases:
  - KB2598607
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2598607
kb_number: KB2598607
last_modified: 2025-11-04
---

## Issue

When clicking on Configure from following navigation getting a Security constraints prevent access to requested page message when trying to turn on the content service for hardware normalization setup

Asset > Administration > HAM Guided Setup

Continue > Content Service Setup & Opt-in > Configure

## Resolution

To check what is blocking access you can use:  
  
Access Analyzer > Analyze Permissions  
Select user = < User Name >  
UI Page = sn\_hamp\_content\_service\_setup

If it shows status blocked By Access Control : sn\_hamp\_content\_service\_setup  
https://<Instance>.service-now.com/now/nav/ui/classic/params/target/sys\_security\_acl.do%3Fsys\_id%3Dfdf6b4a453d01010249addeeff7b1294

This ALC has required role asset but also has an advanced condition  
answer = !HAMUtils.isZTMOnlyInstance();

Verify user trying to access the Content Setup page has the role asset and add it if they do not.

Once user has asset role if the issue still exist then verify that the script include HAMUtils has the function: isZTMOnlyInstance

https://<Instance>.service-now.com/sys\_script\_include.do?sys\_id=75f6b4a453d01010249addeeff7b1294

Verify the latest version of the script is active and has the function.

If another version of script include that has the function is not set as the current one follow these steps:  
  
1\. Open that version in a new tab   
2\. Then click compare to current   
3\. Clicked on revert to selected version button at bottom of comparision page.   
  
Now the Script include with isZTMOnlyInstance function should be active   
  
Verify your user can now access HAM Guided Setup > Content Service Setup & Opt-in   
  
Another option is to try Repair the HAM Plugin, if repair doesn't change the current script to the one with the isTZMOnlyInstance function then you will need to use the steps provided above.
