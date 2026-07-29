---
title: "Orphaned duplicate request is created via inbound email action using Cart() API"
aliases:
  - KB0743785
tags:
  - servicenow
  - support-kb
  - inbound-email-actions
  - cart-api
  - service-catalog
  - scripting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743785
kb_number: KB0743785
last_modified: 2024-04-07
---

## Orphaned duplicate request is created via inbound email action using Cart() API

  

### Issue

# Symptoms

Orphaned Request is created from an inbound action in addition to a valid request created at the same time. 

# Release

Applicable to all Releases

# Cause

When an inbound action processes an email, it determines if a record is inserted based on whether the 'current' GlideRecord object is inserted with a current.insert(). 

When the inbound action's intention is to create a Request (sc\_request) and the script uses the [Cart() API](https://docs.servicenow.com/csh?topicname=r_ServiceCatalogScriptAPI.html&version=latest), the request is created when below line is executed. 

```
var rc = cart.placeOrder();
```

In addition to this, if the script has either current.insert() or current.update(), an orphaned record will be created. The request created is in the rc object and since the current object is still not inserted, the email log shows that this inbound action is skipped and that it did not create or update sc\_request. 

# Resolution

Since the request is created using the Cart() API, there is no need have a current.insert() or current.update() in the script. To avoid creating orphaned duplicate requests, remove the current.insert() or current.update().  

If you wish to add a custom log to the Email log when the inbound action runs by using logger.info() method. 

Example:

```
logger.info("Processed 'Create Request', created: " + rc.number);
```

This will be now seen in the Email Logs.

## Related

- [[KB0727612 - Copy inbound email into the Work Notes or Additional Comments field of a target record]] - inbound email action scripting pattern
- [[c_ServiceCatalogAPI]] - Service Catalog / Cart() scripting API reference

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727612 - Copy inbound email into the Work Notes or Additional Comments field of a target record|Copy inbound email into the Work Notes or Additional Comments field of a target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type|How to generate a token using sn_auth - oAuth API  for Authorization grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746144 - Users do not see ticket information after ordering a catalog item|Users do not see ticket information after ordering a catalog item]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0748114 - Users see a No Matches Found on catalog item variable|Users see a \"No Matches Found\" on catalog item variable]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0750886 - ACL script is failing at script include function call|ACL script is failing at script include function call]]
