---
title: "Scheduled Job Failing with Error - User Not Authenticated. OAuth token has expired or has not been retrieved."
aliases:
  - KB0753730
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753730
kb_number: KB0753730
last_modified: 2023-10-21
---

## Issue

-   2019-07-07 15:36:49 (991) worker.6 worker.6 txid=xxxxxxxxx <sys\_Id> can't read table oauth\_credential
-   Scheduled job is failing with the above error. 
-   The scheduled job should be downloading the OAuth certificate, but is not

## Resolution

  

-   Check the ACL for the oauth\_credential table for read and write as the scheduled job will read and update the table..
-   Match the roles to the user running the scheduled job.
