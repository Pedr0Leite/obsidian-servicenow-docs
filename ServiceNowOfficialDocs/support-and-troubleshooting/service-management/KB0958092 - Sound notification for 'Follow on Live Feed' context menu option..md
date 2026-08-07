---
title: "Sound notification for 'Follow on Live Feed' context menu option."
aliases:
  - KB0958092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958092
kb_number: KB0958092
last_modified: 2025-01-03
---

## Sound notification for 'Follow on Live Feed' context menu option.

  

### Summary

When we open any active record, we have 2 ways to follow the record to get regular records. They are by:

1.  Clicking the Follow UI action.
2.  Right-click on the context menu header, and select **Follow on Live Feed**

The **Follow on Live Feed** context menu sound notification cannot be changed.  

-   When you select the Follow on Live Feed, you can view the record feed both $live\_feed.do page, and also on Connect Sidebar.
-   The sound that you actually hear is triggered from the Connect Module. Because the live feed and connect notification are triggered at the same time.
-   Live Feed itself does not have a sound notification. Live Feed just shows a browser popup.
-   This context menu functionality is exactly the same as **Follow UI** action that you see on the form banner.
-   If you want to the sound, the change will be applied for the entire connect module, ie - Connect Chat, Connect Support & Live Feed.  
    You cannot do it individually for Live Feed.

### Related Links

If you wish to change the sound for the entire Connect module:  

1.  navigate to db\_audio.list
2.  Search for connect\_alert.mp3
3.  Open the record
4.  Upload a new file
5.  Clear the instance cache.
