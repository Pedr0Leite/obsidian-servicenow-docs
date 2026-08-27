---
title: "Embedded Video and PPT not showing in Knowledge article."
aliases:
  - KB0812448
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812448
kb_number: KB0812448
last_modified: 2025-09-03
---

## Issue

Embedded Video and PPT will show you in the Knowledge article when you attach it however clicking on show preview it will not show you any attachments.

  

## Resolution

System Definition -> Dictionary  
Table = kb\_knowledge, Field = text  
Click the advanced view link  
Set Attributes = serializer= com.glide.script.TranslatedTextXMLSerializer  
  
If still you are seeing the issue Please change the attribute to  
Set Attributes = serializer= com.glide.script.TranslatedTextXMLSerializer,html\_sanitize=false
