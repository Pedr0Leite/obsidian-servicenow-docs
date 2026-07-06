---
title: "Why a sub-production instance with MID Servers is normally required for a Discovery/Service Mapping Case"
aliases:
  - KB0748871
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748871
kb_number: KB0748871
last_modified: 2025-07-15
---

## Why a sub-production instance with MID Servers is normally required for a Discovery/Service Mapping Case

  

### Issue

When opening a Case in HI for help with unexpected behaviour from Discovery or Service Mapping, debugging on a sub-production environment setup is almost certainly going to be required.  Most customer will already have this, or how else can you test your own deployments and custom implementations, but some don't. This explains what Customer Support will require, and some of the reasons why. 

## Requirements

Setup requirements of the sub-production instance to be used to testing/reproducing/debugging:

-   Recently cloned from the Production instance, so that versions are the same, all plugins are present, all relevant apps ideally upgraded to the latest versions, and configurations and CMDB data is more-or-less up to date
-   MID Servers installed, able to access all the required IP Ranges
-   Credentials for access to the target Devices

## Reasons

Things that are likely to need to be done, that would prevent the use of a production instance, either because the Technical Support Engineer or the Customer refuse to allow it:

-   Reproducing the issue by re-running discovery is going to update your data, and potentially corrupt or delete your data. When things are not working, you can't be sure what will happen.
-   Investigating what happens when discovering the device for the first time would require (cascade) deleting the CI first, which also deletes all relationships and references from Tasks and other parts of the platform to the CI. That would cause mass data loss on production.
-   Upgrading app versions to confirm if the issue was already fixed. See [KB1965594 App versions to check before opening ITOM Support cases](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1965594)
-   Changing system properties can cause a full instance cache flush. This can cause performance impact for hours.
-   Reproducing issues that have caused a performance impact may cause another performance impact. e.g. to capture a memory heap dump for a thread that causes OOM, requires going OOM, or at least risking it.
-   MID Servers or Instance App nodes may need restarting to clear stuck threads, if this occurs during testing. To capture a thread call stack to see where it gets stuck, it would have to be run again.
-   Session Debug cannot be used due to most code running in the background, meaning Instance level debugging properties such as glide.db.trace and glide.businessrule.callstack would need turning on, and that has a big impact on performance for all users. 
-   IRE Debug is likely to need turning on.
-   Turning on maximum debug logging does cause huge numbers of syslog table records to be inserted. This may have a performance, usability or cost implication for that table.
-   Adding log statements in code to help debug where things start to go wrong would require Code Changes. This may be in common script includes used by many features. There is a risk those code changes will affect functionality in parts of the product unrelated to the original issue. Syntax errors happen. Customers are likely to have procedures that would prevent any code changes like this in production. 
-   ServiceNow and Customers themselves may have change freezes that apply to production.
-   If we think we have a possible workaround, further configuration, code and data changes may be required during the design and testing of that, and the final implementation of the workaround.
-   Ideally a support engineer would set up an update set before starting, to track any changes that would need reverting later, or to capture a workaround. Like any code changes, it should be dev, then test, then prod. You don't implement for the first time in prod. You don't "test in production".

### Release

All currently supported releases.

### Resolution

.
