---
title: "Edge Encryption Certificate Expiry Notification"
aliases:
  - KB0824810
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824810
kb_number: KB0824810
last_modified: 2025-01-03
---

## Edge Encryption Certificate Expiry Notification

  

### Summary

This KB explains about the Edge Encryption Proxy Certificate Expiry Notification:

-   Customers will receive the notifications with the subject "Your ServiceNow X.509 certificate is about to expire in xx days" when the certificate is going to expire.
-   Please check the certificate which is going to expire. If the certificate is related to LDAP, SSO, Web Services, etc then kindly refer [KB0786447.](https://hi.service-now.com/kb_knowledge.do?sys_id=ed7fd54d1bd148907a5933f2cd4bcb4c&sysparm_view=case)
-   If the certificate belongs to Edge Encryption then the customers no need to do anything.
-   This is the certificate that was installed during the implementation of the Edge Proxy which has no impact on the proxy's functioning, and customers no need to renew this certificate.

  

   Below is the sample Edge Encryption Proxy certificate in the ServiceNow instance.

  

![Edge Encryption Proxy Certificate](sys_attachment.do?sys_id=fc7c1401db5ed890a08a1ea668961944 "Edge Encryption Proxy Certificate")
