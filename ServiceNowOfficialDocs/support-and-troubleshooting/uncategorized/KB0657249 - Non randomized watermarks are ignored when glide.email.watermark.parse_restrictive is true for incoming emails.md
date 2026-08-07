---
title: "Non randomized watermarks are ignored when glide.email.watermark.parse_restrictive is true for incoming emails"
aliases:
  - KB0657249
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657249
kb_number: KB0657249
last_modified: 2024-01-31
---

## Non randomized watermarks are ignored when glide.email.watermark.parse\_restrictive is true for incoming emails

  

### Issue

Incoming email messages watermark are ignored if glide.email.watermark.parse\_restrictive is true for incoming emails, and the watermarks are missing the randomize <watermark>\_xxxxx part.

![](sys_attachment.do?sys_id=f698e04297c4025068d477121153afc9)

You can recognize this problem because

-   You have recently upgraded to an instance version that supports randomized watermarks
-   You have activated the Random Watermark Support plugin.
-   The sys\_properties record glide.email.watermark.parse\_restrictive value is true
-   The emails watermarks are not recognized, and they look like Ref:MSG0000001 (instead of Ref:MSG000001\_asdrewtwer)

### Cause

When the Random Watermark Support plugin is active and enabled, the watermark format changes to add a 20 character random string to the watermarks, to make them unique.

Note: glide.email.watermark.parse\_restrictive is not related to the target record or match with watermark table. The watermark coming from inbound email and the one present in sys\_watermark record should be the same in order to recognize the target record.

### Resolution

Determine a watermark transition period during which the system must recognize both randomized and non-randomized watermarks. This transition period is the time needed for the system to process incoming email replies containing non-randomized watermarks.

During this time, set **glide.email.watermark.parse\_restrictive** to **false** 

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: With sys_properties record glide.email.watermark.parse_restrictive value of false, the system would recognize both randomized and non-randomized watermarks</td></tr></tbody></table>

### Related Links

[https://docs.servicenow.com/csh?topicname=c\_WorkingWithWatermarks.html&version=latest](https://docs.servicenow.com/csh?topicname=c_WorkingWithWatermarks.html&version=latest)
