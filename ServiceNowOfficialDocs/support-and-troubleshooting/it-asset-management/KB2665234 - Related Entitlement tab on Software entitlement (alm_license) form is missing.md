---
title: "Related Entitlement tab on Software entitlement (alm_license) form is missing "
aliases:
  - KB2665234
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2665234
kb_number: KB2665234
last_modified: 2026-05-21
---

## Related Entitlement tab on Software entitlement (alm\_license) form is missing

  

### Issue

The 'Related Entitlement' section is missing from the form layout of the Software Entitlement (alm\_license) table in both the Workspace and Default views.

There is a UI Policy to hide the Related Entitlement "Hide related entitlements section" but even when all the conditions are met, the entitlement form is not showing the this section. 

(In this case, Entitlements with License type = maintenance is not showing the Related Entitlement tab)

### Release

Any

### Cause

  
We do see the Form section(sys\_ui\_section) 'Related Entitlements' available. However, this Form section was not added to the Entitlement form.

### Resolution

Form sections are not added through Plugin repair. You will have to manually add them back

\- From alm\_license Form(sys\_ui\_form), scroll down to the Related List 'Form Sections'  
\- Click 'New' and locate the alm\_license>related entitlements section and re-add it.   
\- Set the position to 9 to match the ootb instance, ensuring the form config looks same in both instances.

Validate that the Entitlement(alm\_license) form should now have the Related Entitlements tab visible
