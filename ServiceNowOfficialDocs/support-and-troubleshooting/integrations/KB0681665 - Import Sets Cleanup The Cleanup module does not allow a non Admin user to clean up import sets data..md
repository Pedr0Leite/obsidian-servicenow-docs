---
title: "Import Sets Cleanup:  The Cleanup module does not allow a non Admin user to clean up import sets data."
aliases:
  - KB0681665
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0681665
kb_number: KB0681665
last_modified: 2024-04-07
---

## Import Sets Cleanup: The Cleanup module does not allow a non Admin user to clean up import sets data.

  

### Issue

DESCRIPTION: 

  

Out of the box, the Cleanup module allows users to access the module if the user has the 'import\_admin' role.  If you grant the user this role without giving the 'admin' role, the user will see the following error:

  

"The import set selected, <table name>, for cleanup doesn't belong to Global application. Transform maps cannot be deleted."

  

STEPS TO REPLICATE:

  

1\. Access any Kinston instance. 

2\. Create a new datasource and attach any spreadsheet or csv file.

3\. Access the Datasouce and perform a 'Test Load 20'.  This will create the import sets table and load the 20 records.

4\. Go to 'abel.tuter' user record and grant the 'itil' and 'import\_admin' roles.

5\. Now impersonate user 'abel.tuter'.

6\. Go to 'Cleanup' in the Filter Navigator.

7\. Move the file created in step 3 above to the right side box to have the records deleted.

8\. Click the Cleanup button.

The user will get the error listed above.

  

  

  

  

  

  

  

### Resolution

Go to ACL's module.

Access the following out of box ACL where sys\_id is:   a54785203730310066512f3c8e41f100

Add the 'import\_admin' to the role list of the ACL

Save the record.

Go to the user in question and also give the 'itil' role.
