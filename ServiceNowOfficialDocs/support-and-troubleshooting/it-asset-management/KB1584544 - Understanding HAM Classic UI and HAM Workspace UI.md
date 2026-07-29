---
title: "Understanding HAM Classic UI and HAM Workspace UI"
aliases:
  - KB1584544
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1584544
kb_number: KB1584544
last_modified: 2024-11-14
---

## Text

### Understanding HAM Classic UI and HAM Workspace UI

### Details

1\. What is Classic user interface? 

Classic interface or Core UI (user interface) interface is the Out of the Box (OOB) ServiceNow interface as shown in the below screenshots. 

**Classic/core UI with the List view**

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=bfd55f6e47477190d1a5ab29736d4331)

**Classic/core UI interface with Form view**

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=c4e59f6e47477190d1a5ab29736d43f2)

2\. What is Workspace user interface? 

Workspace is a new UI experience as shown in the below screenshots. 

**Hardware Asset Workspace (HAM Workspace) landing page** 

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=50e5df6e47477190d1a5ab29736d4316)

**Hardware Asset Workspace List view (called Asset operations)** 

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=fbd553ae47477190d1a5ab29736d434e)

**HAM Workspace Form view**

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=d0e5df6e47477190d1a5ab29736d43de)

3\. What changes when HAM Workspace is activated?

-   Once HAM Workspace is activated, the List menus are hidden on classic UI (core UI). For example, it will not be available in the navigation menu. However, direct links to the pages will still work (/alm\_asset\_list.do).
-   All the List menus which are hidden in classic UI are shown in the Workspace.

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=00e5df6e47477190d1a5ab29736d43eb)

For most pages in the Classic UI, there is an equivalent page in the Workspace. Some of the dashboards have been simplified and have been moved to workspace. For example, the Stockroom form in Classic UI is present and updated as Stockroom in the HAM workspace. 

Classic:

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=e8e553ae47477190d1a5ab29736d43a6)

Workspace:

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=a4e5df6e47477190d1a5ab29736d439e)

4\. What is not changing?

We are NOT deprecating any functionality.

All the underlying tables and logic are present and accessible as usual.

5\. How to activate HAM Workspace? 

To activate HAM Workspace, install the Workspace \[com.sn\_itam\_workspace\] plugin. This will hide all the Classic List menus only for HAM and not any other feature. Important: Once HAM Workspace is installed, it cannot be deactivated.

6\. How to access HAM Workspace?

Access HAM Workspace via the following navigation paths:

![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=14e55f6e47477190d1a5ab29736d43bc)

 ![A screenshot of a computerDescription automatically generated](/sys_attachment.do?sys_id=34e553ae47477190d1a5ab29736d435a) 

7\. Is HAM Workspace licensable?

It is not separately licensed. It is available with Hardware Asset Management.

8\. How do I know if I am using Hardware Asset Management?

To determine if you're using Hardware Asset Management, check if the Hardware Asset Management Foundation \[con.snc.hamp\] plugin is activated or not.

9\. What level of support will be provided for HAM Classic UI for customers who continue to use it after March 2025?

-   Our R&D investments will be focused on the new HAM Workspace, which offers significantly better usability, and we recommend our customers to move to this new experience. No new feature development will be done on Classic UI.
-   Existing features which impact both HAM Workspace and Classic will be tested on the Classic UI.
-   Defects on the Classic UI will be addressed based on impact, on a case-by-case basis.
