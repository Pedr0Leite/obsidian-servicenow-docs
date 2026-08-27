---
title: "Why Full Version and Software Model Do Not Populate for Manually Uploaded Software Installations in ServiceNow"
aliases:
  - KB2629404
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2629404
kb_number: KB2629404
last_modified: 2025-12-11
---

## Issue

When uploading the manual data to software installation table. The discovery model table will fetch the data and the full version is not fetched from the software model table even the version exists and the normalization status shows partially normalized. We wanted to get this full version and also software model automatically  
  
 Summary of the Issue:   
You are uploading software installation records manually into the Software Installation (cmdb\_sam\_sw\_install) table.  
Although the installation record contains the version information, the following are not populated:  
\-- Version / Full Version fields on the Discovery Model  
\-- Software Model field  
\-- Normalization shows as Partially Normalized

## Resolution

\-- Why Full Version and Software Model Are Not Auto-Populating   
i. Full Version is populated only during Discovery, not from manually uploaded data.  
ii. Full Version is extracted by discovery patterns, probes, and sensors.  
iii. Manual imports bypass this logic, so the system does not parse or derive Full Version OOTB.  
  
\-- Software Model is assigned only during SAM Normalization, which requires Mapped Manufacturer + Product + Version to match a catalog entry.  
i. When version is unclear or does not match the normalization library, the model assignment fails or becomes partially normalized.  
ii. For manual data, the normalization engine cannot derive a Software Model unless the imported values match exactly with the normalization content library.  
  
\-- Discovery Model logic does not run for manually uploaded installations.  
i. This logic is triggered only when discovery patterns detect signatures.  
  
3\. Can ServiceNow OOTB Automatically Populate the Full Version and the Software Model for Manual Data?  
\-- Out-of-the-box: No.  
ServiceNow does not automatically calculate or fill the Full Version or Software Model for manually uploaded installation data.  
  
4\. Conclusion  
\-- OOTB, ServiceNow does not populate Version, Full Version, or Software Model for manually uploaded installation data.  
\-- Full Version is only generated during Discovery, not import.  
\-- Software Model assignment requires a complete and exact match with the normalization library, otherwise it remains partially normalized.  
  
Approach:  
However, you can achieve this using customization options, Like Business rules.
