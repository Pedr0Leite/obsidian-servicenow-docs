---
title: "External website URL in iFrame results in a blank CMS page"
aliases:
  - KB0551989
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551989
kb_number: KB0551989
last_modified: 2024-11-18
---

## External website URL in iFrame results in a blank CMS page

  

### Issue

A CMS page containing an iFrame specifying the URL of an external website displays a blank page in the example below:  
  
![Iframe - external link configuration](sys_attachment.do?sys_id=7bfcd6c0934e1ad0101833527cba106d "Iframe - external link configuration")

### Cause

Launching a CMS page with an iframe that contains the URL of an external site results in a blank page and the following console error in the Chrome Developer Tools Console:

-   _Refused to display '<url specified within IFrame>' in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN'_  
      
    !["Refuse to Display" error message when 'X-Frame-Options' set to 'SAMEORIGIN'](/sys_attachment.do?sys_id=f7fcd6c0934e1ad0101833527cba106a "Error message \"Refuse to Display")

This is related to [mixed content blocking in browsers](https://www.howtogeek.com/443032/what-is-mixed-content-and-why-is-chrome-blocking-it/ "mixed content blocking in browsers") \[howtogeek.com\].

### Resolution

Displaying this content within an iframe is not supported by the target domain/server (https://cloud.oracle.com in the above example) and browser security.  
  
The solution is to not use an iframe. For example, here is a link added to the **Get Help** section on the ess homepage that will open the link in a new page:  
  
![Setting up hyperlink to external site instead of using an iFrame](/sys_attachment.do?sys_id=3ffcd6c0934e1ad0101833527cba1070 "Setting up Link to external site")  
  
![Example of link navigating to external site](/sys_attachment.do?sys_id=f7fcd6c0934e1ad0101833527cba1074 "Link to site works fine")

### Related Links

[X-Frame-Options: SAMEORIGIN (instance security hardening)](https://www.servicenow.com/docs/csh?topicname=x-frame-options-sameorigin.html&version=latest "X-Frame-Options: SAMEORIGIN (instance security hardening)")
