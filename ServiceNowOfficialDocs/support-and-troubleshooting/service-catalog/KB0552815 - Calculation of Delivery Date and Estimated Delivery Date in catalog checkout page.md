---
title: "Calculation of Delivery Date and Estimated Delivery Date in catalog checkout page"
aliases:
  - KB0552815
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552815
kb_number: KB0552815
last_modified: 2025-03-13
---

## Calculation of Delivery Date and Estimated Delivery Date in catalog checkout page

  

### Issue

There are two versions of the Service Catalog checkout page, depending on the system property '**Use the sc\_layout driven cart macros**' being enabled (by default) or not:

-   if disabled, the final checkout screen is:  
      com.glideapp.servicecatalog\_checkout\_view
-   if enabled, the final checkout screen is:  
        com.glideapp.servicecatalog\_checkout\_view\_v2

**Delivery Date:** Final date by which the requested item is delivered to the customer. The Delivery Date is associated to the requested items in the cart.

**Estimated Delivery Date:** Estimated delivery date for the request, as the maximum among the delivery dates of all requested items in the cart. The Estimated Delivery Date is associated to the request.

### Resolution

Each catalog item is associated with an execution plan or workflow. If a catalog item is not associated with an execution plan or workflow, the **Default** execution plan is associated to the catalog item by default.

The delivery date of the requested item depends on the associated workflow or the execution plan. If the requested item is associated the workflow, then the delivery date is the expected work effort time to complete the workflow. Each workflow can have a predefined time it is completed. This predefined time is the delivery date of the requested item. Configure this predefined time by modifying the Expected Time column in the WorkFlow Version table for the workflow to which the item is associated.

If the requested item is associated with an execution plan, then the delivery date is calculated based on the time it takes to complete the execution plan. The delivery date is calculated using the **Total Delivery Time** column in the Execution Plan table.

Internally, the delivery date is calculated as follows:

1.  Fetch the current date.
2.  Fetch the time it takes to complete the workflow or execution plan associated to the requested item.
3.  Add the fetched time to the current date to get the **Delivery Date** of the requested item.

In the following scenario, three items have been ordered:

-   KeyBoard (associated with the execution plan named IT Service Hardware)
-   Mouse (associated with the workflow named Service Catalog Request) 
-   Headphones (not associated with a workflow or execution plan)

### Checkout page for the order

![order status](sys_attachment.do?sys_id=47d1bb761b3e9910c552c8031d4bcb17)

The Delivery Date and Estimated Delivery Date of the complete order are shown. To find out how they are calculated, navigate to **Service Catalog > Maintain Items**. 

![catalog items](sys_attachment.do?sys_id=c3d1bb761b3e9910c552c8031d4bcb1a)

The keyboard item is associated with an execution plan and the delivery date is calculated according to the time it takes to complete the execution plan. The delivery date is calculated based on the total delivery time of the execution plan.

![execution plan](sys_attachment.do?sys_id=cfd1bb761b3e9910c552c8031d4bcb1b)

The mouse item is associated with a workflow. The delivery date is calculated according to the workflow schedule.

![workflow](sys_attachment.do?sys_id=cbd1bb761b3e9910c552c8031d4bcb1d)

![workflow version](sys_attachment.do?sys_id=c7d1bb761b3e9910c552c8031d4bcb1f)

The headphones item is not associated with any workflow or execution plan, so, by default, it is associated with the execution plan named Default. The delivery date is calculated according to the **Total Delivery Time** of the Default execution plan. 

![execution plans](sys_attachment.do?sys_id=8bd1bb761b3e9910c552c8031d4bcb2d)

![execution plan](sys_attachment.do?sys_id=87d1bb761b3e9910c552c8031d4bcb2f)

 **Note:** If the catalog item does not an associated workflow or execution plan, by default, the execution plan named Default is assigned.
