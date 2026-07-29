---
title: "Yearly cost field in contracts (ast_contract) not being divided by contract duration"
aliases:
  - KB2694195
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2694195
kb_number: KB2694195
last_modified: 2025-12-24
---

## Yearly cost field in contracts (ast\_contract) not being divided by contract duration

  

## Table of Contents

-   [Description](#mcetoc_1jd561l6h284)
-   [How the value is calculated (OOB)](#mcetoc_1jd561l6h285)
-   [Common misconceptions and confusions regarding the Yearly cost field (and clarifications)](#mcetoc_1jd561l6h286)
-   [Example (to set expectations)](#mcetoc_1jd561l6h287)
-   [Resources](#mcetoc_1jd561l6h288)

## Description

The yearly cost field is a projected value calculated only from Payment amount and Payment schedule.

It **does not divide the contract’s total by the number of years** and it **does not consider the contract’s start/end dates**.

This behavior is OOTB and provided by the business rule “Calculate projected costs (Reports)”.

<table id="r_BusinessRulesIWContractMgmt__table_hmk_t3f_4r" style="width: 1282px;"><tbody><tr><td headers="r_BusinessRulesIWContractMgmt__table_hmk_t3f_4r__entry__1">Calculate projected costs (Reports)</td><td headers="r_BusinessRulesIWContractMgmt__table_hmk_t3f_4r__entry__2">Contract [ast_contract]</td><td headers="r_BusinessRulesIWContractMgmt__table_hmk_t3f_4r__entry__3">Calculates the projected monthly and annual costs for a contract when costs or payment schedule changes.</td></tr></tbody></table>

[Business rules installed with Contract Management](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/contract-management/reference/r_BusinessRulesIWContractMgmt_1.html)

## How the value is calculated (OOB)

-   Yearly cost is a projection recalculated when costs or Payment schedule changes.
-   This is done by the Business Rule “Calculate projected costs (Reports)”.
-    “Calculate projected costs (Reports)” converts the total\_cost into projected values based **only on the payment schedule** and **does not consider contract length**.

> **Note:** The projection uses the Payment schedule (for example, Annual, Monthly, Quarterly…) to express the amount per year/month. It does not amortize the contract over its duration

## Common misconceptions and confusions regarding the Yearly cost field (and clarifications)

-   “Yearly cost should be Total ÷ contract years.”  
    Yearly cost is a projection from Payment amount + Payment schedule. Contract duration is not part of this calculation.
-   “Total cost includes the projection logic.”  
    _T_otal cost is calculated from Payment amount and tax fields via Calculate totals with tax scripts/rules on the Contract form. 
-   “Monthly/Yearly values change when Start/End dates change.”  
    Start/End dates and lifecycle updates are handled by other rules (for lifecycle and history), not by the projection rule.

## Example (to set expectations)

As highlighted earlier yearly\_cost value is not calculated based on contract duration (start date to end date)  
  
For example, when the payment schedule is Annual:  
yearly\_cost = total\_cost  
monthly\_cost = total\_cost / 12  
  
So, if a contract is x years and the total\_cost is entered as 100 with Annual billing, the platform interprets 100 as the annual payable projection, not the full 3-year rolled-up amount. 

The yearly\_cost remains 100 and not 33.33.

## Resources

[Business rules installed with Contract Management](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/contract-management/reference/r_BusinessRulesIWContractMgmt_1.html)
