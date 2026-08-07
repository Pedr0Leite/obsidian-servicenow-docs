---
title: "Images aren't displaying in survey"
aliases:
  - KB0715925
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715925
kb_number: KB0715925
last_modified: 2024-04-07
---

## Images aren't displaying in survey

  

### Issue

# Symptoms

* * *

-   Some images were not displaying within surveys (a gradient image to visually show the scale of \[1\] very dissatisfied \[red color\] to \[5\] very satisfied \[dark green color\])

# Release

* * *

Jakarta Patch 9c

# Cause

* * *

The user who received the survey does not have access to the sys\_attachment table (further explanation below)

# Resolution

* * *

The user who created the survey was utilizing an unsupported method of adding images to a survey (dropping them directly into the details section of a question).   
  
It was recommended to the creator of the survey to utilize the supported method, and to do so by separating their gradient image into color blocks via Image Scale and adding Image Choices. An example solution was provided: use a solid color block for each of the following choices: (1) Very dissatisfied (Red), (2) Dissatisfied (Orange), (3) Good (Yellow), (4) Satisfied (Lime Green), (5) Very satisfied (Hunter or Forest Green).

  
Some helpful documentation was also offered regarding Image Scale / Image Choices:   
  

-   [https://docs.servicenow.com/csh?topicname=r\_SurveyQuestionDataTypes.html&version=latest](https://docs.servicenow.com/csh?topicname=r_SurveyQuestionDataTypes.html&version=latest)
-   [https://docs.servicenow.com/csh?topicname=t\_CreateAMetricTemplate.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CreateAMetricTemplate.html&version=latest)
-   [https://docs.servicenow.com/csh?topicname=c\_SurveyDesignerElements.html&version=latest](https://docs.servicenow.com/csh?topicname=c_SurveyDesignerElements.html&version=latest) (Survey Designer Elements - including Image Scale)
