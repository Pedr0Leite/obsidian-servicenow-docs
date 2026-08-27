---
title: "Navigating back to a form after using an \"Edit\" UI Action displays a page with only unstyled related lists"
aliases:
  - KB0596843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596843
kb_number: KB0596843
last_modified: 2024-04-07
---

## Navigating back to a form after using an "Edit" UI Action displays a page with only unstyled related lists

  

### Issue

After clicking the **Edit** button on a related list and then navigating back to the form, instead of being presented with the form, a page displays containing only the related lists of the form, which appear in an unstyled manner. Instead of the form page (for example, **incident.do**), the related lists of the form appear (for example, **list2\_deferred\_related\_lists.do**).

The following screenshots show an example.

![](/sys_attachment.do?sys_id=e27e3462db0ab450e515c22305961989)

![](/sys_attachment.do?sys_id=e67e3462db0ab450e515c223059619ad)

### Release

All Releases

### Cause

This issue occurs in the following scenario:

-   [**Related List Loading**](https://docs.servicenow.com/csh?topicname=t_ConfigureWhenARelatedListLoads.html&version=latest "Related List Loading") is set to either **On-demand** or **After Form Loads**.
-   One or more JavaScript errors have occurred on the form.
-   The user presses the **Edit** button.

### Resolution

To ensure this behavior does not occur, as an administrator, you should review the browser console before clicking the **Edit** button on forms where this issue occurs and ensure that any JavaScript errors are corrected. JavaScript errors should never occur on forms, and they can cause many other issues apart from the one described.

![](sys_attachment.do?sys_id=789fcebc1bc47014f34d33bc1d4bcb6e)

Some of the places where customer-defined JavaScript could cause errors on a form are:

-   Client scripts
-   UI Policies (Execute if true/Execute if false)
-   UI Scripts
-   UI Macros placed on the form using a UI Formatter

For information about identifying the cause of JavaScript errors by using the Google Chrome browser's DevTools, see the [Google Developers website](https://developers.google.com/web/tools/chrome-devtools/debug/?hl=en "Google Developers website").

**Note** – JavaScript errors in the browser console have sometimes been caused by known problems. If you believe the error you are seeing is related to a known problem, raise an incident in the Now Support (HI).

### Related Links

For more information about debugging client side errors check out this [blog post](https://community.servicenow.com/community?id=community_blog&sys_id=5becee65dbd0dbc01dcaf3231f961940&view_source=searchResult "blog post").
