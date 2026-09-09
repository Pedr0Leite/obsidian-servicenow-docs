---
title: "How to define canonical mapping due to error  \"xxxxx\"  is not registered in canonical mapping\" in the logs"
aliases:
  - KB0818176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818176
kb_number: KB0818176
last_modified: 2024-04-08
---

## Issue

The import set rows are failing to create company records with the error "No Content Returned" then followed by a Sys\_ID.

When the logs checked  , below can be observed:

  
2020-01-27 00:12:28 (238) worker.7 worker.7 txid=xxxxxxxxxxxx CanonicalCompanyCreate: Company 'No Content Returned: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' is not registered in canonical mapping.  
2020-01-27 00:12:28 (477) worker.7 worker.7 txid=xxxxxxxxxxxx CanonicalName: Discovered Name: 'No Content Returned: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' Canonical is: 'No Content Returned: c573cec2db6a0454c8d49f67f4961943'  
2020-01-27 00:12:28 (493) worker.7 worker.7 txid=xxxxxxxxxxxx CanonicalName: Discovered Name: No Content Returned: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx core\_company is: 67db03dadbae00541a25e415ca961998  
2020-01-27 00:12:28 (598) worker.7 worker.7 txid=xxxxxxxxxxxx CanonicalName: Discovered Name: 'Company A' Canonical is: 'Company A'  
  
  

## Resolution

To resolve the issue, these steps can be followed:

-   Create the **cds\_client\_mapping** records for the companies seen in the logs having error **"No Content Returned"** . Any custom company/manufacturer has to be updated manually which shall work.
-   Get the full list of companies for Normalized Mapping and add those by an XML import or any other import option then clone to other instances as a solution.
