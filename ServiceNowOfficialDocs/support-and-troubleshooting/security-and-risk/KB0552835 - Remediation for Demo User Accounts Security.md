---
title: "Remediation for Demo User Accounts | Security "
aliases:
  - KB0552835
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552835
kb_number: KB0552835
last_modified: 2024-01-28
---

## Issue

Remediation for Demo User Accounts | Security 

## Resolution

ServiceNow instances are typically created with demo data, including demo accounts. Some of these demo accounts have default passwords. If an administrator of an instance does not manage these accounts appropriately or request that [demo data be removed](/com.glideapp.servicecatalog_cat_item_view.do?sysparm_id=0755a2696f188200030cf7307f3ee447 "demo data be removed"), it may result in unauthorized access. In an effort to improve security, ServiceNow regularly audits for these default credentials.

### Impact

-   Administrators who [check for failed login attempts](https://docs.servicenow.com/csh?topicname=c_LoginSecurity.html&version=latest "check for failed login attempts") may see failed logins for default demo accounts, such as admin, itil, and employee.
-   The source IP address of the login attempt will be from a 10.0.0.0/8 IP address or a public (non-RFC 1918) IP address which belongs to ServiceNow.
-   Public IP addresses can be confirmed to be ServiceNow's by doing a who is lookup on the IP address in question. 

### Remediation

As a result of periodic auditing for default credentials, ServiceNow may proactively modify the demo accounts by removing the default password and [setting the "locked out" field to true](https://docs.servicenow.com/csh?topicname=c_ManageUserSessions.html&version=latest "setting the \"locked out\" field to true"). ServiceNow will do this if the demo account has a default password or if it is already locked out.

  

### **FAQs  
  
**

-   **Q: How will removal of this these credentials or demo data impact me?**
-   A: You will not be able to access any of the default accounts unless you reactivate them and set up a new password. If these accounts are required, we recommend following the guidance on password management in the [ServiceNow Instance Hardening Guide](/kb_view.do?sysparm_article=KB0550654 "ServiceNow Instance Hardening Guide").  
      
    
-   **Q: Will data created by any of the default accounts be affected?**
-   A: No. We are only altering the _Password_ and _Locked Out_ fields of the accounts.  Any data created by or associated with these default accounts will be in tact.  
      
    
-   **Q: How will I be able to access any of the data created by these default accounts?**
-   A: An account with the admin role can access any of the data created by these default accounts.  
      
    
-   **Q: What if I have already changed the passwords for demo accounts, removed demo accounts, or locked out all demo accounts?**
-   A: No action will be taken on your instance.  
      
    
-   **Q: Will user accounts that I have created by affected?**
-   A: You will not be affected as long as the user ID and the password does not match a default account included in demo data.  
      
    
-   **Q: How often will ServiceNow be performing these audits?**
-   A: Typically on a quarterly basis.
