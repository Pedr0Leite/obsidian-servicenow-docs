---
title: "Determining if the wrong LDAP server is configured"
aliases:
  - KB0538726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538726
kb_number: KB0538726
last_modified: 2024-05-01
---

## Determining if the wrong LDAP server is configured

  

### Issue

Determining if the wrong LDAP server is configured 

Problem

* * *

A single user is unable to log in.  

Symptoms

* * *

-   A single user is unable to log in.
-   Other users are able to access the instance, with the exception of the affected user.

Cause

* * *

If the instance has multiple LDAP servers configured, the user accounts should be associated to the correct LDAP server. If the value of the **LDAP Server** field has changed or cleared, the instance is not able to authenticate the user correctly.  

  
Resolution

* * *

1.  Review the affected user record.
2.  If the **LDAP Server** field is not displayed, right-click the header, and go to **Personalize > Form Layout** and add the **LDAP Server** field.
3.  Click **Save**.
4.  Select the correct LDAP server for the user.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><p><strong>Note</strong>: It may be necessary to review the associated <strong>Transform Map</strong> to ensure that the line of code is in the <strong>Script</strong> field of the LDAP server:</p><p><span style="font-family: 'courier new', courier;">target.ldap_server = source.sys_import_set.data_source.ldap_target.server;</span></p></td></tr></tbody></table>
