---
title: "ODBC Driver Installer"
aliases:
  - KB0540707
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0540707
kb_number: KB0540707
last_modified: 2026-08-18
---

## Issue

### Determining which version to use

If your system is running a 32-bit version of Windows, install the 32-bit version of the ODBC driver. If your system is running a 64-bit version of Windows, then your choice depends on the reporting application that you will be using.

## Resolution

To determine if a Windows version is 32-bit or 64-bit, right-click **My Computer** and select **Properties**. Further OS-specific instructions can also be found in this Microsoft knowledge article: [http://support.microsoft.com/kb/827218](http://support.microsoft.com/kb/827218 "http://support.microsoft.com/kb/827218").  
  
Most reporting applications are 32-bit and require the 32-bit ODBC driver. A 64-bit ODBC driver is required only for 64-bit reporting applications.

### Current versions

These links contain ODBC info:

-   1.0.14\_01: [Getting started with ODBC](https://docs.servicenow.com/bundle/latest-application-development/page/integrate/odbc-driver/concept/c_GettingStartedWithODBC.html "Getting started with ODBC")
-   Latest version App link with download access: [Store App URL](https://store.servicenow.com/sn_appstore_store.do#!/store/application/c847b9ffdb9c5050f20ff5471d9619d6 "Store App URL")
