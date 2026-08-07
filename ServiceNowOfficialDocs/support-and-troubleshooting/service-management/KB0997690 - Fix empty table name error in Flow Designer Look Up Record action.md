---
title: "Fix empty table name error in Flow Designer Look Up Record action"
aliases:
  - KB0997690
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997690
kb_number: KB0997690
last_modified: 2025-08-04
---

## Fix empty table name error in Flow Designer Look Up Record action

  

### Issue

When using the Look Up Record action in your flow, you may see the error "GlideRecord.setTableName - empty table name". 

### Release

Any release

### Cause

This issue typically occurs when you customize the Action Type definition for the Look Up Record action. This causes input mappings to become unlinked. 

### Resolution

To resolve this issue, revert the Action Type Definition to the most recent default system version: 

1.  In your instance, go to https://<instance\_name>.service-now.com/sys\_hub\_action\_type\_definition\_list.do?sysparm\_query=&sysparm\_view=
2.  Open the Action Type Definition table.
3.  In the Name column, filter for Name = "Look Up Record" or "Look Up Records"
4.  Right-click the record, and select **Copy Sys ID.**
5.  Replace <sys\_id\_here> in the following string with the sys\_id just copied: sys\_hub\_action\_type\_definition\_<sys\_id\_here>.This creates the name you need for step 8.
6.  Go to https://<instance\_name>.service-now.com/sys\_update\_version\_list.do?sysparm\_query=&sysparm\_view= 
7.  Open the Version History table.
8.  Filter for Name = sys\_hub\_action\_type\_definition\_<sys\_id\_here> using the name created in step 5.
9.  Sort by **Recorded at**, with the most recent results first. 
10.  Find the most recent record that shows Source starting with System Upgrades.
11.  Right-click and select **Revert to this version.** 
12.  Verify that the issue is resolved.
