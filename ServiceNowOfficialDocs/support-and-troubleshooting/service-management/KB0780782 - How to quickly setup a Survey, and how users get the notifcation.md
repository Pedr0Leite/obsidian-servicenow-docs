---
title: "How to quickly setup a Survey, and how users get the notifcation"
aliases:
  - KB0780782
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780782
kb_number: KB0780782
last_modified: 2025-01-03
---

## How to quickly setup a Survey, and how users get the notifcation

  

### Summary

This article will answer the following

-   How to quickly setup a survey for user feedback
-   What are the major components to making surveys work (survey, trigger condition, notification)
-   use cases for public & private surveys

### Release

All

### Instructions

**Survey Setup**

-   We'll use the out-of-the-box survey (for learning how to create a survey you can find out more in the documentation)
-   navigate to "Survey > View Surveys" select "Helpdesk Satisfaction Survey"
-   notice how "send notification" is checked off, this will ensure that the notifications will send out an email for the user the survey instance is assigned to, the condition on the out-of-the-box notifications checks for this.

  
**Trigger Condition**  
  
Trigger conditions will define when a survey instance is created.

-   with our survey setup, we'll need to set up a trigger condition
-   navigate to "Survey > Administration > Trigger Condition"
-   click on New, in the new record form, select your survey in the assessment field
-   For our example set the table to \[incident\]
-   user field set to "caller," uncheck "trigger randomly"
-   repeat interval set this to 0 days, hours, minutes, seconds. Even after saving your trigger condition this will set back to 30 days, so make sure you change it again and save it.
-   add a condition where "state" changes to "resolve"

Our trigger condition is set to create an assessment instance, to the caller, when the state changes to resolve. When the trigger condition is saved, a business rule is created. Essentially it's a business rule that runs on the table we defined in the trigger condition. Note that it's best practice to create the condition when states "changes to" a different state, otherwise if "is" is used, every time the incident record is updated and state "is" resolve, the trigger condition will run, creating another assessment instance and sending off another email.

**Notification**

-   there is only one notification that is responsible for sending all emails for all surveys
-   the notification is "Survey User Invite"
-   metric type must be "survey," "assign to" must not be empty, send notification must be checked, "state" is "ready to take," or "assign to" changes

**Summary:**

Once the survey is created, you will need to create the trigger condition, this is responsible for creating the assessment instance based on certain conditions that are met on records for a particular table (incident, requested item, cases, etc). Once the assessment instance is created, the out-of-the-box notification "Survey User Invite" will be evaluated to see whether an email will be generated and sent out.

-   On a trigger condition, if you're using the state, make sure on the condition you select "changes to" otherwise any update will fire the trigger condition
-   Survey User Invite will only work for \[asmt\_metric\_type\] where evaluation method is survey
-   If your trigger condition is based on a table extending task, then the task number will be stored on the assessment instance that gets created, in the trigger id & task column
-   Setting a survey to public will allow anyone to take the survey without logging into the platform
-   for public survey a simple URL containing the sys id of the \[asmt\_metric\_type\] is created and can be sent to anyone
-   when users click on the URL, the assessment instance is created, created by guest
-   doing so will not relate the assessment instance to a task record
-   public survey URL can be obtained from the \[asmt\_metric\_type\] record, in the related links
-   you can also have public surveys and have trigger conditions create the assessment instance, and when the assessment instance get created the trigger id and task fields are populated, the use case here is that some users might not have login credentials, once they complete the survey, it would show as updated by guest.
-   Legacy Surveys are no longer supported starting in New York

### Related Links

[KB0763693 - Survey Management](https://docs.servicenow.com/csh?topicname=r_SurveyManagementLandingPage.html&version=latest)
