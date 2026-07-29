---
title: "How to cancel Service Mapping Discovery for a Business Service"
aliases:
  - KB0680014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0680014
kb_number: KB0680014
last_modified: 2025-07-29
---

## How to cancel Service Mapping Discovery for a Business Service

  

### Issue

If you need to stop a Service Mapping discovery process for a business service, this guide shows you how to cancel discovery using a background script. 

### Release

Any supported release

### Resolution

Before you begin, verify that you have:

-   Administrator access to your ServiceNow instance
-   The Business Service ID (sys\_id) for the service you want to stop

#### Find your Business Service ID

1.  Go to **Service Mapping** > **Business Services.**
2.  Locate the Business Service where you want to cancel discovery.
3.  Copy the sys\_id from the record
    -   The sys\_id is a 32-character unique identifier
    -   Example: 0123456789abcdef0123456789abcdef

#### Run the cancellation script

1.  In the navigation filter, type **background script**
2.  Select Background Scripts from the results
3.  In the script editor, paste this code: 

var cancelBS = new CancelBSDiscovery(); cancelBS.cancelAll("your\_business\_service\_sys\_id\_here"); 

4.  Replace your\_business\_service\_sys\_id\_here with the actual sys\_id.
5.  Select **Run script.**

Example script with sample sys\_id:

var cancelBS = new CancelBSDiscovery();
cancelBS.cancelAll("0123456789abcdef0123456789abcdef");  
  

#### Verify the cancellation

To confirm discovery was canceled:

1.  Go to **Service Mapping** > **Discovery Status**
2.  Check that the discovery status shows as canceled.
3.  Review the discovery logs for confirmation messages.
