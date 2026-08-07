---
title: "Unable to validate connnection on Tableau Cloud Integration"
aliases:
  - KB2726458
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2726458
kb_number: KB2726458
last_modified: 2026-01-20
---

## Unable to validate connnection on Tableau Cloud Integration

  

## Table of Contents

-   [Issue](#mcetoc_1jfdmf6hkff)
-   [Cause](#mcetoc_1jfdmf6hkfg) 
-   [How validation builds the URL (OOB)](#mcetoc_1jfdmf6hkfh)
-   [Common misconceptions (and clarifications)](#mcetoc_1jfdmf6hkfi)
    -   [The failure is caused by credentials](#mcetoc_1jfdmf6hkfj)
    -   [Does the spoke auto‑inserts /api/?](#mcetoc_1jfdmf6hkfk)
    -   [The Tableau REST version in the token is wrong.](#mcetoc_1jfdmf6hkfl)
-   [Resolution](#mcetoc_1jfdmf6hkfm)
-   [Related Links](#mcetoc_1jfdmf6hkfn)

## Issue

When configuring the Tableau Cloud integration for SaaS License Management, the Validate connection step fails with:  
`Connection validation is not successful. Please check connections and credentials and try again`

## Cause 

One possible cause is that `/api/` is not included in the Connection URL.

## How validation builds the URL (OOB)

The Validate connection action in the Tableau Cloud spoke derives the REST signin endpoint from the Connection URL you provide.

In the observed behavior, the action appends /<version>/auth/signin to the Connection URL verbatim.

If the Connection URL does not already contain `/api/`, the final path becomes `/<version>/auth/signin` **(missing /api) and Tableau Cloud returns 404.**

Including `/api/` in the Connection URL yields the correct REST path **/api/<version>/auth/signin, and validation completes successfully.** 

Note: Tableau's REST API requires the /api/ segment before the versioned route for authentication (signin).

It has been validated that **/api/<version>/auth/signin returns a valid response, while the non-/api path returned 404**

## Common misconceptions (and clarifications)

### The failure is caused by credentials

In this symptom pattern the request never reaches authentication; it fails with 404 Not Found due to the URL path, not invalid credentials.

### Does the spoke auto‑inserts /api/?

The observed logs show the request was sent to /<version>/auth/signin without /api/, resulting in 404.

Ensure /api/ is present in the Connection URL you configure. 

### The Tableau REST version in the token is wrong.

Even with a version value, the endpoint must include /api/.

A missing /api/ produces the same 404 irrespective of the version number embedded in the call.

## Resolution

You will need to **add the /api/ to the connection URL** , which is also recommended by Tableau (see Related Links )

1.  Open the Connection & Credential record used by the Tableau Cloud integration profile.
2.  Set Connection URL to include the /api/ segment at the end for example:

`https://<server>.online.tableau.com/api/`

1.  Keep Content URL set to your Tableau site (contentUrl).
2.  Save and select Validate connection again.
3.  If validation fails, verify in your Outbound HTTP Logs (or traffic capture) that the request path is `/api/<version>/auth/signin`.

## Related Links

[Docs: Integrating with Tableau Cloud - ServiceNow Documentation](https://www.servicenow.com/docs/csh?topicname=integrate-with-tableau-cloud.html&version=latest "Integrating with Tableau Cloud")

[Tableau.com: Signing In and Signing Out (Authentication) - Tableau REST API Help Documentation](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_auth.htm)
