---
title: "Taking a survey in Service Portal displays a blank screen"
aliases:
  - KB0747451
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747451
kb_number: KB0747451
last_modified: 2025-06-20
---

## Taking a survey in Service Portal displays a blank screen

  

### Issue

When selecting a survey to take, a blank screen appears instead of the survey, but the survey is visible in the **assesment\_take2** page.

### Release

Beginning with the London release

### Cause

It is probable that customization of the script include, SPSurveyAPI, caused the issue. 

### Resolution

The widget, Take Survey, is based on the **one\_click\_survey** value (data.one\_click\_survey) and the **state** value (c.state) defined in the widget's client controller. These settings determine which pages should be displayed.

The SPSurveyAPI script include is used to populate the **one\_click\_survey** value in the widget. If you customized the SPSurveyAPI script include, the London release upgrade bypasses it, resulting in the widgets not receiving the one-click survey information. 

To resolve the issue, apply the London upgrades to the script include, and then reapply the customizations, if needed.
