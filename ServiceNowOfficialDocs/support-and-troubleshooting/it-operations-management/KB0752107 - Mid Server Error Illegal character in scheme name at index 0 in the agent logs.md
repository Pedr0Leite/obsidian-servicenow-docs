---
title: "Mid Server Error: Illegal character in scheme name at index 0 in the agent logs"
aliases:
  - KB0752107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752107
kb_number: KB0752107
last_modified: 2024-04-07
---

## Mid Server Error: Illegal character in scheme name at index 0 in the agent logs

  

### Issue

-    Post-installation of Mid Server, it shows below error in the MID Server agent logs:

\[AMBClientProvider\] ERROR com.snc.glide.amb.AMBClient - Illegal character in scheme name at index 0: [https://<instance-name>.service-now](https://%3Cinstance-name%3E.service-now/)  
java.lang.IllegalArgumentException: Illegal character in scheme name at index 0: [https://<instance-name>.service-now](https://%3Cinstance-name%3E.service-now/)

### Release

-   The issue can occur in any release.

### Cause

-   An extra space character in the instance server URL parameter in the mid server config.xml file.  
    

### Resolution

-   In order to resolve this issue, follow the below steps.  
      
    -   Connect to the Mid Server Host and Navigate to < Mid-Installation Directory>/agent/config.xml file.
    -   Open the file and Locate the following parameter:  
            <parameter name="url" value=" [https://<instance-name>.service-now](https://\<instance-name\>.service-now/)\>
    -   Check if there is any extra space added while adding the URL and remove the same.
    -   Save the file and restart the Mid Server.
