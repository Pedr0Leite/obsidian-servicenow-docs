---
title: "Show Current Domain"
aliases:
  - Show Current Domain
tags:
  - servicenow-dev-program
  - code-snippet
  - show-current-domain
  - client-scripts
---

Domain Separation Current Domain Display
Overview
This functionality provides real-time awareness to users about the current selected domain within ServiceNow's Domain Separation framework. It displays an informational message on form load indicating the active domain context, helping prevent accidental configuration or data entry in the wrong domain.

Components
Script Include: DomainCheckUtil
Global, client-callable Script Include allowing client scripts to query the current domain name via GlideAjax.

Methods:
isCurrentDomain(domainSysId) — Checks if a given domain sys_id matches the current session domain.

Client Script
An onLoad client script configured globally on the Global table, set to true to load on all forms.
Calls the Script Include via GlideAjax to retrieve current domain name asynchronously.

Displays the domain name as an informational message (g_form.addInfoMessage) on the form header on every page load.

Usage
Upon loading any record form, users see a message stating:
"You are currently working in Domain Separation domain: [domain_name]."

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
