---
title: "Firefox: Your connection is not secure."
aliases:
  - KB0714734
tags:
  - servicenow
  - support-kb
  - ssl
  - certificate
  - browser
  - firefox
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714734
kb_number: KB0714734
last_modified: 2024-04-16
---

## Firefox: Your connection is not secure.

  

### Issue

# Symptoms

* * *

Firefox displays "Your connection is not secure" message when trying to access the instance

![](sys_attachment.do?sys_id=1fa8a82edb02b450e515c22305961940)

# Release

* * *

Any

# Environment

* * *

Firefox

# Cause

* * *

On websites which are supposed to be secure (the URL begins with "https://"), Firefox must verify that the certificate presented by the website is valid. If the certificate cannot be validated, Firefox will stop the connection to the website and show a "Your connection is not secure" error page instead.

# Resolution

* * *

Refer to the link the in additional information for resolution.

# Additional Information

* * *

Visit for more information:

[https://support.mozilla.org/en-US/kb/error-codes-secure-websites](https://support.mozilla.org/en-US/kb/error-codes-secure-websites)

## Related

- [[KB0816002 - How to obtain SSL certificate from the browser]]
- [[KB0788812 - SSL certificate of the instance for third party integration]]
- [[KB0744261 - Troubleshooting MID server SSL issues]]
