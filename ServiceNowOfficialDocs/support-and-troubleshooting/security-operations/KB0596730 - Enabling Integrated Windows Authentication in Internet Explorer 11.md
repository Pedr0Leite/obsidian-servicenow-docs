---
title: "Enabling Integrated Windows Authentication in Internet Explorer 11"
aliases:
  - KB0596730
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596730
kb_number: KB0596730
last_modified: 2024-04-07
---

## Issue

Enable Integrated Windows Authentication | Internet Explorer 11

Overview

* * *

Are you trying to [NTLM](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378749%28v=vs.85%29.aspx "NTLM") with IE browsers? If you are Windows authenticated, are you expecting IE browser to authenticate automatically?  
  
Enabling Windows Integrated Windows Authentication in IE11:  
  
[https://docs.secureauth.com/display/KBA/Enable+Integrated+Windows+Authentication+(IWA)+in+Internet+Explorer  
](https://docs.secureauth.com/display/KBA/Enable+Integrated+Windows+Authentication+%28IWA%29+in+Internet+Explorer)

Steps for Enabling Windows Integrated Authentication in IE11

* * *

1.  Open Internet Explorer.
2.  Navigate to the **Tools > Internet Options > Advanced tab**.
3.  Select **Enable Integrated Windows Authentication**.
4.  Open the **Security** tab.
5.  Select **Local Intranet > Custom Level**.
6.  Under **User Authentication**, select **Automatic log-on with current user name and password**.
7.  Click **OK** on all windows.
8.  Restart Internet Explorer by closing all IE windows and then opening them again.
