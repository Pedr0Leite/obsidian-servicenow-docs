---
title: "SLAs cancelling randomly"
aliases:
  - KB0722356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722356
kb_number: KB0722356
last_modified: 2024-04-07
---

## SLAs cancelling randomly

  

### Issue

SLAs are canceling randomly

### Release

ALL

### Cause

Customization

### Resolution

In the course of the investigation, the following were encountered:  
  

-   Custom SLA Script Includes:  
    -   ApertureScienceCustomSLAs (227 lines of custom code)
    -   ApertureScienceSLAConditionBase (203 lines of custom code)
-   A customized version of OOB (Out of Box) SLA Script Include:  
    -   SLATimezone
-   A customized version of OOB "Run SLAs" Business Rule
-   Three additional custom Business Rules touching SLAs, including one which cancels task\_sla records.

  
There were several attempts made to utilize the OOB Repair SLAs functionality in an effort to address the unexpected miscalculation - and strangely, even though all best practices were followed for SLAs in domain separated instances, each time the incident in question was repaired, different results were seen from the Repair SLAs functionality. That is not expected, and not how the functionality behaves OOB.  
  
Support Engineers are experts in OOB behavior and handle break-fix behavior pertaining to OOB functionality.  
  
What was seen in the user's instance was a heavily customized SLA process. Unfortunately, both debugging and the implementation of custom code falls outside the scope of the Support Engineer's area of expertise.   
  
Because of the above, it was recommended that the user inquire of the team who developed these customizations to assist in resolving the behavior the user was facing, as they are much more likely to understand the customizations and how they affect the users' system. They also have a more intimate knowledge of ApertureScience's SLA process.
