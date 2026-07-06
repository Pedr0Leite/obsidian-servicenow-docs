---
title: "Password Reset Windows Application Error: \"This page does not exist\""
aliases:
  - KB0753092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753092
kb_number: KB0753092
last_modified: 2024-04-07
---

## Password Reset Windows Application Error: "This page does not exist"

  

### Issue

# Symptoms

After installing the password reset application on a workstation then clicking on "Forgot Password?" an error says "This page does not exist."

# Release

Any

# Environment

Windows Desktops/laptops/workstations

# Cause

The URL that was configured for the Password Reset Windows Application (PRWA) is probably incorrect. 

# Resolution

1) Get the correct URL by doing the following:

1.  Go Password Reset > Processes on the instance
2.  Open the record for the process you are using 
3.  Copy the full URL from the field "Public URL" (right-click on that link and select "Copy Link Address")
    1.  It should be like https://<instance-name>.service-now.com/$pwd\_reset.do?sysparm\_url=\[URL\_SUFFIX\]

2) Use this URL when configuring your PRWA on the workstation.
