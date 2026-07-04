---
title: "Opening deep link in email message causes error when using Internet Explorer 11"
aliases:
  - KB0565019
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0565019
kb_number: KB0565019
last_modified: 2024-05-01
---

## Opening deep link in email message causes error when using Internet Explorer 11

  

### Issue

Opening deep link in email message causes error 

Issue description

* * *

If a deep link contained within a email is clicked and IE v11 is not open, the following error message is displayed:

SAMLResponse could not be validated

If IE v11 is _open_ before clicking the deep-link, it works properly. If IE v11 is closed and the deep link in Outlook is clicked, the error occurs. The instance logs confirm that the SAML message was received from the browser properly and that a perfect SSO message was returned back to the browser.

Further details:

-   IDP correctly receives authentication message
-   the response is sent back to the browser with a properly formatted SAMLResponse and Relay state
-   this issue only occurs in IE v11 - it does not occur in IE v9
-   if the call is made in the browser directly, it worked properly

Cause

* * *

One possible cause for this behavior is that Internet Explorer's local internet zone list has not been set to allow the \*.service-now.com domain.  

Solution

* * *

If you are experiencing this behavior and \*.service-now.com is not included in your local internet zone, add \*.service-name.com to the Internet zone list in IE v11.
