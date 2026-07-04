---
title: "Give Feedback Button is not visible on Employee Center"
aliases:
  - KB1406108
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1406108
kb_number: KB1406108
last_modified: 2026-04-14
---

## Give Feedback Button is not visible on Employee Center

  

### Issue

Give Feedback Button is not visible on Employee Center as per Give Feedback functionality as per this documentation -https://www.servicenow.com/community/hrsd-blog/listening-posts-voluntary-feedback/ba-p/2279378

### Release

All

### Resolution

**The "Give feedback" tab is displayed using the below widget:** https://**<<Instance Name>>**.service-now.com/nav\_to.do?uri=sp\_widget.do?sys\_id=e15519c8eba73010b5e69ebe1a5228bf  
  
**That widget is used in the below header:** https://**<<Instance Name>>**.service-now.com/nav\_to.do?uri=sp\_header\_footer.do?sys\_id=d0009941eb103010ed7966d6475228c1  
  
The header is used in the '**EC Theme**' on the /esc portal in the OOB instances. In the ESC the portal is configured to use the '**ESC Theme**' which uses the 'Employee Center Header' that does not use the "Give Feedback" tab.  
  
**Theme:** https://**<<Instance Name>>**.service-now.com/nav\_to.do?uri=sp\_theme.do?sys\_id=9b6f06d71bb8f85047582171604bcb9c  
  
**Customization in header:** https://**<<Instance Name>>**.service-now.com/nav\_to.do?uri=sp\_header\_footer.do?sys\_id=d0009941eb103010ed7966d6475228c1  
  
Once the "**Employee Center Header**" is reverted to the **Out of the Box (OOB)** version users were able to see the "GIVE FEEDBACK" Option on ESC portal.
