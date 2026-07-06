---
title: "[CMDB/Rack] Populate \"Power Consumption\" & \"Rack units in use\" fields in \"cmdb_ci_rack\" table based on CI relation rollups."
aliases:
  - KB0788463
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788463
kb_number: KB0788463
last_modified: 2025-04-07
---

## \[CMDB/Rack\] Populate "Power Consumption" & "Rack units in use" fields in "cmdb\_ci\_rack" table based on CI relation rollups.

  

### Summary

-   This article explains on how does [CI Relation Rollups](https://docs.servicenow.com/csh?topicname=t_CreateACIRelationRollup.html&version=latest "CI Relation Rollups") helps in sync or sum the data related to "Power Consumption" & "Rack Units in Use" for the "cmdb\_ci\_rack" table using OOB Business Rules.

### Release

-   Any release.

### Instructions

-   In general a CI relation rollup allows you to sum, count, max, min, or mean a relationship type. You can create CI relation rollups based on the relationship.

## Steps to Reproduce:

1.  Login to the instance.
2.  Navigate >> Configuration >> Data Center>> Rack.
3.  Click "New" to create a Parent Rack CI manually.

![](sys_attachment.do?sys_id=22e4548ddb00b8d066e0a345ca9619e8)

4\. Under the Related Links on the Relationships tab click Edit to create a Child relation (e.g. Windows Server) and select "Type" to "In Rack::Rack contains".![](sys_attachment.do?sys_id=a6e4948ddb00b8d066e0a345ca96191b)

![](sys_attachment.do?sys_id=22e4948ddb00b8d066e0a345ca96191d)

![](sys_attachment.do?sys_id=aae4948ddb00b8d066e0a345ca96191e)

-   Post the above steps the "Power Consumption" & "Rack Units in Use" fields for Parent CI Rack will not get populated.

## Solution:

-   There are 2 ways you can achieve this CI relation rollups using OOB Business rules.

1\. **CMDB Synch Event (cmdb synch event)**

-   -   In general CI relation rollups use the cmdb synch event business rule on the \[cmdb\_ci\] table.

https://<<instance\_name>>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=e6865f610a0a0aa700c7598ec326f608

**(OR)**

2\. **CMDB Rel CI Synch Event (cmdb\_rel\_ci synch event)**.

-   -   This BR can be used if you need CI relation rollups to recalculate when there is a change to a relationship.

https://<<instance\_name>>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=e6ad3b880a0a0aa700d7e3a8a37ba27a

### Steps to achieve using "CMDB Synch Event BR":

-   By default this "**cmdb synch event**" BR is "Active" and you would need to modify based on the use case. i.e. in the "When to run" tab select "Insert", "Update", "Delete".
-   Perform the above steps to reproduce provided and when there is a "Insert" (or) "Update" (or) "Delete" on any fields on the Child CI form, you could see that "Power Consumption" & "Rack units in use" fields in "cmdb\_ci\_rack" table gets populated based on the hardware product model linked to the Windows server CI.

### Steps to achieve using "CMDB Rel CI Synch Event BR":

-   As said if you wish CI relation rollups to recalculate when there is a change to a relationship, select the "Active" check box on the "**cmdb\_rel\_ci synch event**" business rule.
-   In addition to it perform the above steps to reproduce provided and once a Child CI is related with "Type" to "In Rack::Rack contains" the "Power Consumption" & "Rack units in use" fields in "cmdb\_ci\_rack" table gets populated when there is a change to a relationship to the Parent CI.
