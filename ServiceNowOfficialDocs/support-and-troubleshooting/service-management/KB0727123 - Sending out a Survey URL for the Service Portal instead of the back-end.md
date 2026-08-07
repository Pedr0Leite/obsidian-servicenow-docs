---
title: "Sending out a Survey URL for the Service Portal instead of the back-end"
aliases:
  - KB0727123
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727123
kb_number: KB0727123
last_modified: 2026-06-24
---

## Sending out a Survey URL for the Service Portal instead of the back-end

  

### Issue

 

Survey URL is redirecting to Native View instead of Service Portal.

### Release

Any

### Cause

The **AssessmentUtils** Script Include has a method called **getAssessmentInstanceURL()** which can be used in an **Email Notification Script** to send a direct Survey link via email.

By default, this will send out a **'nav\_to.do'** link which is for the back-end

### Resolution

To configure this method to return a URL to the Service Portal, please complete the following:

-   Ensure the **'sn\_portal\_surveys.sp\_survey.email\_redirection'** System Property is set to value **'true'**
-   Navigate to **Service Portal > Portals**
-   Ensure that the **'Service Portal'** Portal record has the field **'Default'** set to the value **'true'**

Once you have completed the above, you will be able to use the following code in an **Email Notification Script:**

-   new AssessmentUtils().getAssessmentInstanceURL(_Survey\_Instance\_Sys\_ID\_Here_)

This will allow you to pass the Service Portal URL to the **Notification** so that the User will be directed to the correct page.
