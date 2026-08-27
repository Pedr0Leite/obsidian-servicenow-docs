---
title: "SOAP traffic sending a large header to the instance generates HTTP 400 and a possible error message \"An existing connection was forcibly closed by the remote host\" "
aliases:
  - KB0623293
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623293
kb_number: KB0623293
last_modified: 2024-04-07
---

## SOAP traffic sending a large header to the instance generates HTTP 400 and a possible error message "An existing connection was forcibly closed by the remote host"

  

### Issue

SOAP traffic sending a large header to the instance generates HTTP 400 and a possible error message "An existing connection was forcibly closed by the remote host"  

Problem

* * *

SOAP traffic to the instance generates HTTP 400 and it may generate an error message "An existing connection was forcibly closed by the remote host".

If a SOAP client need to send a large message, the message gets split into multiple packages. The instance will return errors if there is no session on the headers (persisting HTTP sessions) or an authorization header.

For more information on persistence HTTP, see the product documentation topic [Persisting an HTTP session across all SOAP calls](https://docs.servicenow.com/csh?topicname=persist-session-all-soap-calls.html&version=latest "Persisting an HTTP session across all SOAP calls").

Symptoms

* * *

SOAP messages to the instance will receive a HTTP 400 response from the server. Reviewing the SOAP message sent, the header will be either very large or does not contain the JSESSIONID cookie.

Cause

* * *

Missing or incorrectly implementing a persisting HTTP sessions (for example, just appending the cookies) can cause the header to grow and cause an HTTP 400 error if the JSESSION is not added or the header is too big.

Resolution

* * *

Get the JSESSIONID from the cookies, then reuse that JSESSIONID in subsequent calls. Only JSESSIONID is required to achieve session reuse. There is no need to include other cookies like glide\_session\_store, so there is no need to append the other cookie information.

![Cookies to add](sys_attachment.do?sys_id=703920eedb02b450e515c22305961937 "Cookies to add")
