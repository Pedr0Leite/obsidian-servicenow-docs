---
title: "How to enable SSL debug on the mid server to troubleshoot any issues with SSL connections?"
aliases:
  - KB0717261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717261
kb_number: KB0717261
last_modified: 2026-03-26
---

## How to enable SSL debug on the mid server to troubleshoot any issues with SSL connections?

  

### Issue

How to enable SSL to debug on the mid server to troubleshoot any issues with SSL connections and their TLS Certificates?

### Release

Any

### Resolution

-   Log into the mid server and stop the Mid server service
-   Temporarily edit the .\\agent\\conf\\wrapper-override.conf file and add the following line  
    wrapper.java.additional.500=-Djavax.net.debug=ssl:handshake
-   After saving, Restart the mid server
-   All the SSL handshake logs will be captured in the agent\\logs\\wrapper.log of the mid server.

### Related Links

[KB2912316 Interpreting java ssl/hardshake debug in wrapper.log to resolve MID Server Certificate Check failures](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2912316)
