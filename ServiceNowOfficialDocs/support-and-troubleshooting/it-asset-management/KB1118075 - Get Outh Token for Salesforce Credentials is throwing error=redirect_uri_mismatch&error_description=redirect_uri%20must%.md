---
title: "Get Outh Token for Salesforce Credentials is throwing error=redirect_uri_mismatch&error_description=redirect_uri%20must%20match%20configuration"
aliases:
  - KB1118075
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1118075
kb_number: KB1118075
last_modified: 2026-03-27
---

## Issue

1) Navigate to "Salesforce credentials"  
2) Click on the "Get OAuth Token" related link  
3) We will get a popup page with the below error

```
error=redirect_uri_mismatch&error_description=redirect_uri%20must%20match%20configuration.
```

  
  

## Resolution

The callback URL (Redirect URL) you have in this record, 'https:/<instance>.service-now.com/oauth\_redirect.do', should be the same as on the Salesforce side. They might be pointing it toward different instances.

Please work with the Salesforce Admin team.
