---
title: "Logged users that do not exist on the sys_user table cannot print to PDF with the Webkit plugin WHTP"
aliases:
  - KB0623348
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623348
kb_number: KB0623348
last_modified: 2026-05-04
---

## Logged users that do not exist on the sys\_user table cannot print to PDF with the Webkit plugin WHTP

  

### Issue

If you are logged in with a user that does not exist on the sys\_user table (for example, maint), trying to use the icon to print to PDF on the homepages will fail.

 ![Export failed: error ](sys_attachment.do?sys_id=85f19e2947d3aa102c31b98a436d4351 "Export failed: error ")

### Symptoms

Clicking the download PDF option results in questions, and then when processing starts, the following error is displayed: "**Export failed: An unexpected error has occurred. Please see the instance logs for more details**"

The localhost contains the following message: **Exit with code 1 due to network error: AuthenticationRequiredError**

 --localhost----  
2017-06-05 03:49:12 (283) glide.background.generation.73ef3423db4fba009b835fa0cf96197f SYSTEM SEVERE \*\*\* ERROR \*\*\* com.snc.whtp: An error occured on the server  
2017-06-05 03:49:12 (288) glide.background.generation.73ef3423db4fba009b835fa0cf96197f SYSTEM SEVERE \*\*\* ERROR \*\*\* Loading pages (1/6)  
\[> \] 0%  
\[======> \] 10%  
\[==============================> \] 50%  
\[============================================================\] 100%  
Counting pages (2/6)  
\[============================================================\] Object 1 of 1  
Resolving links (4/6)  
\[============================================================\] Object 1 of 1  
Loading headers and footers (5/6)  
Printing pages (6/6)  
\[> \] Preparing  
\[============================================================\] Page 1 of 1  
Done  
Exit with code 1 due to network error: AuthenticationRequiredError  
\--localhost----

  
Reviewing the authentication tokens: https://<instance-name>.service-now.com/oauth\_credential\_list.do

You can confirm the Authentication token was created correctly for the WebKit HTML to PDF. However, there is no user associated with it.

 ![token with problem](sys_attachment.do?sys_id=c5f19e2947d3aa102c31b98a436d4358 "token with problem")

### Release

All releases

### Cause

OAuth fails to bind to a user (authenticate) if the user does not exist on the sys\_user table.

### Resolution

Do not use a user that does not exist on the sys\_user table to print to PDF from a homepage. (Note that very few users fall into this category.)

Instead, either impersonate another user to print the homepage or use the browser print-to-PDF feature if one is available.
