---
title: Exploring domain separation
description: With domain separation you can separate data, processes, and administrative tasks into logically defined domains.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/c\_DomainSeparation.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Domain separation for service providers, Access Management]
---

# Exploring domain separation

With domain separation you can separate data, processes, and administrative tasks into logically defined domains.

Domain separation is best for those customers who:

-   Need to enforce absolute data segregation between business entities \(data separation\).
-   Customize business process definitions and user interfaces for each domain \(delegated administration\).
-   Maintain some global processes and global reporting in a single instance.
-   Separate data between service providers, customers, partners, or sub-organizations.
-   Have minor or moderate process differences among customers.

## Domain separation compared to separate instances

While domain separation provides multi-tenancy support, multi-tenancy is still contained within a single instance. Some global properties, data, and processes are shared across all domains. For example, having the system [[c_ChSetRemMeChkbxCookie|Remember me]] on the login page of the system is global and cannot be specified per domain.

If you need complete and total separation of all [[ca-system-properties|system properties]] and do not require global reporting or global processes, then separate instances are the best option.

## Data separation

Members of a domain see only the data contained within their domain or the child domains that are lower in the domain hierarchy. By default, all [[users|users]] and all records are members of the global domain unless an administrator assigns them to a particular domain. Once you assign a user or a record to a domain, the instance compares the user's domain to the record's domain to determine whether the user can view the record.

ServiceNow applications are defined with the following incremental support levels. These levels are based on the perspective of actual use cases and personas.

**Data Separation**: Tenants see only data that they have permissions to see. Tenants can be granted access to other tenant data, but cannot query tenant data if they don't have access.

**UI Separation**: Supports a tenant-specific experience for UI elements such as views, lists, labels, and so on.

**[[sc-business-logic|Business Logic]] Separation**: You can create tenant-specific system [[ca-policies|policies]] such as [[email|email]] notifications, business rules, client scripts, UI policy, and UI actions.

**Hierarchical Modeling**: Nested-multi-tenancy so parent tenants can access child tenant resources. Business logic for parent tenants runs automatically for child tenants, and can be overridden at any level.

**Cross-Tenant Intelligence \(Domain Scope\)**: Handles automatically the data, metadata, business logic, and processing context for tenants that have access to additional tenant data.

In general, data defined at a higher level in the domain hierarchy is not visible at lower levels in the hierarchy.

\[Omitted image "bp-ds-hierarchy.png"\] Alt text: Sample domain separation hierarchy

## Domain path migration

Domain paths are used for all customers. Domain numbering is not used. Customer Service and Support can assist in the upgrade.

## Alternatives to domain separation

Separate instances are a common alternative to domain separation. This provides a great degree of flexibility in meeting the requirements for customers and stakeholders with little to no impact on others.

\[Omitted image "bp-alternatives-to-DS.png"\] Alt text: [[bp-domain-separation-alternatives|Alternatives to domain separation]]

**Warning:** Before activating domain separation, consult your representative to verify that it is suitable for your environment. Domain separation adds a level of administration overhead. Although it can be disabled, it cannot be removed from an instance.

-   **[[ds-before-you-begin|Configuration that can be delegated to internal or external customers]]**  
Domain separation is designed to give ServiceNow® service providers \(SPs\) the ability to configure the services they offer to their customers. It is not designed to enable their customers to administer those services themselves, except in a few areas that this topic details.
-   **[[c_DomainAssignment|Domain assignment]]**  
By default, domain separation adds a domain field to tables and their extensions.
-   **[[c_DomainVisibility|Visibility domains and Contains domains]]**  
Visibility domains control what a specific user or group of users can see. "Contains" domains control what an entire domain of users can see.
-   **[[c_DomainScope|Domain scope]]**  
Domain scope defines what users can and cannot access.
-   **[[sp-concepts|Concepts for service providers]]**  
These concepts work with the existing ServiceNow platform capabilities to help you solve for common use cases.
-   **[[r_InstalledWithDomainSeparation|Installed with domain separation]]**  
Several platform components are added or modified with domain separation.

**Parent Topic:**[[domain-sep-landing-page|Domain separation for service providers]]

**Related topics**  


[[bp-domain-sep-recommended|Domain separation recommended practices for service providers]]

[[domain-sep-plugin|Domain separation plugin]]

## Related

- [[ds-before-you-begin|Configuration that can be delegated to internal or external customers]]
- [[c_DomainAssignment|Domain assignment]]
- [[c_DomainVisibility|Visibility domains and Contains domains]]
- [[c_DomainScope|Domain scope]]
- [[sp-concepts|Concepts for service providers]]
- [[r_InstalledWithDomainSeparation|Installed with domain separation]]
- [[domain-sep-landing-page|Domain separation for service providers]]
- [[bp-domain-sep-recommended|Domain separation recommended practices for service providers]]
- [[domain-sep-plugin|Domain separation plugin]]
- [[c_ChSetRemMeChkbxCookie|Remember me]]
- [[ca-system-properties|System properties]]
- [[users|Users]]
- [[sc-business-logic|Business Logic]]
- [[ca-policies|Policies]]
- [[email|Email]]
- [[bp-domain-separation-alternatives|Alternatives to domain separation]]
