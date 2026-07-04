---
title: "How to look for apparently missing reports in the View / Run report list layout"
aliases:
  - KB0550734
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550734
kb_number: KB0550734
last_modified: 2024-04-07
---

## How to look for apparently missing reports in the View / Run report list layout

  

### Issue

When a particular user creates a report, it is not appearing under his/her View / Run reports list, however the report has been successfully created and can be seen by an Admin.

### Release

UI14 or UI15

### Cause

You may have accidentally clicked the star icon in the list header so only favorite reports appear. If some of your reports have not been marked as a favorite, then you would not be able to see or search for them.

![](sys_attachment.do?sys_id=6a2e0ebcdb0c74d0fec4fb24399619ea)

### Resolution

Two simple solutions are:

-   clear the star icon in the list header  
    or
-   mark all the reports you want to see as favorites

![](sys_attachment.do?sys_id=e22e0ebcdb0c74d0fec4fb24399619e9)

### Related Links

In UI14, you can manually mark a report as a favorite by clicking the star icon beside the report title. To toggle between showing only favorite reports and showing all reports, click the star icon in the list header.

In UI14 on Fuji, a report is automatically marked as a favorite when you open the report.

Starting with UI15 (on Fuji and later), the new View/Run reports list layout uses the general Automatically Add Favorites per-user setting to define the preferred behavior. You can modify this by clicking the menu icon in the Application Navigator. Toggle the option to enable or disable automatically adding favorites (see below screen shot). The setting applies to the selection of both application menu modules and reports.

![](sys_attachment.do?sys_id=6e2e0ebcdb0c74d0fec4fb24399619e7)
