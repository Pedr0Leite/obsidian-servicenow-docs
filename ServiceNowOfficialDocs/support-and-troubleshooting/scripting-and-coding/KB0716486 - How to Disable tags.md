---
title: "How to Disable tags"
aliases:
  - KB0716486
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716486
kb_number: KB0716486
last_modified: 2025-01-07
---

## How to Disable tags

  

### Issue

# Description

* * *

Tags are text labels that you can associate with items like records and pages to group and organize them. Some customers may wish to disable the use of tags. In order to achieve this it is necessary to disable the context menu for adding tags via mass edit, and disable the tag bar at the top of each form. Please note that removing context menu actions is done on a per-table basis while removing the tag bar is done for all tables via a system property.

# Procedure

* * *

1) Navigate to the sys\_dictionary record for your table. Note that the "Type" value should be "Collection."

![](sys_attachment.do?sys_id=dd6ae066db42b450e515c223059619cf)

2) Switch to "Advanced" view.

3) Append the following string to the attribute of the collection: ",no\_labels=true"

![](sys_attachment.do?sys_id=916ae066db42b450e515c223059619d5)

4) Create a new sys\_properties record with the following values:

Name: glide.ui.show\_form\_tags\_bar  
Type: true | false  
Value: false

# Applicable Versions

* * *

London, Kingston
