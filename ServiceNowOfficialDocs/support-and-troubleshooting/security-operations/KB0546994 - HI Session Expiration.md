---
title: "HI Session Expiration"
aliases:
  - KB0546994
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546994
kb_number: KB0546994
last_modified: 2025-04-10
---

## Issue

HI session expiration 

  

Overview

* * *

HI session expiration will vary for _some_ users:

-   For non-federal ServiceNow customers and ServiceNow employees that do not have the federal role, HI sessions will expire after 4 hours of inactivity
-   Session expiration will continue to occur after 15 minutes for all ServiceNow federal customers and ServiceNow employees with the federal role

When a session expires, users are required to log back in to continue.  

  

Before a session expires, a pop-up window appears enabling the user to extend their session. The pop-up window only appears on form views tied to tables; it does not appear on list view, homepages, reports, etc.

  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>:&nbsp;Any unsaved work is lost and not recoverable when your session expires.</td></tr></tbody></table>

  

Some examples of activity are: 

-   Loading the case form
-   Any activity that hits the database, such as updating or saving data
-   Going to the homepage
-   Moving from field-to-field may constitute as activity depending on the field (for example, if you try to view information on a reference field)

  

Why are we doing this?

* * *

ServiceNow is continuously improving its overall security posture, including the interaction our employees and customers have with our systems. Session expiration is intended to log a user out of HI to prevent unauthorized system use.

If you have forgotten your password, please see [resetting your HI password](/kb_view.do?sysparm_article=KB0547255 "resetting your HI password").

## Resolution
