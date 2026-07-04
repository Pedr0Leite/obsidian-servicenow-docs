---
title: "Clarification Required on Entra ID Roles for Azure AD Integration (SSO Setup) "
aliases:
  - KB2914712
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2914712
kb_number: KB2914712
last_modified: 2026-05-06
---

## Issue

Entra ID Roles for Azure AD Integration   
  

## Resolution

**Steps to Resolve**  
1\. Assign the Reports Reader role to the Entra ID App Registration's service principal, as it provides full access to sign-in logs, audit logs, and activity reports via the Microsoft Graph API while granting no admin permissions.  
2\. Avoid assigning broader roles such as Security Administrator, Security Operator, or Global Reader, as they carry permissions beyond the required scope for this integration.  
3\. Ensure the AuditLog.Read.All scope is satisfied by the Reports Reader role to meet ServiceNow SAM requirements.
