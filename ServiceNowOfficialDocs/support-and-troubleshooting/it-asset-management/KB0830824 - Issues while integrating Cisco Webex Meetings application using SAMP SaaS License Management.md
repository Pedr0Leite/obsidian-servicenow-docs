---
title: "Issues while integrating Cisco Webex Meetings application using SAMP SaaS License Management"
aliases:
  - KB0830824
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830824
kb_number: KB0830824
last_modified: 2024-04-08
---

## Issue

This KB addresses few issues while integrating Cisco Webex Meetings application.

## Resolution

-   **Issue #1 :**  
    -   Below generic error can be seen for Subscriptions. This job can be found under the Integration profile created for Cisco Webex Meetings Application.  
        -   "Failed to download subscriptions. Please verify that <email address> is the correct admin email address for the Webex Meetings integration. To update the email address, navigate to sn\_webex\_meetings\_spoke\_accounts.list and update the Email field for the Webex account"
-   **Resolution :**  
    -   Make sure attached OOB sys\_alias record is present in the instance and link the same in "Connection & Credential" field of the Integration profile.  
        

  

-   **Issue #2 :**   
    -   Below generic error can be seen for Activity job. This job can be found under the Integration profile created for Cisco Webex Meetings Application.  
        -   "Failed to calculate last activity. Please verify that <email address> is the correct admin email address for the Webex Meetings integration. To update the email address, navigate to sn\_webex\_meetings\_spoke\_accounts.list and update the Email field for the Webex account."
-   **Resolution :**  
    -   Open subflow : "Webex Update User Activity" and remove action : "Look Up Software Subscription Record". This is being addressed by PRB1412287

  

![Remove Look Up Software Subscription Record](sys_attachment.do?sys_id=b7333cc51b487414f34d33bc1d4bcb54 "Remove Look Up Software Subscription Record")

  

-   **Issue #3 :**   
    
-   -   Post integration and once the data is downloaded, we can see many Webex subscriptions reporting activity having a future Last Activity date.
-   **Resolution :**  
    -   **PRB1412287** would be addressing this as well. There is no specific workaround for this due to the API call we are using. However, while we do stamp last activity with future dates it has NO impact on reclamation candidates and savings.

  

-   **Issue #4 :**  
    -   Reclamationation candidates may not match with the reclamation rules.

-   **Reason for this data :**  
    -   When users are flagged as stale with a reclamation candidates, those candidates are not updated with new usage information (so "Stale" might be changed from True to false) but the candidate record still exists. The Total stale rights field in the user summary is always going to be accurate based on a the last daily pull of data from the SaaS account. As it stands, those numbers (stale vs reclamation candidates will almost always be different, because of the dynamic nature of the integration).
-   **Resolution :**  
    -   Customers should DELETE those reclamation candidates who become active again, instead of processing them for reclamation.
