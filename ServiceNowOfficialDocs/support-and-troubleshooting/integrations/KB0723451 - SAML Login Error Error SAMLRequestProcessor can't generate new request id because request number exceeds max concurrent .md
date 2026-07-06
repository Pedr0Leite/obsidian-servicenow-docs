---
title: "SAML Login Error: Error SAMLRequestProcessor: can't generate new request id because request number exceeds max concurrent request size:5 in 5000 milliseconds: no thrown error com.glide.ui.ServletErrorListener"
aliases:
  - KB0723451
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723451
kb_number: KB0723451
last_modified: 2025-02-01
---

## SAML Login Error: Error SAMLRequestProcessor: can't generate new request id because request number exceeds max concurrent request size:5 in 5000 milliseconds: no thrown error com.glide.ui.ServletErrorListener

  

### Issue

# Symptoms

* * *

SAML SSO logins fail, the following is seen in the node logs:

Error SAMLRequestProcessor: can't generate new request id because request number exceeds max concurrent request size:5 in 5000 milliseconds: no thrown error com.glide.ui.ServletErrorListener

# Release

* * *

Starting in London

# Cause

* * *

If the logging in user refreshes the login page several times it may cause this error.

Usually this happens when there is a loop for login or DDOS attack (same session sends multiple requests). Or multiple tabs are open for the login at the same time.

This limit is in place intentionally, for the same session, there is a rate limit for SAML Requests. If the SAML login requests exceed the max number within certain time it will disable the SAML request and the error will be seen.

# Resolution

* * *

There are two system properties used to set these limits:

glide.authenticate.sso.saml2.request.interval in millseconds, the default is 5000 which means 5 seconds.  
glide.authenticate.sso.saml2.max.request, the default is 5. Max allowed 5 requests for every 5 seconds (glide.authenticate.sso.saml2.request.interval)

We don't set the upper limit for these two properties.

Customers can create/change the mentioned system properties as follows if they want to allow a greater threshold for login attempts per second for a session:

glide.authenticate.sso.saml2.request.interval = 1000  
and  
glide.authenticate.sso.saml2.max.request = 50

With these settings, this means we allow 50 requests per second instead of the default of 5 request per 5 seconds.
