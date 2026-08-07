---
title: "Inbound Web Services — Troubleshooting Guide"
aliases:
  - KB0546297
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546297
kb_number: KB0546297
last_modified: 2026-06-04
---

## Inbound Web Services — Troubleshooting Guide

  

### Issue

<table border="1" cellspacing="0" cellpadding="4"><tbody><tr><td><strong>Contents</strong><ol><li><a href="#section-1">Issue — What This Article Covers</a></li><li><a href="#section-2">Quick Symptom Triage</a></li><li><a href="#section-3">The Inbound Request Lifecycle</a></li><li><a href="#section-4">Universal Diagnostic Checklist</a></li><li><a href="#section-5">Common Issue Categories</a><ul><li><a href="#section-5-1">5.1 Network &amp; Connection Failures</a></li><li><a href="#section-5-2">5.2 Authentication, Authorization &amp; ACLs</a></li><li><a href="#section-5-3">5.3 Rate Limits, Semaphores &amp; Throttling</a></li><li><a href="#section-5-4">5.4 Timeouts, Slow Responses &amp; Server Errors</a></li><li><a href="#section-5-5">5.5 Empty Bodies &amp; Wrong Record Counts</a></li></ul></li><li><a href="#section-6">HTTP Status Codes — Quick Reference</a></li><li><a href="#section-7">Related Articles</a></li></ol></td></tr></tbody></table>

## 1\. Issue — What This Article Covers

Starting point for troubleshooting **inbound web service issues** — calls coming into a ServiceNow instance via REST, SOAP, GraphQL, or Scripted REST API.

Symptoms covered:

-   No response, timeout, or connection failure.
-   401 / 403 auth failures.
-   429 throttling.
-   Slow responses, or transactions cancelled at 5 minutes.
-   Empty bodies, or fewer records returned than expected.
-   500 / 502 / 503 server errors.

**How to use this article:** This is a hub article. It points you to the right deep-dive. Start with the Quick Symptom Triage below.

[↑ Back to top](#top)

## 2\. Quick Symptom Triage

Match your symptom on the left and follow the link on the right.

![](/sys_attachment.do?sys_id=29b78bd197958f500ed83bbe2153afa6 "Screenshot 2026-06-04 at 8.13.42 PM.png")

| What you are seeing | Most likely cause | Read this |
| --- | --- | --- |
| No response, connection refused, TLS handshake error, or CORS error in browser console | Network, firewall, certificate, or CORS configuration | [Inbound Web Services — No Response and Connection Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064934) |
| 401 Unauthorized or 403 Forbidden | Auth, API key, token, role, or ACL issue | [Inbound Web Services — Authentication and Authorization Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064952) |
| SOAP request returns "Insert Aborted" | Business rule, mandatory field, or write ACL blocking the insert | [Inbound Web Services — Authentication and Authorization Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064952) |
| GraphQL returns "Could not process ACLs" | User lacks access to the field or record referenced by the query | [Inbound Web Services — Authentication and Authorization Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064952) |
| 403 returned even though the operation succeeded | Known ACL response pattern on POST | [KB2697679](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2697679) |
| 429 Too Many Requests, throttling, or "adding nodes didn't help" | Rate limit rule, semaphore saturation, or per-table quota | [Inbound Web Services — Rate Limits and Throttling](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3046852) |
| Calls timing out at exactly 5 minutes | Per-table transaction quota (300 s default) | [Inbound Web Services — Rate Limits and Throttling](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3046852), Section 7 |
| Slow but eventually succeeds, intermittent 500 / 502 / 503 | Query performance, indexing, or transient platform event | [Inbound Web Services — Timeouts and Slow Responses](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047080) |
| Empty response body, or fewer records returned than sysparm\_limit requested | ACLs filtering rows post-query | [Inbound Web Services — Empty or Incomplete Results](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047115) |
| Table API response sorted differently than expected | Default sort behavior on Table API | [KB2628639](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2628639) |
| Web service export size or throttling concerns | Export sizing limits | [KB0547836](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547836) |

[↑ Back to top](#top)

## 3\. The Inbound Request Lifecycle

Every inbound request passes through five stages. Most failures live in exactly one. Identifying the stage narrows the diagnostic path.

![](/sys_attachment.do?sys_id=b1b78bd197958f500ed83bbe2153afab "Screenshot 2026-06-04 at 8.17.34 PM.png")

1.  **Network & Delivery** — The request travels from the client to the instance. Failures here mean the request never arrives. Symptoms: no response, TLS error, connection refused, CORS error.
2.  **Authentication & Authorization** — The instance verifies the caller's identity and checks roles and ACLs. Failures here return HTTP 401 or 403.
3.  **Throttling & Capacity** — The instance checks rate limit rules, semaphore availability, and per-table quotas. Failures here return HTTP 429 or cancel the transaction.
4.  **Execution & Processing** — The instance runs the query or operation. Failures here produce slow responses, 500 / 502 / 503 errors, or transaction cancellations.
5.  **Response & Data Return** — The instance assembles the response and applies ACL row filtering. Failures here produce empty bodies or fewer records than requested.

[↑ Back to top](#top)

## 4\. Universal Diagnostic Checklist

Capture these items before opening any deep-dive article. They resolve most cases at first touch.

-   **Full HTTP response headers** — especially status code and any header starting with `X-RateLimit-` or `Retry-After`. Their presence or absence is itself diagnostic.
-   **Time of failure** to the second, with timezone (UTC strongly preferred).
-   **Endpoint and target table** (e.g., `POST /api/now/table/incident`).
-   **Client IP and integration user** that made the call.
-   **Recent change context** — platform upgrade, rate limit rule edit, ACL change, or client-side deployment in the last 30 days.
-   **A snapshot of** `https://<instance>.service-now.com/stats.do` captured as close to the failure time as possible.

**Enable debug logging if the request never appears to arrive.** If you turn on debugging and do not see your request in the logs, the call is not reaching the instance — go to [No Response and Connection Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064934). Available debug properties:

-   REST: `glide.rest.debug`
-   SOAP: `glide.processor.debug.SOAPProcessor`
-   JSONv2 (Fuji and later): no dedicated debug property; rely on Transaction and All logs.

[↑ Back to top](#top)

## 5\. Common Issue Categories

Short summaries below. The deep-dive articles are where actual diagnosis happens.

### 5.1 Network & Connection Failures

**When:** request does not reach the instance, TLS handshake errors, connection refused, or CORS errors in the browser console.

**Common causes:** customer-side firewall or proxy block, missing or expired TLS trust chain, DNS or routing failure, missing CORS rule.

**Next:** [Inbound Web Services — No Response and Connection Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064934). Verify instance IP ranges in [KB0538621](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538621).

### 5.2 Authentication, Authorization & ACLs

**When:** 401, 403, SOAP Insert Aborted, or GraphQL ACL error.

**Two ACL levels apply:**

-   **Processor-level** — gates the endpoint. SOAP requires a SOAP role. REST requires `rest_service`.
-   **Table / record-level** — gates which rows the user sees. Empty bodies or short result sets usually mean these.

**Quick check:** if it works as admin but fails as the integration user, it is ACLs — not auth.

**Next:** [Inbound Web Services — Authentication and Authorization Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064952).

### 5.3 Rate Limits, Semaphores & Throttling

**When:** HTTP 429, or failures under load.

**Three layers — confusing them is the most common source of misdiagnosis:**

-   **Per-instance rate limit rules** (`sys_rate_limit_rules`). Hourly cap per user or role. Does not scale with nodes.
-   **Per-node semaphores** (API\_INT, visible at `stats.do`). Scales with nodes.
-   **Per-table transaction quotas**. Cap duration and concurrency on a specific table. Does not scale with nodes.

**Quick check:** 429 with `X-RateLimit-*` headers = Layer 1. 429 without them = Layer 2. Cancels at exactly 5 minutes = Layer 3.

**Next:** [Inbound Web Services — Rate Limits and Throttling](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3046852).

### 5.4 Timeouts, Slow Responses & Server Errors

**When:** calls take much longer than expected, time out without a clean 429, or return HTTP 500 / 502 / 503.

**Common causes:** large or unfiltered Table API queries, missing indexes on integration filter fields, transient 5xx during maintenance windows, server exceptions in System Log.

**Next:** [Inbound Web Services — Timeouts and Slow Responses](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047080).

### 5.5 Empty Bodies & Wrong Record Counts

**When:** the call succeeds (200 or 201) but the response body is empty, or fewer records are returned than `sysparm_limit` requested.

**Common cause:** ACLs filter rows after the query runs. The platform applies `sysparm_limit` first, then drops any rows the user cannot read. Result: fewer rows than requested, with no error.

**Quick check:** re-run as admin. If the row count jumps, the cause is ACL filtering.

**Next:** [Inbound Web Services — Empty or Incomplete Results](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047115).

[↑ Back to top](#top)

## 6\. HTTP Status Codes — Quick Reference

| Code | Meaning | What to do |
| --- | --- | --- |
| **400** | Bad Request | Malformed JSON, missing required field, or invalid endpoint. Fix the request body or URL. |
| **401** | Unauthorized | Credentials missing, invalid, or expired. See [Section 5.2](#section-5-2). |
| **403** | Forbidden | Credentials valid, but user lacks the required role or ACL. See [Section 5.2](#section-5-2). For the success-but-403 pattern, see [KB2697679](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2697679). |
| **429** | Too Many Requests | Throttled by a rate limit rule, semaphore pool, or table quota. See [Section 5.3](#section-5-3). |
| **499** | Client Closed Request | Client disconnected before the instance responded. Extend the client timeout or investigate slow processing. See [No Response and Connection Failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064934), Section 4.4. |
| **500** | Internal Server Error | Exception in processing. Check System Log for the stack trace. See [Section 5.4](#section-5-4). |
| **502** | Bad Gateway | Node unresponsive or high load, or customer-side proxy or load balancer issue. See [Section 5.4](#section-5-4). |
| **503** | Service Unavailable | Usually transient — instance maintenance window or short-term capacity event. Retry with backoff. If sustained, see [Section 5.4](#section-5-4). |

[↑ Back to top](#top)

## 7\. Related Articles

-   [KB3064934](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064934) — Inbound Web Services — No Response and Connection Failures
-   [KB3064952](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3064952) — Inbound Web Services — Authentication and Authorization Failures
-   [KB3046852](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3046852) — Inbound Web Services — Rate Limits and Throttling
-   [KB3047080](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047080) — Inbound Web Services — Timeouts and Slow Responses
-   [KB3047115](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3047115) — Inbound Web Services — Empty or Incomplete Results
-   [KB0538621](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538621) — How to find IP address and datacenter information for your instance
-   [KB2628639](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2628639) — Table API response sorting behavior
-   [KB2697679](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2697679) — POST returns 403 although operation succeeded
-   [KB0547836](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547836) — Web service export sizing and throttling

[↑ Back to top](#top)

### Release

.

### Resolution

#### .
