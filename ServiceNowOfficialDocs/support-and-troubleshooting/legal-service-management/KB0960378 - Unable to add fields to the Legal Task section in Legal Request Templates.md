---
title: "Unable to add fields to the Legal Task section in Legal Request Templates"
aliases:
  - KB0960378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960378
kb_number: KB0960378
last_modified: 2026-03-17
---

## Unable to add fields to the Legal Task section in Legal Request Templates

  

### Issue

1\. Navigate to Legal > Requests > All Legal Requests > Catalog & Knowledge > Legal Request Templates  
https://instance\_name.service-now.com/sn\_sm\_legal\_request\_template\_list.do?sysparm\_query=&sysparm\_view=

2\. Create New

3\. The New Legal Request Template form will open in the $sm\_templates.do UI page

4\. Populate the Name and Short Description in the 'Request Information' section, and Save. Select any category in the popup and Publish 

5\. Select 'Edit fields' 

6\. In the 'Task 1' section, select a new field from the 'add fields' drop down and Save.

7\. Refresh the page and notice how the field added to the 'Task 1' section in step 6 is not there.

### Release

All releases

### Cause

The 'Name' field on the 'Task 1' template section is empty. 

![](sys_attachment.do?sys_id=5323c33793abbe50f538fb2d6cba10cc)

### Resolution

The Legal Task template in the 'Task 1' must have a 'Name' specified, even if the UI Page does not indicate it.

To solve the issue, add a name to it before adding your extra field(s) and saving the record.
