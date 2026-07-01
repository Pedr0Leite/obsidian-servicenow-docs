---
title: Deployment
description: Deploying custom applications from development to non-production and production instances is one of the most critical processes in ServiceNow platform management. Knowing the ServiceNow application deployment life cycle, including migration methods, security considerations, and organizational best practices ensures stability, security, and traceability.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/get-started-deployment.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Getting Started guide for developers, Building applications]
---

# Deployment

Deploying custom applications from development to non-production and production instances is one of the most critical processes in ServiceNow platform management. Knowing the ServiceNow application deployment life cycle, including migration methods, security considerations, and organizational best practices ensures stability, security, and traceability.

## Key ideas for your deployment

-   Use application-scoped deployments and source control over update sets whenever possible.
-   Leverage [[releaseops-landing|ReleaseOps]], App Engine Management Center/Pipelines and Deployments, or [[system-update-sets|System Update Sets]] depending on your organization's chosen management method.
-   Always test in non-production before deploying to production.
-   Implement access control lists \(ACLs\), role-based access control, and Instance Scan checks as part of every deployment.
-   Find out what your platform owner has standardized and follow that protocol.

-   **[[moving-applications-between-instances|Moving applications between instances]]**  
ServiceNow applications are built in Development instances, then promoted through Test and Production environments using update sets or the Application Repository to package and migrate changes. This multi-instance workflow ensures applications are thoroughly tested before reaching end users in Production.
-   **[[store-private-application-repositories|The ServiceNow Store and private application repositories]]**  
The ServiceNow Store provides two main repository mechanisms for application distribution: the ServiceNow® Store and private \(company\) application repositories.
-   **[[managing-application-versions|Managing application versions]]**  
Semantic versioning \(Major.Minor.Patch\) is the standard approach for ServiceNow applications. Each time you publish from [[servicenow-studio-landing|ServiceNow Studio]], you assign a version number, which gives your team a clear audit trail of all changes.
-   **[[management-options|Deployment management options]]**  
ServiceNow offers multiple management options for orchestrating deployments. Your choice depends on your organization’s maturity, [[licensing|licensing]], and operational preferences. You can choose between ReleaseOps, [[app-engine-management-center|App Engine Management Center]] Pipelines and Deployments, or System Update Sets.
-   **[[standard-operating-procedure-for-deployment|Standard operating procedure for deployment]]**  
Every ServiceNow organization should have a documented deployment standard operating procedure. The procedure should specify the approved method for orchestrating deployments, the pipeline stages and approval gates, and the roles authorized to perform deployments.
-   **[[best-practices-use-source-control|Guidelines for using source control]]**  
Source control \(Git\) combined with the Application Repository is the preferred deployment method for custom scoped applications. Using System Update Sets is also an approved deployment mechanism for application development.

**Parent Topic:**[[getting-started-landing-page|Getting Started guide for developers]]

## Related

- [[moving-applications-between-instances|Moving applications between instances]]
- [[store-private-application-repositories|store private application repositories]]
- [[managing-application-versions|Managing application versions]]
- [[management-options|Deployment management options]]
- [[standard-operating-procedure-for-deployment|Standard operating procedure for deployment]]
- [[best-practices-use-source-control|Guidelines for using source control]]
- [[getting-started-landing-page|Getting Started guide for developers]]
- [[releaseops-landing|ReleaseOps]]
- [[system-update-sets|System update sets]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[licensing|Licensing]]
- [[app-engine-management-center|App Engine Management Center]]
