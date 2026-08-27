---
title: "How to change the default font-family and font-size for email notifications"
aliases:
  - KB0783405
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783405
kb_number: KB0783405
last_modified: 2025-11-13
---

## How to change the default font-family and font-size for email notifications

  

### Summary

By default, outbound email notifications in ServiceNow use Times font-family and 13.5 pt font-size for the email body. You can change these defaults by creating a custom email layout with your preferred font settings and applying it to your notification email templates. 

### Release

All supported releases

### Instructions

**Important:** Thoroughly test this procedure in a non-production instance before applying changes to a production instance.

In this example, the font-family is set to Helvetica and the font-size to 10 pt.

1.  Go to **System Notification** > **Email** \> **Layouts**.
2.  Select **New**.
3.  Enter the following information:
    -   Name: name of your choice
    -   Advanced: check this checkbox
    -   Layout:  
        <span style="font-family: helvetica; font-size: 10pt;">  
        ${notification:body}  
        </span>
4.   Select **Submit**.
5.  Apply the new email layout to your existing email templates.  
      
    If you don't have email templates for your notifications:   
      
    
6.  Go to **System Policy** > **Email** \> **Templates**.
7.  Select **New**.
8.  Enter the following information:  
    -   **Name**: Enter a descriptive name
    -   **Email layout**: Select the email layout you created in the previous steps
9.  Select **Submit**.

You can apply the new template and fonts to notifications in bulk from the list view:

1.  Select the notifications you want to update.
2.  From the context menu of any column header, select **Update Selected**.
3.  In the **What it will contain** section, select your template in the **Email Template** field.
4.  Select **Update**.

After completing these steps, notifications using this template will display emails with your custom font settings.
