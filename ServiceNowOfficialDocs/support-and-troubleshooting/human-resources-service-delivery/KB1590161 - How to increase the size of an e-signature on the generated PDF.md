---
title: "How to increase the size of an e-signature on the generated PDF"
aliases:
  - KB1590161
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1590161
kb_number: KB1590161
last_modified: 2025-09-03
---

## How to increase the size of an e-signature on the generated PDF

  

### Summary

Sometimes you might find e-signature on the PDF template is too small. It is possible to adjust the size of the e-signature by following the below Instructions.

### Instructions

The signature size on the generated PDF can be increased by updating the OOB script include GeneralHRForm.\_get\_signature() method.

/sys\_script\_include.do?sys\_id=3a5370019f22120047a2d126c42e7000

![](/sys_attachment.do?sys_id=cef2cef947ccca1011eaf24c736d43e1)

From above screenshot, the signature size can be adjusted by changing both "height" and "width" at lines 474 (useItext7 == true) or 479 (else).

The value of "useItext7" can be determined from System property: sn\_hr\_core.itext7.pdf\_conversion

/sys\_properties.do?sys\_id=11d9c0a40f1900105754c8337a767eb9
