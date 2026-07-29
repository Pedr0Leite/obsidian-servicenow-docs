---
title: "Service Catalog - List Collector Variables not populating data when the list table is set to cmdb_ci"
aliases:
  - KB0635408
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635408
kb_number: KB0635408
last_modified: 2024-04-07
---

## Service Catalog - List Collector Variables not populating data when the list table is set to cmdb\_ci

  

### Issue

Service Catalog - List Collector Variables not populating data when the list table is set to cmdb\_ci

  
  

# Problem

* * *

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Important</strong>:&nbsp;Due to the introduction of the Table-Per-Partition in the CMDB&nbsp;from Jakarta, this article applies only to the Geneva, Helsinki, and Istanbul releases.</td></tr></tbody></table>

In the Service Catalog, users can configure List Collectors to retrieve a large amount of data from a table. One of the examples is the Configuration Item \[cmdb\_ci\] table, where users wish to retrieve a set of data from a CI Class.

However, due to the re-parenting of the cmdb\_ci table, where a new table called "Base Configuration" \[cmdb\] was introduced in Geneva as a parent to cmdb\_ci, it has been noticed that the table schema change can cause list collector variables to no longer populate data when the variable is referencing the list table as "cmdb\_ci"

# Symptoms

* * *

List Collector displays no results on the "Selected" list options.

# Cause

* * *

The main cause of the issue is due to a reference qualifier set on the list collector variable to query data on the "sys\_class\_name" field. The following example shows a sample reference qualifier. managed\_domain=true^sys\_class\_name=cmdb\_ci\_computer^EQ 

This reference qualifier is designed to query cmdb\_ci records, where the sys\_class\_name field is "cmdb\_ci\_computer" and managed\_domain field is set to "true".

From the Geneva through the Istanbul releases, the reference qualifier will no longer work because sys\_class\_name field is no longer a field on the cmdb\_ci table. The sys\_class\_name field was moved from cmdb\_ci to cmdb due to the reparenting of the cmdb\_ci table.

# Resolution

* * *

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>:&nbsp;Note that the following change will alter the behavior of the Service Catalog Item you are modifying the Variable against. This can cause a behavior change within the Catalog Item and might affect end users. Therefore, you are strongly advised to test the recommendation on a sub-production instance that is cloned from production to ensure that the resolution is tested successfully before it is implemented on a live environment.</td></tr></tbody></table>

To resolve the problem, remove the sys\_class\_name filter from the reference qualifier and consider selecting another alternative field to filter records for a specific Configuration Item. 

You can also consider selecting a specific child CMDB table, for example, cmdb\_ci\_computer, to populate a list of computer CIs instead of using the cmdb\_ci table.
