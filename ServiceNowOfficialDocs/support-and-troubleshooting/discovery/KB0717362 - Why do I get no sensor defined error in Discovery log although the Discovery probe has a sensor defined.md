---
title: "Why do I get \"no sensor defined\" error in Discovery log although the Discovery probe has a sensor defined?"
aliases:
  - KB0717362
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717362
kb_number: KB0717362
last_modified: 2024-04-07
---

## Why do I get "no sensor defined" error in Discovery log although the Discovery probe has a sensor defined?

  

### Issue

# Resolution

* * *

Although the probe has a sensor defined, the "no sensor defined" error message is seen when the multi probes are being triggered for a wrong phase.

For example, Linux - Identity comprises of the Linux - Hardware Information and Linux - Network probe. 

These probes are meant to be triggered in the identification phase. If these are added under Ci classification for UNIX server to be triggered under  exploration phase you will see this error message.

The solution is to ensure that the probes are triggered only once and in the correct phase they are intended to be triggered in. In the above example, ensure under the Ci classification, the probes are triggered only in identification phase.
