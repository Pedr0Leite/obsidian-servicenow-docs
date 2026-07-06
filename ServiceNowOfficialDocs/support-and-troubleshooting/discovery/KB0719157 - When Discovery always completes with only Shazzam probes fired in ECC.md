---
title: "When Discovery always completes with only Shazzam probes fired in ECC"
aliases:
  - KB0719157
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719157
kb_number: KB0719157
last_modified: 2024-04-07
---

## When Discovery always completes with only Shazzam probes fired in ECC

  

### Issue

New customers to Discovery might encounter a strange issue that from one day Discovery always completes with only 2 ECCs, one Shazzam Output and one Shazzam Input. No other ECC probes can be fired after Shazzam stage. But Discovery worked fine before that day and all the credential were configured properly.

  

### Release

All

### Resolution

In this case we may check the ECC output/input of Shazzam. If there is no actual ports being scanned by Shazzam, the according IP Services records (for ports) may have been deleted by mistake. The Discovery port probes may show sys\_ids instead of IP Service name as shown in attached screenshot.

  

We should then check the IP Services (cmdb\_ip\_service) table to verify if this is the issue. There should be 44 records in IP Service table on OOTB instance. Please see attached screenshots. The solution is to restore the default IP Services records by importing them from another OOTB instance.

  

  

![](sys_attachment.do?sys_id=d31ce82edb42b450e515c2230596191f)

  

  

  

  

![](sys_attachment.do?sys_id=d71ce82edb42b450e515c22305961924)
