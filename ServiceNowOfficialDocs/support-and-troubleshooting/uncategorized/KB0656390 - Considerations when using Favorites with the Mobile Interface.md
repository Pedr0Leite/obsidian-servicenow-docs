---
title: "Considerations when using Favorites with the Mobile Interface"
aliases:
  - KB0656390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656390
kb_number: KB0656390
last_modified: 2024-04-07
---

## Considerations when using Favorites with the Mobile Interface

  

### Issue

**Favorites** in the Mobile App are shared with the Bookmarks seen in the Desktop UI, and they are stored in the sys\_ui\_bookmarks table. At this time there is not a way to separate the Favorites between the Mobile and Desktop UI.

There are 2 places Favorites can be accessed in the Mobile App.

1.  On the Favorites homepage. By default the Favorites homepage is accessible by swiping right on the Mobile Homepage. The Favorites homepage can be excluded by checking the “Hide Favorites” flag in the corresponding Home Page Collection.

             ![](/sys_attachment.do?sys_id=4a0924aedb02b450e515c22305961960)

2.  In the Navigator. When opening the Navigator, a user can tap the star icon in the upper right corner of the Navigator to view their Favorites. This option **cannot** be hidden, so users will always have at least 1 way to access their Favorites.

![](/sys_attachment.do?sys_id=0e0924aedb02b450e515c22305961965)
