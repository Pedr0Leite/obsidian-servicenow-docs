---
title: "Discovery HTTPClassiProbe error \"response length is larger than 4000 characters\""
aliases:
  - KB0785209
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785209
kb_number: KB0785209
last_modified: 2024-04-08
---

## Discovery HTTPClassiProbe error "response length is larger than 4000 characters"

  

### Issue

Discovery HTTPClassiProbe error "response length is larger than 4000 characters".

### Release

Pre NewYork environments.

### Cause

Pre NewYork release, the HTTPClassyProbe result will be replaced by "response length is larger than 4000 characters" if the response is larger than 4000 characters.

This behavior is changed in NewYork release. Starting in NewYork, the response is truncated to keep the first 4000 characters. Thus the HTTPClassiProbe classification can complete successfully.

### Resolution

1.  Upgrade to NewYork

OR

1.  Use another "path" which returns a smaller response.  
    2\. Possibly use a path which may take a header value which will assist in having a smaller response.

### Related Links

[https://docs.servicenow.com/csh?topicname=create-an-http-classifier.html&version=latest](https://docs.servicenow.com/csh?topicname=create-an-http-classifier.html&version=latest)
