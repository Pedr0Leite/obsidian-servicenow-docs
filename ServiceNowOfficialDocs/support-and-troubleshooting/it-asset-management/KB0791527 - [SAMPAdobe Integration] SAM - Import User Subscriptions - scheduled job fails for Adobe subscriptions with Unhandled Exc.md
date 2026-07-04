---
title: "[SAMP/Adobe Integration] SAM - Import User Subscriptions - scheduled job fails for Adobe subscriptions with \"Unhandled Exception\" error"
aliases:
  - KB0791527
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791527
kb_number: KB0791527
last_modified: 2025-09-29
---

## \[SAMP/Adobe Integration\] SAM - Import User Subscriptions - scheduled job fails for Adobe subscriptions with "Unhandled Exception" error

  

### Issue

-    The "**SAM - Import User Subscriptions**" schedule job fails for the Adobe subscriptions with an error,

 "**SAM:SAM - Import User Subscriptions: Adobe - Unhandled exception: TypeError: Method and Endpoint must be defined: no thrown error"**

### Release

-   Instance with Software Asset Management Professional plugin installed.

### Cause

-    The error "**SAM:SAM - Import User Subscriptions: Adobe - Unhandled exception: TypeError: Method and Endpoint must be defined: no thrown error"** points to an issue with the configuration of the Adobe integration profile.

### Resolution

-   Login to the affected instance.
-   Navigate >> SaaS License >> Administration >> All Integration Profiles and open the Adobe Subscription profile and click "Validate Adobe Credential" UI Action. However, it fails with the message "Connection Failed".

![](sys_attachment.do?sys_id=d6eab3b8db00f0d016d2a345ca9619d7)

-   Meantime if you navigate >> Multi-Provider SSO >> x509 Certificate and choose associated Adobe certificate and click "Validate Stores/Certificates" UI Action it succeeds.

![](sys_attachment.do?sys_id=16eab3b8db00f0d016d2a345ca9619d5)

-   Probable reason would be because the integration profile must be misconfigured.
-   In order to fix this issue, validate the configuration of the Adobe integration profile by following the "[**Set up Adobe Cloud License Management"**](https://docs.servicenow.com/csh?topicname=set-up-adobe-subscription.html&version=latest "Set up Adobe Cloud License Management\"") documentation.

**Note**: The password used in creating the private/public key should be the same as the certificate record password in ServiceNow instance.
