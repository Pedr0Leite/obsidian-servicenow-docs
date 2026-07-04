---
title: "How to set up integration in order to retrieve  custom fields from Jira Instance into ServiceNow Instance via GET Issue by ID"
aliases:
  - KB0815785
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815785
kb_number: KB0815785
last_modified: 2025-01-10
---

## How to set up integration in order to retrieve custom fields from Jira Instance into ServiceNow Instance via GET Issue by ID

  

### Issue

In [KB0815305](https://support.servicenow.com/kb_view.do?sysparm_article=KB0815305 "KB0815305") we created a custom field in Jira and you would like to have it retrieved by ServiceNow while running a "Get Issue by ID" Action.  
You will notice that following the regular "Get Issue by ID" process, your custom field exemplified in [KB0815305](https://support.servicenow.com/kb_view.do?sysparm_article=KB0815305 "KB0815305")will return your fields as following:

"customfield\_10057":"testingtesting" ,    instead of "Testingcustomfield":"testingtesting".

We see therefore that in response, Jira sends its own label instead of the one of created by ServiceNow.

This can be sometimes confusing and inconsistent behaviour.

### Release

London onwards

### Resolution

In order to workaround this behaviour, so that the field is mapped correctly, follow the below steps:

In the configuration screen click on "Open Action in Action Designer"

![](sys_attachment.do?sys_id=2c05e9b8db497410471f9c41ba961961)

Then expand "Get Issue by ID" action  and in the Query Parameters ad the following:

-   Name=expand
-   Value=names

![](sys_attachment.do?sys_id=2805e9b8db497410471f9c41ba961963)

Fill in the project name and Run the test.

![](sys_attachment.do?sys_id=2405e9b8db497410471f9c41ba961965)

Now you should see in the payload the below:

customfield\_10057":"Testingcustomfield" additional to "customfield\_10057":"testingtesting" 

This will help you map the fields in the response, and match the value with the label.

**Important note:**

**In order to be able to modify this action, you would need to create a copy of the action (as admin) and thereafter implement the above workaround on the newly copied action.**
