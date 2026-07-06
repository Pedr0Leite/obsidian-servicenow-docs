---
title: "How to Determine Users Enrolled in Password Reset That Need to Re-validate their Device"
aliases:
  - KB0725008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725008
kb_number: KB0725008
last_modified: 2024-04-07
---

## How to Determine Users Enrolled in Password Reset That Need to Re-validate their Device

  

### Issue

# Description

* * *

You may have an issue in which a user or group of users see an error message for password enrollment that states,

**"The number of questions required for enrollment has changed. Enroll again."**

The number of users affected by this is unknown until a report is run. There is a built in report on your instance named "Password Reset Enrollment By Verification".

# Procedure

* * *

You can view the report by the following methods.

Method 1

1.  Copy this text [https://YOUR\_INSTANCE.service-now.com/nav\_to.do?uri=%2Fsys\_report\_template.do%3Fjvar\_report\_id%3D640da012eb22010045e1a5115206fe06%26jvar\_selected\_tab%3DmyReports%26jvar\_list\_order\_by%3D%26jvar\_list\_sort\_direction%3D%26sysparm\_reportquery%3Denroll%26jvar\_search\_created\_by%3D%26jvar\_search\_table%3D%26jvar\_search\_report\_sys\_id%3D%26jvar\_report\_home\_query%3D](https://YOUR_INSTANCE.service-now.com/nav_to.do?uri=%2Fsys_report_template.do%3Fjvar_report_id%3D640da012eb22010045e1a5115206fe06%26jvar_selected_tab%3DmyReports%26jvar_list_order_by%3D%26jvar_list_sort_direction%3D%26sysparm_reportquery%3Denroll%26jvar_search_created_by%3D%26jvar_search_table%3D%26jvar_search_report_sys_id%3D%26jvar_report_home_query%3D)
2.  Replace YOUR\_INSTANCE with the instance you would like to run the report on
3.  Paste into your browser

Method 2

1.  In your instance, use the navigation filter and type "Reports"
2.  Once you hit Enter on your keyboard you should see the "Reports" module appear
3.  Click "View / Run"
4.  Click "All"
5.  On the top right of this page you'll see a Search field. Type "enroll" and hit enter
6.  On the top left of this page you'll seeYou will then see a report with the title "Password Reset Enrollment By Verification".
7.  Click it to run the report.

![](sys_attachment.do?sys_id=7f896822db42b450e515c22305961923)

Depending on the verification method that you are using, each instance may have different results shown for the report.

![](sys_attachment.do?sys_id=ff896822db42b450e515c22305961928)
