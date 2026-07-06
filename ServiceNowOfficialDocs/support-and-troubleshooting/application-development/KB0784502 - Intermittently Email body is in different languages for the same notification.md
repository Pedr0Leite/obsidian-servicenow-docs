---
title: "Intermittently Email body is in different languages for the same notification"
aliases:
  - KB0784502
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784502
kb_number: KB0784502
last_modified: 2024-04-26
---

## Intermittently Email body is in different languages for the same notification

  

### Issue

Intermittently Email body is in different languages for the same notification.

### Cause

This happens when mail scripts change the language of the content using the script include 'I18Utils' setLanguage() function

 but do not set it back to the original language.

### Resolution

Find all 'Notification Email scripts' that use the setLanguage() function from the script include 'I18Utils'.

You should see statements like the one below:

//language  
var lang = current.request.requested\_for.preferred\_language;  
  
//set language  
var util = new I18nUtils();  
util.setLanguage(lang);

Check the scripts and make sure that they also contain another setLanguage() statement to reset the language to the original.

//restores user's language  
util.setLanguage(g\_user.getUserID().preferred\_language);
