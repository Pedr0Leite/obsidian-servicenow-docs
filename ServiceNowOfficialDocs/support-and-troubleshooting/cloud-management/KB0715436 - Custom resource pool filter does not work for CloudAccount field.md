---
title: "Custom resource pool filter does not work for CloudAccount field "
aliases:
  - KB0715436
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715436
kb_number: KB0715436
last_modified: 2025-08-25
---

## Custom resource pool filter does not work for CloudAccount field

  

### Issue

# Symptoms

* * *

Custom resource pool filter does not work for CloudAccount field

# Release

* * *

Kingston, London

# Steps to Reproduce

* * *

1> Change Application Scope to Cloud Management Platform

2> Open resource pool: CloudAccountPool, create a resource pool filter (named "getbytest" as an example)

3> Change Application Scope back to Global

4> Open the Blueprint Form Parameter "CloudAccount", change Datasource Value from:

ServiceNow::Pools::CloudAccountPool.All

to

ServiceNow::Pools::CloudAccountPool.getbytest

5> In Cloud User Portal, launch the stack, and the resource pool filter does not take effect

# Resolution

* * *

A Form Load Rule is required if custom resource pool filter is used for Cloud Account:

1> Open the Blueprint, make sure it's checked out, then click on Catalog tab > open the catalog > Form Tab > click on Form Load Rules.

2> Click on "New" button next to "Rules", then fill in below fields, and save.

Name: yourchoice

Order: 1000

Event: FormLoad

3> On the Rule form, at the bottom, click on "Actions" tab, then "New" button, and fill in below fields, then save.

Name: yourchoice

Action Type: Reload

DataSource: Reload From Pool

Target Field: CloudAccount

# Troubleshooting

* * *

Make sure there is no "Reload Cloud Account" Form Load Rule that has larger Order, which will reset the filtered result.

Also the "Lookup Field" for CloudAccountPool resource pool is name. So in the custom resource pool filter script, the value returned should be name of Cloud Account instead of sys\_id.
