---
title: "Application extensions and application templates overview"
aliases:
  - KB0552944
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552944
kb_number: KB0552944
last_modified: 2026-06-23
---

## Application extensions and application templates overview

  

### Issue

Organizations often need more than one business unit (BU) or department to use the same ServiceNow application. Without a structured approach, this leads to over-configuration and customization of the base system application to support the requirements of all parties. ServiceNow supports extending base system applications and using Application Templates. Both methods allow each BU or department to operate in its own working application space. Security controls and configuration can be tailored to each group and inherited from the parent configuration where appropriate. 

Why use this approach: Prevent over-configuring a shared application. 

### Release

N/A

### Cause

How: Extend base system applications such as Incident, Change, and Project, or use the Service Management application templates. 

Approach: Set and configure company-wide standards at the parent global application module, and allow BUs and departments to have their own records, configurations, security controls, and more within their own application space in ServiceNow. This keeps global applications close to base system, so that only relevant shared configuration is adopted by all BUs and departments. 

### Resolution

Practice 

-   Single instance environments 
-   Domain separation is not a fit 
-   Process separation is desired 
-   Global organization, shared services, Center of Excellence (CoE) 
-   Subsequent update/release change management — how to manage impact from ServiceNow releases 

New implementation practices 

-   Naming convention for applications 
-   Naming convention for non-production environments 
-   Establish a governance process before initial go-live 
-   Establish the role of process and application owners for global process and application scope 

When to use 

-   When a ServiceNow application will be used by more than one BU or department 
-   To retain the base system ServiceNow application and scope configuration changes to the platform 
-   When multi-tenancy is desired but not operating as a managed service provider (MSP) 

Advantages 

-   Use parent application business rules, forms, views, and configuration 
-   Process deviation or process isolation 
-   Allows for department-specific data without overcomplicating another department's experience 
-   Allows for data segregation (for reporting, viewing, security, and more) 
-   Creates tailored configuration without impacting the base system configuration - Isolates configuration from base system ServiceNow applications 
-   Allows for Application Scoping, which provides additional security controls for admins and users 

**Examples for global configuration** 

Company-wide standards: 

-   Location data (shared reference data) 
-   Brand data (shared reference data) 
-   Company data (shared vendor, location, and affiliate data) 
-   User and department data (corporate standards for user and organizational information) 

Potential global standards: 

-   Categories 
-   Classifications 
-   Priority specifications 

Examples for BU and department extensions:

-   Custom forms 
-   New fields 
-   Process deviation 
-   BU- and department-specific UI actions and rules 
-   Record separation for reporting 
-   Segregated security controls 

This approach allows global standards to be set at the parent module (such as brand information, location details, and other corporate standards), and allows various BUs or departments to have their own sets of records, configurations, security controls, and more within their own application space. This helps with conflict management and supports reporting from the parent where appropriate. 

**Scope applications** 

Each application has an application scope that determines which of its resources are available to other parts of the system. Application scoping helps prevent one application from impacting another. Application access settings control what parts of the application other applications can access. 

**Private scope** 

Applications in a private application scope restrict access to their application artifacts so that only application artifacts in the same scope have full access to create, modify, remove, or run application data. As the application developer, application access settings determine what parts of an application are accessible from other application scopes. 

**Global scope** 

Applications in the global scope function as shared resources that any application developer can modify. Global scope applications do not have a unique namespace identifier in their application artifact names, but they can have their own application access permissions. Typically, only applications provided by ServiceNow are in the global scope. All custom applications created before application scope was implemented are also in the global scope.
