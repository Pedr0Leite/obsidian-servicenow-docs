---
title: "How to download SAM Publisher Part Number (PPN) content for a self-hosted instance"
aliases:
  - KB1380558
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1380558
kb_number: KB1380558
last_modified: 2026-05-19
---

## How to download SAM Publisher Part Number (PPN) content for a self-hosted instance

  

### Issue

When implementing Software Asset Management (SAM) on a self-hosted instance, you need to upload the SAM Publisher Part Number (PPN) content library manually.

### Release

Any

### Cause

Self-hosted instances do not have direct access to the SAM content portal and require a manual download and upload of the PPN content library.

### Resolution

To download SAM content for your self-hosted instance, follow these steps:

1.  Go to the SAM content portal at [https://itam.service-now.com/software\_asset\_content](https://itam.service-now.com/software_asset_content) and log in with your credentials (user ID and password).
2.  After you log in, the portal displays zip files of content specific to each release.
3.  Download the zip file that matches your instance release. Zip file naming convention: `Content_Library_<DD>_<MM>_<YYYY>_<Release Name>.zip` For example: `Content_Library_16_05_2022_Paris.zip` — This file contains content as of 16 May 2022 for the Paris release.
4.  After downloading the zip file, follow the steps in the SAM documentation to upload the content to your instance: [Manage the SAM software library](https://docs.servicenow.com/bundle/tokyo-it-asset-management/page/product/software-asset-management2/task/manage-sam-software-library.html)

Note: If you do not have credentials for the SAM content portal, raise a support case by following the steps in [KB0862581](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862581). Note that this link requires a Now Support login.
