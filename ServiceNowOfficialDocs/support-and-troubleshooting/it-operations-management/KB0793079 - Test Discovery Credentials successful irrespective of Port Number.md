---
title: "Test Discovery Credentials successful irrespective of Port Number"
aliases:
  - KB0793079
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793079
kb_number: KB0793079
last_modified: 2025-01-03
---

## Test Discovery Credentials successful irrespective of Port Number

  

### Summary

-   Navigate to Discovery --> Credentials.
-   Open any Windows Credentials.
-   Test Credentials on an IP which has affinity with these credentials by specifying port number.
-   Test will be successful.  
      
    ![](sys_attachment.do?sys_id=c83e1bfcdb8434d0b55f0b55ca96196b)  
      
    
-   Test Credentials on the same IP without providing port number.
-   Test will again be successful.  
      
          ![](sys_attachment.do?sys_id=443e1bfcdb8434d0b55f0b55ca96196a)  
      
    
-   The port number is displayed only for information purpose.
-   Test credential does not rely on port displayed in the UI.
-   In the background, a powershell cmdlet - `gwmi win32_operatingsystem -computer $computer -credential $cred -impersonation 3 -authentication 6 -EA "Stop"`  is called and by default it directly targets to WMI port of target ip address.
-   Thus irrespective of Port displayed on the UI , the credential test will target port 135 and fails only when there is a credentials issue.

### Related Links

**Useful documents:**

-   [Test Credential](<'Test Credential' fails when using Windows Credentials against the MID server localhost> "Test Credential")
-   [Getting started with credentials](https://docs.servicenow.com/csh?topicname=credentials-getting-started.html&version=latest "Getting started with credentials")
