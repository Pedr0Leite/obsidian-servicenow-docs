---
title: "Incoming email body (html) and body text depends on the content type "
aliases:
  - KB0635957
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635957
kb_number: KB0635957
last_modified: 2026-05-04
---

## Incoming email body (html) and body text depends on the content type

  

### Issue

Some clients allow the creation of different HTML and text part on the emails or auto-generate the missing HTML or text part of the email when it is sent.

  
Symptoms:

When reviewing the sys\_email records, in some cases the HTML body when previewed contains different information than the body text field.

### Release

All releases

### Cause

Some clients allow the creation of different HTML and text part on the emails. When received, incoming emails are treated differently depending on the content type.  
  
Given the HTML content, most clients will automatically create a text version. In that case, each HTML and text version is extracted from the incoming email and there is no need to generate either content. However, if the HTML content exists and the text version is not available, it is generated automatically. Similarly, if only the text content exists and the HTML version is not available, it is generated automatically. 

<table class="MsoNormalTable" style="width: 776px; background: whitesmoke; border: 1pt solid #e0e0e0; height: 204px;" border="1" cellpadding="0"><tbody><tr style="height: 15.0pt;"><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; padding: 6pt; width: 117.281px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Incoming email content type</span></strong></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Email body_html</span></strong></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Email body_text</span></strong></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; padding: 6pt; width: 251.931px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Reason</span></strong></p></td></tr><tr style="height: 15.0pt;"><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 117.281px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">text/plain</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: maroon;">Generated</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Extracted from email if available</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 251.931px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Because the HTML text is not available, it is generated based on the body_text</span></p></td></tr><tr style="height: 15.0pt;"><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 117.281px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">text/html</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Extracted from email if available</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: maroon;">Generated</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 251.931px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Because the TEXT version is not available, it is generated by stripping the HTML tags</span></p></td></tr><tr style="height: 15.0pt;"><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 117.281px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Multipart</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Extracted from email if available or&nbsp;</span><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: maroon;">generated</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 159.738px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">Extracted from email if available or&nbsp;</span><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: maroon;">generated</span></p></td><td style="border-style: dashed solid solid dashed; border-color: #e0e0e0; border-width: 1pt; background: white; padding: 6pt; width: 251.931px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.5pt; font-family: Verdana, sans-serif; color: black;">The available types text/plain or text/html are extracted on the multipart section</span></p></td></tr></tbody></table>

![content type on the email](sys_attachment.do?sys_id=49309a6d4793aa102c31b98a436d4349 "content type on the email")

### Resolution

If either the body text or body (HTML) in the email do not match, validate the email content type to understand the source of the differences. If the text was auto-generated, the source is on the necessary conversion. However, if the incoming emails is multipart, validate whether the client sending the emails is causing the differences because the information is extracted on the email itself.  

If you depend on the email body (HTML), ensure that clients are sending the **text/html** content correctly. If you depend on the body text, ensure that clients are sending the text/plain content on the emails.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Validate whether the differences come from automatic systems integrating by email.</td></tr></tbody></table>
