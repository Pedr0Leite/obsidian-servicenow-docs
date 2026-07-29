---
title: "SAMP Adobe Certifcate load error :  Invalid pkcs12_key_store : Integrity check failed: java.security.NoSuchAlgorithmException: Algorithm HmacPBESHA256 not available"
aliases:
  - KB1113608
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1113608
kb_number: KB1113608
last_modified: 2024-01-30
---

## Issue

\[1\] Created private key to PKS format as mentioned in ServiceNow document however on validating the certificate, getting below error.  
error: Error Messagejava.lang.Exception: Invalid pkcs12\_key\_store : Integrity check failed: java.security.NoSuchAlgorithmException: Algorithm HmacPBESHA256 not available

ServiceNow Doc link: [https://docs.servicenow.com/bundle/rome-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html](https://docs.servicenow.com/bundle/rome-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html)

![](/sys_attachment.do?sys_id=4c682d719708ca10539e35d11153afa4)

\--------------------------

\[2\] Connection Fails with 'Could not match JWT signature to any of the bindings. invalid\_token', when following [Integrate with Adobe Cloud](https://docs.servicenow.com/bundle/tokyo-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html)

The existing openssl version installed on customer instance is unable to transform the private key to PKS format.

Tried generating the PKS format certificate on windows machine and regenerate the certificate using OpenSSL version 3.1.3 worked.

## Resolution

\[1\] Use the openssl version 1.1.1 which is the version just before 3.0 for creating the certificate for the Adobe integration.  
  
\[After installing the new version of openssl you should be able to use the same command listed in the docs:  
openssl pkcs12 -export -out test1-certificate.pfx -inkey private.key -nocerts\]

\[2\] If above still fails check if it's possible OpenSSL installation having issues. There are some know customer case with issues.

Try uninstall/install and try generating certificate. Certificate generation should work with both OpenSSL 1.1\* and 3.\* versions.

## Additional Information

\[-\] Add 2 system properties for debugging:

-   glide.rest.debug = true
-   glide.outbound\_http\_log.override = true
-   glide.outbound\_http\_log.override.level = all

\[-\] Convert the key that was automatically downloaded from Adobe Service Account (JWT) portal app with KEY format to the PKS format using command:

openssl pkcs12 -export -out test1-certificate.pfx -inkey private.key -nocerts
