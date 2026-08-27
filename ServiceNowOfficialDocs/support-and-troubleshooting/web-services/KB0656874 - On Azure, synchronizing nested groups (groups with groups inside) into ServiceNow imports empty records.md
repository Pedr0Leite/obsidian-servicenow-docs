---
title: "On Azure, synchronizing nested groups (groups with groups inside) into ServiceNow imports empty records"
aliases:
  - KB0656874
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656874
kb_number: KB0656874
last_modified: 2024-04-07
---

## On Azure, synchronizing nested groups (groups with groups inside) into ServiceNow imports empty records

  

### Issue

On Azure, synchronizing nested groups (groups with groups inside) into ServiceNow imports empty records

Problem

* * *

Azure allows you to create groups with groups are group members (nested). However, on ServiceNow, the system only allows you to add Users on the group form. When synchronizing nested groups with ServiceNow, Azure creates empty records on the instance group form.  
  
Symptoms

* * *

You recognize this problem because:  

-   You have Azure setup with groups with groups as members (beside users)
-   You have setup a synchronization with a ServiceNow instance
-   You will see empty user records being created on the parent group

Cause

* * *

The problem is caused because ServiceNow group form does not allow nested groups, or groups inside groups. Group members can only be Users. On Azure, the Groups allow both groups and users. However, Azure does not differentiate or add the members of the nested groups, instead it try to create them as members.  
  
Resolution

* * *

Please note Azure is not a ServiceNow product. For specific questions on the synchronization process, please contact Microsoft support.  
  
To resolve this problem, please ensure on Azure to that any Group added to the synchronization, does not have any groups inside any other group, or nested. Instead, add the member of those nested groups into the parent group.  

To accomplish this:

1.  Copy all the users members of the nested group into the parent.
2.  Remove the nested group from the group
3.  Repeat as many times as nested groups present.

  

<table class="noteTable" align="left"><tbody><tr><td class="c3" style="width: 50; vertical-align: middle; text-align: center;"><img class="c2" style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4" style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Azure is not a ServiceNow product. For specific questions on the synchronization process, please contact Microsoft support.</td></tr></tbody></table>
