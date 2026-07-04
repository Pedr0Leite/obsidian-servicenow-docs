---
title: "CSM - Disabled Entitlements are still shown on the Case"
aliases:
  - KB0958998
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958998
kb_number: KB0958998
last_modified: 2024-03-16
---

## CSM - Disabled Entitlements are still shown on the Case

  

### Issue

Inactive Entitlements are searchable on the Case Form.

Steps to Reproduce:

-   Create a CSM Entitlement in the system, but set "Active = false".
-   Now go to a Case - you can see that the disabled Entitlement is still shown up on the Case in the Entitlement field.  
      
      
    

### Release

Paris

### Cause

Expected Behaviour

### Resolution

-   In the case table (sn\_customerservice\_case), the entitlement field has CSManagementUtils().getEntitlements() as a reference qualifier, and in this function extra logic for filtering has to be added if the you would like to filter out inactive entitlements from not being shown.  
      
    
-   It wasn't added because there a couple of ways this can be modified depending on the need - like not showing entitlements based on end date, based on the active property etc, and we will need to re-evaluate this logic if we need to make any changes OOB.  
      
    
-   If you do not want to see Inactive Entitlements then you modify the reference qualifier condition for showing only active entitlements (active = true).
