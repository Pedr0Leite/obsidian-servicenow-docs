---
title: "Import Entitlement fail for Adobe when the Agrement type is \"Value Incentive Plan (VIP)\"
aliases:
  - KB0852394
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852394
kb_number: KB0852394
last_modified: 2024-04-08
---

## Import Entitlement fail for Adobe when the Agrement type is "Value Incentive Plan (VIP)"

  

### Issue

1.  The import entitlement is failing for Adobe Publisher
2.  According to the Excel sheet the Agreement Type is "Value Incentive Plan (VIP)" while trying to import the entitlement the License type is selected as Subscription, if we try to add the entitlement manually it works, but the same fails while importing.
3.  The Excel sheet contains the below information:  
      
    -   PPN: 6529XXXXXXXXX
    -   Publisher: Adobe 
    -   Agreement Type: Value Incentive Plan (VIP)
    -   License Type: Subscription
    -   Purchased Rights: 10
    -   Unit Cost: 10
    -   License Metric: Per User 
    -   Start Date: 3/28/2019  
          
        
4.  The import fails with error "**Import template customized resulting in one or many fields being invalid**"
5.  The excel sheet contains the Agreement type is not accepting "ValueIncentivePlan" and the OOB is only accepting either of the below  
      
    -   Generic
    -   Enterprise License Agreement  
          
        
6.  If we try to create the same entitlement manually with the same 6529XXXXXXXXX PPN it accepts with the License type "ValueIncentivePlan", but import fails
7.  If we modify the excel sheet with the License Type=Generic or ELA, the import works fine

### Cause

1.  Value Incentive Plan has dependent value for Adobe.
2.  Not assigning a value for is defaulting the entitlement to "Common" metric group.

### Resolution

1.  Metric Group is mandatory for the Adobe when the  Agreement type is **"Value Incentive Plan (VIP)"**
2.  Add the "**Metric Group=Adobe**" in the excel sheet and import the entitlement to fix the issue.
