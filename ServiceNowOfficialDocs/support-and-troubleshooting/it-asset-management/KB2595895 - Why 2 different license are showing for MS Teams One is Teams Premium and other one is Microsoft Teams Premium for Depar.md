---
title: "Why 2 different license are showing for MS Teams? One is Teams Premium and other one is Microsoft Teams Premium for Departments."
aliases:
  - KB2595895
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2595895
kb_number: KB2595895
last_modified: 2026-05-22
---

## Why 2 different license are showing for MS Teams? One is Teams Premium and other one is Microsoft Teams Premium for Departments.

  

### Issue

In workspace 2 different license are showing, one is teams premium and other one is Microsoft Teams Premium for Departments. In MSDN portal the user has the teams premium license assigned.

Why are the licenses are consumed under two different models? It should be consumed only under teams premium model, surely? 

### Release

Any

### Resolution

This comes from Microsoft, see this thread - the poster also cannot see the difference but some users have a different SKU:   
https://members.collab365.com/c/microsoft365\_forum/teams-premium-for-departments  
  
"After looking over both Teams Premium and Teams Premium (For Departments), they both have the same exact services in the Service Plan.  
  
The only difference seems to be somehow some users get assigned Teams Premium (For Departments) and I can't seem to understand or figure out how that SKU is getting assigned. "  
  
Checking MS licensing, you can find "Teams Premium (for Departments)" as a licensing plan here:  
https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference  
  
From ServiceNow perspective, we resolve subscriptions to a software model based on the subscription identifier received from the Microsoft graph user API.  
  
We check the Microsoft subscribedSkus API response which lists all of the commercial subscriptions that an organization has acquired, both these software models are present in the API response.  
  
Reach out to Microsoft support for information on why both these SKUs are being used, they will be able to provide information on the Teams Premium (For Departments) subscription which we are getting in the Microsoft API response.
