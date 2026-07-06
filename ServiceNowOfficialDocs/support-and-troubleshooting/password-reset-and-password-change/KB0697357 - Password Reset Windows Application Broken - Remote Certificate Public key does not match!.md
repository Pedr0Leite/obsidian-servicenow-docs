---
title: "Password Reset Windows Application Broken - \"Remote Certificate Public key does not match!\""
aliases:
  - KB0697357
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697357
kb_number: KB0697357
last_modified: 2025-05-27
---

## Password Reset Windows Application Broken - "Remote Certificate Public key does not match!"

  

### Issue

1.  When launching the Password Reset Application, it will produce the following error.  
    "Initialization Error: Unable to communicate with the ServiceNow instance for one of the following reasons: No network connection, the required plugin is not active, or you are using a ServiceNow release that is not compatible with the API"  
      
    ![](/sys_attachment.do?sys_id=fbca1c639769a650708b78ce2153af0a)  
      
    
2.  When you Check Eventviewer for errors log, we could see below screenshot where one information entry log before the actual "Error log" contain information that the "Remote Certificate Public Key does not match"  
      
    ![](/sys_attachment.do?sys_id=67cad8639769a650708b78ce2153afff)

### Resolution

You are getting the above issue because the certificate is rotated on the ServiceNow instance, and the Password Reset Windows Application cannot validate it. You can choose either of the options to fix it, but we recommend upgrading to a new version v5.1.4 (Option 1) as we have fixed the issue permanently, and you may not need to follow these steps again in the future.  
  
Option 1:-  
  
**Update your application to 5.1.4 or newer release version of Password Reset Windows Application.  
****Changes done in v5.1.4** -  
This version onwards the **ServiceNowCertPublicKey** registry entry is not required anymore. Hence we have removed **ServiceNowCertPublicKey** from the path **\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers\\{0780AF60-65C2-4718-942D-E0C56E89EF9B}\]  
**The application is inline with policy of instance certificate rotation. The application doesn't depend on registry value anymore, now we are internally validating the certificate.

Option 2:-  
  
**Note**: If you are not choosing to upgrade to 5.1.4 or newer release(If available), please make sure to update registry value(follow below steps) as instance certificate rotation policy will eventually be changed to 47days in near term.

         1. Check the registry Key for the Public Key that comes with the Installer at the following path.

1.  -   Key Name: ServiceNowCertPublicKey
    -   \[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers\\{0780AF60-65C2-4718-942D-E0C56E89EF9B}\] 
2.   Compare that public key(first line - refer step 7) in Windows Registry with the Certificate value (follow step 2 to 6) on the Instance and you will see that they are different.

Getting Public key from Instance:

          With Google Chrome

1.  Access your instance (i.e https://<instance-name>.service-now.com) in Google Chrome
2.  Click on icon near url -  
    ![](/sys_attachment.do?sys_id=afca1c639769a650708b78ce2153af03)   
3.  Click "Connection is secure" → "Certificate is valid"
4.  Copy certificate value.
5.  ![](/sys_attachment.do?sys_id=e3ca1c639769a650708b78ce2153af06)
6.   For example 7b7c0687696412a5ea236439e900b1bfd98c7067669c1a90efa90c6459ddd64b is the default certificate id valid till 13 October 2025 (Note: This value may vary by instance).
7.  Add or replace the existing key in Windows Registry (ServiceNowCertPublicKey) with the certificate id from Instance. This field supports multiple entries, so you only need to update the first line.  
    ![](/sys_attachment.do?sys_id=f3ca1c639769a650708b78ce2153af1b)
8.  Re-launch the Application and confirm that it worked.
