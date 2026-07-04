---
title: "Download Oracle GLAS Java report for customers before WashingtonDC Patch 9 and Xanadu Patch 3"
aliases:
  - KB1704359
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1704359
kb_number: KB1704359
last_modified: 2025-07-23
---

## Download Oracle GLAS Java report for customers before WashingtonDC Patch 9 and Xanadu Patch 3

  

This article is applicable for users who are on patch versions before WashingtonDC Patch 9 or Xanadu Patch 3 and want to download Oracle GLAS Java report.

Customers in Yokohama, WP9 and XP3 do not need to perform the steps mentioned in this article.

Required role: Admin

**Prerequisites:**

'Data Collection for Oracle Global Licensing and Advisory Services' application and Discovery Core(com.snc.discovery.core) plugin must be installed prior to applying the update sets.

Minimum required app version: 'Data Collection for Oracle Global Licensing and Advisory Services' - V 1.8.4

**Steps to follow:**

For customers before WashingtonDC Patch 9 and Xanadu Patch 3 who want to download Oracle GLAS Java report, must follow below steps.

1.  Download the two attached update sets ([Update set 1](/sys_attachment.do?sys_id=12df632b937aa294d9743f986cba1040&sysparm_this_url=kb_knowledge.do%3Fsys_id%3D1e42332a47495e10b7832920326d43b7%26sysparm_view%3D%26sysparm_domain%3Dnull%26sysparm_domain_scope%3Dnull) and [Update set 2](/sys_attachment.do?sys_id=96df632b937aa294d9743f986cba10b3&sysparm_this_url=kb_knowledge.do%3Fsys_id%3D1e42332a47495e10b7832920326d43b7%26sysparm_view%3D%26sysparm_domain%3Dnull%26sysparm_domain_scope%3Dnull)).
2.  Go to 'Retrieved Update Sets' and import the update sets.
3.  Preview and Commit the update sets

**Note:** If these update set changes are not included, the application will download Database related files regardless of the Java option selected.

**Post applying update sets:**

Once the update sets are applied user will be able to download Oracle Java report.

This can be verified by going to 'Download GLAS Data Collection' menu and download Oracle Java report. Verify Java related files are downloaded in the report

**Note:** Please refer to this [KB article](/kb?id=kb_article_view&sysparm_article=KB1705845) to discover Java deployments
