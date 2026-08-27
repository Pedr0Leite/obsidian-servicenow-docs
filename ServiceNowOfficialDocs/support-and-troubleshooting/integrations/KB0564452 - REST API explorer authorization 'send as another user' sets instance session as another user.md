---
title: "REST API explorer authorization 'send as another user' sets instance session as another user"
aliases:
  - KB0564452
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564452
kb_number: KB0564452
last_modified: 2024-01-28
---

## REST API explorer authorization 'send as another user' sets instance session as another user

  

### Issue

REST API Explorer authorization ‘send as another user’ sets instance session as another user

Objective

* * *

This article explains a current defect that affects session log in after running REST API Explorer. 

Versions affected

* * *

-   Fuji
-   Geneva

Procedure

* * *

Execute a REST call from the REST API Explorer page:

1.  Open Rest API explorer.
2.  Formulate JSON request.
3.  Select **Retrieve a record (GET)** (for example, from the table sys\_user).
4.  In **Authorization** (under **Request headers**), select **Send as another user**.
5.  Provide credentials for another user (for example, AbelTuter).
6.  Click **Send**.

 ![](/REST001.jpgx)

  

Problem

* * *

After running the REST call, the current user for that session changes to the user that executed the REST call (for example, Abel Tuter). However, this is not noticeable since the indicator at the top right of the page still shows the original user that originally logged in to the instance.

If you refresh the browser, for example by typing the URL of the instance on the same browser window, the user changes to the user who executed the REST call (for example, Abel Tuter).

 ![](/REST002.jpgx)

Resolution

* * *

This is the standard behavior and the issue is caused by a limitation in the cookie mechanism.

**Workaround**

Immediately after executing the REST call, use the **impersonate user** feature to login as the original user that initiated the session.

Related links

* * *

-   [REST API Explorer](https://docs.servicenow.com/)
