---
title: "Downgrade Rights not created automatically for Microsoft  Part Numbers"
aliases:
  - KB0814322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814322
kb_number: KB0814322
last_modified: 2024-04-08
---

## Issue

Downgrade Rights are not created automatically for a couple of Microsoft Part Numbers.

A scheduled job, Download software content: Downgrade Rights triggered on a weekly basis, gets the downgrade rights from the Software Asset Management content service and pushes the data to the Downgrade Rights \[samp\_dmap\_downgrade\_model\] table.  
Another scheduled job, SAM- Create downgrades/upgrades for a software entitlement, picks up the information from the \[samp\_dmap\_downgrade\_model\] table. The table propagates the next version and the downgrade rights on the existing software models and their corresponding entitlements.  
If there is no software model corresponding to a discovery map, when populating the Downgrade Rights \[samp\_sw\_downgrade\_model\] table, a new software model is automatically created.

## Resolution

-   When there is Software Assurance attached to a particular part number, they are entitled to have the latest version and the life cycle Is dependent on version.
-   So we cannot define downgrade on especially the life cycle for the part numbers which are Software Assurance + Perpetual and Software Assurance
-   A step-up option might be present.
-   There is an option you can create own custom lifecycle which can help you with that particular product if needed.
-   Attached [documentation](sys_attachment.do?sys_id=49132405dbc8f0d016d2a345ca961985 "documentation") for use rights from Microsoft helps in understanding how to downgrade rights both horizontally and vertically.
