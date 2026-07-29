---
title: "How to configure the title of a list card in split mode using List v3"
aliases:
  - KB0597470
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597470
kb_number: KB0597470
last_modified: 2025-01-03
---

## How to configure the title of a list card in split mode using List v3

  

### Issue

# What is List v3 split mode?

* * *

In List v3, split mode enables users to view a list and form side by side in a split pane layout.

In split mode, the title of the list card is either a default value or a value configured by accessing System Mobile UI > Table Titles. Table title records are used in the mobile application as well as in the list pane. You can change the title for any table or add a title record for a different table, however, the change affects the mobile user interface (UI). For more information, see the documentation topic [Use List v3 split mode](https://docs.servicenow.com/csh?topicname=t_UseListV3SplitMode.html&version=latest "Use List v3 split mode").

# How to configure the title of the list card in split mode using List v3

* * *

1.  Make sure the List v3 plugin is activated and the List v3 properties are enabled.
    
    For more information, see the product documentation topic [Activate List v3](https://docs.servicenow.com/csh?topicname=c_ListV3Administration.html&version=latest).
    
2.  Log in with relevant Administrator roles and go to sys\_ui\_title\_list.do to access the Document Titles table.
    
3.  Click **New** to add a new record.
    
4.  Select the name of the table for which you will be configuring the title of the list card.
    
    This example uses the Incident table.
    
    ![](sys_attachment.do?sys_id=dcf86c6edb02b450e515c2230596198d)
    
5.  Select the fields to be displayed in the title of the card.
    
    1.  Click the lock icon to view all the fields associate to the incident table.
        
    2.  Double-click the field name in the Available list to move it to the Selected list on the right.
        
        This example selects Short Description. Note that you can select more than one field.
        
    3.  After selecting the required field to be displayed on the title of the list card, click **Submit** to save the record.
        
6.  Navigate to the Incident list to review the title that was just configured.
    
    ![](sys_attachment.do?sys_id=98f86c6edb02b450e515c223059619ac)
    

## Optional scripting option

If you want the title to be concatenated with more than one field, you can use the scripting option.

Remove any fields from the selected section and then add the script, as shown in the following example.

![](sys_attachment.do?sys_id=dcf86c6edb02b450e515c223059619c6)

The following illustration shows the result of this example using scripts to concatenate more than one field together.

![](sys_attachment.do?sys_id=a0f86c6edb02b450e515c223059619d4)
