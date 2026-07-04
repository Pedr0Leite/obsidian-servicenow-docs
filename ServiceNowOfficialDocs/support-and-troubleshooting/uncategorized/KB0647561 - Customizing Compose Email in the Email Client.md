---
title: "Customizing \"Compose Email\" in the Email Client"
aliases:
  - KB0647561
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647561
kb_number: KB0647561
last_modified: 2025-06-13
---

## Customizing "Compose Email" in the Email Client

  

### Issue

This KB will assist in customizing of outbound emails composed using the Email Client form within an incident form.

### Resolution

Out of the box, the Email Client comes with:

-   "To" populated with "Caller" email address"
-   Cc" populated with "Opened by" email address
-   "Subject" populated with "Number" - "Short description".
-   The body is empty.

![Incident form with Email highlighted from dropdown menu option](/sys_attachment.do?sys_id=61aa3f2a47426a50b8a4aa25126d4355 "Email from dropdown menu")

![Compose email form with cursor in recipient email address](/sys_attachment.do?sys_id=e9aa3f2a47426a50b8a4aa25126d4357 "Compose email")

To customize the values in these fields:

\- OOB role required: Admin

1.  Go to Email Client Templated table by entering sys\_email\_client\_template\_list.do in the Filter navigator.
2.  Click New

-   Name: Incident Email Client
-   Application: Global
-   Content Type: HTML
-   Table: Incident
-   To: caller\_id \[dictionary name of the user field\] \[only a single variable is permitted\]
-   Cc: opened\_by \[You can use a variable according to your requirement, for example assigned\_to\]
-   Bcc: assigned\_to
-   Subject: ${number} - ${short\_description}

For Body:

1.  Expand Fields on the right
2.  Add variables from Fields according to your requirement
3.  Variables can be dot walked to add details like ${assigned\_to.manager.email}
4.  Click Update once done

![Email Template Client form with selected variables extended list pointing towards their location in Body of HTML](/sys_attachment.do?sys_id=25aa3f2a47426a50b8a4aa25126d435a "Email template")

5\. Check the updated Email Client Compose Email

![Email Client Compose form with desired variables populated](/sys_attachment.do?sys_id=6daa3f2a47426a50b8a4aa25126d435c "Compose email")

6\. To customize the functions available on the Editor toolbar, you need to edit the "glide.ui.html.editor.v4.toolbar.line1" property. By design and default, the editor on the Email Client form looks to the global settings of the toolbar and cannot be edited separately (as opposed to editors on specific tables).   
Please keep this in mind when making changes to the property as it can affect the functions available elsewhere.  
  

For a list of functions that can be added, please refer to our documentation here: [https://docs.servicenow.com/bundle/tokyo-platform-administration/page/administer/form-administration/task/t\_ConfigureTheTinyMCEHTMLToolbar.html](https://docs.servicenow.com/bundle/tokyo-platform-administration/page/administer/form-administration/task/t_ConfigureTheTinyMCEHTMLToolbar.html)

\*\*Note: the documentation may change over time. Please search the Docs site for keyword 'glide.ui.html.editor.v4.toolbar.line1' if the link does not work.
