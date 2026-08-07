---
title: "Identifying the view used on a list or form"
aliases:
  - KB0523467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523467
kb_number: KB0523467
last_modified: 2025-06-02
---

## Identifying the view used on a list or form

  

### Issue

A **View** is a saved version of a personalized form or list. It defines which fields appear on the form or list and in which order. Views enable users to quickly display the same form or list in multiple ways. Administrators can create any number of views for a form or list. If a view is not displaying properly, remove the spaces from the view's name. For example, if the name of the view is _view X_ update the name to _viewX_. 

For additional information, refer to the ServiceNow product documentation:

-   [View management](https://docs.servicenow.com/csh?topicname=view-management-overview.html&version=latest "View management")
-   [Switch views](https://docs.servicenow.com/csh?topicname=p_NavigationAndUIConfiguration.html&version=latest "Switch views")

### Procedure

To identify which view is currently used on a list or form:

1.  Navigate to the form or list presenting the existing view.
2.  Right-click the form header and select **View**. In a list, expand the list context menu and select View.
3.  Note the selected view and record the view name.  
      
    ![Form header choice list displaying View options and an arrow pointing to the check-marked Default view option.](sys_attachment.do?sys_id=f74454d91bf9d510be4955fa234bcbd1 "Form header choice list")  
      
    
4.  Navigate to **System UI > Views**.
5.  Search for and select the view record you want to update. 
    
     **Note:** Verify that there are no spaces in the **Name** field. If so, remove spaces.
    
6.  Click **Update**.

### Switch between list views

A form or list inherits the previous view selected when accessing the object from the latest user session. When switching to a view other than the Default view, it is specified in brackets on the form or list.

A view defines the elements that appear when a user opens a list. A logged in user can switch between list views to which they have access.

1.  Open the list.
2.  Select the view to configure by performing the appropriate action for your list version.  
      
    
    | **Version** | **Action** |
    | --- | --- |
    | List V2 | Open the list title menu and select View > (view name). |
    | List v3 | Open the list title menu and select Change View, and then click the name of the view. |
    
    The page refreshes with in the selected view.
