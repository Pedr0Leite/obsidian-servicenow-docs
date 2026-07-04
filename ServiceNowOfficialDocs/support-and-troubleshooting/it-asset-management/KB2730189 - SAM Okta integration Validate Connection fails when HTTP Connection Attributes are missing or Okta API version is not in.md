---
title: "SAM Okta integration Validate Connection fails when HTTP Connection Attributes are missing or Okta API version is not included in the request URL"
aliases:
  - KB2730189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2730189
kb_number: KB2730189
last_modified: 2026-01-21
---

## Issue

→ Validate Connection fails for the Okta integration used by SAM because the outbound request is constructed without the Okta API version or the HTTP Connection “Attributes” are not populated

## Resolution

→ Confirm the failing outbound call  
↳ Review the outbound HTTP log and verify the URL contains /api//users and Okta returns E0000022

→ Ensure Okta Spoke is up to date  
↳ Upgrade the Okta Spoke to the latest available version in App Manager

→ Fix the Connection Attributes model mapping if Attributes are missing  
↳ Review the Connection Attributes record used by the Okta connection model

[https://<instance\_name>.service-now.com/nav\_to.do?uri=connection\_attributes.do?sys\_id=93628e57c31320105e0599ccc840dd67](https://shri.service-now.com/nav_to.do?uri=connection_attributes.do?sys_id=93628e57c31320105e0599ccc840dd67)

↳ If it is pointing to the wrong model or customised, revert it to the correct OOB version so the HTTP Connection shows the Attributes section and API Version defaults to v1

→ Recreate the integration profile so they reference the corrected model  
↳ Delete and recreate the Integration Profile  
↳ Generate a fresh token and retest Validate Connection  
↳ After recreation, confirm the HTTP Connection shows Attributes populated and API Version is set to v1

→ Role validation  
↳ Ensure the user configuring the integration has the required role such as sam\_integrator or admin
