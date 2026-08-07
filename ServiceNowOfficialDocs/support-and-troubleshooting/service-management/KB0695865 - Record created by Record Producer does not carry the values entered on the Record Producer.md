---
title: "Record created by Record Producer does not carry the values entered on the Record Producer"
aliases:
  - KB0695865
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695865
kb_number: KB0695865
last_modified: 2024-04-07
---

## Record created by Record Producer does not carry the values entered on the Record Producer

  

### Issue

# Symptoms

* * *

Values entered in Record Producer are not passing down to the created record.

# Release

* * *

Jakarta Patch 8a

# Cause

* * *

In order to carry values entered on the Record Producer down to the newly created Record, the user needs to have fields on the Record to receive those values (hence the "mapping to field" functionality). 

# Resolution

* * *

For example, on a Facilities Request record, create a new field and call it "Custodian's First Name". In the Record Producer, go to the "Custodian's First Name" variable, and check the "Map to field" checkbox.  
  
Once the checkbox is checked, a "Field" field appears. Simply select the "Custodian's First Name" field as the choice and save.  
  
Now, anything entered into the "Custodian's First Name" variable will automatically be passed down to the "Custodian's First Name" field on the Facilities Request record.  
  
\--

If the user is creating a different Facilities Request and they do not want or need the "Custodian's First Name" field on the form, they can create a single UI policy on the Facilities Request table which says "If the category is not 'Custodian Work', hide X, Y, and Z fields".  
  
That will resolve that issue, and only the desired fields will show on the Facilities Request.
