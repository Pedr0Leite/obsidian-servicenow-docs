---
title: "Test failed: Custom operation Nutanix API Query failed to execute script due to script error: JAVASCRIPT_CODE_FAILURE: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKI"
aliases:
  - KB0783127
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783127
kb_number: KB0783127
last_modified: 2024-04-07
---

## Issue

Nutanix pattern discovery is failing with an error " Test failed: Custom operation Nutanix API Query failed to execute script due to Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: java.security.cert.CertPathBuilderException: No issuer certificate for certificate in certification path found"

**Steps To Reproduce:**

1\. Run discovery on Nutanix Server.

2\. You will see above error message in discovery logs.

## Resolution

You may need to add certificates to JRE keystore on the target device.

## Additional Information

[https://stackoverflow.com/questions/40162500/why-am-i-getting-no-issuer-certificate-for-certificate-in-certification-path-fo](https://stackoverflow.com/questions/40162500/why-am-i-getting-no-issuer-certificate-for-certificate-in-certification-path-fo)
