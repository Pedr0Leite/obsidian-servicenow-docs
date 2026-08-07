---
title: "Determining if the LDAP source is missing or misconfigured"
aliases:
  - KB0538740
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538740
kb_number: KB0538740
last_modified: 2024-05-01
---

## Determining if the LDAP source is missing or misconfigured

  

### Issue

Determining if the LDAP source is missing or misconfigured 

Problem

* * *

A single user is unable to log in.  

Symptoms

* * *

-   A single user is unable to log in.
-   Other users are able to log in, with the exception of a single user.

Cause

* * *

Each user record has a **Source** field that contains the distinguished name (DN) associated with the user. When LDAP authentication is enabled, the instance uses that field when the user attempts to log in. If this field is blank or contains incorrect information, it prevents the user from logging in.

Resolution

* * *

-   Review the affected user record.
-   If the **Source** field is not empty, verify with the LDAP administrator that the DN of the affected user is correct, and update if necessary.
-   If the **Source** field is empty, verify that the user record is not a local account, which requires both the **Source** and **LDAP Server** field to be left blank.
-   If the **Source** field is empty and **LDAP** server field is populated, update the **Source** field with the correct DN.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Review the <strong>Transform Map</strong> of the associated data source and the LDAP server to confirm that the <strong>Source</strong> field is set correctly.</td></tr></tbody></table>
