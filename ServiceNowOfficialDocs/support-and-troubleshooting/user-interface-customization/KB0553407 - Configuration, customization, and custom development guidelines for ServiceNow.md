---
title: "Configuration, customization, and custom development guidelines for ServiceNow"
aliases:
  - KB0553407
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0553407
kb_number: KB0553407
last_modified: 2026-05-01
---

## Configuration, customization, and custom development guidelines for ServiceNow

  

### Issue

Learn the differences between configuration, customization, and custom development on the ServiceNow platform. This article defines each approach, explains when to use them, and provides general guidelines for managing customizations effectively.

For additional guidance, see the Business-smart customization resource linked in the Related Links section.

### What is a configuration?

Configuration uses capabilities and features built into the Now Platform to meet business demands in a safe and supportable way, such as through modifications to forms or table extensions. While you should avoid over-configuration — for example, adding excessive forms or UI policies — configuration should be your first option for meeting business demands.

### What is a customization?

ServiceNow uses the term customization to refer to any form of custom functionality built to meet business demands.

### What is custom development?

Custom development involves modifying baseline business rules in existing ServiceNow applications or building new applications from table extensions. Use custom development when configuration cannot meet business demands. Custom development should employ consistent, supported tools and methods and be overseen by clear, effective governance.

#### **Configuration example**

Before an incident is promoted to a major incident, the Business impact field must be mandatory. If a value is not provided, the record should not update. A UI policy, one of the many platform tools for tailoring functionality to meet specific requirements, can be used to meet this requirement.

#### **Custom development example**

You are implementing the Service Catalog and need to add fields to gather data on the catalog checkout page. The catalog checkout page is a Service Portal widget that is part of the base system installation. A change to this code is considered custom development.

When someone builds a new custom feature (for example, custom applications or third-party widgets), ServiceNow support provides troubleshooting guidance, but you are responsible for maintaining and fixing the feature.

### Facts

#### **What if you customize code that is part of a base system installation?**

If you customize base system code, the following applies:

-   You must maintain that code going forward.
-   You are responsible for verifying that the functionality still works after an upgrade.

#### **Can you still receive support on a customization?**

Yes. However, if the support team determines that the customization is the cause of the issue, they advise you to revert to the base system code before they can assist further.

#### **What are the ramifications of customizing the platform?**

The ServiceNow platform is flexible and can fulfill a wide range of requirements. However, the platform uses a framework that supports how applications process tasks, how forms render in multiple browsers, and the overall user experience.

ServiceNow relies on the framework's integrity to develop and provide support in a consistent manner. If you have requirements or ideas for enhancements, you can submit an Enhancement Request to the ServiceNow development team. Each request is evaluated and, if approved, is incorporated into a future release.

### Release

Not release specific

### Resolution

Before proceeding with a customization, understand what it involves and how it can affect your instance. 

Make customizations to base system objects where necessary so that conflict resolution and decision-making are appropriately recorded in updates. Hidden customizations may cause administrators to overlook updates in future assessments when reverts or merges are necessary.

If a customization is essential, follow these general guidelines:

1.  Establish the Business-smart customization approach (see Related Links) to verify that customizations are limited and clearly linked to business value.
2.  Avoid copying objects. Instead, update objects in place wherever possible, except for Service Portal widgets and other items designed to be reused.
3.  Default to adding before editing. For example, add fields to forms rather than change the type of an existing field. When adding, avoid using the same names as default objects, methods, or classes. Keep the number of fields you add to a minimum — the more fields on a form, the longer it may take to load.
4.  Use scoped applications as the default for any new custom development.
5.  Clearly document what has been customized and the reason for the change. This makes future maintenance significantly easier.
6.  Verify that customizations work after an upgrade, and keep track of what customizations were made.

### Related Links

[Business-smart customization](https://nowlearning.servicenow.com/nowcreate?id=nc_asset&asset_id=a820de08c3a30a501ac0f60f05013157&nc_source=copy_asset_link)—Provides guidance on evaluating customization value against risks and technical debt, and implementing customizations in a value-driven manner that does not adversely affect upgrades or platform performance.
