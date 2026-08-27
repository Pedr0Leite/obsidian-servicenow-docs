---
title: "A UI Page variable for a Catalog Item to display the calendar not working since upgrading. Why?"
aliases:
  - KB0778503
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778503
kb_number: KB0778503
last_modified: 2024-04-08
---

## A UI Page variable for a Catalog Item to display the calendar not working since upgrading. Why?

  

### Issue

The user has a variable which is calling a custom UI Page. After upgrading to Madrid, the variable no longer works. 

### Cause

The mentioned UI Page is a custom created UI Page which needs revision to be adapted to the current Platform code (see further details below).

### Resolution

As mentioned above, the behavior is surrounding a custom UI Page. It is notable that the UI Page fails outside of using it within a variable, so the variable itself is not the issue - it is the custom UI Page.  
  
To confirm, the user can navigate to the URL of the custom UI Page see that the page is blank when attempting to try to view it:

-   -   -   /ui\_page.do?sys\_id=673c022b6fd8a200bf9f4d1fde3ee4fe

After searching some time, it was found that there are no similar calendar-like UI Pages in an Out of Box (OOB) Madrid instance (in hopes of being able to offer to the user to revert back to OOB and re-develop the customization from there).   
  
Genuinely empathize with the user and kindly share with them that there are many code changes in the Platform between patches, and even more between family releases (Kingston vs. London, London vs. Madrid, etc).  
  
As such, when customizations are developed by users, they are responsible for maintaining those customizations and adapting them to the code changes which occur in the Platform between patches and family changes.  
  
Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementing of customizations like this is not in the engineer's area of expertise.  
  
If the user would like, there are additional resources to help rebuild their customization such as we have a very helpful Community website where our wonderful customers discuss and assist one another with custom implementations. For the user's convenience, here is the URL to that site:

-   -   -   [https://community.servicenow.com/community](https://community.servicenow.com/community)

The user can also make use of our Professional Services team who are experts in debugging, creating, and maintaining customizations like this. Please note, however, that there is a fee associated with this service.
