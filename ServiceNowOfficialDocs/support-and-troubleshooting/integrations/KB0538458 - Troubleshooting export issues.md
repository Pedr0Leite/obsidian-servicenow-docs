---
title: "Troubleshooting export issues"
aliases:
  - KB0538458
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538458
kb_number: KB0538458
last_modified: 2026-06-08
---

## Troubleshooting export issues

  

### Issue

This article guides you through the process of troubleshooting export data. It provides steps to help you eliminate common causes for problems by verifying that networking configuration is correct.

Symptoms may include the following:

-   Export takes too long
-   Export not in correct format
-   Not all data exported
-   Records are missing from export
-   Scheduled export fails to run

### Release

All Releases

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that can help you eliminate possible causes and take corrective action as necessary. 

1.  Determine if there are too many records in the export set. For more information, see [KB0538303: Troubleshooting Export - Determine if there are too many records in the export set](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538303 "KB0538303: Troubleshooting Export - Determine if there are too many records in the export set")
2.  Determine if the configured maximum rows to export is too low. For more information, see [KB0538324: Troubleshooting Export - Determine if the configured maximum rows to export is too low](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538324 "KB0538324: Troubleshooting Export - Determine if the configured maximum rows to export is too low")
3.  Determine if a custom script is manipulating the data at the record level. For more information, see [KB0538304: Troubleshooting Export - Determine if there is a custom script manipulating data at the record level](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538304 "KB0538304: Troubleshooting Export - Determine if there is a custom script manipulating data at the record level")
4.  Determine if you are using the correct encoding for the export. For more information, see [KB0538309: Troubleshooting Export - Determine if the encoding setting is wrong](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538309 "KB0538309: Troubleshooting Export - Determine if the encoding setting is wrong")
5.  Determine if Excel can handle the export size. For more information, see [KB0538306: Troubleshooting Export - Determine if the version of Excel cannot handle the data set size](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538306 "KB0538306: Troubleshooting Export - Determine if the version of Excel cannot handle the data set size")

  
Issues specific to exporting reports:

1.  Determine if Webkit HTML to PDF is enabled and the AVP host is configured correctly. For more information, see [KB0694524: Troubleshooting Report Export - Resolve connection refused error when exporting a report](https://support.servicenow.com/kb_view.do?sysparm_article=KB0694524 "KB0694524: Troubleshooting Report Export - Resolve connection refused error when exporting a report")
2.  Determine if the maximum number of detail pages to export is too low. For more information, see [KB0694525: Troubleshooting Report Export - Determine if the configured maximum detail pages to export is too low](https://support.servicenow.com/kb_view.do?sysparm_article=KB0694525 "KB0694525: Troubleshooting Report Export - Determine if the configured maximum detail pages to export is too low")
3.  Determine if there are too many active requests to the AVP server. For more information, see [KB0695136: Troubleshooting Report Export - Resolving HTTP code 503, no thrown error](https://support.servicenow.com/kb_view.do?sysparm_article=KB0695136 "KB0695136: Troubleshooting Report Export - Resolving HTTP code 503, no thrown error")

### Related Links

If your problem still exists after trying the steps in this article, submit an incident to Technical Support and note this Knowledge Base article ID (KB0538458) in the problem description. For more information, see [Submitting a Case](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260 "Submitting a Case").
