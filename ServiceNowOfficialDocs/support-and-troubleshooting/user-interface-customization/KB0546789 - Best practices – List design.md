---
title: "Best practices – List design"
aliases:
  - KB0546789
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546789
kb_number: KB0546789
last_modified: 2024-10-16
---

## Best practices – List design

  

### Issue

<table style="border-collapse: collapse; width: 100%; border-width: 0px; height: 116.987px;" border="1"><colgroup><col style="width: 11.5841%;"><col style="width: 88.3941%;"></colgroup><tbody><tr style="height: 69.4px;"><td style="border-width: 0px; height: 69.4px;"><img title="overview360.png" src="/sys_attachment.do?sys_id=092b8ac18359d610cdbbc430feaad390" alt="Overview" width="83" height="66" align="bottom"></td><td style="border-width: 0px; height: 69.4px;"><h2><span class="hd1">&nbsp;<span style="color: rgb(0, 0, 0);"><strong>Overview</strong></span></span></h2></td></tr><tr style="height: 47.5875px;"><td style="border-width: 0px; height: 47.5875px;">&nbsp;</td><td style="border-width: 0px; height: 47.5875px;"><h2><span class="hd1" style="font-size: 10pt;">This article discusses how to employ best practices when designing lists. Adhering to these guidelines improves the usability of your instance and enhances user experience.</span></h2></td></tr></tbody></table>

* * *

### Release

All Releases

### Resolution

<table style="height: 72px;" width="674"><tbody><tr><td style="text-align: left;"><img title="ServiceNow_logo_RGB_BL_WasabiGreen.jpg" src="/sys_attachment.do?sys_id=21ed5ac5839dd610cdbbc430feaad341" alt="" width="200" height="58" align="bottom" border="" hspace="" vspace=""></td><td><span class="title"><span style="font-size: 20pt;"><span style="color: rgb(0, 0, 0);">Best practices </span><span style="color: rgb(100, 100, 100);">| <span style="color: rgb(0, 0, 0);">List design</span><br></span></span></span></td></tr></tbody></table>

  
 

<table style="border-collapse: collapse; width: 100%; border-width: 0px;" border="1"><colgroup><col style="width: 16.0917%;"><col style="width: 83.9957%;"></colgroup><tbody><tr><td style="border-width: 0px;"><img title="rockStart.png" src="/sys_attachment.do?sys_id=584bc2058359d610cdbbc430feaad375" alt="Warning" width="120" height="96" align="bottom"></td><td style="border-width: 0px;"><h2 class="blockDiv"><span class="hd1"><span style="color: rgb(0, 0, 0);">Best practices video</span></span></h2></td></tr></tbody></table>

* * *

## 

  

<table style="border-collapse: collapse; width: 100%; border-width: 0px;" border="1"><colgroup><col style="width: 10.3057%;"><col style="width: 89.7817%;"></colgroup><tbody><tr><td style="border-width: 0px;"><img title="listPad.png" src="/sys_attachment.do?sys_id=6a6b8e058359d610cdbbc430feaad3d4" alt="Warning" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h2 class="blockDiv"><span class="hd1">&nbsp;&nbsp;<span style="color: rgb(0, 0, 0);">List design best practices</span></span></h2></td></tr></tbody></table>

* * *

<table style="border-collapse: collapse; width: 99.9704%; border-width: 0px;" border="1"><colgroup><col style="width: 7.5852%;"><col style="width: 92.4741%;"></colgroup><tbody><tr><td style="border-width: 0px;"><img title="Star.png" src="/sys_attachment.do?sys_id=fe3c86098359d610cdbbc430feaad306" alt="" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h3><span class="title" style="font-size: 10pt; color: rgb(0, 0, 0);"><strong>Best Practice #1: Use the record number or other unique information as the first column.</strong></span></h3></td></tr><tr><td style="border-width: 0px;">&nbsp;</td><td style="border-width: 0px;"><p><span style="font-size: 10pt;">For consistency with existing lists in the system, use the record number or other unique information as the first column in a list:</span></p><ul style="list-style-position: inside;"><li style="font-size: 10pt;">When a user clicks an item in the first column of a list, the system opens a record from that list rather than a reference record in some other list. This applies to Incident, Problem, Change Request, Business Rules, and other lists.</li><li style="font-size: 10pt;">When designing a list, avoid using reference fields in the first column. If possible, use the string field that defines the list, for example, the item number, name, or ID. If the record does not have a string field, consider using a date field, such as the date the record was created or updated.&nbsp;</li></ul></td></tr><tr><td style="border-width: 0px;"><img title="Star.png" src="/sys_attachment.do?sys_id=885c4e098359d610cdbbc430feaad301" alt="" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h3><span class="title" style="font-size: 10pt; color: rgb(0, 0, 0);"><strong>Best Practice #2: Avoid displaying fields with long values in list views.</strong></span></h3></td></tr><tr><td style="border-width: 0px;">&nbsp;</td><td style="border-width: 0px;"><span style="font-size: 10pt;">Avoid displaying fields with long values in list views, including HTML, large text, and journal fields. Some fields, such as work notes, take up more vertical and horizontal space in the list without providing the most essential information.&nbsp;</span></td></tr><tr><td style="border-width: 0px;"><img title="Star.png" src="/sys_attachment.do?sys_id=885c4e098359d610cdbbc430feaad301" alt="" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h3><span class="title" style="font-size: 10pt; color: rgb(0, 0, 0);"><strong>Best Practice #3: Limit the number of columns to avoid horizontal scrolling.</strong></span></h3></td></tr><tr><td style="border-width: 0px;">&nbsp;</td><td style="border-width: 0px;"><span style="font-size: 10pt;">To save space, limit the number of columns to avoid horizontal scrolling. To enhance the user experience, include only the columns that most users really need to see. Users can personalize their own view of the list without affecting others if they want to add other columns.&nbsp;</span></td></tr><tr><td style="border-width: 0px;"><img title="Star.png" src="/sys_attachment.do?sys_id=885c4e098359d610cdbbc430feaad301" alt="" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h3><span class="title" style="font-size: 10pt; color: rgb(0, 0, 0);"><strong>Best Practice #4: Review the list controls and list UI actions to understand user access.</strong></span></h3></td></tr><tr><td style="border-width: 0px;">&nbsp;</td><td style="border-width: 0px;"><span style="font-size: 10pt;">If your list includes list controls or UI actions, review these elements to understand what they do, and who has access to them and under what conditions. By clicking this menu icon or right-clicking the list header, you can personalize the list controls to specify which roles are able to perform these actions. &nbsp;</span></td></tr><tr><td style="border-width: 0px;"><img title="Star.png" src="/sys_attachment.do?sys_id=885c4e098359d610cdbbc430feaad301" alt="" width="70" height="56" align="bottom"></td><td style="border-width: 0px;"><h3><span class="title" style="font-size: 10pt; color: rgb(0, 0, 0);"><strong>Best Practice #5: Limit the number of records that a list can show per page.</strong></span></h3></td></tr><tr><td style="border-width: 0px;">&nbsp;</td><td style="border-width: 0px;"><span style="font-size: 10pt;">Users can specify the number of records listed per page from the menu icon in the title bar. It is best to stick with the base system maximum of 100 rows per page and not make larger numbers available. The more items displayed per page, the longer it takes the system to query the database and render the list. This is especially true if some fields must be calculated, or there are related lists on a form with many records. This results in better performance, and users can still view all items by paging through the list.&nbsp;</span></td></tr></tbody></table>

### Related Links

<table style="border-collapse: collapse; width: 100%; border-width: 0px;" border="1"><colgroup><col style="width: 10.7424%;"><col style="width: 89.345%;"></colgroup><tbody><tr><td style="border-width: 0px;"><h2><span class="hd1"><strong><img title="information.png" src="/sys_attachment.do?sys_id=ab6c42498359d610cdbbc430feaad310" alt="Warning" width="70" height="56" align="bottom"></strong></span></h2></td><td style="border-width: 0px;"><h2><span class="hd1"><span style="color: rgb(0, 0, 0);">Additional resources</span></span></h2></td></tr></tbody></table>

* * *

For more information, see [Using Lists](https://docs.servicenow.com/csh?topicname=c_UseLists.html&version=latest "Using Lists documentation").

ServiceNow video series: Did You Know [List Filter Shortcuts](https://youtu.be/F7CoszrSnw8?si=27iAPhRvS6MvZQdh "List Filter Shortcuts - Did You Know")
