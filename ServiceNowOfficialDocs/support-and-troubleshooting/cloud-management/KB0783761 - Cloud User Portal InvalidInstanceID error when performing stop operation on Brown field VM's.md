---
title: "Cloud User Portal : InvalidInstanceID error when performing stop operation on Brown field VM's"
aliases:
  - KB0783761
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783761
kb_number: KB0783761
last_modified: 2026-05-21
---

## Cloud User Portal : InvalidInstanceID error when performing stop operation on Brown field VM's

  

### Issue

When you perform a stop operation on Brown Field VM's (VM's not provisioned through CMP), you receive the below error :

com.amazonaws.services.ec2.model.AmazonEC2Exception: Invalid id: "" (Service: AmazonEC2; Status Code: 400; Error Code: InvalidInstanceID.Malformed; Request ID: b2b7aa0c-95cb-44c7-b80c-947bc59134f3)

### Release

If the customer is on Madrid or later family releases, brownfield management is supported.

### Cause

OOTB mappings refer to Stack but in brownfield context, the stack details are not available. In this case, the mappings need to be changed to allow brownfield VMs to be managed via CMP.

### Resolution

In order to perform stop operations on brownfield VM's (VM's not provisioned through CMP), follow the below steps :  
  
1) Navigate to Cloud Admin Portal -> Design -> Resource Blocks  
  
2) Click on the Virtual Server resource block  
  
3) Go to Operations tab  
  
4) On the OPerations drop down, Select the stop operation  
  
Note: Unpublish the resource block to make the below changes  
  
5) Click on the + button which adds a new input parameter  
  
6) Set the name of the parameter as resourceId with mapping as ${parameter.resourceId}  
  
7) Now change the mapping of the parameter ServerID to ${parameter.resourceId} by removing the current stack expression  
  
8) Click on Save  
  
9) Now publish the resource block again  
  
  
After performing the above steps, you can go ahead and stop the VM from the cloud user portal.
