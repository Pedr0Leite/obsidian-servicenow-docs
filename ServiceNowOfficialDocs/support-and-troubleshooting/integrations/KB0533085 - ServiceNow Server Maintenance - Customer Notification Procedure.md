---
title: "ServiceNow Server Maintenance - Customer Notification Procedure"
aliases:
  - KB0533085
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0533085
kb_number: KB0533085
last_modified: 2025-11-17
---

## ServiceNow Server Maintenance - Customer Notification Procedure

  

### Issue

ServiceNow Server Maintenance | Customer Notification Procedure

  

# Overview

* * *

ServiceNow performs periodic maintenance to the server infrastructure that is hosting customer instances. This is to ensure that these systems are functioning as optimally as possible. This maintenance can involve server restarts, which impacts the reasonable efforts to schedule server maintenance outside of business hours for the data center where the server is located. This is done to mitigate the impact to our customers' business activities. 

# Types of Server Maintenance

* * *

-   Database Server Maintenance
-   Application Service Maintenance

# Database Server Maintenance

* * *

-   ServiceNow uses commercially reasonable efforts to provide a 14-day notification for maintenance on servers that are hosting primary production databases, where the maintenance will result in loss of service availability to instances hosted on the server. Though we will try to give as much notice as possible, at times, we may not be able to provide this 14-day notification if maintenance must be immediately performed to restore service or prevent an imminent system failure.
-   ServiceNow does not provide notification to customers for maintenance on redundant (backup) database servers, because the impact to service availability is almost non-existent, due to minimal use by the instance

# Application Server Maintenance

* * *

-   All ServiceNow instances are supported by multiple application nodes, which are distributed across multiple application servers. This means that if one application server is unavailable, users are still able to access their ServiceNow instance via the other application nodes hosted on the redundant application server(s). Maintenance can be performed on application servers with minimal impact to users of the instance. Because this is the case, ServiceNow does not notify customers when maintenance is performed on an application server.
-   Once maintenance is completed on an application server, it is sometimes necessary for the server to be restarted to complete the maintenance activities. The impact associated with an application server restart is limited to the subset of users logged into the application server at the time of the restart. The scope of the impact is dependent upon certain instance configuration. 

Impact when SAML or Remember Me functionality is enabled

* * *

-   If the instance has been configured to use **SAML authentication** or has the **Remember Me** functionality enabled, users with established sessions on the application server at the time of restart will experience the following: normal navigation is completely transparent except in cases where a ticket update or similar POST to the instance has been requested. In these cases, the user would receive the following warning message for session token mis-match:   
      
    ![warning message for session token mis-match](/sys_attachment.do?sys_id=b8d9fef097315290f03d739c1253af7b "warning message for session token mis-match")  
      
    
    -   Selecting **Continue** will complete the update or POST transaction and the user will be re-directed back to the instance’s welcome page.
    
    # Impact when SAML or Remember Me functionality is not enabled
    
    * * *
    
      
    If **SAML authentication** is not in use or **Remember Me** is not enabled, users with established sessions on the application server at the time of the restart will experience the following:  
      
    
    -   The next click will redirect the user to the ServiceNow instance's login screen. Upon login, if the request was only navigational, the user will be directed to the requested page. If the request is for an update or POST transaction, the SCRF Session token mis-match warning will appear, but the update is lost once **Continue** is selected and will need to be re-processed by the user.
    
      
    For additional information on **SAML authentication** or the **Remember Me** functionality, see the following product documentation pages:  
      
    -   [SAML](https://docs.servicenow.com/csh?topicname=t_CreateASAML2Upd1SSOConfigMultiSSO.html&version=latest)
    -   [Remember Me](https://docs.servicenow.com/bundle/xanadu-platform-security/page/administer/login/concept/c_ChSetRemMeChkbxCookie.html)
