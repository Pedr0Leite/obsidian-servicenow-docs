---
title: "[SAMP-License Workbench] Customization to Software Asset License Workbench and roles requirements"
aliases:
  - KB1581373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1581373
kb_number: KB1581373
last_modified: 2023-12-04
---

## \[SAMP-License Workbench\] Customization to Software Asset License Workbench and roles requirements

  

### Summary

As an admin, we might need to modify/customize the SAM License Workbench ($sam.ui) especially the accessibility.

### Release

All with Software Asset Management Professional installed

### Instructions

Unfortunately the UI for license workbench is coming from the page "$sam.ui" which is built in the backend code. As per docs the accessibility of this page requires min of sam\_user role which is again restricted in back-end code. This is the reason the UI can not be customizable.

Consider latest version of SAM Ui with [Software Asset Workspace](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-workspace.html)

Also, there is an [Idea customizable license workbench](https://support.servicenow.com/ideas?id=view_idea&sysparm_idea_id=ee34f65b97f2bdd0d4743dae2153aff7&sysparm_idea_table=x_snc_com_ideation_idea&sysparm_module_id=enhancement_requests) is raised for this. You can upvote for the same. 

### Related Links

-   [Software Asset Workspac](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-workspace.html)
-   [Configuring Software Asset Management workspace](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/Config-sam-workspace.html)
-   [Using the Software Asset Management workspace](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-workspace.html)
