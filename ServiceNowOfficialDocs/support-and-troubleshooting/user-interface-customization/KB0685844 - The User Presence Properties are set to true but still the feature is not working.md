---
title: "The User Presence Properties are set to true but still the feature is not working"
aliases:
  - KB0685844
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685844
kb_number: KB0685844
last_modified: 2025-01-10
---

## The User Presence Properties are set to true but still the feature is not working

  

### Issue

The User Presence Properties are set to true but still the feature is not working. 

-   Your avatar on the header doesn't show a green dot on the home page:  
      
    ![avatar on the header not showing green dot presence indicator](/sys_attachment.do?sys_id=7ab85a4147871250c4e1a325126d4374 "Presence indicator")  
      
    
-   When two users are watching the same record, user presence is not visible on the header of the form:  
      
    ![User presence in a form](/sys_attachment.do?sys_id=7eb85a4147871250c4e1a325126d4376 "User presence in a form")

### Release

Jakarta - UI16

### Cause

-   The correct user presence property is not enabled
-   After the presence property is enabled, browser cache is not cleared

### Resolution

1.  Make sure the value of the system property '**glide.ui.presence.disabled**' is _**false**_:  
    https://<your\_instance\_name>.service-now.com/sys\_properties\_list.do?sysparm\_query=name%3Dglide.ui.presence.disabled&sysparm\_first\_row=1&sysparm\_view=
2.  Clear browser cache to see the change. User presence works only if the browser cache is cleared after the property is enabled.

### Related Links

-   If you want to read more about why you need to flush browser cache to see the change read more about it in this article: [User presence works only if the browser cache is cleared](https://support.servicenow.com/kb_view.do?sysparm_article=KB0685847 "User presence works only if the browser cache is cleared")
-   Here you can read more about this system property: [Disable user presence](https://docs.servicenow.com/csh?topicname=t_DisableUserPresence.html&version=latest "Disable user presence")
-   Read more about presence: [User presence](https://docs.servicenow.com/csh?topicname=c_UserPresence.html&version=latest "User presence")
