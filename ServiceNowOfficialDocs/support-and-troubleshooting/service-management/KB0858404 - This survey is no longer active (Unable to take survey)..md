---
title: "This survey is no longer active (Unable to take survey)."
aliases:
  - KB0858404
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858404
kb_number: KB0858404
last_modified: 2024-04-08
---

## This survey is no longer active (Unable to take survey).

  

### Issue

The assigned user is unable to take the survey.

**Steps To Replicate:**

1\. Impersonate user 'xyz' to whom the survey is assigned to (check the assessment instance to know the assigned\_to user).

2\. Access the url to take the survey, mentioned in the email notification sent to the assigned\_to user when trigger conditions are met.

Actual Behavior: Error is shown " This survey is no longer active ".

Expected Behavior: Survey page should open and user should be able to take the survey.

Note- The due date is in future.

  

![](sys_attachment.do?sys_id=70fab445db04f4d04cfbeeb5ca96195d)

### Release

ALL

### Cause

The survey definition is inactive.

### Resolution

Set the survey definition to active, this resolves the issue.

https://instance\_name.service-now.com/asmt\_metric\_type.do?sys\_id=\*\*\*

### Related Links

Tested in OOB-

After the assessment is created set the survey definition to inactive, user will not be able to take the survey. 

FYR:

[Survey definitions](https://docs.servicenow.com/csh?topicname=c_SurveyDefinitions.html&version=latest "Survey definitions")

[Get started with Survey Management](https://docs.servicenow.com/csh?topicname=c_SurveyManagement.html&version=latest "Get started with Survey Management")
