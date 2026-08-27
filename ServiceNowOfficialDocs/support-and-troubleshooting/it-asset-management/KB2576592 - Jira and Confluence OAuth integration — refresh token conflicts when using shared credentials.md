---
title: "Jira and Confluence OAuth integration — refresh token conflicts when using shared credentials"
aliases:
  - KB2576592
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2576592
kb_number: KB2576592
last_modified: 2026-05-22
---

## Jira and Confluence OAuth integration — refresh token conflicts when using shared credentials

  

### Issue

When the same OAuth app (using the same client ID and secret) is used for two separate integrations — Jira and Confluence — the integrations unintentionally invalidate each other's refresh tokens.

Atlassian's OAuth 2.0 implementation uses rotating refresh tokens, which means:

1.  Each time a refresh token is used, Atlassian issues a new access token and a new refresh token.
2.  The previous refresh token is immediately invalidated.

Because both integrations share the same app credentials, each token refresh invalidates the other integration's active token. This results in errors like the following when attempting to refresh the Confluence OAuth token:

```
URL: https://auth.atlassian.com/oauth/token
Response:
{
  "error": "unauthorized_client",
  "error_description": "refresh_token is invalid"
}
```

### Release

-   Release: Yokohama
-   Integrations: Jira, Confluence

### Cause

Atlassian allows only one active refresh token per app-user pair. When a single OAuth app (that is, one client ID and secret) is shared across multiple integrations, each token refresh issues a new refresh token and invalidates the previous one. When both the Jira and Confluence integrations share the same OAuth app, each refresh operation invalidates the other integration's token, causing the `"refresh_token is invalid"` error.

### Resolution

Create a separate OAuth app for each integration — one for Jira and one for Confluence — so each has its own client ID and secret. This gives each integration an independent token lifecycle and helps prevent one refresh operation from invalidating the other.

To resolve the issue:

1.  Log in to the Atlassian developer console at [developer.atlassian.com](https://developer.atlassian.com).
2.  Create a new OAuth 2.0 app for the Confluence integration. Note the new client ID and client secret.
3.  In your ServiceNow instance, navigate to the Confluence integration configuration and update the credentials to use the new client ID and secret.
4.  Repeat steps 2–3 for the Jira integration if it is also using the shared app.
5.  Test both integrations to confirm that token refresh completes without error.

* * *

_Note: Steps 1–4 above reference the Atlassian developer console. The exact navigation may vary depending on your Atlassian product version. Refer to the [Atlassian OAuth 2.0 documentation](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/) for current guidance._
