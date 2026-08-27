---
title: " How to configure custom URLs "
aliases:
  - KB0792321
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792321
kb_number: KB0792321
last_modified: 2025-11-06
---

## How to configure custom URLs

  

### Issue

This article shows how to configure custom URLs 

### Release

All

### Cause

### Resolution

It is \*\*not\*\* recommended for end users to use both the new custom URL and the original Servicenow instance URL because only one instance URL can be set at a time for URL link generation.

Custom URL configuration overview:

-   1\. Purchase a custom URL from a domain provider.  
            A certificate from LetsEncrypt is automatically used for custom URL configuration.
-   2\. In ServiceNow, activate custom URL plugin
-   3\. Add a Custom URL record by filling in Domain name(your custom URL) and choose a service portal url to redirect users to when they access instance using custom url.
-   4\. Submit. ServiceNow takes up to 6 hours to complete custom URL creation.
-   5\. The instance administrators receive an email when custom URL is "Active".
-   6\. Once the URL is "Active", set it as instance URL by clicking the "Set instance URL" button.

This will result in the custom url being used for all outbound urls.  
\- glide.servlet.uri updated for ${URI} and ${URI\_REF}.  
\- glide.email.override.url

Please note that only one instance URL can be set at a time for URL link generation.

### Related Links

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0820070](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820070)
