---
title: "How to Set Additional Fields with the Create User in Microsoft AD Spoke using Flow Designer"
aliases:
  - KB0794226
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794226
kb_number: KB0794226
last_modified: 2026-05-05
---

## How to Set Additional Fields with the Create User in Microsoft AD Spoke using Flow Designer

  

### Issue

The Create User action in the Microsoft AD Spoke contains the following fields.

![Create User action in Flow Designer](/sys_attachment.do?sys_id=fe824ff047c65e10f64de825126d43dd "Create User action in Flow Designer")

Depending on your organisational requirements, it may be necessary to add more fields. 

### Release

London onwards

### Resolution

The platform uses Powershell and the New-ADUser to pass the parameters from the Create User to Active Directory. This may be found in the ActionCreateNewUserAD.ps1.

[https://<instance>.service-now.com/nav\_to.do?uri=ecc\_agent\_script\_file.do?sys\_id=7bf3725c93801300eb08925cf67ffbd0](https://\<instance\>.service-now.com/nav_to.do?uri=ecc_agent_script_file.do?sys_id=7bf3725c93801300eb08925cf67ffbd0)

This script may be customised to read more fields from the Flow and pass them to AD.

The list of parameters New-ADUser accepts is available at Microsoft Docs:

[https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps)

The list of Active Directory attributes may also be found in Microsoft Docs.

[https://docs.microsoft.com/en-us/windows/win32/adschema/attributes-all](https://docs.microsoft.com/en-us/windows/win32/adschema/attributes-all)

### Related Links

-   Copy or customise the "Create User" in the Flow Designer
-   Add inputs for the additional fields and define them as payloads
-   Pass these inputs to ActionCreateNewUserAD.ps1 in the Create User step.
-   Modify ActionCreateNewUserAD.ps1 to so that these inputs are received as variables and are included in the New-ADUser commands in the Script section.
