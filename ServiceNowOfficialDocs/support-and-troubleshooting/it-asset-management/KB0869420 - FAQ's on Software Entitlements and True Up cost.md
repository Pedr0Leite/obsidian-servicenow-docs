---
title: "FAQ's on Software Entitlements and True Up cost"
aliases:
  - KB0869420
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869420
kb_number: KB0869420
last_modified: 2023-11-30
---

## FAQ's on Software Entitlements and True Up cost

  

### Issue

-   If the customer's system only has the **start date** and the **PPN** of the entitlement, we will need to apply some business logic to calculate the subscription end date. To do this, we will need to know the duration of the unit entitlement (e.g. it is a monthly one, an annual one, or multi-month/-year one with the exact duration).  
      
    1.  Will that information be available with just PPN ?  
          
        
    2.  Since the unit cost of a monthly entitlement will be different from an annual entitlement, how would this impact on the true-up cost? To be more specific, for certain subscriptions (e.g. Adobe Cloud), the customer may purchase Adobe Cloud licenses at a different time over the year but will always renew all the subscriptions on 1st May every year. Assuming that today is 1 March 2020, we purchase some license for the rest of the year (i.e. 2 more months):  
          
        2a. If the license is annual basis, purchase right = 10, unit cost = 120 USD, start date = 1 March 2020, and end date = 30 April 2020, what would be the true-up cost if the system actually discover 12 users using Adobe Cloud?  
          
        2b. If the license is monthly basis, purchase right = 10, unit cost = 10 USD,  
        \- Shall we create only 1 entitlement record where the start date = 1 March 2020, and end date = 30 April 2020? If so, what would be the true-up cost?  
        \- Shall we actually create 2 entitlement records with one start date = 1 March 2020 & end date = 31 March 2020, and another one which start date = 1 April 2020 & end date = 30 April 2020? If so, what would be the true-up cost?  
          
        
    3.  If the entitlement is on a monthly basis, and the customer only purchased such entitlement with 10 rights for 3 months, what would be the best way of recording the entitlement for an accurate true-up cost?

### Release

-   All

### Resolution

-   If the customer's system only has the **start date** and the **PPN** of the entitlement, we will need to apply some business logic to calculate the subscription end date. To do this, we will need to know the duration of the unit entitlement (e.g. it is a monthly one, an annual one, or multi-month/-year one with the exact duration).  
      
    1.  Will that information be available with just PPN ?  
          
        **Ans**: **No, until the PPN is for the Enterprise software, we don't grab such information as of now.**   
          
        
    2.  Since the unit cost of a monthly entitlement will be different from an annual entitlement, how would this impact on the true-up cost? To be more specific, for certain subscriptions (e.g. Adobe Cloud), the customer may purchase Adobe Cloud licenses at a different time over the year but will always renew all the subscriptions on 1st May every year. Assuming that today is 1 March 2020, we purchase some license for the rest of the year (i.e. 2 more months):  
          
        2a. If the license is annual basis, purchase right = 10, unit cost = 120 USD, start date = 1 March 2020, and end date = 30 April 2020, what would be the true-up cost if the system actually discover 12 users using Adobe Cloud?  
          
        **Ans**: **True Up cost relies on the active entitlements present during the licensing period. So, how many active entitlements are present during a specific timeframe, TrueUp cost will be calculated for those active entitlements based on the active purchased rights and the Unit cost.**2b. If the license is monthly basis, purchase right = 10, unit cost = 10 USD,  
        \- Shall we create only 1 entitlement record where the start date = 1 March 2020, and end date = 30 April 2020? If so, what would be the true-up cost?  
        \- Shall we actually create 2 entitlement records with one start date = 1 March 2020 & end date = 31 March 2020, and another one which start date = 1 April 2020 & end date = 30 April 2020? If so, what would be the true-up cost?**  
          
        Ans : There is no harm in having two separate entitlement records but to avoid the redundant data, you can create only one entitlement record for the whole time period from 1 March 2020 to 30 April 2020.  
          
        **
    3.  If the entitlement is on a monthly basis, and the customer only purchased such entitlement with 10 rights for 3 months, what would be the best way of recording the entitlement for an accurate true-up cost?  
          
        **Ans: As mentioned in the point question 1, True Up cost totally relies on the active entitlements present during the licensing period. So be it an annual licensing or the monthly licensing, the calculation is based on the number of active entitlements for that period. We recommend you to create one entitlement for the whole 3 months.**
