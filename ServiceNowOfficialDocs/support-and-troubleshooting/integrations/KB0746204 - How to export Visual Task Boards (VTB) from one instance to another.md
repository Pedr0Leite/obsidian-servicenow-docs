---
title: "How to export Visual Task Boards (VTB) from one instance to another"
aliases:
  - KB0746204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746204
kb_number: KB0746204
last_modified: 2024-04-07
---

## Issue

How to export Visual Task Boards (VTB) from one instance to another. This is useful in a scenario where the Visual Task Boards have been created on one instance and the same is required on another Instance.

## Resolution

1.  On the Source instance navigate to "vtb\_board.list" 
2.  Open the vtb record   
    3\. Right click on the header and select Export to XML from the menu options   
    4. Now, log in to the Target instance  
    5\. Open any List view and import the vtb board xml exported at step 3 via "Import xml" option   
      
    Repeat for the other VTB tables including vtb\_lane.list , vtb\_task.list , and vtb\_card.list . 

<table class="noteTable" align="left"><tbody><tr><td class="c3"><br></td><td class="c4"><strong>Note</strong>: We usually recommend that&nbsp;you recreate any Visual Task Boards manually.</td></tr></tbody></table>
