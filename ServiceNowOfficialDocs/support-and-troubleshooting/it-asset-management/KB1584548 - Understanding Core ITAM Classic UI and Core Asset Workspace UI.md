---
title: "Understanding Core ITAM Classic UI and Core Asset Workspace UI"
aliases:
  - KB1584548
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1584548
kb_number: KB1584548
last_modified: 2025-04-29
---

## Text

### Understanding Core ITAM Classic UI and Core Asset Workspace UI

### Details

1\. What is Classic user interface? 

Classic interface or Core UI (User Interface) Interface is the Out of the Box (OOB) Classic/Core UI ServiceNow interface as shown in the below screenshots.

**Classic/core UI with the List view**

![](/sys_attachment.do?sys_id=77485f6647877190d1a5ab29736d43c5)

**Classic/core UI Interface with Form view**

![](/sys_attachment.do?sys_id=b34817a647877190d1a5ab29736d435c)

2\. What is Workspace user interface? 

Workspace is a new UI experience as shown in the below screenshots. 

**Asset Workspace Landing page** 

![](/sys_attachment.do?sys_id=485817a647877190d1a5ab29736d43f4)

**Asset Workspace List view**

![](/sys_attachment.do?sys_id=985857a647877190d1a5ab29736d435d)

**Asset Workspace Form view**

![](/sys_attachment.do?sys_id=e05897a647877190d1a5ab29736d4323)

3\. What changes when Asset Workspace is activated?

-   Once Asset Workspace is activated, the List menus are hidden on Classic UI (Core UI). For example, it will not be available in the navigation menu. However, direct links to the pages will still work (/alm\_Asset\_list.do).
-   All the List menus which are hidden in Classic UI are shown in the Workspace.

![](/sys_attachment.do?sys_id=8458df6647877190d1a5ab29736d43d1)

For most pages in the Classic UI (see exceptions in Point 4 below), there is an equivalent page in the Workspace.

4\. What is not changing?

We are NOT deprecating any functionality.

All the underlying tables and logic are present and accessible as usual.

5\. How to activate Asset workspace? 

To activate Asset Workspace, install the Workspace \[com.sn\_itam\_workspace\] plugin. This will hide all the Classic List menus only for Asset and not any other feature. Important: Once Asset Workspace is installed, it cannot be deactivated.

6\. How to access Asset Workspace?

Access Asset Workspace via the following navigation paths:

![](/sys_attachment.do?sys_id=f348df6647877190d1a5ab29736d432c)

 ![](/sys_attachment.do?sys_id=94589f6647877190d1a5ab29736d434e) 

 7. Is Asset Workspace licensable?

It is not separately licensed. It is available with Core Asset Management.

8\. How do I know if I am using Asset Management?

To determine if you're using Asset Management, check if the Asset Management Foundation \[con.snc.Assets\] plugin is activated or not.

9\. What level of support will be provided for Asset Classic UI for customers who continue to use it after March 2025?

-   Our R&D investments will be focused on the new Asset Workspace, which offers significantly better usability, and we recommend our customers to move to this new experience. No new feature development will be done on Classic UI’s.
-   Existing features which impact both Asset Workspace and Classic will be tested on the Classic UI.
-   Defects on the Classic UI will be addressed based on impact, on a case-by-case basis.
