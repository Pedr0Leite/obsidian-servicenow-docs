---
title: "Some of the software installs created by the SG-JAMF source have the assigned_to field populated, while others do not."
aliases:
  - KB2597829
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2597829
kb_number: KB2597829
last_modified: 2026-05-21
---

## Some of the software installs created by the SG-JAMF source have the assigned\_to field populated, while others do not.

  

### Issue

Some of the software installs created by the SG-JAMF source have the assigned\_to field populated, while others do not. As per below doc, SG-JAMF populates the assigned\_to field only on the Computer and Handheld Device classes, not on the cmdb\_sam\_sw\_install table.

[https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/configuration-management/reference/cmdb-jamf-classes.html](https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/configuration-management/reference/cmdb-jamf-classes.html)

However, there are some software install records created by SG-JAMF and the assigned\_to field populated, leading to further questions and behavior.

### Release

NA

### Cause

\[-\] When SG-JAMF creates Hardware or Handheld Device CI records, the assigned\_to field is automatically populated by the SG-JAMF integration. However, when SG-JAMF creates Software Install records, the assigned\_to field is not populated by default, which is expected behavior.

\[-\] The related Hardware CI must have the assigned\_to field populated.

\[-\] For Software Install records that have both norm\_product and norm\_publisher values, the assigned\_to field is populated by the scheduled job "SAM - Set 'assigned\_to' Field on Licensable Install Records", which runs daily.  
  
\[-\] In cases where the Hardware CI's assigned\_to value changes, the OOB business rule "Update Software Installs with User" populates the related Software Install records 'assigned\_to' field to match.  
  
\[-\] Lastly, if a Software Install record has no normalized product or publisher data and there is no change to the assigned\_to field on the related Hardware record, the assigned\_to field remains empty.

### Resolution

To have the assigned\_to field populated on all the SW install records created by SG-JAMF, customization would be required.  
Create a custom business rule on cmdb\_sam\_sw\_install table to populate the assigned\_to value from the related hardware CI record.
