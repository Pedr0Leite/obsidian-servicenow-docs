---
title: "Location of the CIs discovered from SCCM is empty"
aliases:
  - KB0754207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754207
kb_number: KB0754207
last_modified: 2024-04-07
---

## Location of the CIs discovered from SCCM is empty

  

### Issue

# Symptoms

Location Field on some CIs imported from SCCM is empty

# Release

Issue occurs irrespective of version being used

# Cause

When CI records from SCCM are imported on import set table, it populates the data in u\_username field of on import set table.

Transform Map - SCCM 2012 v2 Computer Identity is responsible for populating the computer CIs from Import Set table to target table - cmdb\_ci\_computer. 

The Transform Map holds a script to validate data in u\_username field with data on sys\_user table and the sys id of correct record on sys\_user table is added in assigned\_to field on the target table.

Location of user who is selected in assgined\_to field is populated in location field on target table - cmdb\_ci\_computer.

In Case if u\_username in import set table field doesn't have value, system doesn't populate value in assigned\_to and location field on target table.

Below is the script used - 

```
function setAssignedTo() {    var userName = source.u_username;    if (JSUtil.nil(userName))        return;    var x = userName.indexOf("\\");    if (x > -1)        userName = userName.substring(x + 1);    var nameField = gs.getProperty('glide.discovery.assigned_user_match_field', "user_name");    var userSysID = GlideUser.getSysId(nameField, userName);    target.assigned_to = userSysID;    var gr = new GlideRecord('sys_user');    gr.addQuery('sys_id',userSysID);    gr.query();    if(gr.next()){    target.location = gr.location.getUniqueValue();    target.department = gr.department.getUniqueValue();    }}
```

# Resolution

This is a data issue in SCCM. Ask customer to correct data in SCCM so that it pushes correct value in u\_username column on import set table.
