---
title: "Engagement Messenger does not honor the system default language"
aliases:
  - KB0964071
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964071
kb_number: KB0964071
last_modified: 2024-05-12
---

## Engagement Messenger does not honor the system default language

  

### Issue

Customer has configured Engagement Messenger. The default language of the instance is set to German - Engagement Messenger is only loading in English, not in German for the user.  

### Release

Quebec

### Cause

Store App localisation for Engagement Messenger is planned for Rome version.

### Resolution

Update from i18n channel.

Currently, our official mechanism to support Store app localization is through the TrueUp process and if an app is included as part of the TrueUp process, it will be included within the translation efforts for that family release (and translations will be packaged within the family release language plugins).  
So to answer the question, they get translated in the release in which they are Trued up. Translation is approximately 4M words (including these apps), so translations do not get merged until later in the family release process.  
We also have been adding support for a growing number of apps (approximately 50 at time of writing), whereby we package and deploy translations directly within the apps themselves as part of the fortnightly, monthly or quarterly Store release. There are specific requirements of apps/app teams to join this program (specifically around being i18n-ready, committing to a UI freeze in advance of the store release) doing some maven integration etc. We hope to expand this program over the coming months, as we are currently developing tooling to provide greater scalability.  
  
Localisation will be provided from Rome for Engagement Messenger as it was trued up in Rome.
