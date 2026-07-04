---
title: "HR Onboarding Lifecycle Events are stuck (Pre-boarding will not trigger)"
aliases:
  - KB0814955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814955
kb_number: KB0814955
last_modified: 2024-04-08
---

## HR Onboarding Lifecycle Events are stuck (Pre-boarding will not trigger)

  

### Issue

With regard to the user's Onboarding process, their Pre-boarding is not triggering in many cases.

### Resolution

It was found that the user was utilizing an integration to handle this process. The root of why pre-boarding was not triggering is that the integration sys\_user record of the integration user did not have the necessary roles to process through all of the actions it needs to in order to progress cases/lifecycle events (it was missing the lifecycle admin and hr core admin roles).  
  
After a thorough period of testing, it was found that adding the correct roles to the integration user's sys\_user record resolved the issue.
