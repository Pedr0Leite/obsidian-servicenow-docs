---
title: "Business Roles to grant Servicenow Roles/Groups - HR Lifecycle Events - Product Query"
aliases:
  - KB2642580
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642580
kb_number: KB2642580
last_modified: 2025-12-16
---

## Business Roles to grant Servicenow Roles/Groups - HR Lifecycle Events - Product Query

  

### Issue

Guidance was requested on integrating Business Roles with ServiceNow Groups to inherit ServiceNow roles, rather than using external identity providers like Okta or Azure AD.

-   Example scenario: Assigning a business role (e.g., "Perth Office") to employees based on location so they automatically receive relevant ServiceNow roles or group memberships for facility requests.
-   Query focused on HR Lifecycle Events and automating role/group assignment within ServiceNow.

### Release

Any Release

### Cause

Business Roles in ServiceNow are designed to assign roles to users in external IDP systems (such as Okta and Azure AD), not directly to ServiceNow User groups or roles. There is no out-of-the-box (OOB) solution for this integration within ServiceNow.

### Resolution

-   Business Roles in ServiceNow are associated with Directory Groups, not User Groups.
-   There is no OOB functionality to link Business Roles directly to ServiceNow roles or groups.
-   To achieve this functionality, use supported integrations with external identity providers like Okta or Azure AD, which can manage role assignments based on Business Roles.
-   Alternatively, consider custom development or consult Professional Services for advanced automation requirements.
