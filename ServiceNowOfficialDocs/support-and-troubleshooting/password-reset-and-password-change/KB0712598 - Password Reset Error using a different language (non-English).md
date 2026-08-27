---
title: "Password Reset Error using a different language (non-English)"
aliases:
  - KB0712598
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712598
kb_number: KB0712598
last_modified: 2025-04-10
---

## Issue

When you have users doing password reset in a language other than English (usually Spanish or Portuguese) and they get past the verification step an error is thrown on the screen like:

"The entity "\[some\_text\_here\]" was referenced, but not declared"

i.e. The entity "iacute" was referenced, but not declared

## Resolution

1.  Go to the sys\_translated\_text table.
2.  Find the record for the translation of you password credential store table where the hint is translated.
3.  Look at the HTML text in that record 
4.  Remove any text that is not in plain text (where accents to characters are placed, you will see the issue)

Alternatively, 

You could upload an image with your password reset hints on the image. This way there is no text to translate. 

Example:

You may see something like this in that translated text:

\- <li style="margin: 0cm 0cm 6pt 18pt; font-size: 10pt; font-family: 'Courier New'; color: #222222; text-indent: 0cm; text-align: justify;">Deve conter Letras Mai&uacute;sculas e Minuacute;sculas.</li>

The word "Mai&uacute;sculas" will have an issue. So that "&" should be removed or modified.
