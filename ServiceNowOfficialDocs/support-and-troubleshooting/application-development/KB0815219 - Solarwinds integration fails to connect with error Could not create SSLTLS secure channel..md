---
title: "Solarwinds integration fails to connect with error \"Could not create SSL/TLS secure channel\"."
aliases:
  - KB0815219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815219
kb_number: KB0815219
last_modified: 2024-04-08
---

## Solarwinds integration fails to connect with error "Could not create SSL/TLS secure channel".

  

### Issue

NOTE: This issue, as well as the troubleshooting details, are covered by the vendor (Solarwinds) on the following external knowledge article:

-   [ServiceNow integration failing with error "Could not create SSL/TLS secure channel](https://support.solarwinds.com/SuccessCenter/s/article/ServiceNow-integration-failing-with-error-Could-not-create-SSL-TLS-secure-channel "ServiceNow integration failing with error \"Could not create SSL/TLS secure channel")

* * *

When attempting to connect with Solarwinds integration, the following error is thrown in the third party application:

![](sys_attachment.do?sys_id=ab55784ddbccb8d066e0a345ca9619a0)

In addition, searching for the SolarWinds Alert Integration app in ServiceNow returns no results, despite it being apparently installed:

![](sys_attachment.do?sys_id=2355784ddbccb8d066e0a345ca9619a2)

### Cause

Causes can be:

-   An incorrect installation of the SolarWinds Alert Integration app from the ServiceNow store.
-   TLS1.1 and lower connections are no longer accepted. Note that TLS 1.2 does not support Orion deployment NPM 12.1.

### Resolution

Verify connectivity to ServiceNow by visiting the following URL: 

-   https://\[_INSTANCE NAME_\].service-now.com/x\_sow\_intapp\_connection\_test.do

1.  If connectivity to ServiceNow is okay, the results should look something like:

![](sys_attachment.do?sys_id=2755784ddbccb8d066e0a345ca96199f)

If the connection to ServiceNow is okay:

1.  Uninstall the SolarWinds Alert Integration app in ServiceNow.
2.  Reinstall the application as an administrator.

If Orion is on NPM 12.1 or NPM 12.2, upgrade to the minimum supported version which is NPM 12.3, as it connects via TLS1.2.

### Related Links

-   [ServiceNow integration failing with error "Could not create SSL/TLS secure channel](https://support.solarwinds.com/SuccessCenter/s/article/ServiceNow-integration-failing-with-error-Could-not-create-SSL-TLS-secure-channel "ServiceNow integration failing with error \"Could not create SSL/TLS secure channel")
-   [How to Integrate ServiceNow with the Orion Platform](https://support.solarwinds.com/SuccessCenter/s/article/How-to-Integrate-ServiceNow-with-the-Orion-Platform-Video "How to Integrate ServiceNow with the Orion Platform")
