---
title: "On Service Portal the record producer form  does not display all subcategories option  for users with no role"
aliases:
  - KB0693899
tags:
  - servicenow
  - support-kb
  - sys_choice
  - acl
  - service-portal
  - record-producer
  - catalog-client-script
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693899
kb_number: KB0693899
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Using following catalog client script inside record producer to create display sub-categories values depending on the selected categories option,

all the sub-categories may not be displayed for users with no roles.

function onChange(control, oldValue, newValue, isLoading) {

g\_form.clearOptions('subcategory');

var gp = new GlideRecord('sys\_choice');

gp.addQuery('name', 'incident');

gp.addQuery('dependent\_value', newValue);

gp.addQuery('element', 'subcategory');

gp.addQuery('inactive', false);

gp.query(function(gp)

 {

while(gp.next())

g\_form.addOption('subcategory', gp.value, gp.label);

}); 

}

# Release

* * *

Kingston Patch 5

# Cause

* * *

The code above will query the sys\_choice table and some read ACL might prevent user without role from reading all values in the sys\_choice table

# Resolution

* * *

1.  Log as admin
2.  enable the session debugging
3.  Goto the ‘sys\_choice’ table
4.  Impersonate user
5.  Locate any blocking read ACL
6.  Re-impersonate as admin and disable these read ACLs or allow user without the role to read.

## Related

- [[KB0753132 - Users getting "Unauthorized access" error in Service Portal when REST API level ACLs are in place ]] — another Service Portal ACL/role restriction issue
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — background on ACL evaluation for no-role users
- [[record-producer-vs-catalog-item]] — official docs on record producer configuration

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753132 - Users getting Unauthorized access error in Service Portal when REST API level ACLs are in place|Users getting \"Unauthorized access\" error in Service Portal when REST API level ACLs are in place ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0785229 - Non Role user can open an incomplete incident from the Service Portal|Non Role user can open an incomplete incident from the Service Portal]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749991 - [Service Portal] Injection argument not found (newValue) error|[Service Portal]: Injection argument not found (newValue) error]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
