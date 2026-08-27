---
title: "Security restricted error when running a background script that reads a table from Global scope"
aliases:
  - KB0831584
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831584
kb_number: KB0831584
last_modified: 2026-06-03
---

## Security restricted error when running a background script that reads a table from Global scope

  

### Issue

This error appears when running a background script that attempts to read a table from the Global scope without a declared **cross-scope access privilege**.

The **Caller Access** setting on the target table is set to Caller restrictions, which prevents the Global scope application from reading it without an explicit access privilege declaration. The following error messages appear:

\- Security restricted: Read operation on table 'table\_name' from scope 'Global' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests.   
  
\- Source descriptor is empty while recording access for table 'table\_name': no thrown error   
  
\- Security restricted: Read operation on table 'sn\_hr\_core\_criteria' from scope 'Global' was denied because the source could not be found. Please contact the application admin.   
  
\- Security restricted: Read operation on table 'sn\_hr\_core\_criteria' from scope 'Global' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests.   
  
Script: - 0 -

### Release

All releases

### Cause

The Caller Access setting on the target table is set to Caller restrictions. This prevents the Global scope from reading the table without a declared cross-scope access privilege.

### Resolution

**Warning:** Changing the Caller Access setting from Caller restrictions to -- **None --** removes the restriction that prevents other applications from reading the target table. See the [Restricted caller access privilege settings](https://www.servicenow.com/docs/r/application-development/restricted-caller-access-privilege.html?content-lang=en-US "Restricted caller access privilege settings") for detailed information.

1.  Navigate to the Tables list.
2.  Open the target table (for example, **sn\_hr\_core\_criteria**).
3.  Select the **Application Access** tab.
4.  Locate the **Caller Access** field.
5.  Change the value from Caller restrictions to -- **None** \--.
6.  Save the record.

After saving, re-run the background script to confirm the error no longer appears.

### Related Links

[Cross-scope privilege record](https://www.servicenow.com/docs/r/application-development/c_CrossScopePrivilegeRecord.html "Cross-scope privilege record")

[Restricted caller access privilege settings](https://www.servicenow.com/docs/r/application-development/restricted-caller-access-privilege.html?content-lang=en-US "Restricted caller access privilege settings")

[Configure cross-scope access privileges for topic blocks and custom controls](https://www.servicenow.com/docs/r/conversational-interfaces/virtual-agent/configure-cross-scope-privileges.html "Configure cross-scope access privileges for topic blocks and custom controls")
