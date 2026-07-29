---
title: "How to change the email watermark prefix from MSG"
aliases:
  - KB0761142
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761142
kb_number: KB0761142
last_modified: 2025-06-20
---

## How to change the email watermark prefix from MSG

  

### Summary

To change the default email watermark prefix from MSG to something specific to your company or instance, follow the steps in this article. 

### Instructions

#### Change the Prefix

1.  From the filter navigator, go to the sys\_number table.
2.  Find the record for **Table='Email Watermark'**. The Prefix column should show MSG by default. 
3.  Update the **Prefix** column with the new prefix you want. 
4.  **Save** the record.

#### Enable both old and new prefixes during the transition

During the transition from the old prefix to the new one, you may still receive emails that are replies to emails with the old prefix. For these emails to also be processed, set the following system property. 

<table style="border-collapse: collapse; width: 71.3514%; height: 38px;" border="1"><tbody><tr style="height: 13px;"><td style="width: 19.0594%; height: 13px;">&nbsp;Name</td><td style="width: 6.09814%; height: 13px;">&nbsp;Type</td><td style="width: 5.46804%; height: 13px;">Value&nbsp;</td><td style="width: 69.3745%; height: 13px;">Description&nbsp;</td></tr><tr style="height: 13px;"><td style="width: 19.0594%; height: 13px;">glide.email.prior_watermark_prefix</td><td style="width: 6.09814%; height: 13px;">&nbsp;String</td><td style="width: 5.46804%; height: 13px;">MSG&nbsp;</td><td style="width: 69.3745%; height: 13px;">Previous watermark prefix that is still processed in addition to the current prefix set in sys_number table. Clear this field once the transition is complete.</td></tr></tbody></table>
