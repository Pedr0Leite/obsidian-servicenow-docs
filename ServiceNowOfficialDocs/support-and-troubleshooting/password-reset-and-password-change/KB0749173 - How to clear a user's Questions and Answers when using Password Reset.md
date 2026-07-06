---
title: "How to clear a user's Questions and Answers when using Password Reset "
aliases:
  - KB0749173
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749173
kb_number: KB0749173
last_modified: 2024-04-07
---

## How to clear a user's Questions and Answers when using Password Reset

  

### Issue

# Symptoms

When trying to clear a user's password reset questions you might come across an error after deleting the user's associated pwd\_active\_answer records.

"The number of questions required for enrollment has changed. Enroll again."

![](sys_attachment.do?sys_id=7679a022db42b450e515c2230596198e)

# Release

All

# Resolution

If you want to completely clean up, as if the user never enrolled, we suggest clearing the records in the following tables for that specific user.   
  
pwd\_enrollment   
pwd\_active\_answer   
pwd\_enrollment\_snapshot user's associated "pwd\_enrollment" records.
