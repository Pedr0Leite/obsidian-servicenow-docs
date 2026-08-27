---
title: "[SAMP] How the Allocation available is updated/controlled on Software Entitlements"
aliases:
  - KB2659864
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2659864
kb_number: KB2659864
last_modified: 2025-12-11
---

## Issue

This article will explain how the Allocations available field is updated/controlled on Software Entitlements form.

## Resolution

**Question #1**: How the "Allocation available" is updated ?   
**Answer**: When the allocations are updated (alm\_entitlement\_user / alm\_entitlement\_device) there is a business rule "Calc Entitlement Allocations Availalable" that calculates the allocations and updates the "Allocation available" field on entitlement. Please find the main two business rules that drives the allocations as below:  
  
Business Rule #1: [Calc Entitlement Allocations Availalable](https://instance_name.service-now.com/nav_to.do?uri=sys_script.do?sys_id=2082e52dc32132006081face81d3aeee)  
Purpose: Calculates the available rights while making changes to allocations.  
  
Business Rule #2: [Ensure Entitlements do not exceed rights](https://instance_name.service-now.com/nav_to.do?uri=sys_script.do?sys_id=a9c3fd213784200044e0bfc8bcbe5d24)  
Purpose: Ensures the allocations does not cross the purchased rights for that entitlements.  
  
**Question #2**: Why it does not work when XML is imported ?  
**Answer**: When the XML is imported from one instance to another instance, there is business rules runs (as it did not gro through the engines) and so no business rule "Calc Entitlement Allocations Available" runs and no "Allocation available" field update happens on entitlement.
