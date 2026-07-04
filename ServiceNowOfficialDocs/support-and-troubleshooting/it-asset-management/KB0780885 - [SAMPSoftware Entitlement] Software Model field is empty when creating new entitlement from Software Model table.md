---
title: "[SAMP/Software Entitlement] Software Model field is empty when creating new entitlement from Software Model table"
aliases:
  - KB0780885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780885
kb_number: KB0780885
last_modified: 2024-04-08
---

## Issue

-   When adding a new Software Entitlement from the Software Model (cmdb\_software\_product\_model) table Related Lists, it doesn't fill in the Software model field and returns empty.

![](sys_attachment.do?sys_id=5971ecc9dbc838d0fec4fb2439961972)

## Resolution

#### Troubleshooting:

-   Login to the affected instance.
-   Navigate >> Software Model, and try adding a new Software Entitlement from the Related Lists.
-   The Software Model field should get populated with the specific product to which software rights are applied, but it returns empty.
-   In order to identify the cause check the Related Lists update version of the Software Model (cmdb\_software\_product\_model) table to see whether it uses Customized update set.

![](sys_attachment.do?sys_id=dd71ecc9dbc838d0fec4fb2439961973)

-   Also, this can be checked from "sys\_update\_version" table by filtering for the Name is "**sys\_ui\_related\_cmdb\_software\_product\_model\_null**".

![](sys_attachment.do?sys_id=5571ecc9dbc838d0fec4fb2439961975)

## Additional Information

#### The actual behavior:

-   We have 2 columns on the Software Entitlements i.e. model and software\_model.
-   Both have same value and both should be in "sync", but software\_model is the one displayed on the entitlement form.
-   When the Related Lists gets Customized the values might not get synched and thus the Software model field doesn't get populated.
