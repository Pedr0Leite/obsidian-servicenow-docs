---
title: Implement a nonce
description: You can implement a nonce to be used with single sign-on digest authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/c\_ImplementingANonce.html
release: australia
product: Authentication
classification: authentication
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Local authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-concept
---

# Implement a nonce

You can [[c_Implementation|implement a nonce]] to be used with single sign-on digest [[c_Authentication|authentication]].

To use a nonce with the unencrypted token or encrypted token methods of single sign on, these steps apply with only a few minor changes.

**Note:** The nonce is used only for login requests, not for any other type of [[c_requestAPI|request]]. If the system receives a nonce value after login, the nonce is not consumed.

## Benefits

The usage of a nonce prohibits a malicious user from performing a replay attack in order to log into your system.

## Related

- [[c_Implementation|Implement a nonce]]
- [[c_Authentication|Authentication]]
- [[c_requestAPI|request]]
