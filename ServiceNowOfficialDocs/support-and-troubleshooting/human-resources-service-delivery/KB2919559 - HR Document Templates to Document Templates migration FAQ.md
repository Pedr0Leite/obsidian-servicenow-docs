---
title: "HR Document Templates to Document Templates migration FAQ"
aliases:
  - KB2919559
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2919559
kb_number: KB2919559
last_modified: 2026-03-30
---

## Text

 

## Table of Contents

-   [Overview](#mcetoc_1eivfhctq2g)
-   [Frequently Asked Questions](#mcetoc_1eivfhctq2h)
    -   [Is there any migration utility to migrate deprecated to HR Document Templates (sn\_hr\_core\_document\_template, sn\_hr\_core\_pdf\_template) to new Document Templates (sn\_doc\_html\_template, sn\_doc\_pdf\_template)?](#mcetoc_1eivfhctq2i)
    -   [Does the HR service need service activities to generate signing HR Tasks after migration to new Document templates?](#mcetoc_1jklsesji6)
-   [Additional Information](#mcetoc_1eivfhctq2l)

## Overview

HR Document Templates feature has been deprecated in favour of the generic Document Templates.

## Frequently Asked Questions

### Is there any migration utility to migrate deprecated to HR Document Templates (sn\_hr\_core\_document\_template, sn\_hr\_core\_pdf\_template) to new Document Templates (sn\_doc\_html\_template, sn\_doc\_pdf\_template)?

There is no utility to migrate the deprecated HR Document Templates to new Document Templates. Please follow the [migration guidance](https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/migration-hrdt-dt.html) from docs.

### Does the HR service need service activities to generate signing HR Tasks after migration to new Document templates?

No. With new Document Templates, the signing process is now managed entirely through Document Tasks (sn\_doc\_task), no HR tasks need to be created for signing purposes. When the case option **Automatically Initiate Document tasks** is enabled, the signing process will begin automatically as soon as the case status changes to **Ready/Work in progress**. At this point, users involved in the process will receive document tasks that are assigned based on the participant configurations defined within the document template itself.  If this case option is not enabled for the HR service, the assigned agent still has the ability to manually start the signing process by using **Initiate document tasks** button in **Preview Document** popup. Check [this page](https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/understanding-doc-templates.html) to understand how to use new Document Templates in HR service Delivery.

## Additional Information

-   [Migrating from HR Document Templates to Document Templates](https://www.servicenow.com/docs/r/employee-service-management/hr-service-delivery/migration-hrdt-dt.html)
