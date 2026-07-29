---
title: "Outbound Web Services - Troubleshooting Guide"
aliases:
  - KB0659194
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0659194
kb_number: KB0659194
last_modified: 2026-06-05
---

## Outbound Web Services - Troubleshooting Guide

  

### Issue

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>Contents</strong></p><ul><li><a href="#section-1">1. Issue — What This Article Covers</a></li><li><a href="#section-2">2. Quick Symptom Triage</a></li><li><a href="#section-3">3. The Outbound Call Lifecycle</a></li><li><a href="#section-4">4. Universal Diagnostic Checklist</a></li><li><a href="#section-5">5. Common Issue Categories</a><ul><li><a href="#section-5-1">5.1 Connection Failures &amp; TLS Errors</a></li><li><a href="#section-5-2">5.2 Authentication &amp; Authorization Failures</a></li><li><a href="#section-5-3">5.3 Timeouts &amp; Slow Responses</a></li><li><a href="#section-5-4">5.4 Endpoint Errors (4xx/5xx)</a></li></ul></li><li><a href="#section-6">6. How to Enable and Read Outbound HTTP Logs</a></li><li><a href="#section-7">7. HTTP Status Code Quick Reference</a></li><li><a href="#section-8">8. Related Articles</a></li></ul></td></tr></tbody></table>

# 1\. Issue — What This Article Covers

Outbound web service calls originate from your ServiceNow instance and are sent to a third-party endpoint. This article is the starting point for troubleshooting any failure in that direction — whether the call never reaches the endpoint, returns an unexpected response, times out, or fails partway through a MID Server routing path.

Symptoms covered:

-   No response, connection refused, or socket timeout (HTTP 0 or -1).
-   TLS/certificate handshake errors.
-   401 Unauthorized or 403 Forbidden returned by the endpoint.
-   Slow responses or calls timing out before completion.
-   4xx or 5xx error codes returned by the remote endpoint.
-   MID Server ECC queue not processing the request.

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>How to use this article</strong></p><p>This is a hub article. Start with the Quick Symptom Triage in Section 2, then follow the link to the relevant deep-dive article.</p></td></tr></tbody></table>

# 2\. Quick Symptom Triage

Match your symptom on the left, read the article on the right. The diagram below walks the same logic visually.

![](/sys_attachment.do?sys_id=8ba03e2197d94754dfd73dae2153af17 "Screenshot 2026-06-05 at 2.12.27 PM.png")

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>What you're seeing</strong></p></td><td valign="top"><p><strong>Most likely cause</strong></p></td><td valign="top"><p><strong>Read this</strong></p></td></tr><tr><td valign="top"><p>HTTP 0 or -1, socket timeout, connection refused</p></td><td valign="top"><p>Endpoint unreachable, firewall block, DNS failure</p></td><td valign="top"><p><a href="#section-5-1">Section 5.1</a> below, plus <em>Outbound Web Services — Connection Failures &amp; TLS Errors</em></p></td></tr><tr><td valign="top"><p>TLS handshake error, untrusted certificate, SSL exception</p></td><td valign="top"><p>Missing or untrusted certificate in <code>sys_certificate</code> or MID Server CACert file</p></td><td valign="top"><p><a href="#section-5-1">Section 5.1</a> below, plus <em>Outbound Web Services — Connection Failures &amp; TLS Errors</em></p></td></tr><tr><td valign="top"><p>401 Unauthorized returned by endpoint</p></td><td valign="top"><p>Invalid or expired credentials, missing Authorization header, OAuth token issue</p></td><td valign="top"><p><a href="#section-5-2">Section 5.2</a> below, plus <em>Outbound Web Services — Authentication &amp; Authorization Failures</em></p></td></tr><tr><td valign="top"><p>403 Forbidden returned by endpoint</p></td><td valign="top"><p>Insufficient endpoint permissions, OAuth scope mismatch</p></td><td valign="top"><p><a href="#section-5-2">Section 5.2</a> below, plus <em>Outbound Web Services — Authentication &amp; Authorization Failures</em></p></td></tr><tr><td valign="top"><p>Call times out, slow response, MID Server 175-second timeout</p></td><td valign="top"><p>Endpoint latency, timeout configuration, proxy or load balancer delay</p></td><td valign="top"><p><a href="#section-5-3">Section 5.3</a> below, plus <em>Outbound Web Services — Timeouts &amp; Slow Responses</em></p></td></tr><tr><td valign="top"><p>400, 500, 502, or 503 returned by endpoint</p></td><td valign="top"><p>Malformed request body, endpoint-side error, proxy or gateway failure</p></td><td valign="top"><p><a href="#section-5-4">Section 5.4</a> below, plus <em>Outbound Web Services — Endpoint Errors (4xx/5xx)</em></p></td></tr><tr><td valign="top"><p>ECC queue stuck, "No response after 30/60 seconds" error</p></td><td valign="top"><p>MID Server down or not picking up the probe</p></td><td valign="top"><p><a href="#section-5-3">Section 5.3</a> below, MID Server section — <em>Outbound Web Services — Timeouts &amp; Slow Responses</em></p></td></tr></tbody></table>

# 3\. The Outbound Call Lifecycle

Every outbound call follows one of two paths depending on whether a MID Server is involved. Identifying which path your call takes narrows the diagnostic surface immediately.

![](/sys_attachment.do?sys_id=fc903aed97994754dfd73dae2153afa9 "Screenshot 2026-06-04 at 11.30.21 PM.png")

## Direct path (no MID Server)

1.  A script or Flow Designer step calls `execute()` or `executeAsync()` on a `RESTMessageV2` or `SOAPMessageV2` object.
2.  The instance sends the HTTP request directly over the public internet to the third-party endpoint.
3.  The endpoint processes the request and returns an HTTP response.
4.  The response is returned to the calling script or flow step.

## Via MID Server

1.  A script or Flow Designer step calls `execute()` or `executeAsync()`.
2.  An Output RESTProbe or SOAPProbe record is inserted into the ECC Queue.
3.  The MID Server polls the ECC Queue and picks up the probe record.
4.  The MID Server sends the HTTP request to the third-party endpoint.
5.  The endpoint processes the request and returns an HTTP response to the MID Server.
6.  The MID Server wraps the response and inserts an Input RESTProbe or SOAPProbe record back into the ECC Queue.
7.  The instance reads the Input ECC Queue record and returns the response to the calling script or flow step.

## Where failures cluster

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>Path</strong></p></td><td valign="top"><p><strong>Steps where failures cluster</strong></p></td><td valign="top"><p><strong>Failure type</strong></p></td></tr><tr><td valign="top"><p>Direct</p></td><td valign="top"><p>Steps 2–3</p></td><td valign="top"><p>Network, firewall, TLS, or endpoint-side failures. The call left ServiceNow but did not succeed at the destination.</p></td></tr><tr><td valign="top"><p>MID Server</p></td><td valign="top"><p>Steps 2–3</p></td><td valign="top"><p>ECC Queue processing failures. The call never left ServiceNow.</p></td></tr><tr><td valign="top"><p>MID Server</p></td><td valign="top"><p>Steps 4–5</p></td><td valign="top"><p>Network, firewall, TLS, or endpoint-side failures. The call left the MID Server but did not succeed at the destination.</p></td></tr><tr><td valign="top"><p>Direct &amp; MID Server</p></td><td valign="top"><p>Step 4 (Direct) / Step 6 (MID)</p></td><td valign="top"><p>Auth failures. The endpoint received the call but rejected the credentials.</p></td></tr></tbody></table>

# 4\. Universal Diagnostic Checklist

Capture these items before clicking into any deep-dive article. Having them ready resolves most cases at first touch.

1.  **Outbound HTTP log record.** Navigate to Filter Navigator → Outbound HTTP Requests (`sys_outbound_http_log`). Filter by URL contains your endpoint URL. Open the record and check the Request and Response tabs. Note the Response Status and Response Time fields.
2.  **Transaction ID.** From the same log record, copy the Transaction ID. The first 12 characters identify the transaction in the node logs.
3.  **Node hostname.** From the Source tab of the log record, note the System ID — this is the node that processed the call.
4.  **MID Server involvement.** Confirm whether the call routes through a MID Server. Check the ECC Queue (`ecc_queue`) for a matching RESTProbe or SOAPProbe record if unsure.
5.  **Auth type.** Note the authentication type configured on the REST or SOAP message record — Basic, OAuth, Mutual Auth, or API Key.
6.  **External test.** Run the same request from Postman or cURL outside ServiceNow using the same credentials and endpoint. If it fails externally too, the issue is on the endpoint side, not in ServiceNow.

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>Enable debug logging if no log record appears</strong></p><p>If you navigate to Outbound HTTP Requests and cannot find a record for the failing call, logging may not be enabled. See <a href="#section-6">Section 6</a> to enable it. If logging is enabled and no record appears, the call is not being executed — check the script or flow step configuration before the HTTP call is made.</p></td></tr></tbody></table>

# 5\. Common Issue Categories

Short summaries below. The deep-dive articles are where actual diagnosis happens.

## 5.1 Connection Failures & TLS Errors

**When:** The call returns HTTP 0 or -1, a socket timeout, a connection refused error, or a TLS/SSL handshake exception. The Outbound HTTP log may show no response body at all.

**Common causes:** Endpoint unreachable from the instance IP range, firewall blocking outbound traffic, DNS resolution failure, missing or untrusted SSL certificate.

**MID Server note:** If the call routes through a MID Server, the connectivity check is from the MID Server host machine — not the ServiceNow instance. Confirm the endpoint is reachable from the MID Server host directly before investigating the instance configuration.

**Next:** [_Outbound Web Services — Connection Failures & TLS Errors_](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067060)

## 5.2 Authentication & Authorization Failures

**When:** The endpoint returns 401 Unauthorized or 403 Forbidden. The call reached the endpoint successfully but was rejected at the auth layer.

**Common causes:** Invalid or expired credentials, missing Authorization header in the outbound request, OAuth token not refreshing, incorrect OAuth scope, Mutual Auth certificate mismatch.

**Quick check:** Inspect the Request tab in the Outbound HTTP log. Confirm the Authorization header is present and populated. If it is absent, the auth profile is misconfigured on the ServiceNow side.

**MID Server note:** If routing through a MID Server, also check the MID Server agent logs for any auth-related errors that may not surface in the Outbound HTTP log.

**Next:** [_Outbound Web Services — Authentication & Authorization Failures_](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067106)

## 5.3 Timeouts & Slow Responses

**When:** The call takes longer than expected, returns no response within the configured timeout window, or the Outbound HTTP log shows a high Response Time value.

**Common causes:** Endpoint processing slowly, large payload, proxy or load balancer delay, synchronous call timeout configuration, MID Server 175-second hard timeout on outbound probes.

**Quick check:** Review the Response Time field in `sys_outbound_http_log`. A high value with a successful status means the endpoint is slow. A zero or null value with a failure means the connection never completed.

**MID Server note:** MID Server outbound calls have a hard default timeout of 175 seconds. This is independent of the instance-side timeout configuration. If the endpoint does not respond within 175 seconds, the MID Server cancels the call regardless of what is configured on the instance.

**Next:** [_Outbound Web Services — Timeouts & Slow Responses_](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067152)

## 5.4 Endpoint Errors (4xx/5xx)

**When:** The endpoint returns a 400, 500, 502, or 503. The call reached the endpoint and received a response, but the response signals a failure on the endpoint side.

**Common causes:** Malformed request body (400), endpoint-side exception (500), proxy or gateway failure between the MID Server and the endpoint (502/503).

**Quick check:** Run the same request from Postman or cURL using identical headers and body. If the same error is returned outside ServiceNow, the issue is on the endpoint side. If Postman succeeds, compare the request headers and body in the Outbound HTTP log against what Postman sends.

**MID Server note:** A 502 or 503 can originate from a proxy sitting between the MID Server and the endpoint rather than from the endpoint itself. Check the MID Server agent logs for the full error chain.

**Next:** [_Outbound Web Services — Endpoint Errors (4xx/5xx)_](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067183)

# 6\. How to Enable and Read Outbound HTTP Logs

All outbound calls from the instance — except calls executed by the MID Server itself — are recorded in the Outbound HTTP log (`sys_outbound_http_log`). This is the first place to look for any outbound failure.

## Enabling verbose logging

**For calls made via a configured REST or SOAP message record:**

1.  Navigate to the REST or SOAP message record under System Web Services → Outbound.
2.  Select the method.
3.  Under Related Links, select **Set HTTP Log Level → All**.
4.  Re-run the failing call.
5.  Navigate to Filter Navigator → Outbound HTTP Requests to view the full request and response.

**For calls made via Flow Designer spokes or inline script:**

Set the following system properties at Filter Navigator → `sys_properties.list`. These are global properties that affect all outbound web service logging — disable them once logs are captured.

-   `glide.outbound_http_log.override` = `true`
-   `glide.outbound_http_log.override.level` = `all`
-   `glide.outbound_http.content.max_limit` = `1000`

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>Note</strong></p><p>The global log override properties affect every outbound web service call on the instance, not just the one you are investigating. Set them, capture the logs for the failing call, and then revert them immediately to avoid excessive log growth.</p></td></tr></tbody></table>

## Reading the log record

Open a record in `sys_outbound_http_log` and review the following tabs:

-   **Request tab** — full outbound request including headers, Authorization header, and request body.
-   **Response tab** — full response from the endpoint including HTTP status code and response body.
-   **Source tab** — node hostname (System ID) and Session ID for tracing the call to node logs.

![](/sys_attachment.do?sys_id=b8903aed97994754dfd73dae2153afae "Screenshot 2026-06-04 at 11.31.13 PM.png")

## Tracing to node logs

1.  From the log record, copy the Transaction ID.
2.  Take the first 12 characters — this is the TXID used in the node logs.
3.  Search for this TXID in Splunk (production) or bssh (sub-production) on the node identified in the Source tab System ID field.

# 7\. HTTP Status Code Quick Reference

Match the code, jump to the section.

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top"><p><strong>Code</strong></p></td><td valign="top"><p><strong>Meaning</strong></p></td><td valign="top"><p><strong>What to do</strong></p></td></tr><tr><td valign="top"><p><strong>0 or -1</strong></p></td><td valign="top"><p>No response — connection never completed</p></td><td valign="top"><p>Check network path, firewall, and DNS. See <a href="#section-5-1">Section 5.1</a>.</p></td></tr><tr><td valign="top"><p><strong>400</strong></p></td><td valign="top"><p>Bad Request — endpoint rejected the request body or URL</p></td><td valign="top"><p>Check request body format and endpoint URL. See <a href="#section-5-4">Section 5.4</a>.</p></td></tr><tr><td valign="top"><p><strong>401</strong></p></td><td valign="top"><p>Unauthorized — credentials missing or rejected by endpoint</p></td><td valign="top"><p>Check auth profile and Authorization header in the Request tab. See <a href="#section-5-2">Section 5.2</a>.</p></td></tr><tr><td valign="top"><p><strong>403</strong></p></td><td valign="top"><p>Forbidden — credentials valid but insufficient permissions at endpoint</p></td><td valign="top"><p>Check endpoint permissions and OAuth scopes. See <a href="#section-5-2">Section 5.2</a>.</p></td></tr><tr><td valign="top"><p><strong>500</strong></p></td><td valign="top"><p>Internal Server Error — endpoint-side failure</p></td><td valign="top"><p>Test with Postman to confirm issue is on the endpoint side. See <a href="#section-5-4">Section 5.4</a>.</p></td></tr><tr><td valign="top"><p><strong>502</strong></p></td><td valign="top"><p>Bad Gateway — proxy or gateway between caller and endpoint returned an error</p></td><td valign="top"><p>Check proxy and load balancer configuration. See <a href="#section-5-4">Section 5.4</a>.</p></td></tr><tr><td valign="top"><p><strong>503</strong></p></td><td valign="top"><p>Service Unavailable — endpoint temporarily unavailable</p></td><td valign="top"><p>Retry with backoff. If sustained, see <a href="#section-5-4">Section 5.4</a>.</p></td></tr></tbody></table>

# 8\. Related Articles

-   [KB3067060 - Outbound Web Services — Connection Failures & TLS Errors](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067060)
-   [KB3067106 - Outbound Web Services — Authentication & Authorization Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067106)
-   [KB3067152 - Outbound Web Services — Timeouts & Slow Responses](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067152)
-   [KB3067183 - Outbound Web Services — Endpoint Errors (4xx/5xx)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3067183)
-   [KB1695665 — Landing page for Web Services (Outbound)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1695665)
-   [KB0694711 — RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694711)
-   [KB0960404 — MID Server Landing Page](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960404)

### Release

All

### Cause

### Resolution

.

### Related Links

**Outbound Web Services Logs:**

-   [KB0998511 - Capturing localhost logs for Outbound Web Service issues](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998511)
