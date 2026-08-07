---
title: "Cannot create an interaction from the HR Agent Workspace"
aliases:
  - KB2616336
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2616336
kb_number: KB2616336
last_modified: 2025-11-11
---

## Cannot create an interaction from the HR Agent Workspace

  

### Issue

When creating an interaction within the HR Agent Workspace, we are unable to create the interaction because the 'Create Interaction' button is greyed out.

### Release

All release

### Cause

Customer has configured custom mandatory fields, but these fields are not set up in the Create Interaction form view in HR Workspace.

### Resolution

To display the custom mandatory fields, you need to create a copy of the Interaction Creation page (since it is read-only) in UI Builder and add the fields to the formSectionRows property.

Please see the detailed steps below:   
  
1\. In the navigator in Platform, enter "UI Builder" and select "UI Builder for HR Agent Workspace"  
2\. In the new window that gets opened, select the Interaction Creation Page in the page selector  
3\. Once the Interaction Creation Page is loaded. On left side Select "step 2 Interaction Creation page" > interaction info body > form 1  
4\. Select the Client State button in the bottom left  
5\. In the Client State Parameters window, scroll to the "formSectionRows" property and edit the initial value   
6\. Top left corner click on form dropdown and click JSON  
7\. Add the fields array(see attachment)  
8\. Click Apply and Save  
  

![](/sys_attachment.do?sys_id=f287dd8f9381fe94057c7de86cba1068)

After adding the custom fields to the formSectionRows property, the user is able to create an interaction successfully.

![](/sys_attachment.do?sys_id=55b7d50393c1fe94057c7de86cba1048)
