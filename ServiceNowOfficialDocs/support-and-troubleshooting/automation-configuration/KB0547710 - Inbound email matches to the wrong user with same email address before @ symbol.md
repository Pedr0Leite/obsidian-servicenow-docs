---
title: "Inbound email matches to the wrong user with same email address before @ symbol "
aliases:
  - KB0547710
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547710
kb_number: KB0547710
last_modified: 2024-04-30
---

## Inbound email matches to the wrong user with same email address before @ symbol

  

### Issue

Inbound email matches to the wrong user with same email address before @ symbol 

Problem

* * *

Two separate users have the same email address before the @ symbol. One is active, the other is inactive. When sending an email to the ServiceNow instance to create a new record from the active user, all inbound actions are skipped due to an incorrect match on the inactive user.  

For example:

User Johnfoo: jfoo@google.com

User Jamesfoo: jfoo@yahoo.com 

Symptoms

* * *

When the email from the active user is sent to the ServiceNow instance, the system only compares the first part of the email before the @ symbol. This causes the system to pick up the first user it finds in the system, which happens to be the inactive one. This new record is not created and all inbound actions skipped.

Cause

* * *

The "Email Automatic User Creation" plugin is inactive. The plugin makes the change, which increases the width of the User ID \[sys\_user.user\_name\] column to accommodate email addresses so that users are correctly matched by **full** email addresses. Without activating this plugin, the system only compares the first part of the email before the @ symbol.  
  
  

  
Resolution

* * *

Activate the [Email Automatic User Creation plugin](https://docs.servicenow.com/csh?topicname=t_EnablingAutomaticUserCreation.html&version=latest "Email Automatic User Creation plugin") to match the email to the existing user by the **full** email address.  
  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: ServiceNow strongly recommends reviewing your existing user records to reconcile any that contain identical email addresses. If you activate the plugin prior to reconciling email addresses, your instance cannot distinguish between users with identical email addresses and randomly selects one of the users with the matching email address.</td></tr></tbody></table>

Activating this plugin and _not_ enabling user creation through email fixes the user matching function. However, it does not automatically create users from incoming emails. Refer to the link below on how to enable/disable automatic user creation: 

[https://docs.servicenow.com/csh?topicname=t\_EnablingAutomaticUserCreation.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EnablingAutomaticUserCreation.html&version=latest)
