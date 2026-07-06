---
title: "Can a MID Server be restricted to prevent less secure SSL/TLS versions/encryption algorithms being used?"
aliases:
  - KB0761130
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761130
kb_number: KB0761130
last_modified: 2025-01-03
---

## Can a MID Server be restricted to prevent less secure SSL/TLS versions/encryption algorithms being used?

  

### Summary

A MID Server can be configured to prevent it using less secure SSL/TLS connection encryption standards when making connections from the MID Server.

e.g. You may want all requests to any non-TLS 1.2 compliant HTTP server to fail.

### Release

Since Fuji.

### Instructions

You can find full details on the various specific standards that can be disabled, and which MID Server properties and JRE settings to use to do this in the MID Server chapter of [KB0550654 ServiceNow instance hardening. Customer security.](https://hi.service-now.com/kb_view.do?sysparm_article=KB0550654 "KB0550654 ServiceNow instance hardening. Customer security.")

For information on disabling particular less secure algorithms that might be used by TLS, see [KB0594703 MID Server support for AES 256 encryption](https://hi.service-now.com/kb_view.do?sysparm_article=KB0594703 "KB0594703 MID Server support for AES 256 encryption").
