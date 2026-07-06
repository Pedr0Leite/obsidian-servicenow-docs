---
title: "Find Groups Without Members"
aliases:
  - Find Groups Without Members
tags:
  - servicenow-dev-program
  - code-snippet
  - find-groups-without-members
  - background-scripts
---

**Initialize an Array:**
var myGroups = [];

**Create a GlideRecord Object for User Groups:**
var grGroup = new GlideRecord("sys_user_group");

**Add a Query for Active Groups:**
grGroup.addActiveQuery();

**Execute the Query:**
grGroup.query();

**Iterate Through Active Groups:**
while (grGroup.next()) {

**Count Group Members:**
var gaGroupMember = new GlideAggregate("sys_user_grmember");
gaGroupMember.addQuery("group", grGroup.sys_id.toString());
gaGroupMember.addAggregate('COUNT');
gaGroupMember.query();

**Check Member Count:**
var gm = 0;
if (gaGroupMember.next()) {
    gm = gaGroupMember.getAggregate('COUNT');
    if (gm == 0) 
        myGroups.push(grGroup.name.toString());
}

**Print the Results:**
gs.print(myGroups);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
