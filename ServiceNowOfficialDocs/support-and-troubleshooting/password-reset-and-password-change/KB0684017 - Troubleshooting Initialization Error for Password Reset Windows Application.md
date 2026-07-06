---
title: "Troubleshooting \"Initialization Error\" for Password Reset Windows Application"
aliases:
  - KB0684017
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684017
kb_number: KB0684017
last_modified: 2025-01-03
---

## Issue

The following error message appears when using the Password Reset Windows Application

"_Initialization Error, Unable to establish connection. Either you cannot connect to the network or the required plugin is not active. Contact the service desk for Assistance_"

**Note**: We will refer to _Password Reset Windows Application_ as **PRWA**

## Resolution

1.  Confirm the plugin is active on the instance:  
    -   Go to System Definition > Plugins, make sure the "**Password Reset Windows App**" plugin is activated
2.  Make sure the URL is working in a web browser:  
    -   Navigate to **Password Reset > Processes**
    -   Open the process record
    -   Right click on "Public URL", then click on "Copy Link Address"
    -   Paste it in a browser, and test it.
3.  Make sure the Password Reset process is active, and the Credential Store type is "AD Credential Store"
4.  On the machine where PRWA is installed, check windows registry key below, make sure the reset URL is correct (as you copied in _Step 2_  
    -   \[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers\\{0780AF60-65C2-4718-942D-E0C56E89EF9B}
    -   "PasswordResetLinkURL"="https://<instance-name>.service-now.com/$pwd\_reset.do?sysparm\_url=xxxxxx"
5.  On the same machine, open the reset URL in a web browser, and see if it works.
6.  On the computer where PRWA is installed, Start the application via C:\\Program Files\\ServiceNow>PasswordResetWinApp.exe, test if it works.
7.  If you are using Web Proxy in your environment, it's necessary to set up proxy for PRWA.  
    -   Please refer to the section "_Installation and Configuration Instructions_" in [KB0542328 - Password Reset Windows Application](https://support.servicenow.com/kb_view.do?sysparm_article=KB0542328 "KB0542328 - Password Reset Windows Application")
8.  Check if there's any customization on **System UI > UI Page > $pwd\_reset** 
9.  Check supported TLS versions in the instance. Notice that for TLS 1.2 PRWA 2.9 and above is required. You can check the list of supported TLS versions by using the site below (replace instance with the instance name):

[https://www.ssllabs.com/ssltest/analyze.html?d=instance.service-now.com](https://www.ssllabs.com/ssltest/analyze.html?d=instance.service-now.com)

## Additional Information

Check the \[pwd\_access\_log\] table, which shows events when PRWA connects to the instance
