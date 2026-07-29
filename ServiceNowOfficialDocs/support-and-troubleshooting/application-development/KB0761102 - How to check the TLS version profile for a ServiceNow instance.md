---
title: "How to check the TLS version profile for a ServiceNow instance"
aliases:
  - KB0761102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761102
kb_number: KB0761102
last_modified: 2026-06-29
---

## How to check the TLS version profile for a ServiceNow instance

  

### Issue

Use this article to determine whether an instance uses the TLS 1.0–1.2 profile or the TLS 1.2-only profile. TLS changes are applied at the VIP level, so changes are not possible on a per-instance basis. TLS 1.0 and 1.1 have been deprecated, and instances may be migrated to a TLS 1.2-only profile as a result.

### Release

NA

### Cause

Deprecation of TLS 1.1 and 1.0

### Resolution

Two methods are available to check which TLS profile an instance is using.

**Method 1** — curl command

Run the appropriate curl command for each TLS version against the instance URL. A successful TLS handshake in the output confirms that the instance accepts connections at that version. 

1.  TLS 1.0

curl -v -s --tlsv1.0 https://<instance-name>.service-now.com/stats.do -o /dev/null/ 2>&1

1.  TLS 1.1

curl -v -s --tlsv1.1 https://<instance-name>.service-now.com/stats.do -o /dev/null/ 2>&1

1.  TLS 1.2

curl -v -s https://<instance-name>.service-now.com/stats.do -o /dev/null/ 2>&1

**Method 2** — SSL Labs SSL Test

1\. Open the [SSL Labs SSL Test](https://www.ssllabs.com/ssltest/index.html) in a new tab.

2\. Enter the instance hostname (for example, `<instance-name>.service-now.com`) in the Hostname field.

3\. Select Submit. 

The Configuration section shows which TLS versions the instance accepts, see screenshot below. If only TLS 1.2 is listed, the instance is on the TLS 1.2-only profile. If TLS 1.0 or TLS 1.1 are also listed, the instance uses the broader TLS 1.0–1.2 profile. 

![TLS configuration](/sys_attachment.do?sys_id=af5ad5dd47358f18ac90112a636d4387 "TLS configuration")

### Related Links

[SSL Labs SSL Test](https://www.ssllabs.com/ssltest/index.html)

Retiring TLS 1.0 and 1.1: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0746078](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746078)

SSL/TLS encryption on instances: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0563633](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563633)
