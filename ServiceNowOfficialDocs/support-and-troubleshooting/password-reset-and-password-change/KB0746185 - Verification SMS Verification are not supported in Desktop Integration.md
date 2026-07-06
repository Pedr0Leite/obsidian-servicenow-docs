---
title: "Verification \"SMS Verification\" are not supported in Desktop Integration"
aliases:
  - KB0746185
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746185
kb_number: KB0746185
last_modified: 2024-04-07
---

## Verification "SMS Verification" are not supported in Desktop Integration

  

### Issue

Possible Cause:

1.  Check to see if URL configured for the Windows Password Reset Application is correct in the Registry?
2.  Use the URL configured in the registry on the Web Browser and verify that Password Reset Process is working or not?
3.  If the Password Reset Process is working fine through the Web Browser once users are login but only failing from the "Forgot Password" link then most likely issue is customer may have Custom Verification Type.
4.  Check to see if the Password Reset Process is using the Custom Verification Type.  (Navigate to -> Password Reset -> Verification -> Verification Type)
5.  As per the Documentation below, We currently don't support "Custom Verification" with Windows Password Reset Application.
6.  There is an Enhancement Request for this FTASK37682

[https://docs.servicenow.com/csh?topicname=password-reset-setup-guide.html&version=latest](https://docs.servicenow.com/csh?topicname=password-reset-setup-guide.html&version=latest)

## Restrictions on the Password Reset Windows Application

-   The Password Reset Windows Application does not support custom verifications.
-   For some verification types, you can use only one verification. Custom verifications are not supported. See [Password Reset verifications](https://docs.servicenow.com/csh?topicname=c_PWRVerifications.html&version=latest "Each verification specifies the method and process for verifying the identity of the user that is requesting password reset.") for details.
