---
title: "Handling Retry Mechanisms for Adobe Cloud SaaS Integration"
aliases:
  - KB3006995
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3006995
kb_number: KB3006995
last_modified: 2026-05-07
---

## Handling Retry Mechanisms for Adobe Cloud SaaS Integration

  

### Issue

When integrating with Adobe Cloud APIs, outbound API calls may return the following error in the outbound logs:

Status code: 429  
{"error\_code":"429050","message":"Too many requests"}

This error indicates that Adobe's API throttling limits have been exceeded, causing the API to temporarily reject requests.

### Release

Not release specific

### Cause

Adobe enforces rate limits on its APIs. When the number of API calls within a short time period crosses the allowed threshold, Adobe returns a `429 Too Many Requests` response. In some cases, Adobe's response includes a `Retry-After` header that specifies how long to wait before retrying.

The following HTTP status codes indicate transient failures that are suitable for retry:

-   429 Too Many Requests — Request volume has exceeded Adobe's throttling limits.
-   502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout — Temporary service disruptions or network issues. These are not permanent failures and typically succeed after retrying.

Without a retry mechanism, these errors cause immediate job failure.

### Resolution

The SampAdobeRestClient script include contains built-in retry logic that handles these transient failures. The integration automatically makes up to three retry attempts before throwing an error.

How the retry logic works:

1.  On a `429`, `502`, `503`, or `504` response, the system checks whether Adobe's response includes a `Retry-After` header.
2.  If the header is present, the system waits for the specified duration, plus an additional one-second buffer, before retrying.
3.  If no `Retry-After` header is present, the system defaults to a 60-second wait.
4.  After each failed attempt, the wait time doubles (exponential backoff): 60 seconds → 120 seconds → 240 seconds.
5.  If all three attempts fail, the system throws an error with the response body.

This approach respects Adobe's throttling rules while attempting to recover gracefully from transient failures.

To locate the script include:

Navigate to System Definition > Script Includes and search for SampAdobeRestClient and retry logic is defined in \_httpReqExecuteRetry function.

### Related Links

For more information on Adobe API rate limiting, see the [Adobe Experience League community discussion on API 429 errors](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-platform/api-error-429-too-many-requests/m-p/668236).
