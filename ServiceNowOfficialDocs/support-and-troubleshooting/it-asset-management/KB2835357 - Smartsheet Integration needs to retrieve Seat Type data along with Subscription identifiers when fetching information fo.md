---
title: "Smartsheet Integration needs to retrieve Seat Type data along with Subscription identifiers when fetching information for subscriptions."
aliases:
  - KB2835357
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2835357
kb_number: KB2835357
last_modified: 2026-03-12
---

## Smartsheet Integration needs to retrieve Seat Type data along with Subscription identifiers when fetching information for subscriptions.

  

**Description**

The Smartsheet Integration fails to retrieve Seat Type data and Subscription identifiers (SMARTSHEET\_PAID and SMARTSHEET\_FREE), causing incorrect licensing user classification.

## **Steps to Reproduce**

1.  Configure the Smartsheet Integration in ServiceNow.
2.  Trigger the SAM job "Refresh Smartsheet Integration Subscriptions" from the integration profile created
3.  Navigate to the subscription records table (samp\_sw\_subscription) 
4.  Observe the subscription identifier values fetched for known paid and free users.
5.  Verify identifiers are swapped: paid users show "SMARTSHEET\_FREE" and free users show "SMARTSHEET\_PAID". Confirm by checking the user's license type directly in Smartsheet.  
      
    

### **Releases**

This issue is present in all releases of the Smartsheet Integration

**  
Workaround**

This problem has no workaround, is currently under review and targeted to be fixed in a future release. Subscribe to this Known Error article to receive notifications when more information will be available.

**Related Problem : PRB2002108**
