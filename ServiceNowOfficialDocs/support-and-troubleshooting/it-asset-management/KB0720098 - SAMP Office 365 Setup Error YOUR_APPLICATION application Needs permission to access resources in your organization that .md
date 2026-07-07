---
title: "SAMP Office 365 Setup Error \"YOUR_APPLICATION application Needs permission to access resources in your organization that only an admin can grant. Please ask an admin to grant permission to this app before you can use it.\"
aliases:
  - KB0720098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720098
kb_number: KB0720098
last_modified: 2024-04-07
---

## SAMP Office 365 Setup Error "YOUR\_APPLICATION application Needs permission to access resources in your organization that only an admin can grant. Please ask an admin to grant permission to this app before you can use it."

  

### Issue

# Symptoms

* * *

During the [Set up Microsoft Office 365 integration](https://docs.servicenow.com/csh?topicname=set-up-microsoft-office-365.html&version=latest "Set up Microsoft Office 365 integration") procedure, you may encounter the below error message at step #2:

YOUR\_APPLICATION application Needs permission to access resources in your organization that only an admin can grant. Please ask an admin to grant permission to this app before you can use it. 

# Cause

* * *

This is not an issue with the configuration. When we try to set-up Office-365 integration, we need to access the users and reports information. For this we configure the secrets in the step 1.C. This needs admin consent (approval). So once we set-up the secrets, a user with admin access needs to consent this then only the secrets are fulfilled.

# Resolution

* * *

Login as admin user into the Application Registration Portal and approve/consent the requests:

![](/sys_attachment.do?sys_id=9ebaaca6db42b450e515c22305961976)

# Additional Resources

* * *

[https://social.msdn.microsoft.com/Forums/office/en-US/0c3bbb38-468c-4e4b-9fcf-cbe42bb3dfda/aadsts90093-this-operation-can-only-be-performed-by-an-administrator-but-user-is-a-global-admin?forum=WindowsAzureAD](https://social.msdn.microsoft.com/Forums/office/en-US/0c3bbb38-468c-4e4b-9fcf-cbe42bb3dfda/aadsts90093-this-operation-can-only-be-performed-by-an-administrator-but-user-is-a-global-admin?forum=WindowsAzureAD) 

  
[https://nicksnettravels.builttoroam.com/post/2017/01/24/Admin-Consent-for-Permissions-in-Azure-Active-Directory.aspx](https://nicksnettravels.builttoroam.com/post/2017/01/24/Admin-Consent-for-Permissions-in-Azure-Active-Directory.aspx) 

  
[https://blogs.msdn.microsoft.com/aaddevsup/2018/05/08/receiving-aadsts90094-the-grant-requires-admin-permission/](https://blogs.msdn.microsoft.com/aaddevsup/2018/05/08/receiving-aadsts90094-the-grant-requires-admin-permission/) 

  
[https://social.msdn.microsoft.com/Forums/office/en-US/0c3bbb38-468c-4e4b-9fcf-cbe42bb3dfda/aadsts90093-this-operation-can-only-be-performed-by-an-administrator-but-user-is-a-global-admin?forum=WindowsAzureAD](https://social.msdn.microsoft.com/Forums/office/en-US/0c3bbb38-468c-4e4b-9fcf-cbe42bb3dfda/aadsts90093-this-operation-can-only-be-performed-by-an-administrator-but-user-is-a-global-admin?forum=WindowsAzureAD)
