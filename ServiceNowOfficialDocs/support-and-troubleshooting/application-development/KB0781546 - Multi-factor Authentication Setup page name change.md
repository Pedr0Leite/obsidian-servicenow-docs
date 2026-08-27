---
title: "Multi-factor Authentication Setup page name change "
aliases:
  - KB0781546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781546
kb_number: KB0781546
last_modified: 2024-04-07
---

## Multi-factor Authentication Setup page name change

  

### Issue

As part of security and legal mandate, we have made certain changes in the multi-factor authentication setup instructions. This includes updating in the verbose of the setup instruction and changing the UI page name. This KB will provide details about these changes and it's impact. 

### Release

The UI page name change is applicable from Orlando release.

### Cause

As part of legal requirement we were needed to remove direct reference to download Google Authenticator TOTP app in the MFA setup page.  
ServiceNow MFA offering supports many other time based OTP (TOTP) apps. We must not provide links to customer to download Google Authenticator app. Previously the instruction said  
  
1\. Download the Authenticator app for your mobile device

-   [Apple iTunes](https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8)
-   [Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)
-   [Windows Store](http://www.windowsphone.com/en-us/store/app/authenticator/e7994dbc-2336-4950-91ba-ca22d653759b)

![MFA setup page](sys_attachment.do?sys_id=afcf0330db0834d0471f9c41ba9619c7 "google_auth_setup_page.do")

Apart from the verbose changes, we were also needed to update the name of the page from **google\_auth\_setup\_page** UI page to **multi\_factor\_auth\_setup\_page.** Now because of this name change of UI page, customers who has modified the **google\_auth\_setup\_page** page will face the page not found error while setting up MFA. As due to customisations, the name will not be auto-updated to **multi\_factor\_auth\_setup\_page.**

### Resolution

If the customer has made changes in the **google\_auth\_setup\_page** UI page, prior to upgrade to Orlando, we can set **_replace\_on\_upgrade_** flag **"true"** for this **UI page** in _**sys\_update\_xml**_ table for this record.  
  
Alternatively, post upgrade we can manually rename the **google\_auth\_setup\_page** UI page to **multi\_factor\_auth\_setup\_page.  
**This will fix the page not found issue.

####   
Verbose Changes

  
As part of the requirement, we have removed the direct links to Google Authenticator app.  
1\. Download an authenticator app that supports Time Based One-Time Password(TOTP) on your mobile device.  
[More Details](https://docs.servicenow.com/search?q=CSHelp:MFA-Authenticator)  
  
![New MFA setup Page](sys_attachment.do?sys_id=27cf0330db0834d0471f9c41ba9619c9 "multi_factor_auth_setup_page.do")

### Related Links

Supported third-party authenticators with MFA

[https://docs.servicenow.com/csh?topicname=mfa-authenticator-supported.html&version=latest](https://docs.servicenow.com/csh?topicname=mfa-authenticator-supported.html&version=latest)
